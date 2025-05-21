from django.db import models
from django.core.validators import MinValueValidator
from apps.users.models import Order

class Restaurant(models.Model):
    """Модель ресторана/кафе"""
    name = models.CharField(max_length=255, verbose_name="Название заведения")
    description = models.TextField(blank=True, verbose_name="Описание")
    address = models.CharField(max_length=500, verbose_name="Адрес")
    contact_phone = models.CharField(max_length=20, verbose_name="Контактный телефон")
    opening_hours = models.CharField(max_length=100, verbose_name="Часы работы")
    delivery_time = models.PositiveIntegerField(verbose_name="Среднее время доставки (мин)")
    min_order = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="Минимальный заказ"
    )
    rating = models.FloatField(default=0, verbose_name="Рейтинг")

    class Meta:
        verbose_name = "Ресторан"
        verbose_name_plural = "Рестораны"

    def __str__(self):
        return self.name

class Category(models.Model):
    """Категория блюд (пицца, суши, бургеры и т.д.)"""
    name = models.CharField(max_length=100, verbose_name="Название категории")
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        related_name='categories',
        verbose_name="Ресторан"
    )

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"

    def __str__(self):
        return f"{self.name} ({self.restaurant.name})"

class MenuItem(models.Model):
    """Модель блюда в меню"""
    name = models.CharField(max_length=255, verbose_name="Название блюда")
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE,
        related_name='menu_items',
        verbose_name="Категория"
    )
    description = models.TextField(blank=True, verbose_name="Описание")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        validators=[MinValueValidator(0)],
        verbose_name="Цена"
    )
    image = models.ImageField(upload_to='menu_items/', blank=True, null=True, verbose_name="Изображение")
    is_available = models.BooleanField(default=True, verbose_name="Доступно для заказа")

    class Meta:
        verbose_name = "Позиция меню"
        verbose_name_plural = "Позиции меню"

    def __str__(self):
        return f"{self.name} - {self.price} руб."

class Order(models.Model):
    """Модель заказа"""
    STATUS_CHOICES = (
        ('new', 'Новый'),
        ('accepted', 'Принят'),
        ('preparing', 'Готовится'),
        ('on_way', 'В пути'),
        ('delivered', 'Доставлен'),
        ('cancelled', 'Отменен'),
    )

    user = models.ForeignKey(
        Order,
        on_delete=models.PROTECT,
        related_name='orders',
        verbose_name="Пользователь"
    )
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.PROTECT,
        verbose_name="Resta"
    )
    status = models.CharField(
        max_length=20,
        choices=STATUS_CHOICES,
        default='new',
        verbose_name="Статус заказа"
    )
    delivery_address = models.CharField(max_length=500, verbose_name="Адрес доставки")
    contact_phone = models.CharField(max_length=20, verbose_name="Контактный телефон")
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    total_price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        default=0,
        verbose_name="1289"
    )
    delivery_time = models.PositiveIntegerField(verbose_name="(30)", default=30)
    comment = models.TextField(blank=True, verbose_name="Комментарий к заказу")

    class Meta:
        verbose_name = "Заказ"
        verbose_name_plural = "Заказы"
        ordering = ['-created_at']

    def __str__(self):
        return f"Заказ #{self.id} - {self.get_status_display()}"

    def update_total_price(self):
        """Обновляет общую стоимость заказа"""
        self.total_price = sum(item.price * item.quantity for item in self.items.all())
        self.save()

class OrderItem(models.Model):
    """Модель позиции в заказе"""
    order = models.ForeignKey(
        Order,
        on_delete=models.CASCADE,
        related_name='items',
        verbose_name="Заказ"
    )
    menu_item = models.ForeignKey(
        MenuItem,
        on_delete=models.PROTECT,
        verbose_name="1 позиция"
    )
    quantity = models.PositiveIntegerField(default=1, verbose_name="100")
    price = models.DecimalField(
        max_digits=10,
        decimal_places=2,
        verbose_name="580"
    )

    class Meta:
        verbose_name = "1 позиция "
        verbose_name_plural = " 2 позиция"

    def __str__(self):
        return f"{self.menu_item.name} x{self.quantity}"

    def save(self, *args, **kwargs):
        """Сохраняет текущую цену блюда при добавлении в заказ"""
        if not self.price:
            self.price = self.menu_item.price
        super().save(*args, **kwargs)

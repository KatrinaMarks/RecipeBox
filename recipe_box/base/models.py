from django.conf import settings
from tabnanny import verbose
from unittest.util import _MAX_LENGTH
from django.db import models
from django.db.models.signals import pre_save, post_save
from django.urls import reverse
from .utils import slugify_instance_name, model_post_save, model_pre_save
# Create your models here.

class Section(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length=120)
    slug = models.SlugField(unique=True, blank=True, null=True)
    description = models.TextField(null=True, blank=True)
    order_index = models.PositiveIntegerField(null=True, blank=True)
    color = models.CharField(max_length = 16, default="#ffffff")
    
    class Meta:
        verbose_name = ('Section')
        verbose_name_plural = ('Sections')
    
    def __str__(self):
        return self.name

    def get_recipes_children(self):
        return self.recipe_set.all()

    def get_absolute_url(self):
        return reverse("individual_section", kwargs={"title": self.slug})
    
pre_save.connect(model_pre_save, sender=Section)
post_save.connect(model_post_save, sender=Section)


class Recipe(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    name = models.CharField(max_length = 150)
    slug = models.SlugField(unique=True, blank=True, null=True)
    ## description = models.TextField(null=True, blank=True) ## DON"T NEED
    time_to_make = models.CharField(max_length = 25, default=0)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    section = models.ForeignKey(Section, related_name='recipes', on_delete=models.SET_NULL, null=True, blank=True)
    pinned = models.BooleanField(default=False)

    class Meta:
        verbose_name = ('Recipe')
        verbose_name_plural = ('Recipes')

    def get_ingredients_children(self):
        return self.ingredient_set.all()

    def get_instructions_children(self):
        return self.instruction_set.all()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("individual_recipe", kwargs={"title": self.slug})
        
    def get_edit_url(self):
        return reverse("edit_recipe", kwargs={"title": self.slug})
    
pre_save.connect(model_pre_save, sender=Recipe)
post_save.connect(model_post_save, sender=Recipe)


class Ingredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    name = models.CharField(max_length = 100)
    quantity = models.CharField(max_length = 50)
    unit = models.CharField(max_length = 50)
    class Meta:
        verbose_name = ('Ingredient')
        verbose_name_plural = ('Ingredients')
        
    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

class Instruction(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE)
    text = models.TextField(blank=False)
    class Meta:
        verbose_name = ('Instruction')
        verbose_name_plural = ('Instructions')
    def __str__(self):
        return self.text

    def get_absolute_url(self):
        return self.recipe.get_absolute_url()

#class EmailChangeAuth(models.Model):
   # auth_key = models.CharField(max_length=42)
# auth_key = models.UUIDField(default=uuid.uuid4, unique=True)
    #user = models.ForeignKey(settings.AUTH_USER_MODEL)
    #new_email = models.CharField(max_length=256)
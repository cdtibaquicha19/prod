from django.urls import path
from .views import CategoriaDel, CategoriaView,CategoriaNew,CategoriaEdit, \
    CategoriaDel, ProductoEdit, ProductoNew, ProductoView, Producto_inactivar, \
        SubCategoriaView , SubCategoriaNew , SubCategoriaEdit ,SubCategoriaDel,\
            MarcaView ,MarcaEdit , MarcaNew, UMEdit, UMNew, UMView, UM_inactivar ,marca_inactivar

urlpatterns = [
    path('categorias/',CategoriaView.as_view(), name='categoria_list'),
    path('categorias/new',CategoriaNew.as_view(), name='categoria_new'),
    path('categorias/edit/<int:pk>',CategoriaEdit.as_view(), name='categoria_edit'),
    path('categorias/delete/<int:pk>',CategoriaDel.as_view(), name='categoria_delete'),
    
    path('subcategorias/',SubCategoriaView.as_view(), name='subcategoria_list'),
    path('subcategorias/new',SubCategoriaNew.as_view(), name='subcategoria_new'),
    path('subcategorias/<int:pk>',SubCategoriaEdit.as_view(), name='subcategoria_edit'),
    path('subcategorias/delete/<int:pk>',SubCategoriaDel.as_view(), name='subcategoria_delete'),
    
    path('marcas/',MarcaView.as_view(), name='marca_list'),
    path('marcas/new',MarcaNew.as_view(), name='marca_new'),
    path('marcas/edit/<int:pk>',MarcaEdit.as_view(), name='marca_edit'),
    path('marcas/inactivar/<int:id>',marca_inactivar, name='marca_inactivar'),
    
    path('um/',UMView.as_view(), name='um_list'),
    path('um/new',UMNew.as_view(), name='um_new'),
    path('um/edit/<int:pk>',UMEdit.as_view(), name='um_edit'),
    path('um/inactivar/<int:id>',UM_inactivar, name='um_inactivar'),
 
    path('productos/',ProductoView.as_view(), name='producto_list'),
    path('productos/new',ProductoNew.as_view(), name='producto_new'),
    path('productos/edit/<int:pk>',ProductoEdit.as_view(), name='producto_edit'),
    path('productos/inactivar/<int:id>',Producto_inactivar, name='producto_inactivar'),
     
     
       
]

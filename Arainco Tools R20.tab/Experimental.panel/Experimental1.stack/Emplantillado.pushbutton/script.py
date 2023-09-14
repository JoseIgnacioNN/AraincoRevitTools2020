# Importa las bibliotecas necesarias
from pyrevit import revit, DB
from pyrevit import forms

# Función para seleccionar elementos de la categoría "Structural Foundation"
def select_structural_foundations():
    # Inicializa una lista vacía para almacenar los elementos seleccionados
    selected_elements = []

    # Crea un filtro para la categoría "Structural Foundation"
    category_filter = DB.ElementCategoryFilter(DB.BuiltInCategory.OST_StructuralFoundation)

    # Abre una transacción para la selección
    with revit.Transaction("Select Structural Foundations"):
        # Utiliza un recolector de elementos para obtener elementos que cumplan con el filtro
        collector = DB.FilteredElementCollector(revit.doc)
        foundations = collector.WherePasses(category_filter).ToElements()

        # Agrega los elementos a la lista de elementos seleccionados
        selected_elements.extend(foundations)

        # Selecciona los elementos en el modelo de Revit
        revit.uidoc.Selection.SetElementIds([element.Id for element in selected_elements])

# Llama a la función para seleccionar elementos de la categoría "Structural Foundation"
select_structural_foundations()

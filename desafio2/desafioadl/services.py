from .models import Tarea, SubTarea

def recupera_tareas_y_sub_tareas():
    tareas = Tarea.objects.all()
    subtareas = SubTarea.objects.all()
    return tareas, subtareas

def crear_nueva_tarea(descripcion):
    tarea = Tarea(descripcion=descripcion)
    tarea.save()
    return recupera_tareas_y_sub_tareas()

def crear_sub_tarea(descripcion, tarea_id):
    tarea = Tarea.objects.get(id=tarea_id)
    subtarea = SubTarea(descripcion=descripcion, tarea=tarea)
    subtarea.save()
    return recupera_tareas_y_sub_tareas()

def elimina_tarea(tarea_id):
    Tarea.objects.get(id=tarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def elimina_sub_tarea(subtarea_id):
    SubTarea.objects.get(id=subtarea_id).delete()
    return recupera_tareas_y_sub_tareas()

def imprimir_en_pantalla(tareas, subtareas):
    for tarea in tareas:
        print(f"[{tarea.id}] {tarea.descripcion}")
        subtareas_de_tarea = subtareas.filter(tarea=tarea)
        for subtarea in subtareas_de_tarea:
            print(f".... [{subtarea.id}] {subtarea.descripcion}")

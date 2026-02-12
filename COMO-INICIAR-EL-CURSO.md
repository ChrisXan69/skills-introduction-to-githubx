# Cómo Iniciar el Curso de GitHub Skills

¡Bienvenido al curso de Introducción a GitHub! 🎉

## ✅ Estado Actual

El curso ha sido **iniciado exitosamente**. El sistema automatizado de GitHub Skills ha:
- ✅ Creado el Issue #2 con las instrucciones del curso
- ✅ Preparado el entorno de aprendizaje
- ✅ Activado los flujos de trabajo de GitHub Actions

> 💡 **Nota:** Si no ves el Issue #2, ve a la [pestaña Issues](../../issues) para verificar. El issue debería haberse creado automáticamente cuando se copió el repositorio.

## 📋 Qué Aprenderás

En este curso aprenderás a:
1. Crear ramas (branches)
2. Hacer commits
3. Abrir pull requests
4. Fusionar pull requests

## 🚀 Próximos Pasos - Comienza Ahora

Para avanzar al siguiente paso del curso, necesitas crear una rama llamada `my-first-branch`:

### Opción 1: Usando la Interfaz Web de GitHub (Recomendado)

1. Abre tu repositorio en GitHub (la página donde estás viendo este archivo)

2. Haz clic en la pestaña **< > Code** en el menú superior

3. Busca y haz clic en el menú desplegable que dice **main** (está cerca de la esquina superior izquierda)

4. En el cuadro de texto que dice **Find or create a branch...**, escribe exactamente:
   ```
   my-first-branch
   ```

5. Haz clic en **Create branch: my-first-branch from main**

6. ¡Listo! GitHub Actions detectará la nueva rama y automáticamente:
   - Verificará que la rama se creó correctamente
   - Publicará las instrucciones para el Paso 2 en el Issue #2
   - Continuará guiándote a través del curso

### Opción 2: Usando Git en la Línea de Comandos

Si prefieres usar la terminal:

```bash
# Asegúrate de estar en el repositorio
cd tu-repositorio  # Reemplaza con el nombre de tu repositorio

# Crea y cambia a la nueva rama desde main
git checkout -b my-first-branch main

# Sube la rama a GitHub
git push -u origin my-first-branch
```

## 📚 Recursos Útiles

- **[Issue #2: Instrucciones Detalladas del Curso](../../issues/2)** - Revisa aquí para ver las instrucciones completas y el progreso
- [Documentación de GitHub sobre Ramas](https://docs.github.com/es/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/about-branches)
- [Video: ¿Qué es GitHub?](https://www.youtube.com/watch?v=pBy1zgt0XPc)

## 💡 Importante

- Este es un curso **interactivo** que requiere acciones manuales
- Cada paso que completes activará automáticamente el siguiente
- GitHub Actions (el bot "Mona") comentará en el Issue #2 con feedback y nuevas instrucciones
- No necesitas cerrar o modificar nada manualmente - el sistema lo hace por ti

## ❓ ¿Problemas?

Si no ves progreso después de crear la rama:
1. Espera unos 20-30 segundos para que GitHub Actions procese tu acción
2. Verifica que la rama se llame exactamente `my-first-branch` (sin espacios extra ni mayúsculas)
3. Revisa la pestaña [Actions](../../actions) para ver si hay trabajos en ejecución
4. Si persisten los problemas, reporta un issue en el [repositorio oficial del curso](https://github.com/skills/introduction-to-github/issues)

---

¡Buena suerte con tu aprendizaje de GitHub! 🚀

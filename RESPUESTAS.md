# RESPUESTAS

## 1. Diferencia entre CI y CD
- **CI (Integración Continua)**: consiste en integrar cambios de código de forma frecuente y automática. Cada integración ejecuta compilaciones, linters y pruebas para detectar errores temprano y evitar que se acumulen problemas grandes.
- **CD (Entrega/Despliegue Continua)**: extiende la CI dejando el software siempre listo para desplegarse. Dependiendo de la configuración, incluso puede automatizar el despliegue a entornos como staging o producción, siempre y cuando las pruebas hayan pasado correctamente.

## 2. Por qué escogí Python
Elegí Python porque es un lenguaje práctico para proyectos pequeños y educativos, con sintaxis clara y herramientas fáciles de configurar.
flake8 funciona bien como linter porque revisa estilo, errores comunes y complejidad sin necesidad de mucha configuración.
pytest hace que las pruebas sean más simples de escribir y mantener, gracias a su sintaxis clara.
Para medir cobertura, coverage junto con pytest-cov se integra muy bien con pytest y permite ver exactamente qué partes del código están siendo ejecutadas y cuáles no.

## 3. Justificación del umbral del 80%
Un 80% de cobertura es un punto intermedio razonable que obliga a probar la mayor parte de la lógica importante, pero sin imponer una meta demasiado exigente que lleve a crear pruebas innecesarias o poco útiles. Es suficiente para mantener buena calidad sin frenar el avance del proyecto.

## 4. Cómo identificar errores de linter, pruebas y cobertura en logs
**Errores de flake8:** normalmente muestra el archivo, la línea y el tipo de error. Si flake8 imprime algo, significa que la etapa falló automáticamente.

**Errores en pruebas con pytest:** el resumen final muestra cuántas pruebas pasaron y cuántas fallaron. Cuando falla una prueba aparece un bloque “FAIL” con la traza de error.

**Errores de cobertura:** el reporte indica qué líneas no fueron ejecutadas. Si el porcentaje no alcanza el mínimo configurado, la etapa se marca como fallida.

## 5. Diferencia entre run fallido y exitoso
Para generar un run fallido, modifiqué una prueba a propósito para que el resultado esperado no coincidiera con la función. Al hacer push, pytest marcó el error y GitHub Actions registró el workflow en rojo.

Después, volví a dejar la prueba correcta y generé un run exitoso, donde todas las etapas (linter, pruebas y cobertura) terminaron con código 0. GitHub Actions marcó ese workflow en verde. La diferencia final es que el run fallido se detiene por un error en alguna etapa, mientras que el exitoso completa todo el pipeline sin interrupciones.

## 6. Qué es act y cómo funciona
es una herramienta que permite ejecutar workflows de GitHub Actions de manera local. Utiliza contenedores Docker para simular el entorno del runner de GitHub, lo que ayuda a probar el pipeline sin necesidad de hacer push al repositorio.

## Requisitos:
Tener Docker instalado

Tener act instalado

Comando para ejecutar el workflow:
```cmd
act -W .github/workflows/ci-quality.yml
```
ejecuta el workflow especificado en el archivo ci-quality.yml, permitiendo verificar que todo funcione correctamente antes de subir los cambios.

## 7. Dos métodos para detectar código generado por IA
Comparación de estilo: se revisa si el código o el texto concuerda con el estilo habitual del autor. Cambios bruscos pueden indicar intervención de IA.

Patrones típicos de IA: algunas herramientas detectan estructuras repetitivas, comentarios genéricos o patrones característicos que suelen producir los modelos.

## 8. Por qué no se puede garantizar la autoría 100%
No es posible asegurarlo porque tanto humanos como IA pueden imitar estilos. Además, los detectores no son perfectos y pueden equivocarse. El código también puede ser modificado después de generarse, lo que vuelve más difícil rastrear el origen real.

## 9. Propuesta de políticas razonables de IA en educación
Una política equilibrada podría incluir transparencia obligatoria sobre el uso de IA, permitirla para documentación o apoyo inicial, pero limitarla en evaluaciones que buscan medir comprensión real. También es útil combinar proyectos escritos con defensas orales, revisar el historial de commits y enseñar sobre el uso ético y responsable de estas herramientas.


# Trabajo Practico Obligatorio: Test Driven Development (TDD)

**Fecha de entrega: Lunes 29 de Abril**

## Requerimientos

Implementar la funcionalidad de **bowling scoring**:

_The game consists of 10 frames as shown in  [BowlingGenius](https://www.bowlinggenius.com/). In each frame the player has two opportunities to knock down 10 pins.  The score for the frame is the total number of pins knocked down, plus bonuses for strikes and spares._

_A spare is when the player knocks down all 10 pins in two tries.  The bonus for that frame is the number of pins knocked down by the next roll.  So in frame 3 above, the score is 10 (the total number knocked down) plus a bonus of 5 (the
number of pins knocked down on the next roll.)_

_A strike is when the player knocks down all 10 pins on his first try.  The bonus for that frame is the value of the next two balls rolled._

_In the tenth frame a player who rolls a spare or strike is allowed to roll the extra balls to complete the frame.  However no more than three balls can be rolled in tenth frame._

_Además, el juego tiene que soportar **hasta 2 jugadores** con sus nombres y decir quien ganó._

## Instrucciones

1. Grupos de **2** integrantes.
2. Crear el repositorio (o bien forkear el presente repo) correspondiente en GitHub y agregar a Franco(Franco94) y a Martin (mgarriga) como colaboradores.
3. Realizar el commit inicial con:
```
test_gutter_game(game):
  assert game.get_score() == 0
```
4. Implementar los requerimientos utilizando la metodología TDD.
5. Escribir el readme.MD el cual será el informe del trabajo.

## Criterios de evaluación

* El uso de Gitflow o [github flow](https://guides.github.com/introduction/flow/index.html) (una version simplificada de GitFlow) es obligatorio y será evaluado. La historia de commits nos servirá para **evaluar** si hicieron el trabajo siguiendo la metodología TDD.

* Hacer branchs por cada feature (aproximadamente una por test case) y hacer commits + Pull Requests que serán cross-checkeados por su compañero. Cada Pull Request comprende los tests además de las funcionalidad.

* Se recomienda, aunque no es obligatorio, usar [pair programming](http://www.extremeprogramming.org/rules/pair.html) (2 programadores con una pc). En ese caso, deben alternar ambos cada rol (piloto/copiloto) y commitear con sus respectivos usuarios a los fines evaluativos.

* Pueden utilizar el lenguaje que prefieran. Si usan javascript recomendamos [mocha](https://mochajs.org/) como herramienta de testing y [nyc/istambul](https://github.com/istanbuljs/nyc)
para analizar el coverage de los tests.

* El informe del proyecto será el Readme.MD del repositorio, el cual debe contener:
  - Instrucciones para correr el proyecto.
  - Ejemplo de un ciclo de TDD (Red/Green/Refactor) para alguna de las funciones implementadas.
  - Tipos de Test aplicados y ejemplos (remitirse a la teoría de la materia).
  - Conclusiones: Dificultades y ventajas percibidas en cuanto a la metodología TDD y al proyecto en sí, críticas constructivas

* La finalidad del trabajo no es sólo la aprobación de la materia sino que utilicen metodologías y herramientas actuales (TDD, Github flow, etc.) y puedan aprender y resolver problemas de manera **autónoma**.

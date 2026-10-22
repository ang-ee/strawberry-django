---
release type: patch
---

Qualify the model class annotation in `StrawberryDjangoDefinition` so cyclic type analysis cannot confuse it with this module's `type` decorator.

Use schema-local type definitions when collecting nested optimizer hints, so annotations and other field hints remain available through relations.

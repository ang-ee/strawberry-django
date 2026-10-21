from typing import Any

from typing_extensions import assert_type

from strawberry_django.optimizer import OptimizerStore
from strawberry_django.type import StrawberryDjangoDefinition

from .models import Fruit


def test_definition_retains_model_class_and_metadata() -> None:
    definition = StrawberryDjangoDefinition[Any, Fruit](origin=object(), model=Fruit, store=OptimizerStore())
    assert_type(definition.model, type[Fruit])
    assert_type(definition.model._meta.label, str)
    assert definition.model is Fruit
    assert definition.model._meta.label == "tests.Fruit"

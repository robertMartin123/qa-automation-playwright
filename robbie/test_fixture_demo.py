import pytest


# @pytest.fixture
# def greeting():
#     print("Fixture is running...")
#     return "Hello Robert"

@pytest.fixture
def resource():
    print("Setting up resource")
    yield "Resource is ready"
    print("Tearing down resource")

def test_using_resource(resource):
    print(resource)
    assert "ready" in resource

import pytest


# def test_print_greeting(greeting):
#     print(greeting)
#     assert greeting == "Hello Robert"



@pytest.fixture(scope="session")
def demo():
    print("Setting up demo")
    yield "demo value"
    print("Tearing down demo")


def test_one(demo):
    print("Running test_one")


def test_two(demo):
    print("Running test_two")


@pytest.fixture(scope="session")
def counter():
    print("Counter created")
    return []

def test_add_one(counter):
    counter.append(1)
    print(counter)

def test_add_two(counter):
    counter.append(2)
    print(counter)




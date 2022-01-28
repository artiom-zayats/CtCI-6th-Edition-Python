import pytest
from collections import deque


def determine_build_order2(projects, dependencies):
    dependency_tree = {p: set() for p in projects}
    build_order = []
    unbuilt_projects = set(projects)
    for dependency, project in dependencies:
        dependency_tree[project].add(dependency)

    while unbuilt_projects:
        something_built = False
        for project in list(unbuilt_projects):
            dependencies = dependency_tree[project]
            if not unbuilt_projects.intersection(dependencies):
                build_order.append(project)
                unbuilt_projects.remove(project)
                something_built = True
        if not something_built:
            raise NoValidBuildOrderError("No valid build order exists")

    return build_order



def determine_build_order(projects,dependencies):
    dic = {}
    inputs = {i:0 for i in projects}
    for a,b in dependencies:
        if b not in dic:
            dic[b] = []
        dic[b].append(a)
        inputs[a] += 1
    sources = deque()
    for a in inputs:
        if inputs[a] == 0:
            sources.append(a)
    build_order = []
    while sources:
        a = sources.popleft()
        build_order.append(a)
        if a in dic:
            for b in dic[a]:
                inputs[b]-=1
                if inputs[b] == 0:
                    sources.append(b)
    if len(projects) != len(build_order):
        raise NoValidBuildOrderError
    return build_order





class NoValidBuildOrderError(Exception):
    pass


def test_determine_build_order():
    projects = ["a", "b", "c", "d", "e", "f"]
    dependencies = [
        ("d", "a"),
        ("b", "f"),
        ("d", "b"),
        ("a", "f"),
        ("c", "d"),
    ]
    build_order = determine_build_order(projects, dependencies)
    assert ["e","f","b","a","d","c"] == build_order
    print("test2")


def test_impossible_build_order():
    projects = ["a", "b"]
    dependencies = [("a", "b"), ("b", "a")]
    with pytest.raises(NoValidBuildOrderError):
        determine_build_order(projects, dependencies)
    print("test1")

if __name__ == "__main__":
    test_impossible_build_order()
    test_determine_build_order()
                             
    print("Done")


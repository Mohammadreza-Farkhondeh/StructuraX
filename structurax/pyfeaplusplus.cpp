#include <pybind11/pybind11.h>

#include "fea/mesh.h"
#include "fea/fea.h"
#include "common/common.h"
#include "geometry/node.h"
#include "geometry/element.h"
#include "material/material.h"
#include "loads/point_load.h"
#include "loads/distributed_load.h"
#include "postprocessor/postprocessor.h"
#include "preprocessor/preprocessor.h"

namespace py = pybind11;

void bind_node(py::module &m) {
    py::class_<Node>(m, "Node")
        .def(py::init<double, double, double>())
        .def_readonly("x", &Node::x)
        .def_readonly("y", &Node::y)
        .def_readonly("z", &Node::z);
}

void bind_element(py::module &m) {
    py::class_<Element>(m, "Element")
        .def(py::init<>());
}

void bind_load(py::module &m) {
    py::class_<Load>(m, "Load")
        .def(py::init<>());
}

void bind_material(py::module &m) {
    py::class_<Material>(m, "Material")
        .def(py::init<>());
}

void bind_mesh(py::module &m) {
    py::class_<Mesh>(m, "Mesh")
        .def(py::init<>())
        .def("addNode", &Mesh::addNode)
        .def("addElement", &Mesh::addElement)
}

void bind_fea(py::module &m) {
    py::class_<FEA>(m, "FEA")
        .def(py::init<>())
        .def("setupModel", &FEA::setupModel)
        .def("analyze", &FEA::analyze)
}

PYBIND11_MODULE(pyfeaplusplus, m) {
    bind_node(m);
    bind_element(m);
    bind_load(m);
    bind_material(m);
    bind_mesh(m);
    bind_fea(m);
}

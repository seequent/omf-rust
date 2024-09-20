/// Python bindings.
use pyo3::prelude::*;

mod array;
mod attribute;
mod element;
mod errors;
mod file;
mod geometry;
mod omf1;
mod project;
mod validate;

use array::{PyColorArray, PyIndexArray, PyNameArray, PyTriangleArray, PyVertexArray};
use attribute::{PyAttribute, PyAttributeDataCategory, PyAttributeDataColor};
use element::{PyColor, PyElement};
use errors::OmfException;
use file::reader::{PyLimits, PyReader};
use geometry::{PyGeometry, PyLineSet, PyPointSet, PySurface};
use omf1::converter::{detect_open, PyConverter};
use project::PyProject;

/// Returns the version of the library
#[pyfunction]
fn version() -> String {
    env!("CARGO_PKG_VERSION").to_string()
}

/// This module provides python bindings for omf-rust.
#[pymodule]
fn omf_python(py: Python<'_>, m: &Bound<'_, PyModule>) -> PyResult<()> {
    m.add_class::<PyAttribute>()?;
    m.add_class::<PyAttributeDataCategory>()?;
    m.add_class::<PyAttributeDataColor>()?;
    m.add_class::<PyColor>()?;
    m.add_class::<PyColorArray>()?;
    m.add_class::<PyIndexArray>()?;
    m.add_class::<PyVertexArray>()?;
    m.add_class::<PyTriangleArray>()?;
    m.add_class::<PyNameArray>()?;
    m.add_class::<PyElement>()?;
    m.add_class::<PyGeometry>()?;
    m.add_class::<PyPointSet>()?;
    m.add_class::<PyLineSet>()?;
    m.add_class::<PyProject>()?;
    m.add_class::<PyReader>()?;
    m.add_class::<PySurface>()?;
    m.add_class::<PyLimits>()?;

    m.add_function(wrap_pyfunction!(version, m)?)?;

    let omf1_submodule = PyModule::new_bound(m.py(), "omf1")?;
    omf1_submodule.add_function(wrap_pyfunction!(detect_open, m)?)?;
    omf1_submodule.add_class::<PyConverter>()?;
    m.add_submodule(&omf1_submodule)?;

    m.add("OmfException", py.get_type_bound::<OmfException>())?;

    Ok(())
}

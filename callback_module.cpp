#include <Python.h>

// Module definition
static struct PyModuleDef callbackmodule = {
    PyModuleDef_HEAD_INIT,
    "callback_module",   // name of module
    NULL,                // module documentation, may NULL
    -1,                  // size of per-interpreter state of the module, or -1
    CallbackMethods      // method table
};

// Method definition object for this extension
static PyMethodDef CallbackMethods[] = {
    {"process_with_callback", py_process_with_callback, METH_VARARGS, 
     "Call C function with Python callback"},
    {NULL, NULL, 0, NULL}  // Sentinel
};

// Global variable to store the Python callback
static PyObject* global_callback = NULL;

// This method is directly called from Python. This is the infrastructure part.
static PyObject* py_process_with_callback(PyObject* self, PyObject* args) {
    PyObject* callback_obj;
    
    // Parse arguments: expect a callable Python object
    if (!PyArg_ParseTuple(args, "O", &callback_obj)) {
        return NULL;
    }
    
    // Verify the callback is actually callable
    if (!PyCallable_Check(callback_obj)) {
        PyErr_SetString(PyExc_TypeError, "Argument must be callable");
        return NULL;
    }
    
    // Store the callback globally and increment its reference count
    global_callback = callback_obj;
    Py_INCREF(global_callback);
    
    // Call our C function with the wrapper
    int final_result = process_with_callback(python_callback_wrapper);
    
    // Decrement the reference count
    Py_DECREF(global_callback);
    global_callback = NULL;
    
    // Return result to Python
    return PyLong_FromLong(final_result);
}

// Business logic of method called from Python.
int process_with_callback(int (*callback)(int)) {
    if (!callback) {
        return -1;
    }
    
    // Simulate some processing
    int intermediate_value = 42;
    
    // Call back into Python with an intermediate result
    return callback(intermediate_value);
}

// This method calls back into Python
int python_callback_wrapper(int value) {
    PyGILState_STATE gstate = PyGILState_Ensure();
    
    // Call the Python function
    PyObject* py_result = PyObject_CallFunction(global_callback, "i", value);
    
    int result = -1;
    if (py_result) {
        result = PyLong_AsLong(py_result);
        Py_DECREF(py_result);
    }
    
    PyGILState_Release(gstate);
    
    return result;
}

// Module initialization function
PyMODINIT_FUNC PyInit_callback_module(void) {
    return PyModule_Create(&callbackmodule);
}

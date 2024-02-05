#include <Python.h>
#include <stdio.h>

/**
 * print_python_float_info - prints information about a Python float object
 * @p: pointer to the PyObject
 */
void print_python_float_info(PyObject *p)
{
    double value = 0;
    char *string_value = NULL;

    fflush(stdout);
    printf("[.] float object info\n");

    if (!PyFloat_CheckExact(p))
    {
        printf("  [ERROR] Invalid Float Object\n");
        return;
    }

    value = ((PyFloatObject *)p)->ob_fval;
    string_value = PyOS_double_to_string(value, 'r', 0, Py_DTSF_ADD_DOT_0, NULL);
    printf("  value: %s\n", string_value);
}

/**
 * print_python_bytes_info - prints information about a Python bytes object
 * @p: pointer to the PyObject
 */
void print_python_bytes_info(PyObject *p)
{
    Py_ssize_t size = 0, i = 0;
    char *string = NULL;

    fflush(stdout);
    printf("[.] bytes object info\n");

    if (!PyBytes_CheckExact(p))
    {
        printf("  [ERROR] Invalid Bytes Object\n");
        return;
    }

    size = PyBytes_Size(p);
    printf("  size: %zd\n", size);

    string = PyBytes_AsString(p);
    printf("  trying string: %s\n", string);

    printf("  first %zd bytes:", size < 10 ? size + 1 : 10);
    for (i = 0; i < size + 1 && i < 10; i++)
    {
        printf(" %02hhx", string[i]);
    }
    printf("\n");
}

/**
 * print_python_list_info - prints information about a Python list object
 * @p: pointer to the PyObject
 */
void print_python_list_info(PyObject *p)
{
    Py_ssize_t size = 0;
    PyObject *item;
    int i = 0;

    fflush(stdout);
    printf("[*] Python list info\n");

    if (!PyList_CheckExact(p))
    {
        printf("  [ERROR] Invalid List Object\n");
        return;
    }

    size = PyList_Size(p);
    printf("[*] Size of the Python List = %zd\n", size);
    printf("[*] Allocated = %zd\n", ((PyListObject *)p)->allocated);

    for (i = 0; i < size; i++)
    {
        item = PyList_GetItem(p, i);
        printf("Element %d: %s\n", i, item->ob_type->tp_name);
        if (PyBytes_Check(item))
            print_python_bytes_info(item);
        else if (PyFloat_Check(item))
            print_python_float_info(item);
    }
}


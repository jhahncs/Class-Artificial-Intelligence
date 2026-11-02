import nbformat

nb = nbformat.read('인공지능_3장_MNIST_MLP.ipynb', as_version=4)
code_idx = 1

for cell in nb.cells:
    if cell.cell_type == 'code':
        cell.execution_count = code_idx
        code_idx += 1

nbformat.write(nb, '인공지능_3장_MNIST_MLP.ipynb')
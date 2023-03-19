# Start from a core stack version
FROM jupyter/datascience-notebook:python-3.8
# Install in the default python3 environment

RUN conda install --quiet --yes zipline-reloaded quandl tensorflow pandas numpy gym=0.22.0 && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
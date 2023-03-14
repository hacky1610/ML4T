# Start from a core stack version
FROM jupyter/datascience-notebook:latest
# Install in the default python3 environment
RUN conda install --quiet --yes zipline-reloaded quandl && \
    conda clean --all -f -y && \
    fix-permissions "${CONDA_DIR}" && \
    fix-permissions "/home/${NB_USER}"
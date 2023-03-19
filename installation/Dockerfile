# Start from a core stack version
FROM jupyter/datascience-notebook:python-3.8
# Install in the default python3 environment
COPY ./linux/ml4t.yml /var/tmp/ml4t.yml
RUN conda create -n ml4t python=3.8
RUN mamba env update -n ml4t -f /var/tmp/ml4t.yml
RUN conda activate ml4t
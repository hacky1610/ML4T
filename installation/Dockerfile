# Start from a core stack version
FROM jupyter/datascience-notebook:python-3.8
# Install in the default python3 environment
COPY ./linux/ml4t.yml /var/tmp/ml4t1.yml
RUN conda create -n ml4t python=3.8
RUN mamba env update -n ml4t -f /var/tmp/ml4t1.yml
SHELL ["conda", "run", "-n", "ml4t", "/bin/bash", "-c"]
RUN conda install -c anaconda ipykernel
RUN python -m ipykernel install --user --name=ml4t

# Use miniconda image base from Dockerhub
FROM rocker/tidyverse:4.1.0

# Metadata
LABEL container.base.image = "rocker:tidyverse"
LABEL software.name = "qorts"

# Install system packages and AWS CLI
RUN apt-get -y update && \
    apt-get -y install python3.7 python3-pip
RUN pip install awscli boto3
RUN echo 'local({r <- getOption("repos"); r["CRAN"] <- "http://cran.r-project.org"; options(repos=r)})' > /.Rprofile
RUN R -e 'install.packages("png")'
RUN R -e 'install.packages("http://hartleys.github.io/QoRTs/QoRTs_STABLE.tar.gz", repos=NULL, type="source")'
RUN apt-get -y install default-jre
RUN ln -s /usr/local/lib/R/lib/libR.so /lib/x86_64-linux-gnu/libR.so

WORKDIR /

# copy relevant scripts to root dir
RUN mkdir -p global_utils/src
COPY src/run_main.py /
COPY src/qortsGenMultiQC.R /
COPY src/QoRTs.jar /
COPY src/global_utils/src/module_utils.py /global_utils/src/
COPY src/global_utils/src/file_utils.py /global_utils/src/
COPY src/global_utils/src/global_keys.py /global_utils/src/
COPY src/global_utils/src/aws_s3_utils.py /global_utils/src/
ENV PATH="/usr/local/bin/:/usr/bin/:$PATH"
RUN ln -s /usr/bin/python3.8 /usr/bin/python
ENTRYPOINT ["python","/run_main.py"] 

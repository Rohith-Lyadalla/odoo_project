# Use official Python image as a base
FROM python:3.12
LABEL authors="amunoz"

# Set working directory
WORKDIR /odoo

# Install system dependencies
RUN apt-get update && \
    apt-get install -y \
    build-essential \
    libxml2-dev \
    libssl-dev \
    libsasl2-dev \
    libldap2-dev \
    zlib1g-dev \
    libjpeg-dev \
    liblcms2-dev \
    libblas-dev \
    libatlas-base-dev \
    git \
    npm \
    node-less \
    && apt-get clean

# Copy the Odoo source code
COPY ./odoo/ /odoo/


# Copy the Odoo configuration file
#COPY ./odoo-git/odoo-18.0/ /app/

# Install Python dependencies
RUN  pip3 install --upgrade pip && \
     pip3 install -r requirements.txt
RUN  ./setup/debinstall.sh
# Expose default Odoo port
EXPOSE 8069

# Environment variable pointing to config
#ENV ODOO_CONFIG=/etc/odoo/odoo.conf
WORKDIR /odoo
RUN ls -l
RUN cat /odoo/odoo-conf
# Start Odoo
#CMD ["python", "odoo-bin", "-c", "/etc/odoo/odoo.conf"]
CMD ["python3", "odoo-bin",  "--config", "/odoo/odoo-conf", "--addons-path", "addons", "-d", "db"]
#CMD ["python3", "odoo-bin", "--addons-path=addons", "-d db"]

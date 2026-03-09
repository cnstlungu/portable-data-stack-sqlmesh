FROM python:3.11-slim

RUN apt-get update && apt-get install -y git make automake gcc g++ subversion && rm -rf /var/lib/apt/lists/*

RUN git clone -n --depth=1 --filter=tree:0 https://github.com/cnstlungu/postcard-company-datamart.git /datamart

WORKDIR /datamart

RUN git sparse-checkout set --no-cone postcard_company

RUN git checkout

WORKDIR /datamart/postcard_company

RUN pip install uv

COPY sqlmesh-dbt/requirements.txt sqlmesh-dbt/config.py /datamart/postcard_company/

RUN uv pip install --system -r requirements.txt

RUN dbt deps

CMD bash -c "sqlmesh plan --create-from prod --auto-apply & tail -f /dev/null"

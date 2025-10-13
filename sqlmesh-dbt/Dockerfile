FROM python:3.11

RUN apt-get install git make automake gcc g++ subversion

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
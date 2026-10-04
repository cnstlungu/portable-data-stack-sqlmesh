FROM python:3.11-slim

RUN pip install uv

COPY sqlmesh-dbt/requirements.txt /tmp/requirements.txt

RUN uv pip install --system -r /tmp/requirements.txt

WORKDIR /datamart/postcard_company

# The shared dbt model, from https://github.com/cnstlungu/postcard-company-datamart
# at DATAMART_REF. docker-compose.yml supplies it as the postcard_company build
# context, so there is no clone here.
COPY --from=postcard_company . .

COPY sqlmesh-dbt/config.py .

RUN dbt deps

CMD bash -c "sqlmesh plan --create-from prod --auto-apply & tail -f /dev/null"

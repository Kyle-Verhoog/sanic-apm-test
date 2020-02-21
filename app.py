from sanic import Sanic
from sanic.response import json
from sanic import response
from tracers import sanic_tracing
from tracers import asyncpg_connection
import db

app = Sanic()
sanic_tracing.init_tracer(app, {'apm_service_name': 'sanic-apm.test.anandh.local'})

@app.listener("before_server_start")
async def register_db(app, loop):
    await db.register_db(
            {'host':'localhost', 'user':'appuser', 'password': '', 'database': 'postgres'},
            asyncpg_connection.TracingConnection,
            loop
        )

@app.listener("after_server_stop")
async def cleanup(app, loop):
    await db.cleanup(loop)


@app.route('/')
async def test(request):
    return json({'hello': 'world'})


@app.route("/query")
async def query(request):
    result = await db.run_query()
    print(result)
    return json({'hello': 'sql'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)

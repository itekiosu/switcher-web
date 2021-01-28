import quart.flask_patch
import json
import asyncio
from aiofile import async_open
from quart import Quart, jsonify, send_file

app = Quart(__name__)

@app.route('/json')
async def redir():
    hosts = {
    "target": "Iteki",
    "data": {
      "servers": [
        {
          "host": "c.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "ce.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "c4.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "c5.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "c6.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "a.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "osu.ppy.sh",
          "newTarget": "144.91.70.152"
        },
        {
          "host": "bm6.ppy.sh",
          "newTarget": "144.91.70.152"
        }
      ]
    }
  }
    return jsonify(hosts)

if __name__ == '__main__':
    app.run(debug=True)


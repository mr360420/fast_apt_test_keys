import os

import uvicorn
from fastapi import FastAPI, APIRouter

from api.heandlers import router_for_ml

app = FastAPI(title='test_task_with_ml_model')

main_api_router = APIRouter()

main_api_router.include_router(router_for_ml, prefix='/api', tags=['ML'])
app.include_router(main_api_router)

if __name__ == '__main__':
    filename = os.path.basename(__file__)[:-3]
    uvicorn.run(f'{filename}:app', host='127.0.0.1',
                port=8000, reload=True, reload_delay=0.3
                )

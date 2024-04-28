from fastapi import APIRouter
from ml_functions.pick_regno import pick_regno
from api.models import MLData, MLDataResult
from pathlib import Path
from pprint import pprint

router_for_ml = APIRouter()


@router_for_ml.post("/work_with_pick_regno",
                    response_model=MLDataResult)
async def predict(data: list[MLData]):
    result_for_send = list()
    for input_data in data:
        result = pick_regno(input_data.regno_recognize,
                            input_data.afts_regno_ai,
                            input_data.recognition_accuracy,
                            input_data.afts_regno_ai_score,

                            input_data.afts_regno_ai_char_scores,
                            input_data.afts_regno_ai_length_scores,

                            input_data.camera_type,
                            input_data.camera_class,
                            input_data.time_check,
                            input_data.direction,
                            Path('db', 'micromodel.cbm')
                            )
        result_for_send.append(result.tolist())

    return MLDataResult(result=result_for_send)

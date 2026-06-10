modules = [
    'src',
    'src.utils',
    'src.exception',
    'src.logger',
    'src.pipeline',
    'src.pipeline.train_pipeline',
    'src.pipeline.predict_pipeline',
    'src.components.data_ingestion',
    'src.components.data_transformation',
    'src.components.model_trainer'
]
import importlib
for m in modules:
    try:
        importlib.import_module(m)
        print('OK', m)
    except Exception as e:
        print('ERR', m, type(e).__name__, e)

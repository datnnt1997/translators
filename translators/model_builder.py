from translators.configuration import Config
from translators.models import NMTModel, GNMT
from translators.cores.modules.inputters import tokenizer, BPETokenizer


def build_model(config: Config) -> NMTModel:
    if config.model_type == "GNMT":
        model = GNMT(config)
    else:
        model = None
    return model


def build_tokenizer(config: Config) -> tokenizer:
    t = BPETokenizer()


def build_examples(config: Config):
    raise NotImplementedError
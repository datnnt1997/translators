import os
import json
import torch.nn.init as init
import matplotlib.pyplot as plt

from translators.logger import logger


def plot_figure(save_dir: str, historys: dict):
    # plot train LOSS history
    plt.plot(historys['TRAIN_STEP_LOSSES'], label='TRAIN')
    plt.xlabel('STEP')
    plt.ylabel('LOSS')
    plt.title('Model Train Loss')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'train_loss.png'))
    plt.close()
    logger.info(f'Training loss diagrams was saved in {os.path.join(save_dir, "train_loss.png")} !!!')

    # plot train ACC history
    plt.plot(historys['TRAIN_STEP_ACCS'], label='TRAIN')
    plt.xlabel('STEP')
    plt.ylabel('ACC')
    plt.title('Model Train ACC')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'train_acc.png'))
    plt.close()
    logger.info(f'Training acc diagrams was saved in {os.path.join(save_dir, "train_acc.png")} !!!')

    # plot train PPL history
    plt.plot(historys['TRAIN_STEP_PPLS'], label='TRAIN')
    plt.xlabel('EPOCH')
    plt.ylabel('PPL')
    plt.title('Model Train Perplexity')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'train_perplexity.png'))
    plt.close()
    logger.info(f'Training ppl diagrams was saved in {os.path.join(save_dir, "train_perplexity.png")} !!!')
    # ========================================================================================================= #

    # plot eval LOSS history
    plt.plot(historys['AVG_EVAL_LOSSES'], label='EVAL')
    plt.xlabel('STEP')
    plt.ylabel('LOSS')
    plt.title('Model Eval Loss')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'eval_loss.png'))
    plt.close()
    logger.info(f'EVAL loss diagrams was saved in {os.path.join(save_dir, "eval_loss.png")} !!!')

    # plot eval ACC history
    plt.plot(historys['EVAL_ACCS'], label='EVAL')
    plt.xlabel('STEP')
    plt.ylabel('ACC')
    plt.title('Model Eval ACC')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'eval_acc.png'))
    plt.close()
    logger.info(f'EVAL acc diagrams was saved in {os.path.join(save_dir, "eval_acc.png")} !!!')

    # plot eval PPL history
    plt.plot(historys['EVAL_PPLS'], label='EVAL')
    plt.xlabel('STEP')
    plt.ylabel('PPL')
    plt.title('Model Eval Perplexity')
    plt.legend()
    plt.savefig(os.path.join(save_dir, 'eval_perplexity.png'))
    plt.close()
    logger.info(f'EVAL ppl diagrams was saved in {os.path.join(save_dir, "eval_perplexity.png")} !!!')


def save_train_history(save_dir: str, historys: dict):
    with open(os.path.join(save_dir, 'training_history.json'), "w", encoding="utf-8") as out:
        json.dump(historys, out)
    logger.info(f'Training history was saved in {os.path.join(save_dir, "training_history.png")} !!!')


def init_lstm_(lstm, init_weight=0.1):
    """
    Initializes weights of LSTM layer.
    Weights and biases are initialized with uniform(-init_weight, init_weight)
    distribution.
    :param lstm: instance of torch.nn.LSTM
    :param init_weight: range for the uniform initializer
    """
    # Initialize hidden-hidden weights
    init.uniform_(lstm.weight_hh_l0.data, -init_weight, init_weight)
    # Initialize input-hidden weights:
    init.uniform_(lstm.weight_ih_l0.data, -init_weight, init_weight)

    # Initialize bias. PyTorch LSTM has two biases, one for input-hidden GEMM
    # and the other for hidden-hidden GEMM. Here input-hidden bias is
    # initialized with uniform distribution and hidden-hidden bias is
    # initialized with zeros.
    init.uniform_(lstm.bias_ih_l0.data, -init_weight, init_weight)
    init.zeros_(lstm.bias_hh_l0.data)

    if lstm.bidirectional:
        init.uniform_(lstm.weight_hh_l0_reverse.data, -init_weight, init_weight)
        init.uniform_(lstm.weight_ih_l0_reverse.data, -init_weight, init_weight)

        init.uniform_(lstm.bias_ih_l0_reverse.data, -init_weight, init_weight)
        init.zeros_(lstm.bias_hh_l0_reverse.data)

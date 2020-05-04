import os
import pickle
import sys

import save_restore_generators as jump


class Checkpoint:
    def __init__(self, name):
        self.name = name
        self.generator_state = None


def save_checkpoints(gen):
    os.makedirs("__checkpoints__", exist_ok=True)
    for ckpt in gen:
        ckpt.generator_state = jump.save_generator_state(gen)
        pickle.dump(ckpt, open(os.path.join("__checkpoints__", ckpt.name), "wb"))


def processing():
    lst = []
    step = "step1"
    a = 1
    lst.append(step)
    print(step, lst)
    yield Checkpoint("step1")

    step = "step2"
    b = 2
    a *= 2
    lst.append(step)
    print(step, lst)
    yield Checkpoint("step2")

    step = "step3"
    c = 2
    a *= 2
    lst.append(step)
    print(step, lst)
    yield Checkpoint("step3")

    print("end")


def main():
    if len(sys.argv) > 1:
        # Restore the requested checkpoint
        ckpt = pickle.load(open(os.path.join("__checkpoints__", sys.argv[1]), "rb"))
        gen_restored = jump.restore_generator(processing(), ckpt.generator_state)
        for _ in gen_restored:
            pass
    else:
        # Do a full run
        print("Running to completition and dumping checkpoints")
        checkpoints = save_checkpoints(processing())
        print("Re-run passing checkpoint filename to restart")


main()

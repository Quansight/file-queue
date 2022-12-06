import argparse
import importlib


def cli():
    parser = argparse.ArgumentParser(help="file-queue worker")
    parser.add_argument("queue path", type=str, default=".")
    parser.add_argument(
        "--lock-class", action=ParseClassImport, default="file_queue.core.DummyLock"
    )
    parser.add_argument(
        "--job-serializer-class",
        action=ParseClassImport,
        default="file_queue.core.JSONSerializer",
    )
    parser.add_argument(
        "--result-serializer-class",
        action=ParseClassImport,
        default="file_queue.core.JSONSerializer",
    )
    parser.add_argument(
        "--queue-class", action=ParseClassImport, default="file_queue.core.Queue"
    )
    parser.add_argument(
        "--job-class", action=ParseClassImport, default="file_queue.core.Job"
    )
    parser.add_argument(
        "--worker-class", action=ParseClassImport, default="file_queue.core.Worker"
    )
    return handle_cli(parser.parse_args())


class ParseClassImport(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None, first=[True]):
        _values = []
        for value in values:
            module, function = values[0].rsplit(".", 1)
            _values.append(getattr(importlib.import_module(module), function))
        setattr(namespace, self.dest, values)


def handle_cli(args):
    queue = args.queue_class(
        directory=args.path,
        job_serializer_class=args.job_serializer_class,
        result_serializer_class=args.result_serializer_class,
        lock_class=args.lock_class,
        job_class=args.job_class,
    )
    worker = args.worker_class(
        queue=queue,
    )
    worker.run()

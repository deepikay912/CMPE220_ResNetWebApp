
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import argparse
import traceback

from converter import ModelConverter

parser = argparse.ArgumentParser(
    description='Exports TensorflowJS model to Keras')

parser.add_argument(
    '--config_json_path',
    help='Path to the TensorFlow.js weights manifest file '
    'containing the model architecture (model.json)',
    action='store',
    required=True,
    dest='config_json_path',
    type=str)
parser.add_argument(
    '--weights_path_prefix',
    help='Optional path to weights files (model.weights.bin). '
    'If not specified (`None`), will assume the prefix is the same directory '
    'as the dirname of `model_json` with name `model.weights.bin',
    action='store',
    required=False,
    dest='weights_path_prefix',
    type=str,
    default=None)

parser.add_argument(
    '--model_tflite',
    help='Converted tflite model file',
    action='store',
    required=False,
    dest='model_tflite',
    type=str,
    default='model.tflite')

args = parser.parse_args()
parser.print_help()
print('input args: ', args)

try:
  converter = ModelConverter(args.config_json_path, args.weights_path_prefix,
                             args.model_tflite)

  converter.convert()

except ValueError as e:
  print(traceback.format_exc())
  print('Error occurred while converting')

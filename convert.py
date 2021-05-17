import os
import numpy as np
from glob import glob                                                           
from pathlib import Path
from tqdm import tqdm

#YOLO Labels: <object-class> <x> <y> <width> <height>

dataset_root_path = '/media/bjarne/ssd/Forschungsarbeit/SeeingThroughFog/'

from header_imports import *
from color_cube_model_training import *

if __name__ == "__main__":
    
    # Begin analysis for building model or training it
    if len(sys.argv) != 1:
        if sys.argv[1] == "model_building":
            brain_analysis_obj = color_cube_building(model_type = sys.argv[2])

        # Seperate images base on names
        if sys.argv[1] == "model_training":
            brain_analysis_obj = color_cube_training(model_type = sys.argv[2])

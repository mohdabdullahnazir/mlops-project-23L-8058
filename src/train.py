"""Standard training entry point for Student ID 23L-8058."""

from pathlib import Path
import runpy


STUDENT_SCRIPT = Path(__file__).with_name("train_model_23L-8058.py")


if __name__ == "__main__":
    runpy.run_path(str(STUDENT_SCRIPT), run_name="__main__")
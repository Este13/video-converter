# Import the subprocess module
import subprocess

# Define the input and output file paths  /!\ every backslash of the paths needs to be doubled /!\
input_file = "C:\\User\\Videos\\input.avi"
output_file = "C:\\User\\Videos\\output.mp4"

# Run the ffmpeg command to convert the video file
subprocess.run(["ffmpeg", "-i", input_file, output_file])

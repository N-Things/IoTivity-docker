import os
import subprocess

apps_dir = os.getenv('LD_LIBRARY_PATH', '') + '/resource/examples'
samples = {
    'Simple Server (C++)': 'simpleserver',
    'Simple Client (C++)': 'simpleclient',
}
samples_list = [pair for pair in enumerate(samples)]

print("Choose the sample app: \n")

for index, key in enumerate(samples):
    print(index, '-', key)

app = input("> ")

#print(samples[samples_list[int(app)][1]])

# TODO: remove hardcoded argument for the simpleserver sample.

subprocess.run(
    ['./' + samples[samples_list[int(app)][1]], '2'],
    cwd=apps_dir,
)

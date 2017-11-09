# iotivity-docker
----

There are two Dockerfiles:
* base: fetch and build iotivity and also set the ```LD_LIBRARY_PATH```
* samples: execute the sample apps provided by IoTivity

#### Building the images
* ``` cd base/ && docker build -t thiagogcm/iotivity-base . ```
* ``` cd samples/ && docker build -t thiagogcm/iotivity-samples . ```

#### Running the samples

* ``` docker run -it --rm thiagogcm/iotivity-samples ```
* Choose the Server App
* Open a new terminal window
* ``` docker run -it --rm thiagogcm/iotivity-samples ```
* Choose the Client App

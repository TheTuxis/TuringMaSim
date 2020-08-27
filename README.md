# TuringMaSim

Is a simple turing machine simulator.

## How Install ##
 0. Install tk
    ```shell
    $ sudo apt-get install python3-tk graphviz
    ```
 1. Create virualenv 
    ```shell
    $ virtualenv venv -p python3
    ```
 2. Activate virutalenv
     ```shell
    $ source venv/bin/activate
    ```
 3. Install requirement.txt
    ```shell
    $ pip install -r requirement.txt
    ```
 4. Go to src 
    ```shell
    $ cd src
    ```
 5. run main.py
    ```shell
    $ python main.py
    ```

## Run Docker
 0. Build Docker Image
    ```shell
    $ docker build . -t turingmasim:latest
    ```
 1. Set-up
    ```shell
    $ xhost +local:docker
    ```
 2. Run TuringMaSim
    ```shell
    $ docker run -e DISPLAY=$DISPLAY -v /tmp/.X11-unix:/tmp/.X11-unix turingmasim
    ```

## How Use

*WORK IN PROGRESS* 

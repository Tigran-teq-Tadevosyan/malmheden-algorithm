# Implementaion of Malmheden Algorithm for solving Dirichlet Problem in disk

## Description
This little program is computing the value of harmonic function after calculating it with Malmheden method
It only works for disk boundry conditions
It takes as an input radius of the disk ( which is centered at (0,0) ) and the values of x,y coordinates and boundry conditions function from set of selected functions ( Potentialy it could work with and functions I just could not found a way for user to input it's own function ) and outputs the harmonic function's value at that point
Program was tested on 'Ubuntu 16.04' with 'Python 3.6.5 |Anaconda, Inc.|'

## Some Screenshots

![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/malmheden-algorithm/master/screenshots/first.png)
![alt text](https://raw.githubusercontent.com/Tigran-teq-Tadevosyan/malmheden-algorithm/master/screenshots/second.png)

## Installation and Excution

1. Install PyQt5
    ```shell
    pip install PyQt5
    ```
2. Install scipy
    ```shell
    pip install scipy
    ```
3. Install numpy
    ```shell
    pip install numpy
    ```
4. Run the program by going to the directory
    * If you are using Windows run
    ```bash
    ./run.bat
    ```
    * If you are using OSX/Linux run
    ```shell
    sudo chmod -x ./run.sh # This will make 'run.sh' shell script executable so it must be executed just ones
    ./run.sh
    ```
## License
[MIT](https://choosealicense.com/licenses/mit/)
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "mount_file_id": "1cOkZeNse_IBpneqS5ytiHnefh3Fvh2GR",
      "authorship_tag": "ABX9TyPqqtTdzLdULo1pO4dW7oSD"
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "code",
      "execution_count": 25,
      "metadata": {
        "id": "pDKJCZIsC14M"
      },
      "outputs": [],
      "source": [
        "import numpy as np\n",
        "import pandas as pd\n",
        "import matplotlib.pyplot as plt"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "data=pd.read_csv('/content/Salary_Data.csv')\n",
        "x=data.iloc[:,:-1].values\n",
        "y=data.iloc[:,1:2].values"
      ],
      "metadata": {
        "id": "hafUIUqkDJ6N"
      },
      "execution_count": 26,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "print(x)\n",
        "print(y)"
      ],
      "metadata": {
        "id": "TTWBO4PUdF6f",
        "outputId": "c4294c4d-5877-45cd-c22e-c2660c8988f1",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 27,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ 1.1]\n",
            " [ 1.3]\n",
            " [ 1.5]\n",
            " [ 2. ]\n",
            " [ 2.2]\n",
            " [ 2.9]\n",
            " [ 3. ]\n",
            " [ 3.2]\n",
            " [ 3.2]\n",
            " [ 3.7]\n",
            " [ 3.9]\n",
            " [ 4. ]\n",
            " [ 4. ]\n",
            " [ 4.1]\n",
            " [ 4.5]\n",
            " [ 4.9]\n",
            " [ 5.1]\n",
            " [ 5.3]\n",
            " [ 5.9]\n",
            " [ 6. ]\n",
            " [ 6.8]\n",
            " [ 7.1]\n",
            " [ 7.9]\n",
            " [ 8.2]\n",
            " [ 8.7]\n",
            " [ 9. ]\n",
            " [ 9.5]\n",
            " [ 9.6]\n",
            " [10.3]\n",
            " [10.5]]\n",
            "[[ 39343.]\n",
            " [ 46205.]\n",
            " [ 37731.]\n",
            " [ 43525.]\n",
            " [ 39891.]\n",
            " [ 56642.]\n",
            " [ 60150.]\n",
            " [ 54445.]\n",
            " [ 64445.]\n",
            " [ 57189.]\n",
            " [ 63218.]\n",
            " [ 55794.]\n",
            " [ 56957.]\n",
            " [ 57081.]\n",
            " [ 61111.]\n",
            " [ 67938.]\n",
            " [ 66029.]\n",
            " [ 83088.]\n",
            " [ 81363.]\n",
            " [ 93940.]\n",
            " [ 91738.]\n",
            " [ 98273.]\n",
            " [101302.]\n",
            " [113812.]\n",
            " [109431.]\n",
            " [105582.]\n",
            " [116969.]\n",
            " [112635.]\n",
            " [122391.]\n",
            " [121872.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.model_selection import train_test_split\n",
        "xtr,xt,ytr,yt=train_test_split(x,y,test_size=0.3,random_state=2)\n",
        "print(xtr)\n",
        "print(ytr)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9t6vOPd5DmBy",
        "outputId": "8a771468-3455-4c48-8e6d-c7dede64d0e3"
      },
      "execution_count": 28,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[ 6.8]\n",
            " [ 2.9]\n",
            " [ 9.6]\n",
            " [ 4. ]\n",
            " [ 2.2]\n",
            " [ 3.9]\n",
            " [ 5.1]\n",
            " [10.3]\n",
            " [ 9. ]\n",
            " [ 5.3]\n",
            " [ 1.5]\n",
            " [ 3.2]\n",
            " [ 9.5]\n",
            " [ 8.7]\n",
            " [ 5.9]\n",
            " [ 4. ]\n",
            " [ 7.9]\n",
            " [10.5]\n",
            " [ 4.1]\n",
            " [ 4.9]\n",
            " [ 3.2]]\n",
            "[[ 91738.]\n",
            " [ 56642.]\n",
            " [112635.]\n",
            " [ 56957.]\n",
            " [ 39891.]\n",
            " [ 63218.]\n",
            " [ 66029.]\n",
            " [122391.]\n",
            " [105582.]\n",
            " [ 83088.]\n",
            " [ 37731.]\n",
            " [ 54445.]\n",
            " [116969.]\n",
            " [109431.]\n",
            " [ 81363.]\n",
            " [ 55794.]\n",
            " [101302.]\n",
            " [121872.]\n",
            " [ 57081.]\n",
            " [ 67938.]\n",
            " [ 64445.]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "from sklearn.linear_model import LinearRegression\n",
        "Lr=LinearRegression()\n",
        "Lr.fit(xtr,ytr)\n",
        "print(xt)\n",
        "yp=Lr.predict(xt)\n",
        "print(yp)"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "eeyrdPmSEamc",
        "outputId": "7d0c6692-690b-4751-f795-84435a07a1d3"
      },
      "execution_count": 29,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "[[1.3]\n",
            " [1.1]\n",
            " [4.5]\n",
            " [3.7]\n",
            " [7.1]\n",
            " [6. ]\n",
            " [8.2]\n",
            " [3. ]\n",
            " [2. ]]\n",
            "[[ 36143.62176044]\n",
            " [ 34237.05465324]\n",
            " [ 66648.69547576]\n",
            " [ 59022.42704693]\n",
            " [ 91434.06786946]\n",
            " [ 80947.94877982]\n",
            " [101920.1869591 ]\n",
            " [ 52349.44217171]\n",
            " [ 42816.60663567]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "plt.scatter(xtr,ytr,color='Blue')\n",
        "plt.plot(xtr,Lr.predict(xtr),color='Green')\n",
        "plt.title('Salary Predict')\n",
        "plt.xlabel('Experience(years)')\n",
        "plt.ylabel('Salary(in rupees)')\n",
        "plt.show()"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 472
        },
        "id": "RuIAwievG_aM",
        "outputId": "688672b4-5a5a-4779-a5e0-fdcb910d7712"
      },
      "execution_count": 30,
      "outputs": [
        {
          "output_type": "display_data",
          "data": {
            "text/plain": [
              "<Figure size 640x480 with 1 Axes>"
            ],
            "image/png": "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\n"
          },
          "metadata": {}
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "print(f\"Expected salary is{Lr.predict([[22]])}\")"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "9pyG-mi1Ji47",
        "outputId": "83a4ef6c-c3d5-438c-f397-967b8aab4a5e"
      },
      "execution_count": 31,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Expected salary is[[233473.3173564]]\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "B8gXwFAzLOv5"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "EjQCg_4seoaY"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
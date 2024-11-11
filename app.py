{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOYuhCp3BP6kz0MQhVi4h9Q",
      "include_colab_link": true
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
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/syedaayesha2309/scientific-calculator/blob/main/app.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Importing necessary libraries\n",
        "import math\n",
        "\n",
        "def scientific_calculator():\n",
        "    print(\"Welcome to the Scientific Calculator!\")\n",
        "    print(\"Available operations:\")\n",
        "    print(\"1. Addition (+)\")\n",
        "    print(\"2. Subtraction (-)\")\n",
        "    print(\"3. Multiplication (*)\")\n",
        "    print(\"4. Division (/)\")\n",
        "    print(\"5. Power (x^y)\")\n",
        "    print(\"6. Square root (√x)\")\n",
        "    print(\"7. Logarithm (log base 10)\")\n",
        "    print(\"8. Sine (sin)\")\n",
        "    print(\"9. Cosine (cos)\")\n",
        "    print(\"10. Tangent (tan)\")\n",
        "    print(\"11. Exit\")\n",
        "\n",
        "    while True:\n",
        "        choice = input(\"\\nEnter the number corresponding to your choice of operation (1-11): \")\n",
        "\n",
        "        if choice == '11':\n",
        "            print(\"Exiting the calculator. Goodbye!\")\n",
        "            break\n",
        "\n",
        "        if choice in ['1', '2', '3', '4', '5']:\n",
        "            try:\n",
        "                num1 = float(input(\"Enter the first number: \"))\n",
        "                num2 = float(input(\"Enter the second number: \"))\n",
        "            except ValueError:\n",
        "                print(\"Invalid input! Please enter numeric values.\")\n",
        "                continue\n",
        "\n",
        "        if choice == '1':\n",
        "            print(f\"The result is: {num1 + num2}\")\n",
        "        elif choice == '2':\n",
        "            print(f\"The result is: {num1 - num2}\")\n",
        "        elif choice == '3':\n",
        "            print(f\"The result is: {num1 * num2}\")\n",
        "        elif choice == '4':\n",
        "            if num2 != 0:\n",
        "                print(f\"The result is: {num1 / num2}\")\n",
        "            else:\n",
        "                print(\"Error! Division by zero.\")\n",
        "        elif choice == '5':\n",
        "            print(f\"The result is: {num1 ** num2}\")\n",
        "        elif choice == '6':\n",
        "            try:\n",
        "                num = float(input(\"Enter the number: \"))\n",
        "                if num >= 0:\n",
        "                    print(f\"The square root of {num} is: {math.sqrt(num)}\")\n",
        "                else:\n",
        "                    print(\"Error! Square root of a negative number is not supported.\")\n",
        "            except ValueError:\n",
        "                print(\"Invalid input! Please enter a numeric value.\")\n",
        "        elif choice == '7':\n",
        "            try:\n",
        "                num = float(input(\"Enter the number: \"))\n",
        "                if num > 0:\n",
        "                    print(f\"The logarithm base 10 of {num} is: {math.log10(num)}\")\n",
        "                else:\n",
        "                    print(\"Error! Logarithm for non-positive numbers is not defined.\")\n",
        "            except ValueError:\n",
        "                print(\"Invalid input! Please enter a numeric value.\")\n",
        "        elif choice == '8':\n",
        "            try:\n",
        "                angle = float(input(\"Enter the angle in degrees: \"))\n",
        "                print(f\"The sine of {angle} degrees is: {math.sin(math.radians(angle))}\")\n",
        "            except ValueError:\n",
        "                print(\"Invalid input! Please enter a numeric value.\")\n",
        "        elif choice == '9':\n",
        "            try:\n",
        "                angle = float(input(\"Enter the angle in degrees: \"))\n",
        "                print(f\"The cosine of {angle} degrees is: {math.cos(math.radians(angle))}\")\n",
        "            except ValueError:\n",
        "                print(\"Invalid input! Please enter a numeric value.\")\n",
        "        elif choice == '10':\n",
        "            try:\n",
        "                angle = float(input(\"Enter the angle in degrees: \"))\n",
        "                print(f\"The tangent of {angle} degrees is: {math.tan(math.radians(angle))}\")\n",
        "            except ValueError:\n",
        "                print(\"Invalid input! Please enter a numeric value.\")\n",
        "        else:\n",
        "            print(\"Invalid input! Please enter a number between 1 and 11.\")\n",
        "\n",
        "# Run the calculator\n",
        "scientific_calculator()\n"
      ],
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/"
        },
        "id": "ox_RWPlwLV27",
        "outputId": "00996316-d9a3-4025-edae-0cbd4be362e2"
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Welcome to the Scientific Calculator!\n",
            "Available operations:\n",
            "1. Addition (+)\n",
            "2. Subtraction (-)\n",
            "3. Multiplication (*)\n",
            "4. Division (/)\n",
            "5. Power (x^y)\n",
            "6. Square root (√x)\n",
            "7. Logarithm (log base 10)\n",
            "8. Sine (sin)\n",
            "9. Cosine (cos)\n",
            "10. Tangent (tan)\n",
            "11. Exit\n",
            "\n",
            "Enter the number corresponding to your choice of operation (1-11): 1\n",
            "Enter the first number: 2\n",
            "Enter the second number: 2\n",
            "The result is: 4.0\n"
          ]
        }
      ]
    }
  ]
}
{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "provenance": [],
      "authorship_tag": "ABX9TyOrQG5WtfsaQZeAbm0WThet",
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
      "execution_count": 2,
      "metadata": {
        "colab": {
          "base_uri": "https://localhost:8080/",
          "height": 703
        },
        "id": "iS0IATDszSS9",
        "outputId": "68d15125-8eda-471f-ca53-45bdbfa60890"
      },
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "Select operation:\n",
            "1. Addition\n",
            "2. Subtraction\n",
            "3. Multiplication\n",
            "4. Division\n",
            "5. Power\n",
            "6. Square Root\n",
            "7. Sine\n",
            "8. Cosine\n",
            "9. Tangent\n",
            "\n",
            "Enter choice (1/2/3/4/5/6/7/8/9): 9\n",
            "Enter the number: 5\n",
            "Tangent(5.0) = 0.08748866352592401\n",
            "\n",
            "Do you want to perform another calculation? (yes/no): yes\n",
            "\n",
            "Enter choice (1/2/3/4/5/6/7/8/9): 3\n",
            "Enter first number: 6\n",
            "Enter second number: 2\n",
            "6.0 * 2.0 = 12.0\n"
          ]
        },
        {
          "output_type": "error",
          "ename": "KeyboardInterrupt",
          "evalue": "Interrupted by user",
          "traceback": [
            "\u001b[0;31m---------------------------------------------------------------------------\u001b[0m",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m                         Traceback (most recent call last)",
            "\u001b[0;32m<ipython-input-2-8ea16cd1683c>\u001b[0m in \u001b[0;36m<cell line: 60>\u001b[0;34m()\u001b[0m\n\u001b[1;32m     58\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     59\u001b[0m \u001b[0;31m# Run the calculator function\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 60\u001b[0;31m \u001b[0mscientific_calculator\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m",
            "\u001b[0;32m<ipython-input-2-8ea16cd1683c>\u001b[0m in \u001b[0;36mscientific_calculator\u001b[0;34m()\u001b[0m\n\u001b[1;32m     53\u001b[0m             \u001b[0mprint\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid input\"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     54\u001b[0m \u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m---> 55\u001b[0;31m         \u001b[0mnext_calculation\u001b[0m \u001b[0;34m=\u001b[0m \u001b[0minput\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"\\nDo you want to perform another calculation? (yes/no): \"\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m     56\u001b[0m         \u001b[0;32mif\u001b[0m \u001b[0mnext_calculation\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlower\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;34m!=\u001b[0m \u001b[0;34m'yes'\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m     57\u001b[0m             \u001b[0;32mbreak\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36mraw_input\u001b[0;34m(self, prompt)\u001b[0m\n\u001b[1;32m    849\u001b[0m                 \u001b[0;34m\"raw_input was called, but this frontend does not support input requests.\"\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    850\u001b[0m             )\n\u001b[0;32m--> 851\u001b[0;31m         return self._input_request(str(prompt),\n\u001b[0m\u001b[1;32m    852\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_ident\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    853\u001b[0m             \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0m_parent_header\u001b[0m\u001b[0;34m,\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;32m/usr/local/lib/python3.10/dist-packages/ipykernel/kernelbase.py\u001b[0m in \u001b[0;36m_input_request\u001b[0;34m(self, prompt, ident, parent, password)\u001b[0m\n\u001b[1;32m    893\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    894\u001b[0m                 \u001b[0;31m# re-raise KeyboardInterrupt, to truncate traceback\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0;32m--> 895\u001b[0;31m                 \u001b[0;32mraise\u001b[0m \u001b[0mKeyboardInterrupt\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Interrupted by user\"\u001b[0m\u001b[0;34m)\u001b[0m \u001b[0;32mfrom\u001b[0m \u001b[0;32mNone\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[0m\u001b[1;32m    896\u001b[0m             \u001b[0;32mexcept\u001b[0m \u001b[0mException\u001b[0m \u001b[0;32mas\u001b[0m \u001b[0me\u001b[0m\u001b[0;34m:\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n\u001b[1;32m    897\u001b[0m                 \u001b[0mself\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mlog\u001b[0m\u001b[0;34m.\u001b[0m\u001b[0mwarning\u001b[0m\u001b[0;34m(\u001b[0m\u001b[0;34m\"Invalid Message:\"\u001b[0m\u001b[0;34m,\u001b[0m \u001b[0mexc_info\u001b[0m\u001b[0;34m=\u001b[0m\u001b[0;32mTrue\u001b[0m\u001b[0;34m)\u001b[0m\u001b[0;34m\u001b[0m\u001b[0;34m\u001b[0m\u001b[0m\n",
            "\u001b[0;31mKeyboardInterrupt\u001b[0m: Interrupted by user"
          ]
        }
      ],
      "source": [
        "import math\n",
        "\n",
        "def scientific_calculator():\n",
        "    print(\"Select operation:\")\n",
        "    print(\"1. Addition\")\n",
        "    print(\"2. Subtraction\")\n",
        "    print(\"3. Multiplication\")\n",
        "    print(\"4. Division\")\n",
        "    print(\"5. Power\")\n",
        "    print(\"6. Square Root\")\n",
        "    print(\"7. Sine\")\n",
        "    print(\"8. Cosine\")\n",
        "    print(\"9. Tangent\")\n",
        "\n",
        "    while True:\n",
        "        # Take input from the user\n",
        "        choice = input(\"\\nEnter choice (1/2/3/4/5/6/7/8/9): \")\n",
        "\n",
        "        if choice in ['1', '2', '3', '4', '5']:\n",
        "            num1 = float(input(\"Enter first number: \"))\n",
        "            num2 = float(input(\"Enter second number: \"))\n",
        "\n",
        "            if choice == '1':\n",
        "                print(f\"{num1} + {num2} = {num1 + num2}\")\n",
        "            elif choice == '2':\n",
        "                print(f\"{num1} - {num2} = {num1 - num2}\")\n",
        "            elif choice == '3':\n",
        "                print(f\"{num1} * {num2} = {num1 * num2}\")\n",
        "            elif choice == '4':\n",
        "                if num2 == 0:\n",
        "                    print(\"Error! Division by zero.\")\n",
        "                else:\n",
        "                    print(f\"{num1} / {num2} = {num1 / num2}\")\n",
        "            elif choice == '5':\n",
        "                print(f\"{num1} ^ {num2} = {math.pow(num1, num2)}\")\n",
        "\n",
        "        elif choice in ['6', '7', '8', '9']:\n",
        "            num = float(input(\"Enter the number: \"))\n",
        "\n",
        "            if choice == '6':\n",
        "                if num < 0:\n",
        "                    print(\"Error! Cannot find the square root of a negative number.\")\n",
        "                else:\n",
        "                    print(f\"Square root of {num} = {math.sqrt(num)}\")\n",
        "            elif choice == '7':\n",
        "                print(f\"Sine({num}) = {math.sin(math.radians(num))}\")\n",
        "            elif choice == '8':\n",
        "                print(f\"Cosine({num}) = {math.cos(math.radians(num))}\")\n",
        "            elif choice == '9':\n",
        "                print(f\"Tangent({num}) = {math.tan(math.radians(num))}\")\n",
        "\n",
        "        else:\n",
        "            print(\"Invalid input\")\n",
        "\n",
        "        next_calculation = input(\"\\nDo you want to perform another calculation? (yes/no): \")\n",
        "        if next_calculation.lower() != 'yes':\n",
        "            break\n",
        "\n",
        "# Run the calculator function\n",
        "scientific_calculator()\n"
      ]
    },
    {
      "cell_type": "code",
      "source": [],
      "metadata": {
        "id": "ox_RWPlwLV27"
      },
      "execution_count": null,
      "outputs": []
    }
  ]
}
{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "import csv\n",
    "f = open('정보숙제.csv')\n",
    "\n",
    "data = csv.reader(f)\n",
    "max = 0\n",
    "min = 100000\n",
    "g= []\n",
    "t=0\n",
    "for row in data: \n",
    "    d = int(row[1])-t\n",
    "    t = int(row[1])\n",
    "    if int(d) >= int(max) : \n",
    "        max = d\n",
    "        maxd = row[0]\n",
    "    if int(d) <= int(min) : \n",
    "        min = d\n",
    "        mind = row[0]\n",
    "    g.append(d)\n",
    "import matplotlib.pyplot as plt\n",
    "plt.plot(g)\n",
    "plt.show()\n",
    "print(\"최댓값은\")\n",
    "print(maxd)\n",
    "print(\"일때\")\n",
    "print(max)\n",
    "print(\"최솟값은\")\n",
    "print(mind)\n",
    "print(\"일때\")\n",
    "print(min)\n",
    "\n",
    "# 나머지는 row[]안의 숫자만 바꾼 것이기 때문에 생략했습니다. \n",
    "# 1506 곽준혁 1507 김동규"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.6.4"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}

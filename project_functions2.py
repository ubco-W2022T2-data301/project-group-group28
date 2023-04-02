{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cdf9772-0625-4264-979f-27a50b3e84d3",
   "metadata": {},
   "outputs": [],
   "source": [
    "def load_and_process(path):\n",
    "    df = pd.read_csv(path).drop(df.columns[[1,8,11,12]], axis = 1).rename(columns = {\"CO2 emissions\": \"CO2\"})\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
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
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}

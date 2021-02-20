import pandas as pd
import matplotlib.pyplot as plt

# Acquire the data and create our environment
plt.style.use(style='ggplot')
plt.rcParams['figure.figsize'] = (10 ,6)

# training data set
train_data = pd.read_csv('data.csv')

# Show a data set of Sale Price
print('Sale Price Info:', '\n', train_data.SalePrice.describe(), '\n')

# Show a data set of Garage Area
print('Garage Area Info: ', '\n', train_data.GarageArea.describe(), '\n')

# Print plot without Outlier data
plt.scatter(train_data.GarageArea, train_data.SalePrice, color='black')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()

# Outlier data for GarageArea
outlier = train_data[(train_data['GarageArea'] <= 999) & (train_data['GarageArea'] >= 100)]

# Print plot with Outlier data
plt.scatter(outlier.GarageArea, outlier.SalePrice, color='green')
plt.xlabel('GarageArea')
plt.ylabel('SalePrice')
plt.show()

# Print higher Anomalies
print('Higher Anomalies: ', '\n', train_data[(train_data['GarageArea'] <= 1460) & (train_data['GarageArea'] >= 1000)])

# Print Lower Anomalies
print('Lower Anomalies: ', '\n', train_data[(train_data['GarageArea'] <= 99) & (train_data['GarageArea'] >= 0)])


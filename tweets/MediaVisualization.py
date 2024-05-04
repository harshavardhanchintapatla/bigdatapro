import pandas as pd
import matplotlib.pyplot as plt

# Convert Spark DataFrame to Pandas DataFrame for visualization
media_usage_pd = media_usage_results.toPandas()

# Plotting
plt.figure(figsize=(10, 6))
plt.bar(media_usage_pd['type'], media_usage_pd['count'], color='blue')
plt.xlabel('Media Type')
plt.ylabel('Count')
plt.title('Count of Each Media Type in Tweets')
plt.xticks(rotation=45)
plt.show()
---
source_url: https://docs.aws.amazon.com/connect-decisions/legacy/userguide/demand-patterns-recommendations.html
---

# Demand Patterns Recommendations
<a name="demand-patterns-recommendations"></a>

The system provides targeted recommendations based on identified demand patterns to help improve forecast accuracy. For products displaying erratic demand, characterized by irregular spikes in order volume, the system suggests incorporating potential external influences, such as promotions or price changes. In such cases, you can significantly improve forecast accuracy by collaborating with your data administrator to upload relevant demand driver data to the [**Supplementary Time Series**](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/demand_drivers.html) table in the data lake. This additional context helps the forecasting models better understand and predict demand fluctuations.

For products with insufficient history (less than 2 years) or no history at all, the system recommends leveraging alternate product mapping. This approach allows you to utilize the demand patterns of similar, established products to enhance forecast reliability. Work with your data administrator to upload these product relationships to the [**Product Alternate**](https://docs.aws.amazon.com/aws-supply-chain/latest/userguide/product_lineage.html) table in the data lake. This is particularly important because accurate seasonality and long-term trend detection requires at least 2 full years of historical data. By mapping to alternate products with sufficient history, you can establish a more reliable forecast baseline for newer or limited-history products.

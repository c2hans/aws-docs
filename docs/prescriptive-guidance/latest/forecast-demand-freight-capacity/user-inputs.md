---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/user-inputs.html
---

# User inputs for forecasting freight demand
<a name="user-inputs"></a>

Although the futures of most of the features are unknown, there may be some features that the business has control over. For example, price is one feature that usually has a strong relationship with demand volume. Because the business sets prices, you know when prices will increase or when there will be a discount or promotion. In addition, the size of the sales team can also affect demand volume, and businesses control how big their sales teams are. For these data points that the business manages, you can provide user inputs. In the ML modeling step, the 1D time series models give a forecast for each feature, then users can examine these forecasted values and overwrite them with user inputs. These overwritten inputs are then used in the model when making the final forecast.

This user input step can be critical in situations where the 1D time series model forecasts do not match the business's expectations of the feature's future behavior. You can overwrite these forecasted values, which can improve the overall output forecast.

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/introduction.html
---

# Forecasting demand for freight capacity by using Amazon SageMaker AI
<a name="introduction"></a>

*Tianxia Jia and Hengzhi Chen, Amazon Web Services*

Demand forecasting is critical in the transportation and logistics industry, especially during periods of supply chain constraints. Accurate freight demand estimates benefit companies involved in logistics and supply chain, such as those that ship containers and air cargoes across borders. This helps companies effectively manage the cost of securing their transport network, which helps them manage shipping costs and maximize revenue and profit.

A machine learning (ML) model that is able to make an accurate forecast depends on high-quality training data. For demand forecasting, training data can include historical demand volume and other internally generated data that could be related to volume, such as price, inventory, and sales team headcount. In addition, external data, such as competitors, market environment, holidays, weather, and macro-economy, could also affect the demand volume. These internal and external data factors can be used as features in an ML model.

After all features are identified, the business may also want to provide input to some of these features that are within their control. For example, the business can set the shipping price in advance or decide when to do promotions and discounts. These types of user inputs can be incorporated into the model when making the forecast.

This guide describes a strategy to build a solution on AWS that makes an accurate logistic demand forecast by using an ML model. You train the model on a historical dataset that contains demand volume and features related to the demand. These features and metrics include both internal organic data and external data. The solution also provides the flexibility for the user and business analyst to provide inputs, which can then be incorporated into the forecast model.

The following image shows an example of a historical time series and 12-month forecasted range. You can use the recommendations in this guide to create an ML model that produces this type of forecast.

![Line chart of historical data and 12-month forecasted range](http://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-freight-capacity/images/guide-img/4600072e-6d1e-414c-b39d-f89e1eed9438/images/9fbd42b7-edc2-47c8-8296-55149d48f512.png)

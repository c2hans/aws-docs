---
source_url: https://docs.aws.amazon.com/whitepapers/latest/demand-forecasting/demand-forecasting-background-and-barriers-to-adopt-aiml-based-approaches.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Demand forecasting: background and barriers to adopt AI/ML-based approaches
<a name="demand-forecasting-background-and-barriers-to-adopt-aiml-based-approaches"></a>

## Background
<a name="background"></a>

 Demand forecasting is a necessary capability for most industries. Demand forecasting touches everyone’s lives on a daily basis. For example, demand forecasting ensures grocery shelves are stocked, packages are delivered on time, electricity generation meets the electricity load to keep our lights on, and wait times for our favorite restaurant delivery are short.

 Demand forecasting is a field of [predictive analytics](https://en.wikipedia.org/wiki/Predictive_analytics), which attempts to forecast customer demand to optimize supply decisions. Demand forecasting methods are often split into two classes: *qualitative* and *quantitative* methods. Qualitative methods are based on subject matter expert (SME) opinion, while quantitative methods use [data](https://en.wikipedia.org/wiki/Data). The focus of this paper is on *quantitative* demand forecasting.

 In quantitative demand forecasting, the basic assumption is that the demand of the factual past can be used to define future demand. Mathematically, historical demand is described by a [time series](https://en.wikipedia.org/wiki/Time_series), demonstrating a chronological sequence of logged observation points. By reflecting the specific features of this time series (pattern), this series is projected into the future using different forecasting methods and models.

 While all businesses use some form of forecasting today, traditional methods such as rule-based forecasting, statistical methods such as [extrapolation](https://en.wikipedia.org/wiki/Extrapolation) with regression analysis, or time series analyses may have limitations due to the increasing number of demand signals. The large size and variety of data available today was not factored into these older methods, and may be beyond their capacity. The use of ML, such as [artificial neural networks](https://en.wikipedia.org/wiki/Neural_network) (ANNs), has proven to be a preferable method of handling huge volumes of data. The main reason behind the accuracy of ML models is the complexity of the models and their ability to consider the amount of data, which may or may not be related to demand – a concept which is hard for statistical methods to grasp.

 Customers often acquire large amounts of structured and non-structured data from internal and external resources, which makes ML forecasting a good solution for them. Market leaders make investments to bring in flexible, accurate ML-forecasting to all parts of their business. According to a recent study by [McKinsey](https://www.mckinsey.com/capabilities/quantumblack/our-insights/most-of-ais-business-uses-will-be-in-two-areas), organizations that have implemented ML forecasting techniques improved forecasting accuracy by 10 to 20 percent, which translated into a 5% reduction in inventory costs and a 2-3% increase in revenue. AI/ML-based forecasting can increase your revenue as you make more informed decisions, prepare for upcoming changes, and invest better and more effectively based on the forecast.

 However, there are some challenges to adopting AI/ML-based demand forecasting. There are various reasons and solutions for these pain points which we address in the following sections.

## Challenges to adopting AI/ML-based demand forecasting
<a name="challenges-to-adopting-aiml-based-demand-forecasting"></a>

 Even though there is growing interest by many organizations in investing in AI/ML capabilities for demand forecasting, quantifying and demonstration of the value of AI/ML remains a challenge. This has slowed widespread adoption of ML. Even if the organization decides to proceed with AI/ML-based demand forecasting, they can face challenges organizationally, technologically and skill-wise to realize the technology in their organization.

 These challenges are grouped into five categories:
+  **Adequate data to start with** — Demand is driven by multiple factors which may require a wide variety and a large set of data. In some cases, even if the customer has the expertise, they may not have collected enough data to accurately forecast the demand.
+  **Data science expertise** — A company may not have necessary technical resources, such as data science expertise, available in their organization. Building in-house-grown models and the necessary data pipelines to perform recurring forecasting generally requires a dedicated team. The cost of building a data science team that has the expertise to build an in-house demand forecasting model can be high. For most organizations, this is not their business focus, so leadership may not provide the investment to proceed. A customer can always outsource this capability to data science vendors, but this comes with its own costs and operational dependencies.
+  **Building competitive models** — Not all models are the same. A competitive model should be highly accurate to provide competitive advantage to the customer. Creating such a model requires heavy lifting efforts such as building the ANN model and tuning it, which can distract from the main work of the business without adding value.
+  **Model lifecycle and ML operations (MLOps)** — A competitive model must be kept up to date. [AI/ML models can drift](https://www.youtube.com/watch?v=J9T0X9Jxl_w) over time, which can impact the model’s accuracy. Having such a model is not a one-time effort, but a constant process of maintenance to keep it accurate and reliable. However, the data to train and keep the model updates are expected to be on a data pipeline which requires ingestion and storage layers. The pipeline is expected to work seamlessly with the AI/ML models hosted in the consumption layer. Multiple data scientists and ML engineers may be needed to maintain the model. Continuous integration and continuous delivery (CI/CD) pipelines must be agile and high quality to keep AI/ML models and their endpoints up to date.
+  **Incorporating and interpreting AI/ML-based demand insights into the decision cycles** — Eventually, the business data as well as the AI/ML inferred forecasted data should be ready to be *consumed* by various business stakeholders. A challenge is presented if there is a gap between the business and ML teams on how to best use and interpret the produced ML insights in the business decision-making processes, in a timely manner.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

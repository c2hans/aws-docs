---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/forecast-demand-new-product/introduction.html
---

# Forecasting demand for new product introductions by using AWS machine learning services
<a name="introduction"></a>

*Raju Patil, Daniel Aucoin, Ivan Cui, and Peter Molnar, Amazon Web Services*

## Overview
<a name="overview"></a>

Demand forecasting, also known as *sales forecasting*, is a key focus of many manufacturing companies, especially in the consumer electronics (CE) sector. Demand forecasting for new products that are being introduced into the market is considered *new product introduction (NPI) forecasting*.

The best strategies for demand forecasting must consider a variety of factors that can potentially affect sales. In the context of NPI forecasting, and particularly for the CE sector, one of the largest factors that influence product sales is the *product lifecycle*. Often, many CE categories see a large number of sales early in the product lifecycle. For example, more sales are expected in the weeks immediately following the product launch. The demand for many CE products usually decreases significantly after the initial spike, and sometimes, the product becomes obsolete within a couple of years. This especially occurs when companies release new versions of a product on an annual or biannual cadence. Sales of new versions of products often follow a similar pattern, even if the new versions are not released at the same point in time during the year. Apart from the product lifecycle, other significant influences on demand include marketing spend, promotions, seasonality, and price.

Companies use forecasts in a variety of ways, such as for supply planning and revenue forecasts. For supply planning, NPI forecasts need to be generated well ahead of launch because lead times can be greater than nine months. It can take contract manufacturers 6–7 months to procure supplies, one month for manufacturing, and one month to ship from international factory locations.

Machine learning (ML) models can unlock value across your supply chain by improving forecast accuracy. They can help you answer questions such as the following:
+ Will my suppliers have enough raw material to manufacture according to predicted demand?
+ How many of each component do I need to manufacture?
+ How much product should I manufacture?
+ When will my finished goods arrive?
+ How much product should I store in each distribution and fulfillment center?
+ How will demand for my new product be spread across each sales channel?

Low NPI forecast accuracy can cause a situation of too little inventory or saddle companies with too much inventory. Manufacturers would like early warnings in order to correct course. Without ML models, the first demand signal arrives weeks after the initial product launch, giving low or no time to align the supply chain and manufacturing operations with the expected demand. The prevailing industry practices for NPI demand forecasting rely heavily on subject matter experts and domain knowledge.

Adopting a modern ML-based approach helps organizations to exploit data-driven strategies for NPI demand forecasting. ML-based approaches can provide forecasts with long horizons, which are generated many weeks prior to product launch. These long-horizon forecasts are crucial for supply planning and distribution logistics.

## Objectives
<a name="objectives"></a>

By providing best practices and a recommended architecture, this guide helps you do the following:
+ Meet data readiness requirements for data-driven NPI demand forecasting
+ Build cost-effective data ingestion mechanisms
+ Determine the feasible ML approaches for NPI demand forecasting
+ Scale and track forecast effects and measure business value

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

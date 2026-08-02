---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/measure-progress.html
---

# Measure progress
<a name="measure-progress"></a>

Earlier sections highlighted how cloud leaders can create a compelling vision for their Cloud Operating Model. We provided guidance on how to connect strategy to implementation to support building your Cloud Operating Model. We also explained the need for a framework, such as the AWS COM Framework, to understand and develop maturity levels, and build a roadmap of capabilities that meet the needs of your organization. There is one more piece that is required: ensuring that KPIs are established to measure progress and indicate where a change in direction is required to maintain momentum.

In the internal AWS transformation community, one of the most frequently asked questions is: *"How can our customers measure whether they are actually transforming their business?"*

To understand why this question is important and what can be done about it, see Eric Tachibana's 2015 re:Invent presentation [9 Best Practices to Avoid A Stalled Cloud Transformation Program](https://www.youtube.com/watch?v=dU3gFDcsZOw). In this talk, Eric demonstrates how customers can slow down or even halt their cloud adoption journey (*The* *Great Stall*) and provides best practices gathered from AWS customers who have successfully accelerated through those delays.

The following graphic highlights what can happen at The Great Stall, and Eric discusses ways to get through that phase. We can take that discussion further to say that progression beyond The Great Stall and managing the journey require that you establish measures and have the ability to correct your course.

![Measuring progress](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/images/guide-img/9a407f0b-ea38-4662-8d39-755295f71238/images/7978f0b4-085a-4f55-b7cf-386a6fa5eb3e.png)

The adoption and consumption of cloud services enable this transformation journey, so the absence of a functional Cloud Operating Model and the lack of visibility into the journey can cause adoption to enter The Great Stall. Therefore, we recommend that cloud leaders look to establish observability in the form of a [balanced scorecard](https://www.investopedia.com/terms/b/balancedscorecard.asp). This scorecard consists of a set of metrics that are aligned to the digital or cloud transformation. It provides a way to understand your current position and foresee any trouble ahead.

## Visualizing metrics
<a name="visualizing-metrics.2ca999c1-aace-5499-96ce-43ce7634093f"></a>

Building a balanced scorecard to visualize metrics helps to understand and put the current transformation efforts in context of the business value they intend to provide. One approach used by AWS teams with their customers is to create a Transformation Dashboard. This approach is based on analyst research of customers who have successfully completed their cloud transformation, and internal analysis of (anonymized) AWS service consumption data of over 5,000 customers from around the world, and across multiple industry segments.

Although our discussion in this guide is based only on AWS Cloud services, you can extend this approach for a hybrid or multi-cloud environment. Using this method, we have identified a balanced scorecard for transformation and several patterns that can be associated with customers who are at different stages of their Cloud Operating Model journey. The objective of this approach is to help customers identify ways in which they can track their overall level of transformative growth, avoid stall, and ensure that they continue to mature their Cloud Operating Model as an enabler of overall business transformation.

Our Transformation Dashboard balanced scorecard has four segments:
+ Agility and time to market
+ Strategic advantage (and service Innovation)
+ Risk reduction
+ Operational efficiency

In this scorecard, two segments highlight the values associated with time to market, agility, innovation, and gaining an advantage over competitors (in a commercial environment). The other two segments focus on measuring how the organization is becoming more efficient, effective, and resilient, and avoiding being at a disadvantage when compared with competitors. The scorecard is shown in the following diagram.

![Visualizing metrics](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-cloud-operating-model/images/guide-img/9a407f0b-ea38-4662-8d39-755295f71238/images/7111fedd-b76c-45e0-91ac-4482ba6bdfb8.png)

By plotting data points on this matrix you can represent the focus of your organization. This helps you understand whether your Cloud Operating Model is being developed to *avoid disadvantage* or to *gain advantage*. If it's the former, we recommend that you correct your course to ensure that you're developing capabilities to focus on the latter, because gaining advantage is where you can realize the greatest value.

Generally speaking, large-scale migration programs for rehosting workloads (*lift and shift*) focus on avoiding disadvantages. After migration has occurred, modernization activities such as adopting Platform as a Service (PaaS) or serverless technologies support gaining advantages. For example metrics, see the following two AWS-commissioned studies that review these approaches and provide KPIs based on market research:
+ **Migration:** [The Business Value of Migration to Amazon Web Services](https://pages.awscloud.com/rs/112-TZM-766/images/hackett-group-the-business-value-of-migration-to-aws-012022.pdf) (The Hackett Group, February 2022). In this research, The Hackett Group measured the value of migrating to AWS across four categories: resiliency, agility, cost savings, and staff productivity.
+ **Modernization:** [Business Value of Cloud Modernization](https://pages.awscloud.com/rs/112-TZM-766/images/known-business-value-of-cloud-%20modernization-012022.pdf) (Known, January 2022) captured the use of 22 unique KPIs to understand the value of modernization through cloud services. In this study, they surveyed over 500 enterprises that had already migrated workloads to the cloud to understand the value associated with four technical modernization strategies: containers, serverless, managed analytics, and managed data.

Throughout your Cloud Operating Model journey, it's important to choose measures that can cover both the Migration and Modernization aspects so that progress is tracked, data can be compared throughout the journey, and the results of course correction can be seen.

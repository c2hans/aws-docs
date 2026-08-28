---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-transformation/phase-1.html
---

# Phase 1: Identifying business objectives
<a name="phase-1"></a>

[The business case for the digital investment report](https://econsultancy.com/reports/the-business-case-for-digital-investment/) (Econsultancy website) states that "The lack of a clear longer-term business case and ROI, an absence of board-level understanding and sponsorship, and the perception of digital marcoms as tactical rather than strategic are all viewed as significant challenges to securing the right levels of investment for a digital strategy by at least three-quarters of responding companies." Therefore, it is important to identify and prioritize business opportunities based on measurable KPIs.

Note that business cases might differ for different industrial sectors, such as manufacturing, energy, automotive, healthcare, life sciences, agriculture. For an example of the business impacts to manufacturing, see the *Achieved impact from Successful Digital Industrial Solutions* section of the [Hitachi Vantara Solution Brief](https://d1.awsstatic.com/HitachiVantaraSolutionBrief.pdf).

In this phase, you do the following:

1. [Identify business challenges](#identify-business-challenges)

1. [Identify measurable KPIs](#identify-measurable-kpis)

1. [Identify business objectives](#identify-business-objectives)

1. [Identify use cases](#identify-use-cases)

The outcome of this phase is that all stakeholders are aligned on the target objectives, understand expectations, and know how success will be measured.

## Identify business challenges
<a name="identify-business-challenges"></a>

The first step in defining the business objectives is making a list of the current business challenges that you want to solve and the new business challenges you might encounter by implementing an IIoT digital transformation solution in your environment.

The following are some common business challenges for manufacturing and industrial companies that are in the early phases of their IIoT digital transformation journey:
+ Making legacy industrial machines and equipment smart
+ Extracting trapped production data for new insights
+ Reduced productivity and increased downtime due to chaotic operations and slow processes for root-cause analysis
+ Asset management challenges due to data silos and lack of digital tracking of assets
+ Lack of near real-time monitoring at different levels of operations, such as monitoring overall equipment effectiveness (OEE), throughput, and cycle time at the plant, line, and machine level

## Identify measurable KPIs
<a name="identify-measurable-kpis"></a>

Based on the identified business challenges, you can start asking *How would I measure a successful solution to this problem?* Answering this question helps you take data-driven approach to evaluating the success of the solution.

Determine the KPIs that you will use to measure the success of your journey, and make sure that they are measurable. The following are example KPIs for that apply to a variety of industrial sectors:
+ % improvement for overall equipment effectiveness (OEE) or similar KPIs
+ % reduction in operational cost
+ % reduction in storage and compute cost for cloud, compared to on-premises
+ % reduction in unplanned downtime due to proactive monitoring and maintenance
+ % accuracy in demand forecasting and inventory management
+ % reduction in latency observed by business users for business intelligence (BI) reporting
+ % reduction in time to make the historical data available for advanced analytics, such as machine learning
+ % reduction in time to scale compute and storage
+ % increase in system uptime
+ % increase in productivity
+ % reduction in downtime

## Identify business objectives
<a name="identify-business-objectives"></a>

Now that you have identified the business challenges you want to solve and decided how to measure success, you can now define your business objectives. These objectives help you answer the questions *Why is this problem worth solving?* and *Who benefits from solving this problem?* You decide on a data-driven strategy for measuring success, such as comparing current state KPIs with the target state KPIs for the particular business objective.

For each metric or KPI you want to use, rephrase it as a business objective with a target measurable value. For example, if your business challenge is *product1 is frequently out of stock due to a manual detection process* and your metric is *% reduction in latency to detect the problem*, the business objective might be* 95% reduction in latency to identify possible out-of-stock situations for product1*.

Prioritize your business objectives so that the team has a clear understanding of how to prioritize resource allocation.

## Identify use cases
<a name="identify-use-cases"></a>

After you have defined your business objectives, you can now focus on the use cases. *Use cases* define the exact interactions end-users have with the system, and you use them to determine how to automatically create the expected business outcome. Use cases act as the main requirements when building your blueprint.

Each use case should consist of four key elements:
+ One or more end-user personas who interact with the system
+ Goals for each persona
+ System actions that you want to implement, as experienced by the persona
+ The expected result of the system actions, as experienced by the persona

Using the example business objective *95% reduction in latency to identify possible out-of-stock situations for product1*, the following is an example use case for this objective:
+ **Persona** – Business analyst
+ **Goal **–** **Use trend analysis to estimate out-of-stock situations for product1 within minutes
+ **Action** – Use a BI reporting tool to generate a report that shows the trend
+ **Result** – New solution should have 95% reduced latency to identify out-of-stock situations, compared to the previous manual process

After you have the list of use cases, evaluate them with the stakeholders based on the importance and feasibility of each use case. *Importance* is the value you expect to gain from the use case, such as its return on investment (ROI), and *feasibility* is the ease of implementation. Create a table like the following, and ask stakeholders to vote on the importance and feasibility of each use case. For example, in the following table, use case 1 received 4 votes for high importance and 3 votes for low importance. The majority vote indicates this use case has a high importance.

|
|
|   | Importance | Feasibility | Majority vote |
| --- |--- |--- |--- |
| ** ** | **High** | **Low** | **High** | **Low** | **Importance** | **Feasibility** |
| Use case 1 | 4 | 3 | 5 | 2 | High | High |
| Use case 2 | 5 | 2 | 1 | 6 | High | Low |
| Use case 3 | 1 | 6 | 3 | 4 | Low | Low |

Next, you use the voting results to prioritize the use cases. Use cases with two high ratings are considered *quick wins*. Put use case with one high rating and one low rating in the *evaluate* category, and put use cases with two low ratings in the *consider* category. The following table shows a quadrant chart you can use to visualize this categorization.

![Quadrant chart showing categories based on high and low importance and feasibility ratings](http://docs.aws.amazon.com/prescriptive-guidance/latest/strategy-iiot-transformation/images/guide-img/2cc5efa2-2b32-4bb7-bd9d-d0a92a28e1ac/images/44837446-c588-4163-9586-7833969249bf.png)

Prioritize use cases that are quick wins, and make sure that you consider dependencies. As you complete your journey, you start with the quick wins and as you progress, you can add use cases in the evaluate and consider categories, based on your budget and schedule.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

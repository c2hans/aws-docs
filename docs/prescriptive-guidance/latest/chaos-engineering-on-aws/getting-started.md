---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/getting-started.html
---

# Getting started with chaos engineering
<a name="getting-started"></a>

Before you conduct an experiment, we recommend that you put a few essentials in place to make the most of your chaos engineering practices. These essentials include:
+ Observability (metrics, logging, request tracing)
+ A list of real-world events or faults that you would like to explore
+ Organizational resilience sponsorship through leadership buy-in
+ Prioritization of critical findings based on potential business impact over new features that are discovered when running chaos experiments

## Observability for chaos experiments
<a name="observability"></a>

Observability, which comprises metrics, logging, and request tracing, plays a key role in chaos engineering. You will want to understand business metrics, server-side metrics, client experience metrics, and operations metrics when you run an experiment. Without observability, you won't be able to define steady-state behavior or create a meaningful experiment to verify if your hypothesis about your application holds true.

### Metrics
<a name="metrics.dd09edcb-a271-563c-896d-4ca3638de42b"></a>

The following diagram shows the types of metrics that you can track for chaos experiments for different types of applications.

![Types of metrics to track for chaos experiments.](http://docs.aws.amazon.com/prescriptive-guidance/latest/chaos-engineering-on-aws/images/guide-img/4119a10b-a241-4431-9681-0b62a5da1a70/images/3ccf6eba-449a-46e2-8cb4-4048f48b7142.png)

+ **Business metrics** – *Steady state* indicates the normal operation of your system and is defined by your business metrics. It can be represented by transactions per second (TPS), click streams per second, orders per second, or a similar measurement. Your application exhibits steady state when it is operating as expected. Therefore, verify that your application is healthy before you run experiments. Steady state doesn't necessarily mean that there will be no impact to the application when a fault occurs, because a percentage of faults could be within acceptable limits. The steady state is your baseline. For example, the steady state of a payments system might be defined as the processing of 300 TPS with a success rate of 99 percent and round-trip time of 500 ms. Visually, think of steady state as an electrocardiogram (EKG). If the steady state of your system suddenly fluctuates, you know that there is a problem with your service.
+ **Server-side metrics** – To understand how your resources perform during the experiment, you need insights into their performance before, during, and after the experiment. To measure the impact of your resources on AWS, you can use [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html). CloudWatchis a service that monitors applications, responds to performance changes, optimizes resource use, and provides insights into operational health. During your experiments, you will want to capture server-side metrics such as saturation, request volumes, error rates, and latency.
+ **Customer experience metrics** – On AWS, you can capture real user metrics by using [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) to simulate user requests through tools such as Locust, Grafana k6, Selenium, or Puppeteer. Real user metrics are crucial for organizations that conduct chaos engineering experiments. By monitoring how real users are impacted during an experiment, teams can get an accurate picture of how faults and disruptions will affect customers in production. Key client experience metrics are Time to First Byte (TTFB), Largest Contentful Paint (LCP), Interaction to Next Paint (INP), and Total Blocking Time (TBT).
+ **Operations metrics** – Interventions measure how successfully you mitigate faults in an automated way―for example, successful client request latency during a reboot of pods, tasks, or EC2 instances with mechanisms such as replication controller or automatic scaling. Being able to automatically intervene during a fault directly correlates with a good user experience. Understanding if there is any drift in these mitigation mechanisms over time is crucial. By defining metrics for both successful and failed automated mitigations, you create guideposts that help identify potential regressions throughout your system.

### Logging
<a name="logging.591bca78-7cbc-5132-b571-0114cb521d93"></a>

Centralized logging is key to understanding your application's components' states before, during, and after a chaos experiment. We recommend that you collect logs from all your application components to build a consolidated view of what each component was doing at the time the experiment was injected. This provides a clear picture of the end-to-end experiment flow.

### Request tracing
<a name="request-tracing.483e0ca9-5e2a-5a78-84c0-e684a7cf6186"></a>

Request tracing enables you to observe the flow of any single request across the components in your application to gain a comprehensive understanding of the impact that the injected failure has on the system and its dependencies. By tracing the requests, you can see how the failure propagates through different services and components, so you can better assess the scope of the disruption. To trace your requests on AWS, you can use [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html).

## Failure scenarios to inject in chaos experiments
<a name="failure-scenarios"></a>

The goal of injecting common faults into your application is to understand how the application reacts to these unexpected events, so you can create mitigation mechanisms and make your system resilient to such faults. Additionally, you should use chaos engineering to replay historical failure scenarios to verify that your mitigation mechanisms are still functioning as expected and did not drift over time.

Consider the following events when you plan your chaos engineering experiments.

|
|
| Failure mode | Description |
| --- |--- |
| Server impairment | Reboot EC2 instances, delete Kubernetes pods or Amazon Elastic Container Service (Amazon ECS) tasks to understand how your application reacts to such crashes. |
| API errors | Inject faults into AWS and your own service APIs to understand application behavior. |
| Network issues | Introduce latency or congestion, or block connections to mimic real-world network problems. |
| AWS Availability Zone impairment | Replay the impairment of an entire Availability Zone to verify recovery across zones. |
| AWS Region connectivity impairment | Replay a network impairment across AWS Regions to verify how resources in the secondary Region react to such an event. |
| Database failures | Fail over database replicas or corrupt data, or make database instances unreachable, to understand impact to your application and recovery strategies. |
| Pause in database and Amazon S3 replication | Pause database or Amazon Simple Storage Service (Amazon S3) replication across Availability Zones or AWS Regions to understand downstream application impact. |
| Storage degradation | Pause I/O, remove Amazon Elastic Block Store (Amazon EBS) volumes, or delete files to verify data durability and recovery. |
| Dependency impairment | Take down or degrade the performance of the downstream or upstream services that you depend on, including third-party services, to understand the end-to-end flow and impact to your customers. |
| Traffic surges | Generate spikes in user traffic to test automatic scaling capabilities, and see how cold boot time might impact your overall application state. |
| Resource exhaustion | Max out CPU, memory, and disk space to verify the graceful degradation of your application. |
| Cascading failures | Initiate primary failures that cascade to downstream applications and components. |
| Bad deployments | Roll out problematic changes or configurations to verify rollback mechanisms. |

## Organizational resilience sponsorship
<a name="sponsorship"></a>

Chaos engineering provides the most value when it's applied across your organization. We recommend that you work with an executive sponsor who can help set resilience goals across your organization, remove the fear, uncertainty, and doubt about the domain, and start the transformation process to make resilience everyone's responsibility.

To support the business case of building a chaos engineering practice, attach chaos engineering efforts to your critical business projects. Making resilience an asset and driver for acceleration will help you track success over time. Start with a count of critical incidents per month or per quarter, the average time to recover, and the impact that these incidents caused to your customers and organization. Set a goal with your teams to reduce the number of incidents over a 6-month to 12-month period as improvements are made across your application stacks in response to chaos engineering experiments.

Measure whether incidents are highly repetitive. For example, let's say an expired TLS certificate leads to downtime because clients cannot establish a trusted connection. If multiple incidents occur in a year because of multiple TLS certificate expirations, you can run an experiment of a TLS certificate expiration and verify that your teams get alerts or are able to automatically mitigate such issues. This will help ensure that you become resilient to such faults.

To track progress in chaos engineering over time, capture the following metrics to help highlight the value of chaos engineering across an application's lifecycle:
+ **Reduced incident rate** ‒ Track the number of production incidents over time and correlate this number with the adoption of chaos engineering. The expectation is that the rate of severe incidents will decline.
+ **Improved mean time to resolution (MTTR) **‒ Calculate the average time it takes to resolve incidents and track this data to see if it improves with chaos engineering over time.
+ **Increased application availability** ‒ Use service-level metrics to show availability improvements as application resilience increases through chaos experiments.
+ **Faster time to market** ‒ Chaos engineering can provide the confidence to launch innovative offerings faster, because you know that your applications are resilient. Track increases in product release velocity.
+ **Operational cost reduction** ‒ Quantify if indicators such as alert noise, operational load, and manual effort to manage applications decrease with chaos practices in place.
+ **Boosting confidence** ‒ Survey developers, site reliability engineers (SREs), and other technical staff to gauge if chaos engineering boosted their confidence in application resilience. Perceptions matter.
+ **Improved customer experiences** ‒ Connect chaos engineering to positive outcomes for customers, such as fewer service disruptions, rollbacks, and outages.

## Prioritizing remediation
<a name="remediation"></a>

As you perform chaos experiments, you are likely to identify areas for improvement where the application does not perform as intended. Remediation of such items will become work in your backlog that will have to be prioritized along with other work such as feature development. We recommend that you make time for these enhancements to avoid future failure. Consider prioritizing these learnings and remediation tasks based on the level of impact they might cause. Findings that directly impact the resilience or security of your application should have priority over new features, to avoid customer impact. If the team struggles to prioritize remediation work over feature development, consider reaching out to your executive sponsor to ensure that priorities are set based on business risk tolerance.

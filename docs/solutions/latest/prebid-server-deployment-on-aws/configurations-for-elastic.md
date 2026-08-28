---
source_url: https://docs.aws.amazon.com/solutions/latest/prebid-server-deployment-on-aws/configurations-for-elastic.html
---

# Configurations for Elastic Container Service (ECS) Auto Scaling
<a name="configurations-for-elastic"></a>

The recommended configurations for the deployed solution’s automatic scaling are dependent on the approximate maximum requests per second (RPS) and maximum number of users the solution is expected to support.

In this context, RPS means HTTP or HTTPS requests per second. A single request can contain multiple bid requests that can result in multiple bid responses inside the HTTP response. The request and response might both contain a payload. The average response time refers to the amount of time it takes to receive winning bids, measured in seconds, and the timer starts when the requests for advertisement bids are sent out and stops when the winning bids are received.

The recommendations in this section were determined via load testing with [Distributed Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/). In the load tests, 10,000 users with 16.7 new users being added per second were spawned across `us-east-1`, `us-west-1`, `us-east-2`, and `us-west-2` Regions to generate traffic to the Prebid server cluster.

In the context of load testing, a user continuously makes an auction request to the auction API. 80% of the total RPS are auction API requests. The user infrequently sends requests to the non-auction APIs. This includes information and status check requests. The approximate average payload sizes for an API request and response is 123 KB and 331 KB respectively.

The statistics in the tables below were calculated by the data collected from `us-east-1`, `us-west-1`, `us-east-2`, and `us-west-2` Regions.

## Static cluster size configurations
<a name="static-cluster-size-configurations"></a>

The following table lists the recommended static cluster sizes and their associated maximum stable RPS limits, average response time, and success rate if ECS Auto Scaling is turned off.

| ECS number of tasks with no Auto Scaling | Transactions per second | Average response time in seconds | Success rate |
| --- | --- | --- | --- |
| 1 | 800.79 | 9.56630 | 87.70% |
| 10 | 4145.95 | 1.84996 | 97.38% |
| 25 | 11074.86 | 0.69569 | 98.93% |
| 50 | 75912 | 0.35765 | 99.60% |
| 100 | 75411 | 0.17981 | 99.89% |
| 200 | 64621.02 | 0.13120 | 99.86% |
| 400 | 128793.61 | 0.07452 | 99.97% |

Significant latency and failed requests were observed when the traffic was exceeded for each number of tasks tested. Further increases to the number of tasks were able to handle the 10,000-user test load with better success rate, average response time, and RPS.

## Auto Scaling cluster configurations
<a name="auto-scaling-cluster-configurations"></a>

Turning on Auto Scaling in ECS increases the performance of the solution’s maximum RPS. The following recommended ECS Auto Scaling policies and parameters were used in the load tests.

Parameters:
+ Minimum number of tasks: 10
+ Maximum number of tasks: 100

Policies:
+  `ALBRequestCountPerTarget`
  + Target value: 5000
  + Scale-out cooldown period: 300
  + Scale-in cooldown period: 300
+  `ECSServiceAverageCPUUtilization`
  + Target value: 66%
  + Scale-out cooldown period: 300
  + Scale-in cooldown period: 300
+ `ECSServiceAverageMemoryUtilization `
  + Target value: 50%
  + Scale-out cooldown period: 300
  + Scale-in cooldown period: 300

The following table lists the auto-scaling policies and their associated maximum stable RPS limits, average response time, and success rate.

| Auto-scaling policies | Min number of tasks scaled | Max number of tasks scaled | Transactions per second | Average response time in seconds | Success rate |
| --- | --- | --- | --- | --- | --- |
| ALBRequestCountPerTarget (ALB) | 10 | 100 | 17367.6 | 0.44486 | 99.51% |
| ECSServiceAverageCPUUtilization (CPU) | 10 | 13 | 4708.65 | 1.85956 | 96.41% |
| ECSServiceAverageMemoryUtilization (Mem) | 10 | 12 | 5820.56 | 1.31274 | 98.59% |
| ALB & CPU | 10 | 100 | 14948.84 | 0.51504 | 99.48% |
| ALB & Mem | 10 | 100 | 15208.86 | 0.50105 | 99.50% |
| CPU & Mem | 10 | 13 | 4747.65 | 1.60875 | 97.08% |
| ALB & CPU & Mem | 10 | 100 | 16211.21 | 0.49361 | 99.42% |

The `ALBRequestCountPerTarget` policy is the most important auto-scaling policy and plays the biggest influence on the performance. However, we recommend that you use all three of the Auto Scaling policies above. Removing them will decrease the maximum RPS and increase response time because then the containers are more prone to becoming overloaded. The policies also make the deployed solution more resilient to cases where there is a burst of users.

The maximum number of tasks and minimum number of tasks can be adjusted depending on the solution’s usage. We recommend to at least have 50 tasks and have Auto Scaling turned on for the deployed solution to reduce response times and the chance of errors occurring.

## Fargate Spot instances ratio configurations
<a name="fargate-spot-instances-ratio-configurations"></a>

We recommend that you keep the solution’s default 50:50 ratio of the Fargate Spot instances to Fargate instances at least. This is because during testing, the Fargate instances were found to help the system scale and react more quickly to user traffic and support higher RPS more quickly with higher success rate.

The following table lists the Fargate Spot instances ratio and their associated maximum stable RPS limits, average response time, and success rate.

| Fargate: Fargate Spot | Transactions per second | Average response time in seconds | Success rate |
| --- | --- | --- | --- |
| 50:50 | 17789.75 | 0.43171 | 99.60% |
| 100:0 | 134244.83 | 0.07305 | 100% |

## Example cluster size, Auto-scaling policy, and Fargate Spot instances ratio configurations
<a name="example-cluster-size-auto-scaling-policy-and-fargate-spot-instances-ratio-configurations"></a>

You can use the following specifications for Prebid Server, based upon the testing conducted in this document.

Parameters:
+ Minimum number of tasks: 50
+ Maximum number of tasks: 400

Policies:
+  `ALBRequestCountPerTarget`
  + Target value: 5000
  + Scale-out cooldown period: 300
  + Scale-in cooldown period: 300
+  `ECSServiceAverageCPUUtilization`
  + Target value: 66%
  + Scale-out cooldown period: 300
  + Scale-in cooldown period: 300
+  `ECSServiceAverageMemoryUtilization`
  + Target value: 50%
  + Scale-out cooldown period: 300
  + Scale-in cooldown period: 300

Fargate Spot instances ratio:
+ Fargate instances: 80
+ Fargate Spot instances: 20

The metrics achieved in testing with the above configurations are in the following table.

| Results from recommended configurations |  |
| --- | --- |
| Maximum transaction per second | 190881.19 |
| Average response time in seconds | 0.05533 |
| Success rate | 100% |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Guidance for Deploying a Prebid Server on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

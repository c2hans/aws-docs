---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/operations-testing.html
---

# Operations testing
<a name="operations-testing"></a>

Like products, IT operations should be tested, end to end, on a regular cadence. Although enterprise customers have adopted operational testing for activities such as disaster recovery, operational testing should be extended to other operations domains such as incident and event management. Game-day scenarios, like ﬁre drills, are activities that test how your processes, tools, and people react when an operations event occurs.

Here are some prescriptive game-day scenarios used to test incident and event management on AWS:
+ Amazon Elastic Compute Cloud (Amazon EC2) CPU utilization stress test
+ Amazon EC2 network stress test
+ Amazon EC2 memory stress  test
+ Amazon Elastic Container Service (Amazon ECS) task failure scenarios
+ AWS Lambda concurrency limits and cold start impact
+ Amazon API Gateway throttling and latency injection
+ Amazon Relational Database Service (Amazon RDS) memory stress test
+ Amazon RDS failover testing
+ Amazon RDS storage stress
+ Amazon DynamoDB throttling and hot partition testing
+ Availability Zone failure simulation

Consider using the following AWS services to run testing scenarios:
+ [AWS Fault Injection Service (AWS FIS)](https://aws.amazon.com/fis/) for controlled chaos engineering experiments
+ [Amazon CloudWatch Synthetics](https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/Welcome.html) for application endpoint testing
+ [Automation](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-automation.html), a capability of AWS Systems Manager, for orchestrating complex scenarios
+ [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) for assessing and improving application resiliency

As a best practice, you should test your IT operations starting with incident and event management, and extend testing to other operational domains. It's also crucial to have a predetermined game-day schedule. Here are some example schedules:

**Prod or non-prod schedule**

![Prod OR non-prod gameday schedule.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/images/guide-img/6545b5e3-3780-4eb8-a195-e92454bb488e/images/493d1eb8-8f18-47d0-890f-9b9c5ebc690e.png)

**Prod and non-prod schedule**

![Prod AND non-prod gameday schedule.](http://docs.aws.amazon.com/prescriptive-guidance/latest/migration-operations-integration/images/guide-img/6545b5e3-3780-4eb8-a195-e92454bb488e/images/66e05bc8-fa43-4f72-b0df-a3713fc10633.png)

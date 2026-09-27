---
source_url: https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/concepts-and-definitions.html
---

# Concepts and definitions
<a name="concepts-and-definitions"></a>

This section describes key concepts and defines terminology specific to this solution:

 **scenario**

Test definition including the test’s name, description, traffic shape mode, task count, concurrency, AWS Region, ramp-up, hold-for, test type, schedule date, and recurrence configurations.

 **traffic shape mode**

Which side controls the load the test generates. In **Standard** mode, the solution controls it through the values you set for concurrency, ramp-up, and hold for. In **Native** mode, the script you upload controls it, and the solution sets only the task count and a safety duration. Standard is the default. The concurrency, ramp-up, and hold-for concepts below apply to Standard mode.

 **task count**

Number of containers that will be launched in the Fargate cluster to run the test scenario. Additional tasks will not be created once the account limit on Fargate resources has been reached. However, tasks already running will continue.

 **concurrency**

The concurrency (number of concurrent virtual users per task). The recommended concurrency based on default settings is 200. Concurrency is limited by CPU and memory. For tests based on Apache JMeter, higher concurrency increases the memory utilized by the JVM on the ECS task. The default ECS Task Definition creates tasks with 4 GB of memory. It is recommended to start with lower concurrency values for 1 task and monitor the ECS CloudWatch metrics for the Task Cluster. Refer to [Amazon ECS cluster utilization metrics](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/cluster_utilization.html).

 **ramp-up**

The time period to gradually increase from zero to the target concurrency level.

 **hold for**

The time period to maintain the target concurrency level after ramp-up completes.

For a general reference of AWS terms, see the [AWS Glossary](https://docs.aws.amazon.com/general/latest/gr/glos-chap.html).

---
source_url: https://docs.aws.amazon.com/solutions/latest/cognito-user-profiles-export-reference-architecture/design-considerations.html
---

# Design considerations
<a name="design-considerations"></a>

## One-way scheduled export
<a name="one-way-scheduled-export"></a>

This guidance automatically exports data from your primary user pool to Amazon DynamoDB on a [scheduled basis](#export-frequency). If you create a new user pool and populate it by running the `ImportWorkflow` AWS Step Functions workflow, you can configure scheduled exports of this new user pool by launching a new instance of this guidance and configuring it to point to the new user pool.

## Guidance configuration
<a name="guidance-configuration"></a>

There are two parameters you can use to influence the guidance’s behavior.

### Export frequency
<a name="export-frequency"></a>

This parameter sets the [schedule expression](https://docs.aws.amazon.com/AmazonCloudWatch/latest/events/ScheduledEvents.html) for the Amazon CloudWatch Events rule that starts the `ExportWorkflow` Step Functions workflow. There are options for every day, seven days, or 30 days. If you require a different schedule, update the CloudWatch Events rule after the guidance is deployed.

### Cognito transactions per second (TPS)
<a name="cognito-transactions-per-second-tps"></a>

This parameter sets the maximum number of times an Amazon Cognito API is called per second. While the `ExportWorkflow` Step Functions workflow is running, API calls are made to list users and groups in the primary user pool. When the `ImportWorkflow` Step Functions workflow is running, it adds groups and adds users to groups. These API calls count against your existing Cognito API limits. This parameter can reduce the risk of the guidance inadvertently impacting your applications. Lowering this value results in this guidance taking longer to run.

| User pool | Cognito TPS setting | Action | Approximate run time |
| --- | --- | --- | --- |
| 10,000 users No groups | 10 | Sync workflow | 2.62 minutes |
|  |  | Recovery workflow | 8.13 minutes |
|  | 5 | Sync workflow | 2.66 minutes |
|  |  | Recovery workflow | 8.32 minutes |
| 10,000 users Each user in one group | 10 | Sync workflow | 4.76 minutes |
|  |  | Recovery workflow | 29.24 minutes |
|  | 5 | Sync workflow | 4.82 minutes |
|  |  | Recovery workflow | 47.73 minutes |
| 100,000 users No groups | 10 | Sync workflow | 21.82 minutes |
|  |  | Recovery workflow | 56.31 minutes |
| 100,000 users Each user in one group | 10 | Sync workflow | 40.26 minutes |
|  |  | Recovery workflow | 290.24 minutes |
| 250,000 users No groups | 10 | Sync workflow | 54.79 minutes |
|  |  | Recovery workflow | 128.2 minutes |
| 250,000 users Each user in one group | 10 | Sync workflow | 98.65 minutes |
|  |  | Recovery workflow | 678.29 minutes |
| 500,000 users No groups | 10 | Sync workflow | 146.52 minutes |
|  |  | Recovery workflow | 247.63 minutes |
| 500,000 users Each user in one group | 10 | Sync workflow | 181.46 minutes |
|  |  | Recovery workflow | 1,313.31 minutes |

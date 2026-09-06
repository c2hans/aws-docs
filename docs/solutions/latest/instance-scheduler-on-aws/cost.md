---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/cost.html
---

# Cost
<a name="cost"></a>

You are responsible for the cost of the AWS services used while running Instance Scheduler. Understanding how costs scale with your deployment size helps you plan and optimize your implementation.

## Cost scaling factors
<a name="cost-scaling-factors"></a>

Instance Scheduler costs scale based on several factors:

 **Number of scheduling targets**: The number of unique account-region-service combinations being managed. Each target requires a separate Lambda invocation per scheduling interval.

 **Resources per target**: The number of resources (EC2 instances, RDS databases, etc.) within each target influences Lambda execution time and duration costs.

 **Operational metrics complexity**: Optional CloudWatch metrics costs scale with the number of unique instance types and active schedules being tracked across your deployment.

 **Scheduling frequency**: The solution runs based on your configured frequency (default: 5 minutes). More frequent checks increase Lambda invocations from 24 times daily (hourly) to 288 times daily (5-minute intervals).

## Calculating scheduling targets
<a name="calculating-scheduling-targets"></a>

A scheduling target is a unique combination of account-region-service that contains at least one actively managed instance. Multiple instances within the same account-region-service combination count as a single scheduling target.

 **Example calculation:**
+ Account A, us-east-1, 5 EC2 instances = 1 scheduling target
+ Account A, us-east-1, 3 RDS databases = 1 scheduling target
+ Account A, us-east-1, 2 Auto Scaling groups = 1 scheduling target
+ Account A, us-west-2, 2 EC2 instances = 1 scheduling target
+ Account B, us-east-1, 10 EC2 instances = 1 scheduling target

Total: 5 scheduling targets

This means the solution will invoke 5 separate Lambda functions per scheduling interval to manage all resources across these account-region-service combinations.

**Note**
Targets can be in scope for scheduling but are not considered "active" for cost calculations until at least one resource is tagged for scheduling in that target.
For cost optimization, Instance Scheduler groups all Amazon RDS-related services into a single invocation. Therefore Amazon RDS, [Amazon Aurora](https://aws.amazon.com/rds/aurora/), [Amazon Neptune](https://aws.amazon.com/neptune/), and [Amazon DocDB scheduling](https://aws.amazon.com/documentdb/) all count as one "RDS" service for cost calculations.

## Cost optimization strategies
<a name="cost-optimization-strategies"></a>

1. Deploy in a Region with lower Lambda pricing

1. Use the default 512 MB Lambda memory setting unless required to increase it by single-target scale limitations

1. Minimize the number of unique schedules and instance types in active use

1. Adjust scheduling frequency based on your requirements

1. Disable operational metrics dashboard if not planning to use it

See the pricing webpage for each [AWS service in this solution.](aws-services-used-in-this-solution.md)

We recommend creating a [budget](https://docs.aws.amazon.com/cost-management/latest/userguide/budgets-create.html) through AWS Cost Explorer to help manage costs. Prices are subject to change.

## Reference pricing examples (monthly)
<a name="pricing-examples-monthly"></a>

The following examples demonstrate how costs scale across different deployment sizes. Use these as reference points to estimate costs for your specific deployment.

**Note**
All reference pricing are rough estimations of cost for the primary services used by the solution.

### Small deployment (\~$9 monthly)
<a name="small-deployment"></a>

This example represents a typical development or small production deployment:
+ 5 active targets
+ 20 managed resources
+ 3 active schedules
+ 2 instance types
+ 5-minute scheduling interval
+ 512 MB Lambda function, 5-second average runtime

| AWS service | Monthly Cost [USD] |
| --- | --- |
| AWS Lambda | \~$2.00 |
| AWS KMS | \~$1.50 |
| CloudWatch Logs | \~$0.30 |
| CloudWatch Metrics | \~$5.30 |
| Amazon DynamoDB | \~$0.05 |
| Total: | \~$9.15 |

### Medium deployment (\~$161 monthly)
<a name="medium-deployment"></a>

This example represents a mid-size enterprise deployment:
+ 250 active targets
+ 1000 managed resources
+ 15 active schedules
+ 15 instance types
+ 5-minute scheduling interval
+ 512 MB Lambda function, 5-second average runtime
+ 5 EC2 Maintenance Windows

| AWS service | Monthly Cost [USD] |
| --- | --- |
| AWS Lambda | \~$95.00 |
| Amazon DynamoDB | \~$1.00 |
| CloudWatch Logs | \~$10.00 |
| CloudWatch Metrics | \~$40.00 |
| AWS KMS | \~$15.00 |
| Total: | \~$161.00 |

### Large deployment (\~$630 monthly)
<a name="large-deployment"></a>

This example represents a large enterprise deployment:
+ 1000 active targets
+ 5000 managed resources
+ 500 active schedules
+ 50 instance types
+ 5-minute scheduling interval
+ 512 MB Lambda function, 5-second average runtime
+ 100 EC2 Maintenance Windows

| AWS service | Monthly Cost [USD] |
| --- | --- |
| AWS Lambda | \~$380.00 |
| Amazon DynamoDB | \~$5.00 |
| CloudWatch Logs | \~$50.00 |
| CloudWatch Metrics | \~$140.00 |
| AWS KMS | \~$55.00 |
| Total: | \~$630.00 |

## Cost estimation for your deployment
<a name="cost-estimation-for-your-deployment"></a>

To estimate costs for your specific deployment:

1. Count your total managed resources (EC2 instances, RDS databases, etc.)

1. Determine the number of accounts and Regions you’ll manage

1. Consider your required scheduling frequency

1. Decide whether you need operational metrics

1. Use the reference examples above to interpolate your expected costs

---
source_url: https://docs.aws.amazon.com/solutions/latest/instance-scheduler-on-aws/aws-services-used-in-this-solution.html
---

# AWS services used in this solution
<a name="aws-services-used-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core**. Solution deploys a Lambda function that contains all the logic to schedule the instances and to manage updates to the CloudFormation stack using a custom resource feature. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core.** Solution creates DynamoDB tables to store schedule configuration, state information, last actions performed of the instances, and a table to store Systems Manager maintenance window for scheduling purpose. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Core.** Solution stores debugging and information logs. |
|  [AWS IAM](https://aws.amazon.com/iam/)  |  **Core.** Solution uses IAM to get permissions for scheduling instances. |
|  [Amazon SNS](https://aws.amazon.com/sns/)  |  **Core.** Solution creates an SNS topic to send error messages for the users to subscribe to and troubleshoot in case of any errors. |
|  [AWS KMS](https://aws.amazon.com/kms/)  |  **Core.** Solution creates an AWS KMS key to encrypt the SNS topic. |
|  [Amazon EventBridge](https://aws.amazon.com/eventbridge/)  |  **Core.** Solution creates an EventBridge Solution creates EventBridge scheduled rules that invoke AWS lambda on a consistent interval" |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** Provides application-level resource monitoring and visualization of resource operations and cost data. |
|  [Amazon EC2](https://aws.amazon.com/ec2/)  |  **Scheduled.** Solution is used to start and stop EC2 instances. The instances are identified by specific tags key/values which are configured in the solution. |
|  [Amazon RDS](https://aws.amazon.com/rds/)  |  **Scheduled.** Solution is used to change RDS DB instances status to Available or Stopped. The instances are identified by specific tags key/values which are configured in the solution. |
|  [Amazon Aurora](https://aws.amazon.com/rds/aurora/)  |  **Scheduled.** Solution is used to change Aurora clusters status to Available or Stopped. The clusters are identified by specific tags key/values which are configured in the solution. |
|  [Amazon Neptune](https://aws.amazon.com/neptune/)  |  **Scheduled.** Solution is used to change Neptune instances status to Available or Stopped. The instances are identified by specific tags key/values which are configured in the solution. |
|  [Amazon DocumentDB](https://aws.amazon.com/documentdb/)  |  **Scheduled.** Solution is used to change DocumentDB instances status to Available or Stopped. The instances are identified by specific tags key/values which are configured in the solution. |
|  [Amazon EC2 Auto Scaling groups](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-groups.html)  |  **Scheduled.** Solution is used to manage scheduled scaling rules for EC2 Auto Scaling groups. These rules will start/stop Auto Scaling groups in accordance with an associated schedule. Groups are identified by specific tags key/values which are configured in the solution. |

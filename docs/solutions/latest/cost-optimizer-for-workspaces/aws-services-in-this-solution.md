---
source_url: https://docs.aws.amazon.com/solutions/latest/cost-optimizer-for-workspaces/aws-services-in-this-solution.html
---

# AWS services in this solution
<a name="aws-services-in-this-solution"></a>

The following AWS services are included in this solution:

| AWS service | Description |
| --- | --- |
|  [Amazon WorkSpaces](https://aws.amazon.com/workspaces/)  | The solution does not create any resources for the Amazon WorkSpaces service but monitors the existing WorkSpaces in the customer accounts. |
|  [Amazon Simple Storage Service](https://aws.amazon.com/s3/)  | The solution creates an Amazon S3 bucket to store the daily and the monthly reports for the processed WorkSpaces. |
|  [AWS Organizations](https://aws.amazon.com/organizations/)  | The solution monitors WorkSpaces for accounts which are part of the given organization. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  | The solution creates Lambda functions to register spoke accounts with the hub account. |
|  [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)  | The solution creates an Amazon ECS task which is used to monitor WorkSpaces in hub and spoke accounts. |
|  [AWS Directory Service](https://aws.amazon.com/directoryservice/)  | The solution does not create any resources for the AWS Directory Service but monitors the WorkSpaces in the existing Directories. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  | The solution creates log groups to store logs for the Amazon ECS task and Lambda functions. |
|  [AWS Fargate](https://aws.amazon.com/fargate/)  | The solution uses Fargate launch type to run Amazon ECS tasks. |
|  [AWS EventBridge](https://aws.amazon.com/eventbridge/)  | The solution creates Amazon EventBridge rules to trigger an Amazon ECS task on a scheduled basis. |
|  [AWS IAM](https://aws.amazon.com/iam/)  | The solution creates IAM roles needed to access WorkSpaces in the hub and spoke accounts. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  | The solution creates a DyanamoDB table to store spoke account details. |
|  [AWS Service Catalog](https://aws.amazon.com/servicecatalog/)  | The solution creates a service catalog application and associates the CloudFormation stack to this application. |
|  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)  | The solution uses CloudFormation templates to deploy the resource needed to monitor WorkSpaces. |

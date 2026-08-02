---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/aws-services-in-this-solution.html
---

# AWS services in this solution
<a name="aws-services-in-this-solution"></a>

| AWS service | Description |
| --- | --- |
|  [AWS AppSync](https://aws.amazon.com/appsync)  |  **Core.** This solution uses AppSync to provide a serverless GraphQL API that the Web UI consumes. |
|  [Amazon CloudFront](https://aws.amazon.com/cloudfront/)  |  **Core**. This solution uses CloudFront with an Amazon S3 bucket as the origin. This restricts access to the Amazon S3 bucket so that it is not publicly accessible and prevents direct access from the bucket. |
|  [AWS Config](https://aws.amazon.com/config/)  |  **Core**. The solution uses AWS Config as the primary data source for the resources and relationships the solution discovers. |
|  [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/)  |  **Core**. The solution uses Amazon OpenSearch Service for application monitoring, log analytics, and observability. |
|  [Amazon DynamoDB](https://aws.amazon.com/dynamodb/)  |  **Core**. This solution uses DynamoDB to store configuration data for the solution. |
|  [Amazon Elastic Container Service (ECS)](https://aws.amazon.com/ecs/)  |  **Core**. This solution uses Amazon ECS to orchestrate running the task that discovers resources and relationships in your AWS accounts. |
|  [AWS Fargate](https://aws.amazon.com/fargate/)  |  **Core**. This solution uses AWS Fargate on Amazon ECS as the compute layer for the discovery task. |
|  [AWS Lambda](https://aws.amazon.com/lambda/)  |  **Core.** This solution uses serverless Lambda functions, with Node.js and Python runtimes, to handle API calls. |
|  [Amazon Neptune](https://aws.amazon.com/neptune/)  |  **Core.** This solution uses Neptune as the primary datastore for the resources and relationships the solution discovers. |
|  [Amazon Simple Storage Service](https://aws.amazon.com/s3/)  |  **Core.** This solution uses Amazon S3 for frontend and backend storage purposes. |
|  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)  |  **Supporting.** This solution uses CloudWatch to collect and visualize real-time logs, metrics, and event data in automated cases. Additionally, you can monitor the deployed solution’s resource usage and performance issues. |
|  [AWS CodeBuild](https://aws.amazon.com/codebuild/)  |  **Supporting**. This solution uses CodeBuild to build the Docker container that contains the code for the discovery task and to deploy the assets for the frontend to Amazon S3. |
|  [Amazon Cognito](https://aws.amazon.com/cognito/)  |  **Supporting.** This solution uses Cognito user pools to authenticate and authorize users to access the solution web UI. |
|  [AWS Systems Manager](https://aws.amazon.com/systems-manager/)  |  **Supporting.** This solution uses AWS Systems Manager to provide application-level resource monitoring and visualization of resource operations and cost data. |
|  [Amazon Virtual Private Cloud](https://aws.amazon.com/vpc/)  |  **Supporting**. This solutions uses a VPC to launch Neptune and OpenSearch databases in. |
|  [AWS WAF](https://aws.amazon.com/waf/)  |  **Supporting.** This solution uses AWS WAF to protect the AppSync API from common exploits and bots that can affect availability, compromise security, or consume excessive resources. |
|  [Amazon Athena](https://aws.amazon.com/athena/)  |  **Optional.** This solution uses Athena to query Cost and Usage Reports if the cost feature is enabled. |

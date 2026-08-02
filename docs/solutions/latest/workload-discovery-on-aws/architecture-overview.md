---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/architecture-overview.html
---

# Architecture overview
<a name="architecture-overview"></a>

This section provides a reference implementation architecture diagram for the components deployed with this solution.

## Architecture diagram
<a name="architecture-diagram"></a>

Deploying this solution with the default parameters builds the following environment in the AWS Cloud.

 **Workload Discovery on AWS architecture**

![workload discovery arch diagram](http://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/images/workload-discovery-arch-diagram.png)

The high-level process flow for the solution components deployed with the AWS CloudFormation template is as follows:

1.  [HTTP Strict-Transport-Security (HSTS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Headers/Strict-Transport-Security) adds security headers to each response from the [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution.

1. An [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3) bucket hosts the web UI, which is distributed with Amazon CloudFront. [Amazon Cognito](https://aws.amazon.com/cognito/) authenticates user access to the web UI.

1.  [AWS WAF](https://aws.amazon.com/waf/) protects the AppSync API from common exploits and bots that can affect availability, compromise security, or consume excessive resources.

1.  [AWS AppSync](https://aws.amazon.com/appsync/) endpoints allow the web UI component to request resource relationship data, query costs, import new AWS Regions, and update preferences. AWS AppSync also allows the discovery component to store persistent data in the solution’s databases.

1. AWS AppSync uses [JSON Web Tokens](https://datatracker.ietf.org/doc/html/rfc7519) (JWTs) provisioned by Amazon Cognito to authenticate each request.

1. The `Settings` [AWS Lambda](https://aws.amazon.com/lambda/) function persists imported Regions and other configurations to [Amazon DynamoDB](https://aws.amazon.com/dynamodb/).

1. The solution deploys [AWS Amplify](https://aws.amazon.com/amplify/) and an Amazon S3 bucket as the storage management component to store user preferences and saved architecture diagrams.

1. The data component uses the `Gremlin Resolver` AWS Lambda function to query and return data from an [Amazon Neptune](https://aws.amazon.com/neptune/) database.

1. The data component uses the `Search Resolver` Lambda function to query and persist resource data into an [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/) domain.

1. The `Cost` Lambda function uses [Amazon Athena](https://aws.amazon.com/athena) to query [AWS Cost and Usage Reports](https://docs.aws.amazon.com/cur/latest/userguide/what-is-cur.html) (AWS CUR) to provide estimated cost data to the web UI.

1. Amazon Athena runs queries on AWS CUR.

1. AWS CUR delivers the reports to the `CostAndUsageReportBucket` Amazon S3 bucket.

1. The `Cost` Lambda function stores the Amazon Athena results in the `AthenaResultsBucket` Amazon S3 bucket.

1.  [AWS CodeBuild](https://aws.amazon.com/codebuild) builds the discovery component container image in the image deployment component.

1.  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) (Amazon ECR) contains a [Docker image](https://docs.docker.com/engine/reference/commandline/images/) provided by the image deployment component.

1.  [Amazon Elastic Container Service](https://aws.amazon.com/ecs) (Amazon ECS) manages the [AWS Fargate](https://aws.amazon.com/fargate/) task and provides the configuration required to run the task. AWS Fargate runs a container task every 15 minutes to refresh inventory and resource data.

1.  [AWS Config](https://aws.amazon.com/config) and [AWS SDK](https://docs.aws.amazon.com/AWSJavaScriptSDK/latest/index.html) calls help the discovery component maintain an inventory of resource data from imported Regions, then store its results in the data component.

1. The AWS Fargate task persists the results of the AWS Config and AWS SDK calls into an Amazon Neptune database and an Amazon OpenSearch Service domain with API calls to the AppSync API.

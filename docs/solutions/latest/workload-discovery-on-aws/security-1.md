---
source_url: https://docs.aws.amazon.com/solutions/latest/workload-discovery-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit the [AWS Security Center](https://aws.amazon.com/security/).

## Resource access
<a name="resource-access"></a>

### IAM roles
<a name="iam-roles"></a>

IAM roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. Multiple roles are required to run Workload Discovery on AWS and discover resources in AWS accounts.

### Amazon Cognito
<a name="amazon-cognito"></a>

Amazon Cognito is used to authenticate access with short-lived, strong credentials granting access to components needed by Workload Discovery on AWS.

## Network access
<a name="network-access"></a>

### Amazon VPC
<a name="amazon-vpc"></a>

Workload Discovery on AWS is deployed within an Amazon VPC and configured according to best practices to deliver security and high availability. For additional details, refer to [Security best practices for your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html). VPC endpoints allow non-internet transit between services and are configured where available.

Security groups are used to control and isolate network traffic between the components needed to run Workload Discovery on AWS.

We recommend that you review the security groups and further restrict access as needed once the deployment is up and running.

### Amazon CloudFront
<a name="amazon-cloudfront"></a>

This solution deploys a web console UI [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket which is distributed by Amazon CloudFront. By using the origin access identity feature, the contents of this Amazon S3 bucket are accessible only through CloudFront. For more information, refer to [Restricting access to an Amazon S3 origin](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.

CloudFront activates additional security mitigations to append HTTP security headers to each viewer response. For additional details, refer to [Adding or removing HTTP headers in CloudFront responses](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/adding-response-headers.html).

This solution uses the default CloudFront certificate which has a minimum supported security protocol of TLS v1.0. To enforce the use of TLS v1.2 or TLS v1.3, you must use a custom SSL certificate instead of the default CloudFront certificate. For more information, refer to [How do I configure my CloudFront distribution to use an SSL/TLS certificate](https://aws.amazon.com/premiumsupport/knowledge-center/install-ssl-cloudfront/).

## Application configuration
<a name="application-configuration"></a>

### AWS AppSync
<a name="aws-appsync"></a>

Workload Discovery on AWS GraphQL APIs have request validation provided by AWS AppSync according to the [GraphQL specification](https://spec.graphql.org/June2018/#sec-Validation). Furthermore, authentication and authorization are implemented using IAM and Amazon Cognito, which use the JWT provided by Amazon Cognito when a user authenticates successfully in the web UI.

### AWS Lambda
<a name="aws-lambda"></a>

By default, the Lambda functions are configured with the most recent stable version of the language runtime. No sensitive data or secrets are logged. Service interactions are carried out with the least required privilege. Roles that define these privileges are not shared between functions.

### Amazon OpenSearch Service
<a name="amazon-opensearch-service"></a>

Amazon OpenSearch Service domains are configured with an access policy that restricts access to stop any unsigned requests made to the OpenSearch Service cluster. This is restricted to a single Lambda function.

The OpenSearch Service cluster is built with node-to-node encryption activated to add an extra layer of data protection on top of the existing OpenSearch Service [security features](https://docs.aws.amazon.com/elasticsearch-service/latest/developerguide/security.html).

### Log Retention
<a name="log-retention"></a>

This solution captures application and service logs by creating CloudWatch logs groups in your account. By default, logs are kept for 1 year. You can [adjust the LogRetentionPeriod parameter](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html#SettingLogRetention) for each log group, keeping the default retention period, or choosing a period between one day and 10 years based on your requirements.

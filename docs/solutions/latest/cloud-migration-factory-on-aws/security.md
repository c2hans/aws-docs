---
source_url: https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/security.html
---

# Security
<a name="security"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared model](https://aws.amazon.com/compliance/shared-responsibility-model/) can reduce your operational burden as AWS operates, manages, and controls the components from the host operating system and virtualization layer down to the physical security of the facilities in which the services operate. For more information about security on AWS, visit [AWS Cloud Security](https://aws.amazon.com/security).

## IAM roles
<a name="security-iam"></a>

AWS Identity and Access Management (IAM) roles allow you to assign granular access policies and permissions to services and users in the AWS Cloud. This solution creates IAM roles that grants the AWS Lambda function access to the other AWS services used in this solution.

## Amazon Cognito
<a name="security-cognito"></a>

The Amazon Cognito user created by this solution is a local user with permissions to access only the RestAPIs for this solution. This user does not have permissions to access any other services in your AWS account. For more information, refer to [Amazon Cognito User Pools](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools.html) in the *Amazon Cognito Developer Guide*.

The solution optionally supports external SAML sign-in through the configuration of federated identity providers and the hosted UI functionality of Amazon Cognito.

## Amazon CloudFront
<a name="security-cloudfront"></a>

This default solution deploys a web console [hosted](https://docs.aws.amazon.com/AmazonS3/latest/dev/WebsiteHosting.html) in an Amazon S3 bucket. To help reduce latency and improve security, this solution includes an [Amazon CloudFront](https://aws.amazon.com/cloudfront/) distribution with an origin access identity, which is a special CloudFront user that helps provide public access to the solution’s website bucket contents. For more information, refer to [Restricting Access to Amazon S3 Content by Using an Origin Access Identity](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/private-content-restricting-access-to-s3.html) in the *Amazon CloudFront Developer Guide*.

If a **private** deployment type is selected during stack deployment, then a CloudFront distribution is not deployed, and requires that another web hosting service is used to host the web console.

## AWS WAF - Web Application Firewall
<a name="amazon-aws-waf-aeb-application-firewall"></a>

If deployment type selected in the stack is Public with [AWS WAF](https://aws.amazon.com/waf/) then the CloudFormation will deploy the required AWS WAF Web ACLs and Rules configured to protect CloudFront, API Gateway, and Cognito endpoints created by the CMF solution. These endpoints will be restricted to allow only specified source IP addresses to access these endpoints. During stack deployment, two CIDR ranges must be supplied with the facility to add additional rules after deployment via the AWS WAF console.

**Important**
When configuring WAF IP restrictions, ensure that the IP address of your CMF automation server or the outgoing NAT Gateway IP is included in the allowed CIDR ranges. This is critical for the proper functioning of CMF automation scripts that need to access the solution’s API endpoints.

## Amazon API Gateway
<a name="security-apigateway"></a>

This solution deploys Amazon API Gateway REST APIs and uses the default API endpoint and SSL certificate. The default API endpoint supports TLSv1 security policy. It is recommended to use the TLS\_1\_2 security policy to enforce TLSv1.2\+ with your own custom domain name and custom SSL certificate. For more information, refer to [choosing a minimum TLS version for a custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) and [configuring custom domains](https://docs.aws.amazon.com/apigateway/latest/developerguide/how-to-custom-domains.html) in the *Amazon API Gateway Developer Guide*.

## Amazon CloudWatch Alarms / Canaries
<a name="security-cloudwatch"></a>

Amazon CloudWatch alarms help you monitor the solution’s functional and security assumptions are being followed. The solution includes logging and metrics for AWS Lambda functions and API Gateway endpoints. If additional monitoring is needed for your specific use case, you can configure CloudWatch alarms to monitor:
+  **API Gateway Monitoring:**
  + Set up alarms for 4XX and 5XX errors to detect unauthorized access attempts or API issues
  + Monitor API Gateway latency to ensure performance
  + Track the count of API requests to identify unusual patterns
+  **AWS Lambda Function Monitoring:**
  + Create alarms for Lambda function errors and timeouts
  + Monitor Lambda function duration to ensure optimal performance
  + Set up alarms for concurrent executions to prevent throttling

You can create these alarms using the CloudWatch console or through AWS CloudFormation templates. For detailed instructions on creating CloudWatch alarms, refer to [Creating Amazon CloudWatch Alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in the *Amazon CloudWatch User Guide*.

## Customer Managed AWS KMS Keys
<a name="security-kms"></a>

This solution uses encryption at rest for securing data and employs AWS managed keys for customer data. These keys are used to automatically and transparently encrypt your data before it is written to storage layers. Some users might prefer to have more control over their data encryption processes. This approach allows you to administer your own security credentials, offering a greater level of control and visibility. For more information, refer to [Basic Concepts](https://docs.aws.amazon.com/kms/latest/cryptographic-details/basic-concepts.html) and [AWS KMS Keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#kms_keys) in the *AWS Key Management Service Developer Guide*.

## Log Retention
<a name="security-logs"></a>

This solution captures application and service logs by creating Amazon CloudWatch logs groups in your account. By default, logs are kept for 10 years. You can adjust the LogRetentionPeriod parameter for each log group, switching to indefinite retention, or choosing a retention period between one day and 10 years based on your requirements. For more information, refer to [What is Amazon CloudWatch Logs?](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/WhatIsCloudWatchLogs.html#cloudwatch-logs-features) in the *Amazon CloudWatch Logs User Guide*.

## Amazon Bedrock
<a name="security-bedrock"></a>

The solution automatically selects the best available foundation model for your region during CloudFormation stack deployment. The selection process uses a Lambda function that calls `list_foundation_models()` and chooses the first available model from this priority order:

1.  `anthropic.claude-sonnet-4-20250514-v1:0` (Sonnet 4)

1.  `anthropic.claude-3-7-sonnet-20250219-v1:0` (Sonnet 3.7)

1.  `anthropic.claude-3-5-sonnet-20241022-v2:0` (Sonnet 3.5v2)

1.  `anthropic.claude-3-5-sonnet-20240620-v1:0` (Sonnet 3.5)

1.  `anthropic.claude-3-sonnet-20240229-v1:0` (Sonnet 3)

1.  `amazon.nova-pro-v1:0` (Nova Pro)

You must enable the selected model in your AWS account through the Bedrock console to use the GenAI features. The solution’s core functionalities remain fully operational without enabling the GenAI features. Customers can choose to use the tool with manual inputs if they prefer not to use the AI-assisted capabilities.

After deployment, you can find the selected model ARN in the CloudFormation stack outputs under the `GenAISelectedModelArn` field in the WPMStack.

![CloudFormation stack output showing selected GenAI model ARN](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/cloudformation-genai-model-output.png)

![Amazon Bedrock model enablement interface](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/bedrock-model-enablement.png)

This solution’s default configuration will deploy Amazon Bedrock Guardrails in order to:
+ Filter out harmful content
+ Block prompt injections that are irrelevant to your use case

![Amazon Bedrock Guardrails configuration interface](https://docs.aws.amazon.com/solutions/latest/cloud-migration-factory-on-aws/images/bedrock-guardrails.png)

For more information, refer to [Amazon Bedrock Guardrails](https://aws.amazon.com/bedrock/guardrails/). To opt out Guardrails in CMF solution, you can select false in template parameter section.

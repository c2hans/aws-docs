---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/security-1.html
---

# Security
<a name="security-1"></a>

When you build systems on AWS infrastructure, security responsibilities are shared between you and AWS. This [shared responsibility model](https://aws.amazon.com/compliance/shared-responsibility-model/) reduces your operational burden because AWS operates, manages, and controls the components including the host operating system, the virtualization layer, and the physical security of the facilities in which the services operate. For more information about AWS security, visit [AWS Cloud Security](https://aws.amazon.com/security/).

## Security best practices
<a name="security-best-practices"></a>

QnABot on AWS is designed with security best practices in mind. However, the security of a guidance differs based on your specific use case. Adding additional security measures can add to the cost of the guidance. The following are additional recommendations to enhance the security posture of QnABot on AWS in production environments.

## Amazon S3 access logging bucket configuration
<a name="amazon-s3-access-logging-bucket-configuration"></a>

We recommend having a central access logging Amazon S3 bucket, and updating the S3 buckets that this guidance creates to allowing access logging. QnABot on AWS by default configures a central access logging Amazon S3 bucket to store access logging. For more information about Amazon S3 access logging see [Enabling Amazon S3 server access logging](https://docs.aws.amazon.com/AmazonS3/latest/userguide/enable-server-access-logging.html) in the *Amazon Simple Storage Service User Guide*.

## Multi-factor authentication (MFA) in Amazon Cognito user pools
<a name="multi-factor-authentication-mfa-in-amazon-cognito-user-pools"></a>

This guidance creates only one user in its Cognito user pools. MFA is not activated by default; however, we recommend using MFA for users in Cognito for a stronger security posture in production workloads. For more information about setting up MFA in Cognito, see [Adding MFA to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-settings-mfa.html) and [Adding advanced security to a user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pool-settings-advanced-security.html) in the *Amazon Cognito Developer Guide.*

## Single sign-on with AWS IAM Identity Center
<a name="single-sign-on-with-aws-iam-identity-center"></a>

Guidance administrators can also federate into the content designer UI and OpenSearch Dashboards using single sign-on with AWS IAM Identity Center. In this case, IAM Identity Center serves as the identity provider for the Cognito user pool. Additionally, using Cognito, you can configure a SAML or OpenID Connect identity provider to federate with as well.

When users federate into Cognito, a user profile is dynamically provisioned for them, but they will not be granted access to QnABot on AWS until they are added to the `Admins` group. For more information about automating using a Lambda trigger see [Customizing User Pool Workflows with Lambda](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html) in the *Amazon Cognito Developer Guide*.

## AWS WAF for Amazon API Gateway
<a name="aws-waf-for-amazon-api-gateway"></a>

When the chatbot application is open to public access in production, we recommend allowing AWS WAF for API Gateway. For guidance about setting up AWS WAF, see [Using AWS WAF to protect your APIs](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-control-access-aws-waf.html) in the *Amazon API Gateway Developer Guide*. We also recommend reviewing the [AWS Best Practices for DDoS Resiliency](https://docs.aws.amazon.com/whitepapers/latest/aws-best-practices-ddos-resiliency/welcome.html) whitepaper for information about protecting your AWS applications from Distributed Denial of Service (DDoS) attacks.

For best security practices, we recommend adding rules/rule groups when creating your web access control list (ACL) in AWS WAF. AWS WAF provides the ability to set AWS managed rules and custom rule groups which the customer creates and maintains. We recommend adding [Core rule set](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-crs) and [Known bad inputs managed rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/aws-managed-rule-groups-baseline.html#aws-managed-rule-groups-baseline-known-bad-inputs) when setting up your web ACL. See [AWS WAF rule groups](https://docs.aws.amazon.com/waf/latest/developerguide/waf-rule-groups.html) in the *AWS WAF, AWS Firewall Manager, and AWS Shield Advanced Guide* for more information on setting up managed and created rule groups.

## Creating a custom domain in Amazon API Gateway
<a name="creating-a-custom-domain-in-amazon-api-gateway"></a>

By default, QnABot deploys the default domain in API Gateway. The default domain uses a TLS version 1.0 security policy, which uses outdated encryption protocols and weak encryption cyphers. We recommend that the customer sets up a [custom domain name](setting-up-a-custom-domain-name-for-qnabot-content-designer-and-client.md) and uses a TLS version 1.2 security policy. See [Choosing a security policy for your custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html) in the *Amazon API Gateway Guide.*

## Children Online Privacy Protection Act (COPPA) settings for Amazon Lex
<a name="children-online-privacy-protection-act-coppa-settings-for-amazon-lex"></a>

When using this guidance to create or update an Amazon Lex chatbot, set the Amazon Lex API **childDirected** parameter to `true` if the bot’s users are subject to COPPA. For more information, see [DataPrivacy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DataPrivacy.html) in the *Amazon Lex API Reference*.

## AWS CloudFormation parameters
<a name="aws-cloudformation-parameters"></a>

Before deployment, we recommend reviewing the **PublicOrPrivate** parameter. It has two possible values: `Public` or `Private`. We recommend choosing `Private` unless the use case for this guidance dictates having the chatbot open to the public without needing to sign up or register. If you select `Public`, we recommend enabling [AWS WAF for Amazon API Gateway](#aws-waf-for-amazon-api-gateway).

## Amazon Cognito
<a name="amazon-cognito"></a>

The guidance uses a Cognito user pool for controlling administrative access to the QnABot on AWS content designer UI, Amazon Lex web client, and OpenSearch Dashboards. Users are also required to be members of the `Admins` group in the Cognito user pool.

The content designer UI requires that you sign in with credentials defined in an Amazon Cognito user pool. Using temporary AWS credentials from Cognito, the content designer UI interacts with secure API Gateway endpoints backed by the content designer’s Lambda functions.

The Amazon Lex web client is deployed to an Amazon S3 bucket in your account, and accessed via API Gateway. An API Gateway endpoint provides run time configuration. Using this configuration, the web client connects to Cognito to obtain temporary AWS credentials, and then connects with the Amazon Lex service.

## AWS Lambda
<a name="aws-lambda"></a>

The guidance uses Lambda functions. Depending on your use case, we recommend that you configure [Lambda function-level concurrency run limits](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html). Adding concurrency limits can prevent a rapid spike in usage and costs, while also increasing or lowering the default concurrency limit.

## IAM roles
<a name="iam-roles"></a>

IAM roles allow customers to assign granular access policies and permissions to services and users on the AWS Cloud. This guidance creates IAM roles with least privileges that grant the guidance’s resources with needed permissions.

## CloudWatch Logs
<a name="cloudwatch-logs"></a>

For QnABot on AWS, CloudWatch Logs are set by default to never expire. You can [Export log data to Amazon S3](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/S3Export.html).

## Cross-site scripting (XSS) protection
<a name="xss-protection"></a>

QnABot on AWS applies server-side HTML sanitization to the `alt.html` and `alt.markdown` response fields to prevent stored XSS attacks. The guidance uses an allowlist of safe HTML tags and attributes. If your Q&A responses require custom HTML tags or attributes beyond the defaults, see [Server-side HTML sanitization](server-side-html-sanitization.md) for instructions on updating the allowlist.

## Data storage and protection
<a name="data-storage-and-protection"></a>

The guidance uses multiple services to store and protect your data. This guidance defaults to the following when storing and protecting the customer’s data:

| Service/Resource | Default |
| --- | --- |
| CloudWatch Logs | - Default CloudWatch Logs set to **Never Expire**. |
| DynamoDB | - User table stores chat message history (per user) - never expires.<br />- Data fully encrypted at rest (managed by DynamoDB).<br />- Point-in-time recovery enabled by default.<br />- Continuous backups disabled. |
| OpenSearch Dashboards index | - Default expiry set to 30 days. |
| Amazon S3 | - Default **Never Expire** for Metrics bucket and Export bucket.<br />- All buckets are enabled with server-side encryption (SSE) by default. See [Setting default server-side encryption behavior for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) for additional guidance.<br />- Access logging is disabled, customer can configure. For additional guidance, see [Setting default server-side encryption for Amazon S3 buckets](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html) in the *Amazon Simple Storage Service User Guide*. |
| Amazon Lex | - Default, logs not enabled. For additional guidance, see [Conversation Logs](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-configure.html) in the *Amazon Lex V2 Developer Guide*.<br />- Encrypting conversation logs is optional, but can be implemented if needed. For additional guidance, see [Encrypting Conversation Logs](https://docs.aws.amazon.com/lexv2/latest/dg/conversation-logs-configure.html#conversation-logs-enable) in the *Amazon Lex V2 Developer Guide*.<br />- Audio logs are stored in Amazon S3 (default encryption).<br />- The **childDirected** parameter for COPPA defaults to `false`. For additional guidance, see [DataPrivacy](https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DataPrivacy.html) in the *Amazon Lex API Reference*.<br />- PII redaction capability is implemented on logs. |
| AWS Key Management Service | - The guidance can store PII data. By default, DynamoDB is encrypted, but we recommend using Customer Managed Keys (CMK) if you intend to store sensitive data. For additional guidance, see the [utility\_scripts](https://github.com/aws-solutions/qnabot-on-aws/tree/main/source/utility_scripts) section in the GitHub repository. |
| Amazon Data Firehose | - SSE enabled via AWS KMS key. |

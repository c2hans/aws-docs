---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/step-4-post-deployment-configuration.html
---

# Step 4: Post-deployment configuration
<a name="step-4-post-deployment-configuration"></a>

This section provides recommendations for configuring the solution after deployment.

## Amazon S3 bucket versioning, lifecycle policies, and cross-Region replication
<a name="amazon-s3-bucket-versioning-lifecycle-policies-and-cross-region-replication"></a>

This solution doesn’t enforce lifecycle configurations on the buckets it creates. We recommend the following:
+ Setting lifecycle configurations for production deployments. For details, see [Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) in the *Amazon Simple Storage Service User Guide*.
+ Enabling [versioning](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Versioning.html) and [cross-Region replication](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html) for Amazon S3 buckets based on the use case for which the solution is deployed.

## Amazon DynamoDB backups
<a name="amazon-dynamodb-backups"></a>

This solution uses DynamoDB for several purposes (see [AWS services in this solution](architecture-details.md#aws-services-in-this-solution)). The solution doesn’t enable backups for the tables it creates. We recommend creating a backup of this feature for production deployments. See [Backing up a DynamoDB table](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/Backup.Tutorial.html) and [Using AWS Backup for DynamoDB](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/backuprestore_HowItWorksAWS.html) for details.

## Amazon CloudWatch dashboard and alarms
<a name="amazon-cloudwatch-dashboard-and-alarms"></a>

The solution deploys a custom dashboard in CloudWatch to render charts from custom published metrics and AWS service metrics. We recommend creating CloudWatch [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) and adding notifications based on the use case for which the solution is deployed.

## Amazon CloudWatch Logs
<a name="amazon-cloudwatch-logs"></a>

Lambda logs are configured to never expire and API Gateway logs are configured with a 10-year expiry. You can update the expiry of the respective log groups to align with your enterprise’s record retention policy.

## Custom web domains with TLS v1.2 or higher certificates
<a name="custom-web-domains-with-tls-v1.2-or-higher-certificates"></a>

The solution deploys a web UI and Edge Optimized API Gateway using CloudFront. CloudFront’s domain doesn’t enforce TLS v1.2 or higher certificates. We recommend creating a custom domain using [Amazon Route 53](https://aws.amazon.com/route53/), creating a certificate using [AWS Certificate Manager](https://aws.amazon.com/certificate-manager/), or using an existing certificate if your organization has one.

For additional details, refer to the [Amazon Route 53 Developer Guide](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/domain-register.html) and [Choosing a minimum TLS version for a custom domain in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/apigateway-custom-domain-tls-version.html).

## Scaling with Amazon Kendra
<a name="scaling-with-amazon-kendra"></a>

This solution provides the ability to use Amazon Kendra to perform NLP-powered intelligent search across the ingested documents. You can increase the capacity of Amazon Kendra using the following CloudFormation parameters for larger workloads:

| Parameter | Default | Description |
| --- | --- | --- |
|  [Amazon Kendra additional query capacity](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-querycapacityunits)  |  `0`  | The amount of extra query capacity for an index and [GetQuerySuggestions](https://docs.aws.amazon.com/kendra/latest/dg/API_GetQuerySuggestions.html) capacity. An additional capacity unit for an index provides approximately 8,000 queries per day. |
|  [Amazon Kendra additional storage capacity](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-kendra-index-capacityunitsconfiguration.html#cfn-kendra-index-capacityunitsconfiguration-storagecapacityunits)  |  `0`  | The amount of extra storage capacity for an index. A single capacity unit provides 30 GB of storage space or 100,000 documents, whichever reaches first. |
|  [Amazon Kendra edition](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-kendra-index.html)  |  `Developer`  | Amazon Kendra provides Developer and Enterprise Editions to create indexes. For more information about the differences between Amazon Kendra Editions, see [Amazon Kendra pricing](https://aws.amazon.com/kendra/pricing/). |

To modify the values of these CloudFormation parameters, select the appropriate values at the time of stack deployment. For more information on query and storage capacity units, see [Adjusting capacity](https://docs.aws.amazon.com/kendra/latest/dg/adjusting-capacity.html).

**Note**
If the Text use case is not deployed with RAG enabled, then an Amazon Kendra index is not used or created.

## Setting up SSO using Idp federation
<a name="setting-up-sso-using-idp-federation"></a>

This solution allows integration with external identity providers that support SAML or OIDC based identity federation. When the solution deploys, it creates an Amazon Cognito user pool and individual app client integration for the Deployment dashboard and individual use cases. Based on the external Idp, follow the steps provided in the [Configuring identity providers for your user pool](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-identity-provider.html) section of the *Amazon Cognito Developer Guide* and choose the app client integration for the Deployment dashboard or use case you would like to setup SSO with.

To pass the user group information to knowledge base or vector stores in a RAG based architecture, you will need to map user groups from the external Idp to Amazon Cognito user groups. The solution provides an initial scaffolding [Lambda function](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/tree/main/source/lambda/ext-idp-group-mapper) trigger to be mapped with the [pre token generation](https://docs.aws.amazon.com/cognito/latest/developerguide/user-pool-lambda-pre-token-generation.html) phase. The Lambda function has the [group\_mapping.json](https://github.com/aws-solutions/generative-ai-application-builder-on-aws/tree/main/source/lambda/ext-idp-group-mapper/config/group_mapping.json) file which must be updated to provide the group mappings. Refer to [Customizing user pool workflows with Lambda triggers](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-identity-pools-working-with-aws-lambda-triggers.html) for Lambda triggers supported by Amazon Cognito.

## Manual User Pool configuration
<a name="manual-user-pool-configuration"></a>

If you choose not to pass an Admin or default user email during deployment, you must manually create the appropriate user groups in Amazon Cognito to ensure correct permissions:

1. For the Deployment dashboard, create a group named `Admin` in your Cognito user pool.

1. For each use case, create a group named `${UseCaseName}-Users` in your Cognito user pool, where `${UseCaseName}` is the name of your deployed use case.

These groups are required for the authorization mechanism to work correctly. Any users you want to grant access to must be added to the appropriate groups.

If `placeholder@example.com` is passed, the Cognito group will be created, but you must still create the associated users and assign them to the group.

## Customizing login screen
<a name="customizing-login-screen"></a>

This solution uses [Amazon Cognito hosted UI](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-integration.html) to render the login page. To customize the built-in sign-in page, refer to [Customizing the built-in sign-in and sign-up webpages](https://docs.aws.amazon.com/cognito/latest/developerguide/cognito-user-pools-app-ui-customization.html) in the *Amazon Cognito Developer Guide*.

## Additional security considerations
<a name="additional-security-considerations"></a>

Based on the use case for which you deploy the solution, review the following security recommendations:
+  **Customer managed AWS KMS encryption keys** - The solution uses AWS managed AWS KMS keys by default, since these are available at no additional cost. Review your use case to determine if you should update the solution to use [customer managed AWS KMS keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html#customer-cmk).
+  **API Gateway throttling rules** - The solution deploys with default throttling rules on API Gateway. Based on your use case and expected transaction volumes, we recommend that you configure throttling for the APIs. For details, see [Throttle API requests for better throughput](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-request-throttling.html) in the *Amazon API Gateway Developer Guide*.
+  **Enabling AWS CloudTrail** - As a recommended security practice, consider enabling [AWS CloudTrail](https://aws.amazon.com/cloudtrail/) in the AWS account where the solution is deployed to log API calls in the AWS account. For details, see the [AWS CloudTrail User Guide](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-user-guide.html).
+  **Drift detection** - We recommend configuring drift detection on CloudFormation stacks to identify and be notified of unintentional or malicious changes to the deployed solution stack. For details, see [Implementing an alarm to automatically detect drift in AWS CloudFormation stacks](https://aws.amazon.com/blogs/mt/implementing-an-alarm-to-automatically-detect-drift-in-aws-cloudformation-stacks/).
+  **Cognito JSON Web Tokens (JWTs)** - The solution uses Amazon Cognito-issued JWTs to authenticate with the REST API endpoints. We configured the solution with a five-minute expiry for [ID tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-id-token.html) and [access tokens](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-access-token.html). When a user logs out, their ability to generate new tokens is revoked ([refresh token](https://docs.aws.amazon.com/cognito/latest/developerguide/amazon-cognito-user-pools-using-the-refresh-token.html) is revoked). However, until the expiry of the current token, any requests to the API endpoint will be successfully authenticated, since they have a valid token. Review the security considerations for your use case and adjust the token validity period.

 **Customizing lifecycle policies:**

For production deployments, review and adjust the lifecycle policies based on your retention requirements. See [Setting lifecycle configuration on a bucket](https://docs.aws.amazon.com/AmazonS3/latest/userguide/how-to-set-lifecycle-configuration-intro.html) in the *Amazon Simple Storage Service User Guide*.

## Multimodal file storage and lifecycle
<a name="multimodal-file-storage-and-lifecycle"></a>

If you enabled multimodal input capabilities (**MultimodalEnabled** set to `Yes`) for your use case, the solution creates an Amazon S3 bucket to store uploaded files and a DynamoDB table to track file metadata.

 **Default lifecycle policies:**
+  **S3 files:** Automatically deleted after 48 hours
+  **DynamoDB metadata:** Records expire after 24 hours (conversation history TTL)

 **Security considerations:**
+ Files are partitioned by use case ID, user ID, conversation ID and message ID and a file is stored with a UUID name instead. The mapping for the UUID to file names is available in the DynamoDB metadata table
+ Users can only access files they uploaded within their own conversations
+ File type validation is performed using magic number detection
+ We recommend enabling [Amazon GuardDuty Malware Protection for S3](https://docs.aws.amazon.com/guardduty/latest/ug/gdu-malware-protection-s3.html) to scan uploaded files for malicious content

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

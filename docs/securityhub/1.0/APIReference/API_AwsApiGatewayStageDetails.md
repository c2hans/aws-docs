---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayStageDetails.html
---

# AwsApiGatewayStageDetails
<a name="API_AwsApiGatewayStageDetails"></a>

Provides information about a version 1 Amazon API Gateway stage.

## Contents
<a name="API_AwsApiGatewayStageDetails_Contents"></a>

 ** AccessLogSettings **   <a name="securityhub-Type-AwsApiGatewayStageDetails-AccessLogSettings"></a>
Settings for logging access for the stage.
Type: [AwsApiGatewayAccessLogSettings](API_AwsApiGatewayAccessLogSettings.md) object
Required: No

 ** CacheClusterEnabled **   <a name="securityhub-Type-AwsApiGatewayStageDetails-CacheClusterEnabled"></a>
Indicates whether a cache cluster is enabled for the stage.
Type: Boolean
Required: No

 ** CacheClusterSize **   <a name="securityhub-Type-AwsApiGatewayStageDetails-CacheClusterSize"></a>
If a cache cluster is enabled, the size of the cache cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CacheClusterStatus **   <a name="securityhub-Type-AwsApiGatewayStageDetails-CacheClusterStatus"></a>
If a cache cluster is enabled, the status of the cache cluster.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CanarySettings **   <a name="securityhub-Type-AwsApiGatewayStageDetails-CanarySettings"></a>
Information about settings for canary deployment in the stage.
Type: [AwsApiGatewayCanarySettings](API_AwsApiGatewayCanarySettings.md) object
Required: No

 ** ClientCertificateId **   <a name="securityhub-Type-AwsApiGatewayStageDetails-ClientCertificateId"></a>
The identifier of the client certificate for the stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedDate **   <a name="securityhub-Type-AwsApiGatewayStageDetails-CreatedDate"></a>
Indicates when the stage was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DeploymentId **   <a name="securityhub-Type-AwsApiGatewayStageDetails-DeploymentId"></a>
The identifier of the deployment that the stage points to.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsApiGatewayStageDetails-Description"></a>
A description of the stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** DocumentationVersion **   <a name="securityhub-Type-AwsApiGatewayStageDetails-DocumentationVersion"></a>
The version of the API documentation that is associated with the stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastUpdatedDate **   <a name="securityhub-Type-AwsApiGatewayStageDetails-LastUpdatedDate"></a>
Indicates when the stage was most recently updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** MethodSettings **   <a name="securityhub-Type-AwsApiGatewayStageDetails-MethodSettings"></a>
Defines the method settings for the stage.
Type: Array of [AwsApiGatewayMethodSettings](API_AwsApiGatewayMethodSettings.md) objects
Required: No

 ** StageName **   <a name="securityhub-Type-AwsApiGatewayStageDetails-StageName"></a>
The name of the stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** TracingEnabled **   <a name="securityhub-Type-AwsApiGatewayStageDetails-TracingEnabled"></a>
Indicates whether active tracing with AWS X-Ray is enabled for the stage.
Type: Boolean
Required: No

 ** Variables **   <a name="securityhub-Type-AwsApiGatewayStageDetails-Variables"></a>
A map that defines the stage variables for the stage.
Variable names can have alphanumeric and underscore characters.
Variable values can contain the following characters:
+ Uppercase and lowercase letters
+ Numbers
+ Special characters -.\_\~:/?\#&=,
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** WebAclArn **   <a name="securityhub-Type-AwsApiGatewayStageDetails-WebAclArn"></a>
The ARN of the web ACL associated with the stage.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsApiGatewayStageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayStageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayStageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayStageDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

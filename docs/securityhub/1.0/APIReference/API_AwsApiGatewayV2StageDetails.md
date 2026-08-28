---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiGatewayV2StageDetails.html
---

# AwsApiGatewayV2StageDetails
<a name="API_AwsApiGatewayV2StageDetails"></a>

Contains information about a version 2 stage for Amazon API Gateway.

## Contents
<a name="API_AwsApiGatewayV2StageDetails_Contents"></a>

 ** AccessLogSettings **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-AccessLogSettings"></a>
Information about settings for logging access for the stage.
Type: [AwsApiGatewayAccessLogSettings](API_AwsApiGatewayAccessLogSettings.md) object
Required: No

 ** ApiGatewayManaged **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-ApiGatewayManaged"></a>
Indicates whether the stage is managed by API Gateway.
Type: Boolean
Required: No

 ** AutoDeploy **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-AutoDeploy"></a>
Indicates whether updates to an API automatically trigger a new deployment.
Type: Boolean
Required: No

 ** ClientCertificateId **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-ClientCertificateId"></a>
The identifier of a client certificate for a stage. Supported only for WebSocket API calls.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CreatedDate **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-CreatedDate"></a>
Indicates when the stage was created.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DefaultRouteSettings **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-DefaultRouteSettings"></a>
Default route settings for the stage.
Type: [AwsApiGatewayV2RouteSettings](API_AwsApiGatewayV2RouteSettings.md) object
Required: No

 ** DeploymentId **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-DeploymentId"></a>
The identifier of the deployment that the stage is associated with.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Description **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-Description"></a>
The description of the stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastDeploymentStatusMessage **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-LastDeploymentStatusMessage"></a>
The status of the last deployment of a stage. Supported only if the stage has automatic deployment enabled.
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastUpdatedDate **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-LastUpdatedDate"></a>
Indicates when the stage was most recently updated.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** RouteSettings **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-RouteSettings"></a>
The route settings for the stage.
Type: [AwsApiGatewayV2RouteSettings](API_AwsApiGatewayV2RouteSettings.md) object
Required: No

 ** StageName **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-StageName"></a>
The name of the stage.
Type: String
Pattern: `.*\S.*`
Required: No

 ** StageVariables **   <a name="securityhub-Type-AwsApiGatewayV2StageDetails-StageVariables"></a>
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

## See Also
<a name="API_AwsApiGatewayV2StageDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiGatewayV2StageDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiGatewayV2StageDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiGatewayV2StageDetails)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_CreateDeploymentStrategy.html
---

# CreateDeploymentStrategy
<a name="API_CreateDeploymentStrategy"></a>

Creates a deployment strategy that defines important criteria for rolling out your configuration to the designated targets. A deployment strategy includes the overall duration required, a percentage of targets to receive the deployment during each interval, an algorithm that defines how percentage grows, and bake time.

## Request Syntax
<a name="API_CreateDeploymentStrategy_RequestSyntax"></a>

```
POST /deploymentstrategies HTTP/1.1
Content-type: application/json

{
   "DeploymentDurationInMinutes": {{number}},
   "Description": "{{string}}",
   "FinalBakeTimeInMinutes": {{number}},
   "GrowthFactor": {{number}},
   "GrowthType": "{{string}}",
   "Name": "{{string}}",
   "ReplicateTo": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateDeploymentStrategy_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateDeploymentStrategy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeploymentDurationInMinutes](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-DeploymentDurationInMinutes"></a>
Total amount of time for a deployment to last.
 AWS AppConfig Agent supports deploying feature flag or free-form configuration data to specific segments or individual users during a gradual rollout. Entity-based gradual deployments ensure that once a user or segment receives a configuration version, they continue to receive that same version throughout the deployment period, regardless of which compute resource serves their requests. For more information, see [Using AWS AppConfig Agent for user-based or entity-based gradual deployments](https://docs.aws.amazon.com/appconfig/latest/userguide/appconfig-agent-how-to-use.html#appconfig-entity-based-gradual-deployments)
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: Yes

 ** [Description](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-Description"></a>
A description of the deployment strategy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [FinalBakeTimeInMinutes](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-FinalBakeTimeInMinutes"></a>
Specifies the amount of time AWS AppConfig monitors for Amazon CloudWatch alarms after the configuration has been deployed to 100% of its targets, before considering the deployment to be complete. If an alarm is triggered during this time, AWS AppConfig rolls back the deployment. You must configure permissions for AWS AppConfig to roll back based on CloudWatch alarms. For more information, see [Configuring permissions for rollback based on Amazon CloudWatch alarms](https://docs.aws.amazon.com/appconfig/latest/userguide/getting-started-with-appconfig-cloudwatch-alarms-permissions.html) in the * AWS AppConfig User Guide*.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** [GrowthFactor](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-GrowthFactor"></a>
The percentage of targets to receive a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.
Required: Yes

 ** [GrowthType](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-GrowthType"></a>
The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:
 **Linear**: For this type, AWS AppConfig processes the deployment by dividing the total number of targets by the value specified for `Step percentage`. For example, a linear deployment that uses a `Step percentage` of 10 deploys the configuration to 10 percent of the hosts. After those deployments are complete, the system deploys the configuration to the next 10 percent. This continues until 100% of the targets have successfully received the configuration.
 **Exponential**: For this type, AWS AppConfig processes the deployment exponentially using the following formula: `G*(2^N)`. In this formula, `G` is the growth factor specified by the user and `N` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:
 `2*(2^0)`
 `2*(2^1)`
 `2*(2^2)`
Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`
Required: No

 ** [Name](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-Name"></a>
A name for the deployment strategy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [ReplicateTo](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-ReplicateTo"></a>
Save the deployment strategy to a Systems Manager (SSM) document.
Type: String
Valid Values: `NONE | SSM_DOCUMENT`
Required: No

 ** [Tags](#API_CreateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-CreateDeploymentStrategy-request-Tags"></a>
Metadata to assign to the deployment strategy. Tags help organize and categorize your AWS AppConfig resources. Each tag consists of a key and an optional value, both of which you define.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateDeploymentStrategy_ResponseSyntax"></a>

```
HTTP/1.1 201
Content-type: application/json

{
   "DeploymentDurationInMinutes": number,
   "Description": "string",
   "FinalBakeTimeInMinutes": number,
   "GrowthFactor": number,
   "GrowthType": "string",
   "Id": "string",
   "Name": "string",
   "ReplicateTo": "string"
}
```

## Response Elements
<a name="API_CreateDeploymentStrategy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 201 response.

The following data is returned in JSON format by the service.

 ** [DeploymentDurationInMinutes](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-DeploymentDurationInMinutes"></a>
Total amount of time the deployment lasted.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.

 ** [Description](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-Description"></a>
The description of the deployment strategy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [FinalBakeTimeInMinutes](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-FinalBakeTimeInMinutes"></a>
The amount of time that AWS AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.

 ** [GrowthFactor](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-GrowthFactor"></a>
The percentage of targets that received a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.

 ** [GrowthType](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-GrowthType"></a>
The algorithm used to define how percentage grew over time.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`

 ** [Id](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-Id"></a>
The deployment strategy ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Name](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-Name"></a>
The name of the deployment strategy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ReplicateTo](#API_CreateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-CreateDeploymentStrategy-response-ReplicateTo"></a>
Save the deployment strategy to a Systems Manager (SSM) document.
Type: String
Valid Values: `NONE | SSM_DOCUMENT`

## Errors
<a name="API_CreateDeploymentStrategy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The number of one more AWS AppConfig resources exceeds the maximum allowed. Verify that your environment doesn't exceed the following service quotas:
Applications: 100 max
To resolve this issue, you can delete one or more resources and try again. Or, you can request a quota increase. For more information about quotas and to request an increase, see [Service quotas for AWS AppConfig](https://docs.aws.amazon.com/general/latest/gr/appconfig.html#limits_appconfig) in the Amazon Web Services General Reference.
HTTP Status Code: 402

## Examples
<a name="API_CreateDeploymentStrategy_Examples"></a>

### Example
<a name="API_CreateDeploymentStrategy_Example_1"></a>

This example illustrates one usage of CreateDeploymentStrategy.

#### Sample Request
<a name="API_CreateDeploymentStrategy_Example_1_Request"></a>

```
POST /deploymentstrategies HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.create-deployment-strategy
X-Amz-Date: 20210916T214947Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210916/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 118

{
	"Name": "Example-Deployment",
	"DeploymentDurationInMinutes": 15,
	"GrowthFactor": 25.0,
	"ReplicateTo": "SSM_DOCUMENT"
}
```

#### Sample Response
<a name="API_CreateDeploymentStrategy_Example_1_Response"></a>

```
{
	"DeploymentDurationInMinutes": 15,
	"Description": null,
	"FinalBakeTimeInMinutes": 0,
	"GrowthFactor": 25.0,
	"GrowthType": "LINEAR",
	"Id": "1225qzk",
	"Name": "Example-Deployment",
	"ReplicateTo": "SSM_DOCUMENT"
}
```

## See Also
<a name="API_CreateDeploymentStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/CreateDeploymentStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/CreateDeploymentStrategy)

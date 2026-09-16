---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_UpdateDeploymentStrategy.html
---

# UpdateDeploymentStrategy
<a name="API_UpdateDeploymentStrategy"></a>

Updates a deployment strategy.

## Request Syntax
<a name="API_UpdateDeploymentStrategy_RequestSyntax"></a>

```
PATCH /deploymentstrategies/{{DeploymentStrategyId}} HTTP/1.1
Content-type: application/json

{
   "DeploymentDurationInMinutes": {{number}},
   "Description": "{{string}}",
   "FinalBakeTimeInMinutes": {{number}},
   "GrowthFactor": {{number}},
   "GrowthType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateDeploymentStrategy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DeploymentStrategyId](#API_UpdateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-request-uri-DeploymentStrategyId"></a>
The deployment strategy ID.
Pattern: `(^[a-z0-9]{4,7}$|^AppConfig\.[A-Za-z0-9]{9,40}$)`
Required: Yes

## Request Body
<a name="API_UpdateDeploymentStrategy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DeploymentDurationInMinutes](#API_UpdateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-request-DeploymentDurationInMinutes"></a>
Total amount of time for a deployment to last.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** [Description](#API_UpdateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-request-Description"></a>
A description of the deployment strategy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

 ** [FinalBakeTimeInMinutes](#API_UpdateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-request-FinalBakeTimeInMinutes"></a>
The amount of time that AWS AppConfig monitors for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.
Required: No

 ** [GrowthFactor](#API_UpdateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-request-GrowthFactor"></a>
The percentage of targets to receive a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.
Required: No

 ** [GrowthType](#API_UpdateDeploymentStrategy_RequestSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-request-GrowthType"></a>
The algorithm used to define how percentage grows over time. AWS AppConfig supports the following growth types:
 **Linear**: For this type, AWS AppConfig processes the deployment by increments of the growth factor evenly distributed over the deployment time. For example, a linear deployment that uses a growth factor of 20 initially makes the configuration available to 20 percent of the targets. After 1/5th of the deployment time has passed, the system updates the percentage to 40 percent. This continues until 100% of the targets are set to receive the deployed configuration.
 **Exponential**: For this type, AWS AppConfig processes the deployment exponentially using the following formula: `G*(2^N)`. In this formula, `G` is the growth factor specified by the user and `N` is the number of steps until the configuration is deployed to all targets. For example, if you specify a growth factor of 2, then the system rolls out the configuration as follows:
 `2*(2^0)`
 `2*(2^1)`
 `2*(2^2)`
Expressed numerically, the deployment rolls out as follows: 2% of the targets, 4% of the targets, 8% of the targets, and continues until the configuration has been deployed to all targets.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`
Required: No

## Response Syntax
<a name="API_UpdateDeploymentStrategy_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_UpdateDeploymentStrategy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DeploymentDurationInMinutes](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-DeploymentDurationInMinutes"></a>
Total amount of time the deployment lasted.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.

 ** [Description](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-Description"></a>
The description of the deployment strategy.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [FinalBakeTimeInMinutes](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-FinalBakeTimeInMinutes"></a>
The amount of time that AWS AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.

 ** [GrowthFactor](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-GrowthFactor"></a>
The percentage of targets that received a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.

 ** [GrowthType](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-GrowthType"></a>
The algorithm used to define how percentage grew over time.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`

 ** [Id](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-Id"></a>
The deployment strategy ID.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Name](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-Name"></a>
The name of the deployment strategy.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ReplicateTo](#API_UpdateDeploymentStrategy_ResponseSyntax) **   <a name="appconfig-UpdateDeploymentStrategy-response-ReplicateTo"></a>
Save the deployment strategy to a Systems Manager (SSM) document.
Type: String
Valid Values: `NONE | SSM_DOCUMENT`

## Errors
<a name="API_UpdateDeploymentStrategy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
The input fails to satisfy the constraints specified by an AWS service.
 ** Details **
Detailed information about the input that failed to satisfy the constraints specified by a call.
HTTP Status Code: 400

 ** InternalServerException **
There was an internal failure in the AWS AppConfig service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource could not be found.
HTTP Status Code: 404

## Examples
<a name="API_UpdateDeploymentStrategy_Examples"></a>

### Example
<a name="API_UpdateDeploymentStrategy_Example_1"></a>

This example illustrates one usage of UpdateDeploymentStrategy.

#### Sample Request
<a name="API_UpdateDeploymentStrategy_Example_1_Request"></a>

```
PATCH /deploymentstrategies/1225qzk HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.update-deployment-strategy
X-Amz-Date: 20210920T213749Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 30

{
    "FinalBakeTimeInMinutes": 20
}
```

#### Sample Response
<a name="API_UpdateDeploymentStrategy_Example_1_Response"></a>

```
{
    "Id": "1225qzk",
    "Name": "Example-Deployment",
    "DeploymentDurationInMinutes": 15,
    "GrowthType": "LINEAR",
    "GrowthFactor": 25.0,
    "FinalBakeTimeInMinutes": 20,
    "ReplicateTo": "SSM_DOCUMENT"
}
```

## See Also
<a name="API_UpdateDeploymentStrategy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/UpdateDeploymentStrategy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/UpdateDeploymentStrategy)

---
source_url: https://docs.aws.amazon.com/appconfig/2019-10-09/APIReference/API_StopDeployment.html
---

# StopDeployment
<a name="API_StopDeployment"></a>

Stops a deployment. This API action works only on deployments that have a status of `DEPLOYING`, unless an `AllowRevert` parameter is supplied. If the `AllowRevert` parameter is supplied, the status of an in-progress deployment will be `ROLLED_BACK`. The status of a completed deployment will be `REVERTED`. AWS AppConfig only allows a revert within 72 hours of deployment completion.

## Request Syntax
<a name="API_StopDeployment_RequestSyntax"></a>

```
DELETE /applications/{{ApplicationId}}/environments/{{EnvironmentId}}/deployments/{{DeploymentNumber}} HTTP/1.1
Allow-Revert: {{AllowRevert}}
```

## URI Request Parameters
<a name="API_StopDeployment_RequestParameters"></a>

The request uses the following URI parameters.

 ** [AllowRevert](#API_StopDeployment_RequestSyntax) **   <a name="appconfig-StopDeployment-request-AllowRevert"></a>
A Boolean that enables AWS AppConfig to rollback a `COMPLETED` deployment to the previous configuration version. This action moves the deployment to a status of `REVERTED`.

 ** [ApplicationId](#API_StopDeployment_RequestSyntax) **   <a name="appconfig-StopDeployment-request-uri-ApplicationId"></a>
The ID or name of the application.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

 ** [DeploymentNumber](#API_StopDeployment_RequestSyntax) **   <a name="appconfig-StopDeployment-request-uri-DeploymentNumber"></a>
The sequence number of the deployment.
Required: Yes

 ** [EnvironmentId](#API_StopDeployment_RequestSyntax) **   <a name="appconfig-StopDeployment-request-uri-EnvironmentId"></a>
The ID or name of the environment.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: Yes

## Request Body
<a name="API_StopDeployment_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_StopDeployment_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "ApplicationId": "string",
   "AppliedExtensions": [
      {
         "ExtensionAssociationId": "string",
         "ExtensionId": "string",
         "Parameters": {
            "string" : "string"
         },
         "VersionNumber": number
      }
   ],
   "CompletedAt": "string",
   "ConfigurationLocationUri": "string",
   "ConfigurationName": "string",
   "ConfigurationProfileId": "string",
   "ConfigurationVersion": "string",
   "DeploymentDurationInMinutes": number,
   "DeploymentNumber": number,
   "DeploymentStrategyId": "string",
   "Description": "string",
   "EnvironmentId": "string",
   "EventLog": [
      {
         "ActionInvocations": [
            {
               "ActionName": "string",
               "ErrorCode": "string",
               "ErrorMessage": "string",
               "ExtensionIdentifier": "string",
               "InvocationId": "string",
               "RoleArn": "string",
               "Uri": "string"
            }
         ],
         "Description": "string",
         "EventType": "string",
         "OccurredAt": "string",
         "TriggeredBy": "string"
      }
   ],
   "FinalBakeTimeInMinutes": number,
   "GrowthFactor": number,
   "GrowthType": "string",
   "KmsKeyArn": "string",
   "KmsKeyIdentifier": "string",
   "PercentageComplete": number,
   "StartedAt": "string",
   "State": "string",
   "VersionLabel": "string"
}
```

## Response Elements
<a name="API_StopDeployment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [ApplicationId](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-ApplicationId"></a>
The ID of the application that was deployed.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [AppliedExtensions](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-AppliedExtensions"></a>
A list of extensions that were processed as part of the deployment. The extensions that were previously associated to the configuration profile, environment, or the application when `StartDeployment` was called.
Type: Array of [AppliedExtension](API_AppliedExtension.md) objects

 ** [CompletedAt](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-CompletedAt"></a>
The time the deployment completed.
Type: Timestamp

 ** [ConfigurationLocationUri](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-ConfigurationLocationUri"></a>
Information about the source location of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [ConfigurationName](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-ConfigurationName"></a>
The name of the configuration.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [ConfigurationProfileId](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-ConfigurationProfileId"></a>
The ID of the configuration profile that was deployed.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [ConfigurationVersion](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-ConfigurationVersion"></a>
The configuration version that was deployed.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [DeploymentDurationInMinutes](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-DeploymentDurationInMinutes"></a>
Total amount of time the deployment lasted.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.

 ** [DeploymentNumber](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-DeploymentNumber"></a>
The sequence number of the deployment.
Type: Integer

 ** [DeploymentStrategyId](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-DeploymentStrategyId"></a>
The ID of the deployment strategy that was deployed.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [Description](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-Description"></a>
The description of the deployment.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.

 ** [EnvironmentId](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-EnvironmentId"></a>
The ID of the environment that was deployed.
Type: String
Pattern: `[a-z0-9]{4,7}`

 ** [EventLog](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-EventLog"></a>
A list containing all events related to a deployment. The most recent events are displayed first.
Type: Array of [DeploymentEvent](API_DeploymentEvent.md) objects

 ** [FinalBakeTimeInMinutes](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-FinalBakeTimeInMinutes"></a>
The amount of time that AWS AppConfig monitored for alarms before considering the deployment to be complete and no longer eligible for automatic rollback.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1440.

 ** [GrowthFactor](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-GrowthFactor"></a>
The percentage of targets to receive a deployed configuration during each interval.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.

 ** [GrowthType](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-GrowthType"></a>
The algorithm used to define how percentage grew over time.
Type: String
Valid Values: `LINEAR | EXPONENTIAL`

 ** [KmsKeyArn](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-KmsKeyArn"></a>
The Amazon Resource Name of the AWS Key Management Service key used to encrypt configuration data. You can encrypt secrets stored in AWS Secrets Manager, Amazon Simple Storage Service (Amazon S3) objects encrypted with SSE-KMS, or secure string parameters stored in AWS Systems Manager Parameter Store.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z]+:((eusc-)?[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1})?:(\d{12})?:[a-zA-Z0-9-_/:.]+`

 ** [KmsKeyIdentifier](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-KmsKeyIdentifier"></a>
The AWS Key Management Service key identifier (key ID, key alias, or key ARN) provided when the resource was created or updated.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [PercentageComplete](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-PercentageComplete"></a>
The percentage of targets for which the deployment is available.
Type: Float
Valid Range: Minimum value of 1.0. Maximum value of 100.0.

 ** [StartedAt](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-StartedAt"></a>
The time the deployment started.
Type: Timestamp

 ** [State](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-State"></a>
The state of the deployment.
Type: String
Valid Values: `BAKING | VALIDATING | DEPLOYING | COMPLETE | ROLLING_BACK | ROLLED_BACK | REVERTED`

 ** [VersionLabel](#API_StopDeployment_ResponseSyntax) **   <a name="appconfig-StopDeployment-response-VersionLabel"></a>
A user-defined label for an AWS AppConfig hosted configuration version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `.*[^0-9].*`

## Errors
<a name="API_StopDeployment_Errors"></a>

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
<a name="API_StopDeployment_Examples"></a>

### Example
<a name="API_StopDeployment_Example_1"></a>

This example illustrates one usage of StopDeployment.

#### Sample Request
<a name="API_StopDeployment_Example_1_Request"></a>

```
DELETE /applications/abc1234/environments/54j1r29/deployments/2 HTTP/1.1
Host: appconfig.us-east-1.amazonaws.com
Accept-Encoding: identity
User-Agent: aws-cli/2.2.4 Python/3.8.8 Linux/5.4.134-73.228.amzn2int.x86_64 exe/x86_64.amzn.2 prompt/off command/appconfig.stop-deployment
X-Amz-Date: 20210920T210612Z
Authorization: AWS4-HMAC-SHA256 Credential=AKIAIOSFODNN7EXAMPLE/20210920/us-east-1/appconfig/aws4_request, SignedHeaders=host;x-amz-date, Signature=39c3b3042cd2aEXAMPLE
Content-Length: 0
```

#### Sample Response
<a name="API_StopDeployment_Example_1_Response"></a>

```
{
    "DeploymentNumber": 0,
    "DeploymentDurationInMinutes": 0,
    "GrowthFactor": 0.0,
    "FinalBakeTimeInMinutes": 0,
    "PercentageComplete": 0.0
}
```

## See Also
<a name="API_StopDeployment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appconfig-2019-10-09/StopDeployment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appconfig-2019-10-09/StopDeployment)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS AppConfig. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appconfig` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

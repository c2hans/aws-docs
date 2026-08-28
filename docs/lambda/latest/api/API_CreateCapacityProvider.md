---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_CreateCapacityProvider.html
---

# CreateCapacityProvider
<a name="API_CreateCapacityProvider"></a>

Creates a capacity provider that manages compute resources for Lambda functions

## Request Syntax
<a name="API_CreateCapacityProvider_RequestSyntax"></a>

```
POST /2025-11-30/capacity-providers HTTP/1.1
Content-type: application/json

{
   "CapacityProviderName": "{{string}}",
   "CapacityProviderScalingConfig": {
      "MaxVCpuCount": {{number}},
      "ScalingMode": "{{string}}",
      "ScalingPolicies": [
         {
            "PredefinedMetricType": "{{string}}",
            "TargetValue": {{number}}
         }
      ]
   },
   "InstanceRequirements": {
      "AllowedInstanceTypes": [ "{{string}}" ],
      "Architectures": [ "{{string}}" ],
      "ExcludedInstanceTypes": [ "{{string}}" ]
   },
   "KmsKeyArn": "{{string}}",
   "PermissionsConfig": {
      "CapacityProviderOperatorRoleArn": "{{string}}"
   },
   "PropagateTags": {
      "ExplicitTags": {
         "{{string}}" : "{{string}}"
      },
      "Mode": "{{string}}"
   },
   "Tags": {
      "{{string}}" : "{{string}}"
   },
   "TelemetryConfig": {
      "LoggingConfig": {
         "LogGroup": "{{string}}",
         "SystemLogLevel": "{{string}}"
      }
   },
   "VpcConfig": {
      "SecurityGroupIds": [ "{{string}}" ],
      "SubnetIds": [ "{{string}}" ]
   }
}
```

## URI Request Parameters
<a name="API_CreateCapacityProvider_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateCapacityProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CapacityProviderName](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-CapacityProviderName"></a>
The name of the capacity provider.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

 ** [CapacityProviderScalingConfig](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-CapacityProviderScalingConfig"></a>
The scaling configuration that defines how the capacity provider scales compute instances, including maximum vCPU count and scaling policies.
Type: [CapacityProviderScalingConfig](API_CapacityProviderScalingConfig.md) object
Required: No

 ** [InstanceRequirements](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-InstanceRequirements"></a>
The instance requirements that specify the compute instance characteristics, including architectures and allowed or excluded instance types.
Type: [InstanceRequirements](API_InstanceRequirements.md) object
Required: No

 ** [KmsKeyArn](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-KmsKeyArn"></a>
The ARN of the KMS key used to encrypt data associated with the capacity provider.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10000.
Pattern: `arn:(aws[a-zA-Z-]*)?:[a-z0-9-.]+:.*`
Required: No

 ** [PermissionsConfig](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-PermissionsConfig"></a>
The permissions configuration that specifies the IAM role ARN used by the capacity provider to manage compute resources.
Type: [CapacityProviderPermissionsConfig](API_CapacityProviderPermissionsConfig.md) object
Required: Yes

 ** [PropagateTags](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-PropagateTags"></a>
The tag propagation configuration for the capacity provider. Specifies tags to apply to managed resources at launch.
Type: [PropagateTags](API_PropagateTags.md) object
Required: No

 ** [Tags](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-Tags"></a>
A list of tags to associate with the capacity provider.
Type: String to string map
Required: No

 ** [TelemetryConfig](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-TelemetryConfig"></a>
The telemetry configuration for the capacity provider. Specifies logging settings for managed resources.
Type: [CapacityProviderTelemetryConfig](API_CapacityProviderTelemetryConfig.md) object
Required: No

 ** [VpcConfig](#API_CreateCapacityProvider_RequestSyntax) **   <a name="lambda-CreateCapacityProvider-request-VpcConfig"></a>
The VPC configuration for the capacity provider, including subnet IDs and security group IDs where compute instances will be launched.
Type: [CapacityProviderVpcConfig](API_CapacityProviderVpcConfig.md) object
Required: Yes

## Response Syntax
<a name="API_CreateCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "CapacityProvider": {
      "CapacityProviderArn": "string",
      "CapacityProviderScalingConfig": {
         "MaxVCpuCount": number,
         "ScalingMode": "string",
         "ScalingPolicies": [
            {
               "PredefinedMetricType": "string",
               "TargetValue": number
            }
         ]
      },
      "InstanceRequirements": {
         "AllowedInstanceTypes": [ "string" ],
         "Architectures": [ "string" ],
         "ExcludedInstanceTypes": [ "string" ]
      },
      "KmsKeyArn": "string",
      "LastModified": "string",
      "PermissionsConfig": {
         "CapacityProviderOperatorRoleArn": "string"
      },
      "PropagateTags": {
         "ExplicitTags": {
            "string" : "string"
         },
         "Mode": "string"
      },
      "State": "string",
      "TelemetryConfig": {
         "LoggingConfig": {
            "LogGroup": "string",
            "SystemLogLevel": "string"
         }
      },
      "VpcConfig": {
         "SecurityGroupIds": [ "string" ],
         "SubnetIds": [ "string" ]
      }
   }
}
```

## Response Elements
<a name="API_CreateCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [CapacityProvider](#API_CreateCapacityProvider_ResponseSyntax) **   <a name="lambda-CreateCapacityProvider-response-CapacityProvider"></a>
Information about the capacity provider that was created.
Type: [CapacityProvider](API_CapacityProvider.md) object

## Errors
<a name="API_CreateCapacityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** CapacityProviderLimitExceededException **
The maximum number of capacity providers for your account has been exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html)
 ** Type **
The exception type.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ResourceConflictException **
The resource already exists, or another operation is in progress.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 409

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_CreateCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/CreateCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/CreateCapacityProvider)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Lambda. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lambda` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

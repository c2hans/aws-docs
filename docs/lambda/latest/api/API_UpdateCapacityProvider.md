---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_UpdateCapacityProvider.html
---

# UpdateCapacityProvider
<a name="API_UpdateCapacityProvider"></a>

Updates the configuration of an existing capacity provider.

## Request Syntax
<a name="API_UpdateCapacityProvider_RequestSyntax"></a>

```
PUT /2025-11-30/capacity-providers/{{CapacityProviderName}} HTTP/1.1
Content-type: application/json

{
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
   "PropagateTags": {
      "ExplicitTags": {
         "{{string}}" : "{{string}}"
      },
      "Mode": "{{string}}"
   },
   "TelemetryConfig": {
      "LoggingConfig": {
         "LogGroup": "{{string}}",
         "SystemLogLevel": "{{string}}"
      }
   }
}
```

## URI Request Parameters
<a name="API_UpdateCapacityProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityProviderName](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="lambda-UpdateCapacityProvider-request-uri-CapacityProviderName"></a>
The name of the capacity provider to update.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_UpdateCapacityProvider_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [CapacityProviderScalingConfig](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="lambda-UpdateCapacityProvider-request-CapacityProviderScalingConfig"></a>
The updated scaling configuration for the capacity provider.
Type: [CapacityProviderScalingConfig](API_CapacityProviderScalingConfig.md) object
Required: No

 ** [PropagateTags](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="lambda-UpdateCapacityProvider-request-PropagateTags"></a>
Configuration for tag propagation to managed resources launched by the capacity provider.
Type: [PropagateTags](API_PropagateTags.md) object
Required: No

 ** [TelemetryConfig](#API_UpdateCapacityProvider_RequestSyntax) **   <a name="lambda-UpdateCapacityProvider-request-TelemetryConfig"></a>
The updated telemetry configuration for the capacity provider.
Type: [CapacityProviderTelemetryConfig](API_CapacityProviderTelemetryConfig.md) object
Required: No

## Response Syntax
<a name="API_UpdateCapacityProvider_ResponseSyntax"></a>

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
<a name="API_UpdateCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [CapacityProvider](#API_UpdateCapacityProvider_ResponseSyntax) **   <a name="lambda-UpdateCapacityProvider-response-CapacityProvider"></a>
Information about the updated capacity provider.
Type: [CapacityProvider](API_CapacityProvider.md) object

## Errors
<a name="API_UpdateCapacityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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

 ** ResourceNotFoundException **
The resource specified in the request does not exist.
HTTP Status Code: 404

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_UpdateCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/UpdateCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/UpdateCapacityProvider)

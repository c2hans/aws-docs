---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_GetCapacityProvider.html
---

# GetCapacityProvider
<a name="API_GetCapacityProvider"></a>

Retrieves information about a specific capacity provider, including its configuration, state, and associated resources.

## Request Syntax
<a name="API_GetCapacityProvider_RequestSyntax"></a>

```
GET /2025-11-30/capacity-providers/{{CapacityProviderName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCapacityProvider_RequestParameters"></a>

The request uses the following URI parameters.

 ** [CapacityProviderName](#API_GetCapacityProvider_RequestSyntax) **   <a name="lambda-GetCapacityProvider-request-uri-CapacityProviderName"></a>
The name of the capacity provider to retrieve.
Length Constraints: Minimum length of 1. Maximum length of 140.
Pattern: `(arn:aws[a-zA-Z-]*:lambda:[a-z]{2}((-gov)|(-iso([a-z]?)))?-[a-z]+-\d{1}:\d{12}:capacity-provider:[a-zA-Z0-9-_]+)|[a-zA-Z0-9-_]+`
Required: Yes

## Request Body
<a name="API_GetCapacityProvider_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCapacityProvider_ResponseSyntax"></a>

```
HTTP/1.1 200
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
<a name="API_GetCapacityProvider_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityProvider](#API_GetCapacityProvider_ResponseSyntax) **   <a name="lambda-GetCapacityProvider-response-CapacityProvider"></a>
Information about the capacity provider, including its configuration and current state.
Type: [CapacityProvider](API_CapacityProvider.md) object

## Errors
<a name="API_GetCapacityProvider_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

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
<a name="API_GetCapacityProvider_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/GetCapacityProvider)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/GetCapacityProvider)

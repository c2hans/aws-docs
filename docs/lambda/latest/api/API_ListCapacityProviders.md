---
source_url: https://docs.aws.amazon.com/lambda/latest/api/API_ListCapacityProviders.html
---

# ListCapacityProviders
<a name="API_ListCapacityProviders"></a>

Returns a list of capacity providers in your account.

## Request Syntax
<a name="API_ListCapacityProviders_RequestSyntax"></a>

```
GET /2025-11-30/capacity-providers?Marker={{Marker}}&MaxItems={{MaxItems}}&State={{State}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListCapacityProviders_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Marker](#API_ListCapacityProviders_RequestSyntax) **   <a name="lambda-ListCapacityProviders-request-uri-Marker"></a>
Specify the pagination token that's returned by a previous request to retrieve the next page of results.

 ** [MaxItems](#API_ListCapacityProviders_RequestSyntax) **   <a name="lambda-ListCapacityProviders-request-uri-MaxItems"></a>
The maximum number of capacity providers to return.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [State](#API_ListCapacityProviders_RequestSyntax) **   <a name="lambda-ListCapacityProviders-request-uri-State"></a>
Filter capacity providers by their current state.
Valid Values: `Pending | Active | Failed | Deleting`

## Request Body
<a name="API_ListCapacityProviders_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListCapacityProviders_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "CapacityProviders": [
      {
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
   ],
   "NextMarker": "string"
}
```

## Response Elements
<a name="API_ListCapacityProviders_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [CapacityProviders](#API_ListCapacityProviders_ResponseSyntax) **   <a name="lambda-ListCapacityProviders-response-CapacityProviders"></a>
A list of capacity providers in your account.
Type: Array of [CapacityProvider](API_CapacityProvider.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.

 ** [NextMarker](#API_ListCapacityProviders_ResponseSyntax) **   <a name="lambda-ListCapacityProviders-response-NextMarker"></a>
The pagination token that's included if more results are available.
Type: String

## Errors
<a name="API_ListCapacityProviders_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterValueException **
One of the parameters in the request is not valid.
 ** message **
The exception message.
 ** Type **
The exception type.
HTTP Status Code: 400

 ** ServiceException **
The AWS Lambda service encountered an internal error.
HTTP Status Code: 500

 ** TooManyRequestsException **
The request throughput limit was exceeded. For more information, see [Lambda quotas](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#api-requests).
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
HTTP Status Code: 429

## See Also
<a name="API_ListCapacityProviders_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/lambda-2015-03-31/ListCapacityProviders)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/lambda-2015-03-31/ListCapacityProviders)

---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteFleetMetric.html
---

# DeleteFleetMetric
<a name="API_DeleteFleetMetric"></a>

Deletes the specified fleet metric. Returns successfully with no error if the deletion is successful or you specify a fleet metric that doesn't exist.

Requires permission to access the [DeleteFleetMetric](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteFleetMetric_RequestSyntax"></a>

```
DELETE /fleet-metric/{{metricName}}?expectedVersion={{expectedVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteFleetMetric_RequestParameters"></a>

The request uses the following URI parameters.

 ** [expectedVersion](#API_DeleteFleetMetric_RequestSyntax) **   <a name="iot-DeleteFleetMetric-request-uri-expectedVersion"></a>
The expected version of the fleet metric to delete.

 ** [metricName](#API_DeleteFleetMetric_RequestSyntax) **   <a name="iot-DeleteFleetMetric-request-uri-metricName"></a>
The name of the fleet metric to delete.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_\-\.]+`
Required: Yes

## Request Body
<a name="API_DeleteFleetMetric_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteFleetMetric_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteFleetMetric_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteFleetMetric_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service is temporarily unavailable.
 ** message **
The message for the exception.
HTTP Status Code: 503

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

 ** VersionConflictException **
An exception thrown when the version of an entity specified with the `expectedVersion` parameter does not match the latest version in the system.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_DeleteFleetMetric_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteFleetMetric)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteFleetMetric)

---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_GetResourceDashboard.html
---

# GetResourceDashboard
<a name="API_GetResourceDashboard"></a>

Returns a URL that you can use to access the application UIs for a specified resource, such as a session.

For resources in a running state, the application UI is a live user interface such as the Spark web UI. For terminated resources, the application UI is a persistent application user interface such as the Spark History Server.

**Note**
The URL is valid for one hour after you generate it. To access the application UI after that hour elapses, you must invoke the API again to generate a new URL.

## Request Syntax
<a name="API_GetResourceDashboard_RequestSyntax"></a>

```
GET /applications/{{applicationId}}/dashboard?resourceId={{resourceId}}&resourceType={{resourceType}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetResourceDashboard_RequestParameters"></a>

The request uses the following URI parameters.

 ** [applicationId](#API_GetResourceDashboard_RequestSyntax) **   <a name="emrserverless-GetResourceDashboard-request-uri-applicationId"></a>
The ID of the application that the resource belongs to.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [resourceId](#API_GetResourceDashboard_RequestSyntax) **   <a name="emrserverless-GetResourceDashboard-request-uri-resourceId"></a>
The ID of the resource.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[0-9a-z]+`
Required: Yes

 ** [resourceType](#API_GetResourceDashboard_RequestSyntax) **   <a name="emrserverless-GetResourceDashboard-request-uri-resourceType"></a>
The type of resource to access the dashboard for. Currently, only `Session` is supported.
Valid Values: `SESSION`
Required: Yes

## Request Body
<a name="API_GetResourceDashboard_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetResourceDashboard_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "url": "string"
}
```

## Response Elements
<a name="API_GetResourceDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [url](#API_GetResourceDashboard_ResponseSyntax) **   <a name="emrserverless-GetResourceDashboard-response-url"></a>
A URL to the resource dashboard. For an active resource, this URL opens the live application UI. For a terminated resource, this URL opens the persistent application UI. This value is not included in the response if the URL is not available.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_GetResourceDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Request processing failed because of an error or failure with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource was not found.
HTTP Status Code: 404

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_GetResourceDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/emr-serverless-2021-07-13/GetResourceDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/GetResourceDashboard)

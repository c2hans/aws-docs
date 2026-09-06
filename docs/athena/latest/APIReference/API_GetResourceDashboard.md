---
source_url: https://docs.aws.amazon.com/athena/latest/APIReference/API_GetResourceDashboard.html
---

# GetResourceDashboard
<a name="API_GetResourceDashboard"></a>

Gets the Live UI/Persistence UI for a session.

## Request Syntax
<a name="API_GetResourceDashboard_RequestSyntax"></a>

```
{
   "ResourceARN": "{{string}}"
}
```

## Request Parameters
<a name="API_GetResourceDashboard_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ResourceARN](#API_GetResourceDashboard_RequestSyntax) **   <a name="athena-GetResourceDashboard-request-ResourceARN"></a>
The The Amazon Resource Name (ARN) for a session.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Required: Yes

## Response Syntax
<a name="API_GetResourceDashboard_ResponseSyntax"></a>

```
{
   "Url": "string"
}
```

## Response Elements
<a name="API_GetResourceDashboard_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Url](#API_GetResourceDashboard_ResponseSyntax) **   <a name="athena-GetResourceDashboard-response-Url"></a>
The Live UI/Persistence UI url for a session.
Type: String

## Errors
<a name="API_GetResourceDashboard_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
Indicates a platform issue, which may be due to a transient condition or outage.
HTTP Status Code: 500

 ** InvalidRequestException **
Indicates that something is wrong with the input to the request. For example, a required parameter may be missing or out of range.
 ** AthenaErrorCode **
The error code returned when the query execution failed to process, or when the processing request for the named query failed.
HTTP Status Code: 400

 ** ResourceNotFoundException **
A resource, such as a workgroup, was not found.
 ** ResourceName **
The name of the Amazon resource.
HTTP Status Code: 400

## See Also
<a name="API_GetResourceDashboard_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetResourceDashboard)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/athena-2017-05-18/GetResourceDashboard)

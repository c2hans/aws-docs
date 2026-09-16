---
source_url: https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_CreateApplicationPresignedUrl.html
---

# CreateApplicationPresignedUrl
<a name="API_CreateApplicationPresignedUrl"></a>

Creates and returns a URL that you can use to connect to an application's extension.

The IAM role or user used to call this API defines the permissions to access the extension. After the presigned URL is created, no additional permission is required to access this URL. IAM authorization policies for this API are also enforced for every HTTP request that attempts to connect to the extension.

You control the amount of time that the URL will be valid using the `SessionExpirationDurationInSeconds` parameter. If you do not provide this parameter, the returned URL is valid for twelve hours.

**Note**
The URL that you get from a call to CreateApplicationPresignedUrl must be used within 3 minutes to be valid. If you first try to use the URL after the 3-minute limit expires, the service returns an HTTP 403 Forbidden error.

## Request Syntax
<a name="API_CreateApplicationPresignedUrl_RequestSyntax"></a>

```
{
   "ApplicationName": "{{string}}",
   "SessionExpirationDurationInSeconds": {{number}},
   "UrlType": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateApplicationPresignedUrl_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ApplicationName](#API_CreateApplicationPresignedUrl_RequestSyntax) **   <a name="APIReference-CreateApplicationPresignedUrl-request-ApplicationName"></a>
The name of the application.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.-]+`
Required: Yes

 ** [SessionExpirationDurationInSeconds](#API_CreateApplicationPresignedUrl_RequestSyntax) **   <a name="APIReference-CreateApplicationPresignedUrl-request-SessionExpirationDurationInSeconds"></a>
The duration in seconds for which the returned URL will be valid.
Type: Long
Valid Range: Minimum value of 1800. Maximum value of 43200.
Required: No

 ** [UrlType](#API_CreateApplicationPresignedUrl_RequestSyntax) **   <a name="APIReference-CreateApplicationPresignedUrl-request-UrlType"></a>
The type of the extension for which to create and return a URL. Currently, the only valid extension URL type is `FLINK_DASHBOARD_URL`.
Type: String
Valid Values: `FLINK_DASHBOARD_URL | ZEPPELIN_UI_URL`
Required: Yes

## Response Syntax
<a name="API_CreateApplicationPresignedUrl_ResponseSyntax"></a>

```
{
   "AuthorizedUrl": "string"
}
```

## Response Elements
<a name="API_CreateApplicationPresignedUrl_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthorizedUrl](#API_CreateApplicationPresignedUrl_ResponseSyntax) **   <a name="APIReference-CreateApplicationPresignedUrl-response-AuthorizedUrl"></a>
The URL of the extension.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_CreateApplicationPresignedUrl_Errors"></a>

 ** InvalidArgumentException **
The specified input parameter value is not valid.
HTTP Status Code: 400

 ** ResourceInUseException **
The application is not available for this operation.
HTTP Status Code: 400

 ** ResourceNotFoundException **
Specified application can't be found.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplicationPresignedUrl_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/kinesisanalyticsv2-2018-05-23/CreateApplicationPresignedUrl)

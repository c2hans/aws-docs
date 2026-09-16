---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateImageBuilderStreamingURL.html
---

# CreateImageBuilderStreamingURL
<a name="API_CreateImageBuilderStreamingURL"></a>

Creates a URL to start an image builder streaming session.

## Request Syntax
<a name="API_CreateImageBuilderStreamingURL_RequestSyntax"></a>

```
{
   "Name": "{{string}}",
   "Validity": {{number}}
}
```

## Request Parameters
<a name="API_CreateImageBuilderStreamingURL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Name](#API_CreateImageBuilderStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilderStreamingURL-request-Name"></a>
The name of the image builder.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [Validity](#API_CreateImageBuilderStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilderStreamingURL-request-Validity"></a>
The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.
Type: Long
Required: No

## Response Syntax
<a name="API_CreateImageBuilderStreamingURL_ResponseSyntax"></a>

```
{
   "Expires": number,
   "StreamingURL": "string"
}
```

## Response Elements
<a name="API_CreateImageBuilderStreamingURL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Expires](#API_CreateImageBuilderStreamingURL_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilderStreamingURL-response-Expires"></a>
The elapsed time, in seconds after the Unix epoch, when this URL expires.
Type: Timestamp

 ** [StreamingURL](#API_CreateImageBuilderStreamingURL_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateImageBuilderStreamingURL-response-StreamingURL"></a>
The URL to start the WorkSpaces Applications streaming session.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateImageBuilderStreamingURL_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OperationNotPermittedException **
The attempted operation is not permitted.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The error message in the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateImageBuilderStreamingURL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateImageBuilderStreamingURL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateImageBuilderStreamingURL)

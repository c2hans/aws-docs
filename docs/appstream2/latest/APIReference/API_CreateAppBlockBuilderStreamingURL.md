---
source_url: https://docs.aws.amazon.com/appstream2/latest/APIReference/API_CreateAppBlockBuilderStreamingURL.html
---

# CreateAppBlockBuilderStreamingURL
<a name="API_CreateAppBlockBuilderStreamingURL"></a>

Creates a URL to start a create app block builder streaming session.

## Request Syntax
<a name="API_CreateAppBlockBuilderStreamingURL_RequestSyntax"></a>

```
{
   "AppBlockBuilderName": "{{string}}",
   "Validity": {{number}}
}
```

## Request Parameters
<a name="API_CreateAppBlockBuilderStreamingURL_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AppBlockBuilderName](#API_CreateAppBlockBuilderStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilderStreamingURL-request-AppBlockBuilderName"></a>
The name of the app block builder.
Type: String
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9_.-]{0,100}$`
Required: Yes

 ** [Validity](#API_CreateAppBlockBuilderStreamingURL_RequestSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilderStreamingURL-request-Validity"></a>
The time that the streaming URL will be valid, in seconds. Specify a value between 1 and 604800 seconds. The default is 3600 seconds.
Type: Long
Required: No

## Response Syntax
<a name="API_CreateAppBlockBuilderStreamingURL_ResponseSyntax"></a>

```
{
   "Expires": number,
   "StreamingURL": "string"
}
```

## Response Elements
<a name="API_CreateAppBlockBuilderStreamingURL_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Expires](#API_CreateAppBlockBuilderStreamingURL_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilderStreamingURL-response-Expires"></a>
The elapsed time, in seconds after the Unix epoch, when this URL expires.
Type: Timestamp

 ** [StreamingURL](#API_CreateAppBlockBuilderStreamingURL_ResponseSyntax) **   <a name="WorkSpacesApplications-CreateAppBlockBuilderStreamingURL-response-StreamingURL"></a>
The URL to start the streaming session.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_CreateAppBlockBuilderStreamingURL_Errors"></a>

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
<a name="API_CreateAppBlockBuilderStreamingURL_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appstream-2016-12-01/CreateAppBlockBuilderStreamingURL)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon WorkSpaces Applications. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstream2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

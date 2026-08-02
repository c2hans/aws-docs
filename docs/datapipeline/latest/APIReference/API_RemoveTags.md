---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_RemoveTags.html
---

# RemoveTags
<a name="API_RemoveTags"></a>

Removes existing tags from the specified pipeline.

## Request Syntax
<a name="API_RemoveTags_RequestSyntax"></a>

```
{
   "pipelineId": "{{string}}",
   "tagKeys": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_RemoveTags_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [pipelineId](#API_RemoveTags_RequestSyntax) **   <a name="DP-RemoveTags-request-pipelineId"></a>
The ID of the pipeline.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\n\t]*`
Required: Yes

 ** [tagKeys](#API_RemoveTags_RequestSyntax) **   <a name="DP-RemoveTags-request-tagKeys"></a>
The keys of the tags to remove.
Type: Array of strings
Required: Yes

## Response Elements
<a name="API_RemoveTags_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_RemoveTags_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceError **
An internal service error occurred.
 ** message **
Description of the error message.
HTTP Status Code: 500

 ** InvalidRequestException **
The request was not valid. Verify that your request was properly formatted, that the signature was generated with the correct credentials, and that you haven't exceeded any of the service limits for your account.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineDeletedException **
The specified pipeline has been deleted.
 ** message **
Description of the error message.
HTTP Status Code: 400

 ** PipelineNotFoundException **
The specified pipeline was not found. Verify that you used the correct user and account identifiers.
 ** message **
Description of the error message.
HTTP Status Code: 400

## See Also
<a name="API_RemoveTags_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datapipeline-2012-10-29/RemoveTags)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/RemoveTags)

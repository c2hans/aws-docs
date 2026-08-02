---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeletePlaybackConfiguration.html
---

# DeletePlaybackConfiguration
<a name="API_DeletePlaybackConfiguration"></a>

Deletes a playback configuration. For information about MediaTailor configurations, see [Working with configurations in AWS Elemental MediaTailor](https://docs.aws.amazon.com/mediatailor/latest/ug/configurations.html).

## Request Syntax
<a name="API_DeletePlaybackConfiguration_RequestSyntax"></a>

```
DELETE /playbackConfiguration/{{Name}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeletePlaybackConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [Name](#API_DeletePlaybackConfiguration_RequestSyntax) **   <a name="mediatailor-DeletePlaybackConfiguration-request-uri-Name"></a>
The name of the playback configuration.
Required: Yes

## Request Body
<a name="API_DeletePlaybackConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeletePlaybackConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeletePlaybackConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeletePlaybackConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeletePlaybackConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DeletePlaybackConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DeletePlaybackConfiguration)

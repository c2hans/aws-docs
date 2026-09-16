---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_DeleteChannelPolicy.html
---

# DeleteChannelPolicy
<a name="API_DeleteChannelPolicy"></a>

The channel policy to delete.

## Request Syntax
<a name="API_DeleteChannelPolicy_RequestSyntax"></a>

```
DELETE /channel/{{ChannelName}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteChannelPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_DeleteChannelPolicy_RequestSyntax) **   <a name="mediatailor-DeleteChannelPolicy-request-uri-ChannelName"></a>
The name of the channel associated with this channel policy.
Required: Yes

## Request Body
<a name="API_DeleteChannelPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteChannelPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteChannelPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteChannelPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_DeleteChannelPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/DeleteChannelPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/DeleteChannelPolicy)

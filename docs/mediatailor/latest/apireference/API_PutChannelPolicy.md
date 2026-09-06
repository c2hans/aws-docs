---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_PutChannelPolicy.html
---

# PutChannelPolicy
<a name="API_PutChannelPolicy"></a>

Creates an IAM policy for the channel. IAM policies are used to control access to your channel.

## Request Syntax
<a name="API_PutChannelPolicy_RequestSyntax"></a>

```
PUT /channel/{{ChannelName}}/policy HTTP/1.1
Content-type: application/json

{
   "Policy": "{{string}}"
}
```

## URI Request Parameters
<a name="API_PutChannelPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_PutChannelPolicy_RequestSyntax) **   <a name="mediatailor-PutChannelPolicy-request-uri-ChannelName"></a>
The channel name associated with this Channel Policy.
Required: Yes

## Request Body
<a name="API_PutChannelPolicy_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutChannelPolicy_RequestSyntax) **   <a name="mediatailor-PutChannelPolicy-request-Policy"></a>
Adds an IAM role that determines the permissions of your channel.
Type: String
Required: Yes

## Response Syntax
<a name="API_PutChannelPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_PutChannelPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_PutChannelPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_PutChannelPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/PutChannelPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/PutChannelPolicy)

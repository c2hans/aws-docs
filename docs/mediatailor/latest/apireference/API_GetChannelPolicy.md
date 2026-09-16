---
source_url: https://docs.aws.amazon.com/mediatailor/latest/apireference/API_GetChannelPolicy.html
---

# GetChannelPolicy
<a name="API_GetChannelPolicy"></a>

Returns the channel's IAM policy. IAM policies are used to control access to your channel.

## Request Syntax
<a name="API_GetChannelPolicy_RequestSyntax"></a>

```
GET /channel/{{ChannelName}}/policy HTTP/1.1
```

## URI Request Parameters
<a name="API_GetChannelPolicy_RequestParameters"></a>

The request uses the following URI parameters.

 ** [ChannelName](#API_GetChannelPolicy_RequestSyntax) **   <a name="mediatailor-GetChannelPolicy-request-uri-ChannelName"></a>
The name of the channel associated with this Channel Policy.
Required: Yes

## Request Body
<a name="API_GetChannelPolicy_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetChannelPolicy_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Policy": "string"
}
```

## Response Elements
<a name="API_GetChannelPolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_GetChannelPolicy_ResponseSyntax) **   <a name="mediatailor-GetChannelPolicy-response-Policy"></a>
The IAM policy for the channel. IAM policies are used to control access to your channel.
Type: String

## Errors
<a name="API_GetChannelPolicy_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_GetChannelPolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/mediatailor-2018-04-23/GetChannelPolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediatailor-2018-04-23/GetChannelPolicy)

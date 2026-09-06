---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_ListTopics.html
---

# ListTopics
<a name="API_ListTopics"></a>

Returns a list of the requester's topics. Each call returns a limited list of topics, up to 100. If there are more topics, a `NextToken` is also returned. Use the `NextToken` parameter in a new `ListTopics` call to get further results.

This action is throttled at 30 transactions per second (TPS).

## Request Parameters
<a name="API_ListTopics_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** NextToken **
Token returned by the previous `ListTopics` request.
Type: String
Required: No

## Response Elements
<a name="API_ListTopics_ResponseElements"></a>

The following elements are returned by the service.

 ** NextToken **
Token to pass along to the next `ListTopics` request. This element is returned if there are additional topics to retrieve.
Type: String

 **Topics.member.N**
A list of topic ARNs.
Type: Array of [Topic](API_Topic.md) objects

## Errors
<a name="API_ListTopics_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

## See Also
<a name="API_ListTopics_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/ListTopics)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/ListTopics)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/ListTopics)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/ListTopics)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/ListTopics)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/ListTopics)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/ListTopics)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/ListTopics)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/ListTopics)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/ListTopics)

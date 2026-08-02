---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

 Removes a tag from the specified flow.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="appflow-UntagResource-request-uri-resourceArn"></a>
 The Amazon Resource Name (ARN) of the flow that you want to untag.
Length Constraints: Maximum length of 512.
Pattern: `arn:aws:.*:.*:[0-9]+:.*`
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="appflow-UntagResource-request-uri-tagKeys"></a>
 The tag keys associated with the tag that you want to remove from your flow.
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Required: Yes

## Request Body
<a name="API_UntagResource_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_UntagResource_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UntagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UntagResource_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
 An internal service error occurred during the processing of your request. Try again later.
HTTP Status Code: 500

 ** ResourceNotFoundException **
 The resource specified in the request (such as the source or destination connector profile) is not found.
HTTP Status Code: 404

 ** ValidationException **
 The request has invalid or missing parameters.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/appflow-2020-08-23/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/appflow-2020-08-23/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/appflow-2020-08-23/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/appflow-2020-08-23/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/appflow-2020-08-23/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/appflow-2020-08-23/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/appflow-2020-08-23/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/UntagResource)

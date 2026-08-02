---
source_url: https://docs.aws.amazon.com/repostprivate/latest/APIReference/API_UntagResource.html
---

# UntagResource
<a name="API_UntagResource"></a>

**Note**
End of support notice: On June 30, 2027, AWS will end support for AWS re:Post Private. After June 30, 2027, you will no longer be able to access the re:Post Private console or re:Post Private resources. For more information, see [AWS re:Post Private end of support](https://docs.aws.amazon.com/repostprivate/latest/userguide/repost-private-end-of-support.html).

Removes the association of the tag with the AWS re:Post Private resource.

## Request Syntax
<a name="API_UntagResource_RequestSyntax"></a>

```
DELETE /tags/{{resourceArn}}?tagKeys={{tagKeys}} HTTP/1.1
```

## URI Request Parameters
<a name="API_UntagResource_RequestParameters"></a>

The request uses the following URI parameters.

 ** [resourceArn](#API_UntagResource_RequestSyntax) **   <a name="repostprivate-UntagResource-request-uri-resourceArn"></a>
The ARN of the resource.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [tagKeys](#API_UntagResource_RequestSyntax) **   <a name="repostprivate-UntagResource-request-uri-tagKeys"></a>
The key values of the tag.
Array Members: Minimum number of 1 item. Maximum number of 50 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `(?!aws:)[a-zA-Z+-=._:/]+`
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

 ** AccessDeniedException **
User does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
 ** retryAfterSeconds **
Advice to clients on when the call can be safely retried.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
 ** quotaCode **
The code to identify the quota.
 ** retryAfterSeconds **
 Advice to clients on when the call can be safely retried.
 ** serviceCode **
The code to identify the service.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
 ** fieldList **
The field that caused the error, if applicable.
 ** reason **
The reason why the request failed validation.
HTTP Status Code: 400

## See Also
<a name="API_UntagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/repostspace-2022-05-13/UntagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/repostspace-2022-05-13/UntagResource)

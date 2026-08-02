---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html
---

# TagResource
<a name="API_TagResource"></a>

Adds or edits tags on an AWS Payment Cryptography key.

**Note**
Tagging or untagging an AWS Payment Cryptography key can allow or deny permission to the key.

Each tag consists of a tag key and a tag value, both of which are case-sensitive strings. The tag value can be an empty (null) string. To add a tag, specify a new tag key and a tag value. To edit a tag, specify an existing tag key and a new tag value. You can also add tags to an AWS Payment Cryptography key when you create it with [CreateKey](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateKey.html).

 **Cross-account use:** This operation supports cross-account use when the key has a resource-based policy that grants access. For more information, see [Resource-based policies](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/security_iam_resource-based-policies.html).

 **Related operations:**
+  [ListTagsForResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListTagsForResource.html)
+  [UntagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UntagResource.html)

## Request Syntax
<a name="API_TagResource_RequestSyntax"></a>

```
{
   "ResourceArn": "{{string}}",
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_TagResource_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [ResourceArn](#API_TagResource_RequestSyntax) **   <a name="paymentcryptography-TagResource-request-ResourceArn"></a>
The `KeyARN` of the key whose tags are being updated.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: Yes

 ** [Tags](#API_TagResource_RequestSyntax) **   <a name="paymentcryptography-TagResource-request-Tags"></a>
One or more tags. Each tag consists of a tag key and a tag value. The tag value can be an empty (null) string. You can't have more than one tag on an AWS Payment Cryptography key with the same tag key. If you specify an existing tag key with a different tag value, AWS Payment Cryptography replaces the current tag value with the new one.
Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
To use this parameter, you must have [TagResource](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_TagResource.html) permission in an IAM policy.
Don't include personal, confidential or sensitive information in this field. This field may be displayed in plaintext in AWS CloudTrail logs and other output.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 200 items.
Required: Yes

## Response Elements
<a name="API_TagResource_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_TagResource_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
HTTP Status Code: 400

 ** ConflictException **
This request can cause an inconsistent state for the resource.
The requested operation conflicts with the current state of the resource. For example, attempting to delete a key that is currently being used, or trying to create a resource that already exists.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception, or failure.
This indicates a server-side error within the AWS Payment Cryptography service. If this error persists, contact support for assistance.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request was denied due to resource not found.
The specified key, alias, or other resource does not exist in your account or region. Verify that the resource identifier is correct and that the resource exists in the expected region.
 ** ResourceId **
The identifier of the resource that was not found.
This field contains the specific resource identifier (such as a key ARN or alias name) that could not be located.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **
This request would cause a service quota to be exceeded.
You have reached the maximum number of keys, aliases, or other resources allowed in your account. Review your current usage and consider deleting unused resources or requesting a quota increase.
HTTP Status Code: 400

 ** ServiceUnavailableException **
The service cannot complete the request.
The AWS Payment Cryptography service is temporarily unavailable. This is typically a temporary condition - retry your request after a brief delay.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
You have exceeded the rate limits for AWS Payment Cryptography API calls. Implement exponential backoff and retry logic in your application to handle throttling gracefully.
HTTP Status Code: 400

 ** ValidationException **
The request was denied due to an invalid request error.
One or more parameters in your request are invalid. Check the parameter values, formats, and constraints specified in the API documentation.
HTTP Status Code: 400

## See Also
<a name="API_TagResource_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/TagResource)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/TagResource)

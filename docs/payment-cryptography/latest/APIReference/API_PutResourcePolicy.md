---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_PutResourcePolicy.html
---

# PutResourcePolicy
<a name="API_PutResourcePolicy"></a>

Attaches or replaces a resource-based policy on an AWS Payment Cryptography key. A resource-based policy can grant cross-account access to your key.

If the policy would grant public access, the request fails with a `PublicPolicyException`.

To remove a resource-based policy from a key, use [DeleteResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteResourcePolicy.html).

 **Cross-account use:** This operation can't be used across different AWS accounts.

 **Related operations:**
+  [GetResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetResourcePolicy.html)
+  [DeleteResourcePolicy](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteResourcePolicy.html)

## Request Syntax
<a name="API_PutResourcePolicy_RequestSyntax"></a>

```
{
   "Policy": "{{string}}",
   "ResourceArn": "{{string}}"
}
```

## Request Parameters
<a name="API_PutResourcePolicy_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [Policy](#API_PutResourcePolicy_RequestSyntax) **   <a name="paymentcryptography-PutResourcePolicy-request-Policy"></a>
The resource-based policy to attach to the key, in JSON format.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`
Required: Yes

 ** [ResourceArn](#API_PutResourcePolicy_RequestSyntax) **   <a name="paymentcryptography-PutResourcePolicy-request-ResourceArn"></a>
The `KeyARN` of the key to attach the resource-based policy to.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: Yes

## Response Syntax
<a name="API_PutResourcePolicy_ResponseSyntax"></a>

```
{
   "Policy": "string",
   "ResourceArn": "string"
}
```

## Response Elements
<a name="API_PutResourcePolicy_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Policy](#API_PutResourcePolicy_ResponseSyntax) **   <a name="paymentcryptography-PutResourcePolicy-response-Policy"></a>
The resource-based policy that was attached to the key.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20480.
Pattern: `[\u0009\u000A\u000D\u0020-\u00FF]+`

 ** [ResourceArn](#API_PutResourcePolicy_ResponseSyntax) **   <a name="paymentcryptography-PutResourcePolicy-response-ResourceArn"></a>
The `KeyARN` of the key that the resource-based policy was attached to.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`

## Errors
<a name="API_PutResourcePolicy_Errors"></a>

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

 ** PublicPolicyException **
The resource-based policy would grant public access to the key.
Modify the policy to restrict access to specific principals and resubmit the request.
HTTP Status Code: 400

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
<a name="API_PutResourcePolicy_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/PutResourcePolicy)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/PutResourcePolicy)

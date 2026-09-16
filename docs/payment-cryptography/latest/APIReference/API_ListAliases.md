---
source_url: https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_ListAliases.html
---

# ListAliases
<a name="API_ListAliases"></a>

Lists the aliases for all keys in the caller's AWS account and AWS Region. You can filter the aliases by `keyARN`. For more information, see [Using aliases](https://docs.aws.amazon.com/payment-cryptography/latest/userguide/keys-managealias.html) in the * AWS Payment Cryptography User Guide*.

This is a paginated operation, which means that each response might contain only a subset of all the aliases. When the response contains only a subset of aliases, it includes a `NextToken` value. Use this value in a subsequent `ListAliases` request to get more aliases. When you receive a response with no NextToken (or an empty or null value), that means there are no more aliases to get.

 **Cross-account use:** This operation can't be used across different AWS accounts.

 **Related operations:**
+  [CreateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_CreateAlias.html)
+  [DeleteAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_DeleteAlias.html)
+  [GetAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_GetAlias.html)
+  [UpdateAlias](https://docs.aws.amazon.com/payment-cryptography/latest/APIReference/API_UpdateAlias.html)

## Request Syntax
<a name="API_ListAliases_RequestSyntax"></a>

```
{
   "KeyArn": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListAliases_RequestParameters"></a>

The request accepts the following data in JSON format.

 ** [KeyArn](#API_ListAliases_RequestSyntax) **   <a name="paymentcryptography-ListAliases-request-KeyArn"></a>
The `keyARN` for which you want to list all aliases.
Type: String
Length Constraints: Minimum length of 70. Maximum length of 150.
Pattern: `arn:aws:payment-cryptography:[a-z]{2}-[a-z]{1,16}-[0-9]+:[0-9]{12}:key/[0-9a-zA-Z]{16,64}`
Required: No

 ** [MaxResults](#API_ListAliases_RequestSyntax) **   <a name="paymentcryptography-ListAliases-request-MaxResults"></a>
Use this parameter to specify the maximum number of items to return. When this value is present, AWS Payment Cryptography does not return more than the specified number of items, but it might return fewer.
This value is optional. If you include a value, it must be between 1 and 100, inclusive. If you do not include a value, it defaults to 50.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListAliases_RequestSyntax) **   <a name="paymentcryptography-ListAliases-request-NextToken"></a>
Use this parameter in a subsequent request after you receive a response with truncated results. Set it to the value of `NextToken` from the truncated response you just received.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.
Required: No

## Response Syntax
<a name="API_ListAliases_ResponseSyntax"></a>

```
{
   "Aliases": [
      {
         "AliasName": "string",
         "KeyArn": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListAliases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Aliases](#API_ListAliases_ResponseSyntax) **   <a name="paymentcryptography-ListAliases-response-Aliases"></a>
The list of aliases. Each alias describes the `KeyArn` contained within.
Type: Array of [Alias](API_Alias.md) objects

 ** [NextToken](#API_ListAliases_ResponseSyntax) **   <a name="paymentcryptography-ListAliases-response-NextToken"></a>
The token for the next set of results, or an empty or null value if there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 8192.

## Errors
<a name="API_ListAliases_Errors"></a>

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
This exception is thrown when the caller lacks the necessary IAM permissions to perform the requested operation. Verify that your IAM policy includes the required permissions for the specific AWS Payment Cryptography action you're attempting.
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
<a name="API_ListAliases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/payment-cryptography-2021-09-14/ListAliases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/payment-cryptography-2021-09-14/ListAliases)

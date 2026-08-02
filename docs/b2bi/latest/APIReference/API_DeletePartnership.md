---
source_url: https://docs.aws.amazon.com/b2bi/latest/APIReference/API_DeletePartnership.html
---

# DeletePartnership
<a name="API_DeletePartnership"></a>

Deletes the specified partnership. A partnership represents the connection between you and your trading partner. It ties together a profile and one or more trading capabilities.

## Request Syntax
<a name="API_DeletePartnership_RequestSyntax"></a>

```
{
   "partnershipId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeletePartnership_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [partnershipId](#API_DeletePartnership_RequestSyntax) **   <a name="b2bi-DeletePartnership-request-partnershipId"></a>
Specifies the unique, system-generated identifier for a partnership.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9_-]+`
Required: Yes

## Response Elements
<a name="API_DeletePartnership_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeletePartnership_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** ConflictException **
A conflict exception is thrown when you attempt to delete a resource (such as a profile or a capability) that is being used by other resources.
HTTP Status Code: 400

 ** InternalServerException **
This exception is thrown when an error occurs in the AWS B2B Data Interchange service.
 ** retryAfterSeconds **
The server attempts to retry a failed command.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Occurs when the requested resource does not exist, or cannot be found. In some cases, the resource exists in a region other than the region specified in the API call.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to throttling: the data speed and rendering may be limited depending on various parameters and conditions.
 ** retryAfterSeconds **
The server attempts to retry a command that was throttled.
HTTP Status Code: 400

 ** ValidationException **
When you use Transformer APIs, `TestConversion`, or `TestParsing`, the service throws a validation exception if a rule is configured incorrectly. For example, a validation exception occurs when:
+ A rule references an element that doesn't exist in the selected transaction set
+ An element length rule specifies a minimum length less than 0
If your custom validation rules are configured correctly but the EDI validation fails due to those rules, this is expected behavior and doesn't result in a `ValidationException`.
For all other API operations, a validation exception occurs when a Trading Partner object can't be validated against a request from another object. This can happen during:
+ Standard EDI validation
+ Custom validation rule evaluation, such as when:
  + Element lengths don't meet specified constraints
  + Code list validations contain invalid codes
  + Required elements are missing based on your element requirement rules
HTTP Status Code: 400

## Examples
<a name="API_DeletePartnership_Examples"></a>

### Example
<a name="API_DeletePartnership_Example_1"></a>

The following example deletes a partnership. If successful, an empty HTTP body,`{}` is returned.

#### Sample Request
<a name="API_DeletePartnership_Example_1_Request"></a>

```
{
   "partnershipId": "ps-5555zzzz4444yyyyy"
}
```

## See Also
<a name="API_DeletePartnership_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/b2bi-2022-06-23/DeletePartnership)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/b2bi-2022-06-23/DeletePartnership)

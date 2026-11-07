---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateGlossaryTerm.html
---

# UpdateGlossaryTerm
<a name="API_UpdateGlossaryTerm"></a>

Updates a glossary term in AWS Glue Data Catalog.

## Request Syntax
<a name="API_UpdateGlossaryTerm_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Identifier": "{{string}}",
   "LongDescription": "{{string}}",
   "Name": "{{string}}",
   "ShortDescription": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGlossaryTerm_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="Glue-UpdateGlossaryTerm-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Identifier](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="Glue-UpdateGlossaryTerm-request-Identifier"></a>
The unique identifier of the glossary term to update.
Type: String
Required: Yes

 ** [LongDescription](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="Glue-UpdateGlossaryTerm-request-LongDescription"></a>
The updated long description of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.
Required: No

 ** [Name](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="Glue-UpdateGlossaryTerm-request-Name"></a>
The updated name of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

 ** [ShortDescription](#API_UpdateGlossaryTerm_RequestSyntax) **   <a name="Glue-UpdateGlossaryTerm-request-ShortDescription"></a>
The updated short description of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_UpdateGlossaryTerm_ResponseSyntax"></a>

```
{
   "GlossaryId": "string",
   "Id": "string",
   "LongDescription": "string",
   "Name": "string",
   "ShortDescription": "string"
}
```

## Response Elements
<a name="API_UpdateGlossaryTerm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlossaryId](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="Glue-UpdateGlossaryTerm-response-GlossaryId"></a>
The unique identifier of the glossary containing this term.
Type: String

 ** [Id](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="Glue-UpdateGlossaryTerm-response-Id"></a>
The unique identifier of the glossary term.
Type: String

 ** [LongDescription](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="Glue-UpdateGlossaryTerm-response-LongDescription"></a>
The long description of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [Name](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="Glue-UpdateGlossaryTerm-response-Name"></a>
The name of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ShortDescription](#API_UpdateGlossaryTerm_ResponseSyntax) **   <a name="Glue-UpdateGlossaryTerm-response-ShortDescription"></a>
The short description of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_UpdateGlossaryTerm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** AlreadyExistsException **
A resource to be created or added already exists.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ConcurrentModificationException **
Two processes are trying to modify a resource simultaneously.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** EntityNotFoundException **
A specified entity does not exist
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** InternalServiceException **
An internal service error occurred.
 ** Message **
A message describing the problem.
HTTP Status Code: 500

 ** InvalidInputException **
The input provided was not valid.
 ** FromFederationSource **
Indicates whether or not the exception relates to a federated source.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_UpdateGlossaryTerm_Examples"></a>

### Example
<a name="API_UpdateGlossaryTerm_Example_1"></a>

The following example updates a glossary term's short description.

```
aws glue update-glossary-term \
    --identifier avugvxvsul6izr \
    --name "Net Revenue" \
    --short-description "Gross revenue minus returns, allowances, and discounts." \
    --long-description "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."

{
    "Id": "avugvxvsul6izr",
    "GlossaryId": "6n5f21s641nbjb",
    "Name": "Net Revenue",
    "ShortDescription": "Gross revenue minus returns, allowances, and discounts.",
    "LongDescription": "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
}
```

## See Also
<a name="API_UpdateGlossaryTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateGlossaryTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateGlossaryTerm)

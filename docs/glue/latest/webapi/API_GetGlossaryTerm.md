---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetGlossaryTerm.html
---

# GetGlossaryTerm
<a name="API_GetGlossaryTerm"></a>

Retrieves a glossary term in AWS Glue Data Catalog by its identifier.

## Request Syntax
<a name="API_GetGlossaryTerm_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetGlossaryTerm_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetGlossaryTerm_RequestSyntax) **   <a name="Glue-GetGlossaryTerm-request-Identifier"></a>
The unique identifier of the glossary term to retrieve.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetGlossaryTerm_ResponseSyntax"></a>

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
<a name="API_GetGlossaryTerm_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GlossaryId](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="Glue-GetGlossaryTerm-response-GlossaryId"></a>
The unique identifier of the glossary containing this term.
Type: String

 ** [Id](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="Glue-GetGlossaryTerm-response-Id"></a>
The unique identifier of the glossary term.
Type: String

 ** [LongDescription](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="Glue-GetGlossaryTerm-response-LongDescription"></a>
The long description of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 4096.

 ** [Name](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="Glue-GetGlossaryTerm-response-Name"></a>
The name of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ShortDescription](#API_GetGlossaryTerm_ResponseSyntax) **   <a name="Glue-GetGlossaryTerm-response-ShortDescription"></a>
The short description of the glossary term.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_GetGlossaryTerm_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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

 ** ThrottlingException **
The throttling threshhold was exceeded.
 ** Message **
A message describing the problem.
HTTP Status Code: 400

## Examples
<a name="API_GetGlossaryTerm_Examples"></a>

### Example
<a name="API_GetGlossaryTerm_Example_1"></a>

The following example retrieves a glossary term by its identifier.

```
aws glue get-glossary-term --identifier avugvxvsul6izr

{
    "Id": "avugvxvsul6izr",
    "GlossaryId": "6n5f21s641nbjb",
    "Name": "Net Revenue",
    "ShortDescription": "Revenue after returns, allowances, and discounts.",
    "LongDescription": "Net revenue is gross revenue minus returns, allowances, and discounts over a reporting period."
}
```

## See Also
<a name="API_GetGlossaryTerm_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetGlossaryTerm)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetGlossaryTerm)

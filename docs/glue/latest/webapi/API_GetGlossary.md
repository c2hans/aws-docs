---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_GetGlossary.html
---

# GetGlossary
<a name="API_GetGlossary"></a>

Retrieves a business glossary in AWS Glue Data Catalog by its identifier.

## Request Syntax
<a name="API_GetGlossary_RequestSyntax"></a>

```
{
   "Identifier": "{{string}}"
}
```

## Request Parameters
<a name="API_GetGlossary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Identifier](#API_GetGlossary_RequestSyntax) **   <a name="Glue-GetGlossary-request-Identifier"></a>
The unique identifier of the glossary to retrieve.
Type: String
Required: Yes

## Response Syntax
<a name="API_GetGlossary_ResponseSyntax"></a>

```
{
   "Description": "string",
   "Id": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_GetGlossary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_GetGlossary_ResponseSyntax) **   <a name="Glue-GetGlossary-response-Description"></a>
The description of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Id](#API_GetGlossary_ResponseSyntax) **   <a name="Glue-GetGlossary-response-Id"></a>
The unique identifier of the glossary.
Type: String

 ** [Name](#API_GetGlossary_ResponseSyntax) **   <a name="Glue-GetGlossary-response-Name"></a>
The name of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_GetGlossary_Errors"></a>

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
<a name="API_GetGlossary_Examples"></a>

### Example
<a name="API_GetGlossary_Example_1"></a>

The following example retrieves a glossary by its identifier.

```
aws glue get-glossary --identifier 6n5f21s641nbjb

{
    "Id": "6n5f21s641nbjb",
    "Name": "Sales Terms",
    "Description": "Glossary of sales-domain business terms"
}
```

## See Also
<a name="API_GetGlossary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/GetGlossary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/GetGlossary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/GetGlossary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/GetGlossary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/GetGlossary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/GetGlossary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/GetGlossary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/GetGlossary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/GetGlossary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/GetGlossary)

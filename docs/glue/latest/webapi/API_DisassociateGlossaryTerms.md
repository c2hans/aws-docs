---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DisassociateGlossaryTerms.html
---

# DisassociateGlossaryTerms
<a name="API_DisassociateGlossaryTerms"></a>

Removes the association of one or more glossary terms from an asset in AWS Glue Data Catalog.

## Request Syntax
<a name="API_DisassociateGlossaryTerms_RequestSyntax"></a>

```
{
   "AssetIdentifier": "{{string}}",
   "ClientToken": "{{string}}",
   "GlossaryTermIdentifiers": [ "{{string}}" ],
   "ItemIdentifier": "{{string}}",
   "IterableFormName": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateGlossaryTerms_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetIdentifier](#API_DisassociateGlossaryTerms_RequestSyntax) **   <a name="Glue-DisassociateGlossaryTerms-request-AssetIdentifier"></a>
The unique identifier of the asset to disassociate glossary terms from.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [ClientToken](#API_DisassociateGlossaryTerms_RequestSyntax) **   <a name="Glue-DisassociateGlossaryTerms-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [GlossaryTermIdentifiers](#API_DisassociateGlossaryTerms_RequestSyntax) **   <a name="Glue-DisassociateGlossaryTerms-request-GlossaryTermIdentifiers"></a>
The list of glossary term identifiers to disassociate from the asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [ItemIdentifier](#API_DisassociateGlossaryTerms_RequestSyntax) **   <a name="Glue-DisassociateGlossaryTerms-request-ItemIdentifier"></a>
The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Required: No

 ** [IterableFormName](#API_DisassociateGlossaryTerms_RequestSyntax) **   <a name="Glue-DisassociateGlossaryTerms-request-IterableFormName"></a>
The name of the iterable form. When specified along with `itemIdentifier`, the glossary terms are disassociated from an item within the iterable form rather than the asset itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`
Required: No

## Response Syntax
<a name="API_DisassociateGlossaryTerms_ResponseSyntax"></a>

```
{
   "AssetIdentifier": "string",
   "GlossaryTerms": [ "string" ],
   "ItemIdentifier": "string",
   "IterableFormName": "string"
}
```

## Response Elements
<a name="API_DisassociateGlossaryTerms_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetIdentifier](#API_DisassociateGlossaryTerms_ResponseSyntax) **   <a name="Glue-DisassociateGlossaryTerms-response-AssetIdentifier"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`

 ** [GlossaryTerms](#API_DisassociateGlossaryTerms_ResponseSyntax) **   <a name="Glue-DisassociateGlossaryTerms-response-GlossaryTerms"></a>
The remaining glossary terms associated with the asset.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.

 ** [ItemIdentifier](#API_DisassociateGlossaryTerms_ResponseSyntax) **   <a name="Glue-DisassociateGlossaryTerms-response-ItemIdentifier"></a>
The identifier of the item within the iterable form, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.

 ** [IterableFormName](#API_DisassociateGlossaryTerms_ResponseSyntax) **   <a name="Glue-DisassociateGlossaryTerms-response-IterableFormName"></a>
The name of the iterable form, if the disassociation targets an item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`

## Errors
<a name="API_DisassociateGlossaryTerms_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to a resource was denied.
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
<a name="API_DisassociateGlossaryTerms_Examples"></a>

### Example
<a name="API_DisassociateGlossaryTerms_Example_1"></a>

The following example removes a glossary term from an asset.

```
aws glue disassociate-glossary-terms \
    --asset-identifier quarterly-sales-2026q1 \
    --glossary-term-identifiers avugvxvsul6izr

{
    "AssetIdentifier": "quarterly-sales-2026q1",
    "GlossaryTerms": []
}
```

## See Also
<a name="API_DisassociateGlossaryTerms_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DisassociateGlossaryTerms)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DisassociateGlossaryTerms)

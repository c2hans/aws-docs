---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateGlossary.html
---

# UpdateGlossary
<a name="API_UpdateGlossary"></a>

Updates a business glossary in AWS Glue Data Catalog.

## Request Syntax
<a name="API_UpdateGlossary_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Identifier": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateGlossary_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateGlossary_RequestSyntax) **   <a name="Glue-UpdateGlossary-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_UpdateGlossary_RequestSyntax) **   <a name="Glue-UpdateGlossary-request-Description"></a>
The updated description of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [Identifier](#API_UpdateGlossary_RequestSyntax) **   <a name="Glue-UpdateGlossary-request-Identifier"></a>
The unique identifier of the glossary to update.
Type: String
Required: Yes

 ** [Name](#API_UpdateGlossary_RequestSyntax) **   <a name="Glue-UpdateGlossary-request-Name"></a>
The updated name of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_UpdateGlossary_ResponseSyntax"></a>

```
{
   "Description": "string",
   "Id": "string",
   "Name": "string"
}
```

## Response Elements
<a name="API_UpdateGlossary_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UpdateGlossary_ResponseSyntax) **   <a name="Glue-UpdateGlossary-response-Description"></a>
The description of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [Id](#API_UpdateGlossary_ResponseSyntax) **   <a name="Glue-UpdateGlossary-response-Id"></a>
The unique identifier of the glossary.
Type: String

 ** [Name](#API_UpdateGlossary_ResponseSyntax) **   <a name="Glue-UpdateGlossary-response-Name"></a>
The name of the glossary.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_UpdateGlossary_Errors"></a>

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
<a name="API_UpdateGlossary_Examples"></a>

### Example
<a name="API_UpdateGlossary_Example_1"></a>

The following example updates a glossary's description.

```
aws glue update-glossary \
    --identifier 6n5f21s641nbjb \
    --name "Sales Terms" \
    --description "Glossary of sales and revenue business terms"

{
    "Id": "6n5f21s641nbjb",
    "Name": "Sales Terms",
    "Description": "Glossary of sales and revenue business terms"
}
```

## See Also
<a name="API_UpdateGlossary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateGlossary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateGlossary)

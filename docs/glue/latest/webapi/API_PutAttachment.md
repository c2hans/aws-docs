---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_PutAttachment.html
---

# PutAttachment
<a name="API_PutAttachment"></a>

Attaches a form to an asset or an iterable form item in AWS Glue Data Catalog. If an attachment with the same name already exists, it is overwritten.

## Request Syntax
<a name="API_PutAttachment_RequestSyntax"></a>

```
{
   "AssetIdentifier": "{{string}}",
   "AttachmentName": "{{string}}",
   "ClientToken": "{{string}}",
   "Content": "{{string}}",
   "FormTypeId": "{{string}}",
   "ItemIdentifier": "{{string}}",
   "IterableFormName": "{{string}}"
}
```

## Request Parameters
<a name="API_PutAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetIdentifier](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-AssetIdentifier"></a>
The unique identifier of the asset to attach the form to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [AttachmentName](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-AttachmentName"></a>
The name of the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*$`
Required: Yes

 ** [ClientToken](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Content](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-Content"></a>
The JSON content of the form, conforming to the schema of the specified form type.
Type: String
Required: Yes

 ** [FormTypeId](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-FormTypeId"></a>
The identifier of the form type for this attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Required: Yes

 ** [ItemIdentifier](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-ItemIdentifier"></a>
The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Required: No

 ** [IterableFormName](#API_PutAttachment_RequestSyntax) **   <a name="Glue-PutAttachment-request-IterableFormName"></a>
The name of the iterable form. When specified along with `itemIdentifier`, the attachment targets an item within the iterable form rather than the asset itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`
Required: No

## Response Syntax
<a name="API_PutAttachment_ResponseSyntax"></a>

```
{
   "AssetIdentifier": "string",
   "AttachmentName": "string",
   "FormTypeId": "string",
   "ItemIdentifier": "string",
   "IterableFormName": "string"
}
```

## Response Elements
<a name="API_PutAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetIdentifier](#API_PutAttachment_ResponseSyntax) **   <a name="Glue-PutAttachment-response-AssetIdentifier"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`

 ** [AttachmentName](#API_PutAttachment_ResponseSyntax) **   <a name="Glue-PutAttachment-response-AttachmentName"></a>
The name of the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*$`

 ** [FormTypeId](#API_PutAttachment_ResponseSyntax) **   <a name="Glue-PutAttachment-response-FormTypeId"></a>
The identifier of the form type for this attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [ItemIdentifier](#API_PutAttachment_ResponseSyntax) **   <a name="Glue-PutAttachment-response-ItemIdentifier"></a>
The identifier of the item within the iterable form, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.

 ** [IterableFormName](#API_PutAttachment_ResponseSyntax) **   <a name="Glue-PutAttachment-response-IterableFormName"></a>
The name of the iterable form, if the attachment targets an item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`

## Errors
<a name="API_PutAttachment_Errors"></a>

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
<a name="API_PutAttachment_Examples"></a>

### Example
<a name="API_PutAttachment_Example_1"></a>

The following example attaches a form to an asset.

```
aws glue put-attachment \
    --asset-identifier quarterly-sales-2026q1 \
    --attachment-name reviewNote \
    --form-type-id DataClassification \
    --content '{"classification":"internal","owner":"analytics-team"}'

{
    "AssetIdentifier": "quarterly-sales-2026q1",
    "AttachmentName": "reviewNote",
    "FormTypeId": "DataClassification"
}
```

## See Also
<a name="API_PutAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/PutAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/PutAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/PutAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/PutAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/PutAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/PutAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/PutAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/PutAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/PutAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/PutAttachment)

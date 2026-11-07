---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_DeleteAttachment.html
---

# DeleteAttachment
<a name="API_DeleteAttachment"></a>

Deletes a form attachment from an asset in AWS Glue Data Catalog.

## Request Syntax
<a name="API_DeleteAttachment_RequestSyntax"></a>

```
{
   "AssetIdentifier": "{{string}}",
   "AttachmentName": "{{string}}",
   "ItemIdentifier": "{{string}}",
   "IterableFormName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteAttachment_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssetIdentifier](#API_DeleteAttachment_RequestSyntax) **   <a name="Glue-DeleteAttachment-request-AssetIdentifier"></a>
The unique identifier of the asset from which to delete the attachment.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [AttachmentName](#API_DeleteAttachment_RequestSyntax) **   <a name="Glue-DeleteAttachment-request-AttachmentName"></a>
The name of the attachment to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*$`
Required: Yes

 ** [ItemIdentifier](#API_DeleteAttachment_RequestSyntax) **   <a name="Glue-DeleteAttachment-request-ItemIdentifier"></a>
The identifier of the item within the iterable form. Required when `iterableFormName` is specified.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Required: No

 ** [IterableFormName](#API_DeleteAttachment_RequestSyntax) **   <a name="Glue-DeleteAttachment-request-IterableFormName"></a>
The name of the iterable form. When specified along with `itemIdentifier`, the attachment is deleted from an item within the iterable form rather than from the asset itself.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`
Required: No

## Response Syntax
<a name="API_DeleteAttachment_ResponseSyntax"></a>

```
{
   "AssetIdentifier": "string",
   "ItemIdentifier": "string",
   "IterableFormName": "string"
}
```

## Response Elements
<a name="API_DeleteAttachment_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssetIdentifier](#API_DeleteAttachment_ResponseSyntax) **   <a name="Glue-DeleteAttachment-response-AssetIdentifier"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`

 ** [ItemIdentifier](#API_DeleteAttachment_ResponseSyntax) **   <a name="Glue-DeleteAttachment-response-ItemIdentifier"></a>
The identifier of the item within the iterable form, if applicable.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.

 ** [IterableFormName](#API_DeleteAttachment_ResponseSyntax) **   <a name="Glue-DeleteAttachment-response-IterableFormName"></a>
The name of the iterable form, if the deletion targets an item.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `^[a-zA-Z][a-zA-Z0-9_]*(::[a-zA-Z][a-zA-Z0-9_]*)?$`

## Errors
<a name="API_DeleteAttachment_Errors"></a>

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
<a name="API_DeleteAttachment_Examples"></a>

### Example
<a name="API_DeleteAttachment_Example_1"></a>

The following example deletes an attachment from an asset.

```
aws glue delete-attachment \
    --asset-identifier quarterly-sales-2026q1 \
    --attachment-name reviewNote

{
    "AssetIdentifier": "quarterly-sales-2026q1"
}
```

## See Also
<a name="API_DeleteAttachment_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/DeleteAttachment)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/DeleteAttachment)

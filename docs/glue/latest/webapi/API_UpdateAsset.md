---
source_url: https://docs.aws.amazon.com/glue/latest/webapi/API_UpdateAsset.html
---

# UpdateAsset
<a name="API_UpdateAsset"></a>

Updates the name and description of an existing asset in AWS Glue Data Catalog. Only the fields that you provide are updated.

## Request Syntax
<a name="API_UpdateAsset_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "Identifier": "{{string}}",
   "Name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateAsset_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_UpdateAsset_RequestSyntax) **   <a name="Glue-UpdateAsset-request-ClientToken"></a>
A unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDC00-\uDBFF\uDFFF\t]*`
Required: No

 ** [Description](#API_UpdateAsset_RequestSyntax) **   <a name="Glue-UpdateAsset-request-Description"></a>
The new description of the asset.
Type: String
Required: No

 ** [Identifier](#API_UpdateAsset_RequestSyntax) **   <a name="Glue-UpdateAsset-request-Identifier"></a>
The unique identifier of the asset to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`
Required: Yes

 ** [Name](#API_UpdateAsset_RequestSyntax) **   <a name="Glue-UpdateAsset-request-Name"></a>
The new name of the asset.
Type: String
Required: No

## Response Syntax
<a name="API_UpdateAsset_ResponseSyntax"></a>

```
{
   "Description": "string",
   "Id": "string",
   "Name": "string",
   "UpdatedAt": number
}
```

## Response Elements
<a name="API_UpdateAsset_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Description](#API_UpdateAsset_ResponseSyntax) **   <a name="Glue-UpdateAsset-response-Description"></a>
The description of the asset.
Type: String

 ** [Id](#API_UpdateAsset_ResponseSyntax) **   <a name="Glue-UpdateAsset-response-Id"></a>
The unique identifier of the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1087.
Pattern: `[a-zA-Z0-9\-\:\/\.\_\*]+`

 ** [Name](#API_UpdateAsset_ResponseSyntax) **   <a name="Glue-UpdateAsset-response-Name"></a>
The name of the asset.
Type: String

 ** [UpdatedAt](#API_UpdateAsset_ResponseSyntax) **   <a name="Glue-UpdateAsset-response-UpdatedAt"></a>
The timestamp at which the asset was last updated.
Type: Timestamp

## Errors
<a name="API_UpdateAsset_Errors"></a>

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
<a name="API_UpdateAsset_Examples"></a>

### Example
<a name="API_UpdateAsset_Example_1"></a>

The following example updates the name and description of an asset.

```
aws glue update-asset \
    --identifier quarterly-sales-2026q1 \
    --name "Quarterly Sales 2026 Q1 (Revised)" \
    --description "Revised aggregated quarterly sales metrics"

{
    "Id": "quarterly-sales-2026q1",
    "Name": "Quarterly Sales 2026 Q1 (Revised)",
    "Description": "Revised aggregated quarterly sales metrics",
    "UpdatedAt": "2026-06-19T22:07:42.000Z"
}
```

## See Also
<a name="API_UpdateAsset_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/glue-2017-03-31/UpdateAsset)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/glue-2017-03-31/UpdateAsset)

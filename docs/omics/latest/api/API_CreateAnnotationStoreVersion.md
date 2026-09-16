---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_CreateAnnotationStoreVersion.html
---

# CreateAnnotationStoreVersion
<a name="API_CreateAnnotationStoreVersion"></a>

 Creates a new version of an annotation store.

## Request Syntax
<a name="API_CreateAnnotationStoreVersion_RequestSyntax"></a>

```
POST /annotationStore/{{name}}/version HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "tags": {
      "{{string}}" : "{{string}}"
   },
   "versionName": "{{string}}",
   "versionOptions": { ... }
}
```

## URI Request Parameters
<a name="API_CreateAnnotationStoreVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_CreateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-CreateAnnotationStoreVersion-request-uri-name"></a>
 The name of an annotation store version from which versions are being created.
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: Yes

## Request Body
<a name="API_CreateAnnotationStoreVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-CreateAnnotationStoreVersion-request-description"></a>
 The description of an annotation store version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [tags](#API_CreateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-CreateAnnotationStoreVersion-request-tags"></a>
 Any tags added to annotation store version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [versionName](#API_CreateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-CreateAnnotationStoreVersion-request-versionName"></a>
 The name given to an annotation store version to distinguish it from other versions.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: Yes

 ** [versionOptions](#API_CreateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-CreateAnnotationStoreVersion-request-versionOptions"></a>
 The options for an annotation store version.
Type: [VersionOptions](API_VersionOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

## Response Syntax
<a name="API_CreateAnnotationStoreVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "storeId": "string",
   "versionName": "string",
   "versionOptions": { ... }
}
```

## Response Elements
<a name="API_CreateAnnotationStoreVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-creationTime"></a>
 The time stamp for the creation of an annotation store version.
Type: Timestamp

 ** [id](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-id"></a>
 A generated ID for the annotation store
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-name"></a>
 The name given to an annotation store version to distinguish it from other versions.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`

 ** [status](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-status"></a>
 The status of a annotation store version.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

 ** [storeId](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-storeId"></a>
 The ID for the annotation store from which new versions are being created.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [versionName](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-versionName"></a>
 The name given to an annotation store version to distinguish it from other versions.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`

 ** [versionOptions](#API_CreateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-CreateAnnotationStoreVersion-response-versionOptions"></a>
 The options for an annotation store version.
Type: [VersionOptions](API_VersionOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

## Errors
<a name="API_CreateAnnotationStoreVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
The request cannot be applied to the target resource in its current state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The request exceeds a service quota.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_CreateAnnotationStoreVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/CreateAnnotationStoreVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/CreateAnnotationStoreVersion)

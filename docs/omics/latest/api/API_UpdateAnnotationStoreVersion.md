---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_UpdateAnnotationStoreVersion.html
---

# UpdateAnnotationStoreVersion
<a name="API_UpdateAnnotationStoreVersion"></a>

 Updates the description of an annotation store version.

## Request Syntax
<a name="API_UpdateAnnotationStoreVersion_RequestSyntax"></a>

```
POST /annotationStore/{{name}}/version/{{versionName}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateAnnotationStoreVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_UpdateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-request-uri-name"></a>
 The name of an annotation store.
Required: Yes

 ** [versionName](#API_UpdateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-request-uri-versionName"></a>
 The name of an annotation store version.
Required: Yes

## Request Body
<a name="API_UpdateAnnotationStoreVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateAnnotationStoreVersion_RequestSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-request-description"></a>
 The description of an annotation store.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

## Response Syntax
<a name="API_UpdateAnnotationStoreVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "storeId": "string",
   "updateTime": "string",
   "versionName": "string"
}
```

## Response Elements
<a name="API_UpdateAnnotationStoreVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-creationTime"></a>
 The time stamp for when an annotation store version was created.
Type: Timestamp

 ** [description](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-description"></a>
 The description of an annotation store version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [id](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-id"></a>
 The annotation store version ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-name"></a>
 The name of an annotation store.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`

 ** [status](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-status"></a>
 The status of an annotation store version.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

 ** [storeId](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-storeId"></a>
 The annotation store ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [updateTime](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-updateTime"></a>
 The time stamp for when an annotation store version was updated.
Type: Timestamp

 ** [versionName](#API_UpdateAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-UpdateAnnotationStoreVersion-response-versionName"></a>
 The name of an annotation store version.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`

## Errors
<a name="API_UpdateAnnotationStoreVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred. Try the request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The target resource was not found in the current Region.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateAnnotationStoreVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/UpdateAnnotationStoreVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/UpdateAnnotationStoreVersion)

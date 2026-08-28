---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_GetAnnotationStoreVersion.html
---

# GetAnnotationStoreVersion
<a name="API_GetAnnotationStoreVersion"></a>

 Retrieves the metadata for an annotation store version.

## Request Syntax
<a name="API_GetAnnotationStoreVersion_RequestSyntax"></a>

```
GET /annotationStore/{{name}}/version/{{versionName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetAnnotationStoreVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [name](#API_GetAnnotationStoreVersion_RequestSyntax) **   <a name="omics-GetAnnotationStoreVersion-request-uri-name"></a>
 The name given to an annotation store version to distinguish it from others.
Required: Yes

 ** [versionName](#API_GetAnnotationStoreVersion_RequestSyntax) **   <a name="omics-GetAnnotationStoreVersion-request-uri-versionName"></a>
 The name given to an annotation store version to distinguish it from others.
Required: Yes

## Request Body
<a name="API_GetAnnotationStoreVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetAnnotationStoreVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationTime": "string",
   "description": "string",
   "id": "string",
   "name": "string",
   "status": "string",
   "statusMessage": "string",
   "storeId": "string",
   "tags": {
      "string" : "string"
   },
   "updateTime": "string",
   "versionArn": "string",
   "versionName": "string",
   "versionOptions": { ... },
   "versionSizeBytes": number
}
```

## Response Elements
<a name="API_GetAnnotationStoreVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationTime](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-creationTime"></a>
 The time stamp for when an annotation store version was created.
Type: Timestamp

 ** [description](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-description"></a>
 The description for an annotation store version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.

 ** [id](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-id"></a>
 The annotation store version ID.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [name](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-name"></a>
 The name of the annotation store.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`

 ** [status](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-status"></a>
 The status of an annotation store version.
Type: String
Valid Values: `CREATING | UPDATING | DELETING | ACTIVE | FAILED`

 ** [statusMessage](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-statusMessage"></a>
 The status of an annotation store version.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1000.

 ** [storeId](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-storeId"></a>
 The store ID for annotation store version.
Type: String
Pattern: `[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`

 ** [tags](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-tags"></a>
 Any tags associated with an annotation store version.
Type: String to string map
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updateTime](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-updateTime"></a>
 The time stamp for when an annotation store version was updated.
Type: Timestamp

 ** [versionArn](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-versionArn"></a>
 The Arn for the annotation store.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:([^: ]*):([^: ]*):([^: ]*):([0-9]{12}):([^: ]*)`

 ** [versionName](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-versionName"></a>
 The name given to an annotation store version to distinguish it from others.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`

 ** [versionOptions](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-versionOptions"></a>
 The options for an annotation store version.
Type: [VersionOptions](API_VersionOptions.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.

 ** [versionSizeBytes](#API_GetAnnotationStoreVersion_ResponseSyntax) **   <a name="omics-GetAnnotationStoreVersion-response-versionSizeBytes"></a>
 The size of the annotation store version in Bytes.
Type: Long

## Errors
<a name="API_GetAnnotationStoreVersion_Errors"></a>

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
<a name="API_GetAnnotationStoreVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/GetAnnotationStoreVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/GetAnnotationStoreVersion)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

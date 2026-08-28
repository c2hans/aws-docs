---
source_url: https://docs.aws.amazon.com/omics/latest/api/API_DeleteAnnotationStoreVersions.html
---

# DeleteAnnotationStoreVersions
<a name="API_DeleteAnnotationStoreVersions"></a>

 Deletes one or multiple versions of an annotation store.

## Request Syntax
<a name="API_DeleteAnnotationStoreVersions_RequestSyntax"></a>

```
POST /annotationStore/{{name}}/versions/delete?force={{force}} HTTP/1.1
Content-type: application/json

{
   "versions": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_DeleteAnnotationStoreVersions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [force](#API_DeleteAnnotationStoreVersions_RequestSyntax) **   <a name="omics-DeleteAnnotationStoreVersions-request-uri-force"></a>
 Forces the deletion of an annotation store version when imports are in-progress..

 ** [name](#API_DeleteAnnotationStoreVersions_RequestSyntax) **   <a name="omics-DeleteAnnotationStoreVersions-request-uri-name"></a>
 The name of the annotation store from which versions are being deleted.
Required: Yes

## Request Body
<a name="API_DeleteAnnotationStoreVersions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [versions](#API_DeleteAnnotationStoreVersions_RequestSyntax) **   <a name="omics-DeleteAnnotationStoreVersions-request-versions"></a>
 The versions of an annotation store to be deleted.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Length Constraints: Minimum length of 3. Maximum length of 255.
Pattern: `([a-z]){1}([a-z0-9_]){2,254}`
Required: Yes

## Response Syntax
<a name="API_DeleteAnnotationStoreVersions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "errors": [
      {
         "message": "string",
         "versionName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DeleteAnnotationStoreVersions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [errors](#API_DeleteAnnotationStoreVersions_ResponseSyntax) **   <a name="omics-DeleteAnnotationStoreVersions-response-errors"></a>
 Any errors that occur when attempting to delete an annotation store version.
Type: Array of [VersionDeleteError](API_VersionDeleteError.md) objects

## Errors
<a name="API_DeleteAnnotationStoreVersions_Errors"></a>

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

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_DeleteAnnotationStoreVersions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/omics-2022-11-28/DeleteAnnotationStoreVersions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/omics-2022-11-28/DeleteAnnotationStoreVersions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthOmics. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query omics` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

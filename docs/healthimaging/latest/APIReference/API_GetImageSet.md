---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_GetImageSet.html
---

# GetImageSet
<a name="API_GetImageSet"></a>

Get image set properties.

## Request Syntax
<a name="API_GetImageSet_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/imageSet/{{imageSetId}}/getImageSet?version={{versionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetImageSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_GetImageSet_RequestSyntax) **   <a name="healthimaging-GetImageSet-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [imageSetId](#API_GetImageSet_RequestSyntax) **   <a name="healthimaging-GetImageSet-request-uri-imageSetId"></a>
The image set identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [versionId](#API_GetImageSet_RequestSyntax) **   <a name="healthimaging-GetImageSet-request-uri-versionId"></a>
The image set version identifier.
Pattern: `\d+`

## Request Body
<a name="API_GetImageSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetImageSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "datastoreId": "string",
   "deletedAt": number,
   "imageSetArn": "string",
   "imageSetId": "string",
   "imageSetState": "string",
   "imageSetWorkflowStatus": "string",
   "isPrimary": boolean,
   "lastAccessedAt": number,
   "message": "string",
   "overrides": {
      "forced": boolean
   },
   "storageTier": "string",
   "updatedAt": number,
   "versionId": "string"
}
```

## Response Elements
<a name="API_GetImageSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-createdAt"></a>
The timestamp when image set properties were created.
Type: Timestamp

 ** [datastoreId](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [deletedAt](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-deletedAt"></a>
The timestamp when the image set properties were deleted.
Type: Timestamp

 ** [imageSetArn](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-imageSetArn"></a>
The Amazon Resource Name (ARN) assigned to the image set.
Type: String
Pattern: `arn:aws((-us-gov)|(-iso)|(-iso-b)|(-cn))?:medical-imaging:[a-z0-9-]+:[0-9]{12}:datastore/[0-9a-z]{32}(/imageset/[0-9a-z]{32})?`

 ** [imageSetId](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-imageSetId"></a>
The image set identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [imageSetState](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-imageSetState"></a>
The image set state.
Type: String
Valid Values: `ACTIVE | LOCKED | DELETED`

 ** [imageSetWorkflowStatus](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-imageSetWorkflowStatus"></a>
The image set workflow status.
Type: String
Valid Values: `CREATED | COPIED | COPYING | COPYING_WITH_READ_ONLY_ACCESS | COPY_FAILED | UPDATING | UPDATING_FOR_STUDY_CONSISTENCY | UPDATED | UPDATE_FAILED | DELETING | DELETED | IMPORTING | IMPORTED | IMPORT_FAILED`

 ** [isPrimary](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-isPrimary"></a>
The flag to determine whether the image set is primary or not.
Type: Boolean

 ** [lastAccessedAt](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-lastAccessedAt"></a>
When the image set was last accessed.
Type: Timestamp

 ** [message](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-message"></a>
The error message thrown if an image set action fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w -:`]+`

 ** [overrides](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-overrides"></a>
This object contains the details of any overrides used while creating a specific image set version. If an image set was copied or updated using the `force` flag, this object will contain the `forced` flag.
Type: [Overrides](API_Overrides.md) object

 ** [storageTier](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-storageTier"></a>
The storage tier of the image set.
Type: String
Valid Values: `FREQUENT_ACCESS | ARCHIVE_INSTANT_ACCESS`

 ** [updatedAt](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-updatedAt"></a>
The timestamp when image set properties were updated.
Type: Timestamp

 ** [versionId](#API_GetImageSet_ResponseSyntax) **   <a name="healthimaging-GetImageSet-response-versionId"></a>
The image set version identifier.
Type: String
Pattern: `\d+`

## Errors
<a name="API_GetImageSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The user does not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
HTTP Status Code: 409

 ** InternalServerException **
An unexpected error occurred during processing of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The request references a resource which does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_GetImageSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/GetImageSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/GetImageSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

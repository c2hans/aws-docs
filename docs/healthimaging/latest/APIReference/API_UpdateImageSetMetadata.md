---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_UpdateImageSetMetadata.html
---

# UpdateImageSetMetadata
<a name="API_UpdateImageSetMetadata"></a>

Update image set metadata attributes.

## Request Syntax
<a name="API_UpdateImageSetMetadata_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/imageSet/{{imageSetId}}/updateImageSetMetadata?force={{force}}&includeStudyImageSets={{includeStudyImageSets}}&latestVersion={{latestVersionId}} HTTP/1.1
Content-type: application/json

{
   "DICOMUpdates": {
      "removableAttributes": {{blob}},
      "updatableAttributes": {{blob}}
   },
   "revertToVersionId": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateImageSetMetadata_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [force](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-uri-force"></a>
Setting this flag will force the `UpdateImageSetMetadata` operation for the following attributes:
+  `Tag.StudyInstanceUID`, `Tag.SeriesInstanceUID`, `Tag.SOPInstanceUID`, and `Tag.StudyID`
+ Adding, removing, or updating private tags for an individual SOP Instance

 ** [imageSetId](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-uri-imageSetId"></a>
The image set identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [includeStudyImageSets](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-uri-includeStudyImageSets"></a>
Flag to apply the metadata updates to all image sets in the same Study as the requested image set ID.

 ** [latestVersionId](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-uri-latestVersionId"></a>
The latest image set version identifier.
Pattern: `\d+`
Required: Yes

## Request Body
<a name="API_UpdateImageSetMetadata_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DICOMUpdates](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-DICOMUpdates"></a>
The object containing `removableAttributes` and `updatableAttributes`.
Type: [DICOMUpdates](API_DICOMUpdates.md) object
Required: No

 ** [revertToVersionId](#API_UpdateImageSetMetadata_RequestSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-request-revertToVersionId"></a>
Specifies the previous image set version ID to revert the current image set back to.
You must provide either `revertToVersionId` or `DICOMUpdates` in your request. A `ValidationException` error is thrown if both parameters are provided at the same time.
Type: String
Pattern: `\d+`
Required: No

## Response Syntax
<a name="API_UpdateImageSetMetadata_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "datastoreId": "string",
   "imageSetId": "string",
   "imageSetState": "string",
   "imageSetWorkflowStatus": "string",
   "latestVersionId": "string",
   "message": "string",
   "updatedAt": number
}
```

## Response Elements
<a name="API_UpdateImageSetMetadata_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-createdAt"></a>
The timestamp when image set metadata was created.
Type: Timestamp

 ** [datastoreId](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [imageSetId](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-imageSetId"></a>
The image set identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [imageSetState](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-imageSetState"></a>
The image set state.
Type: String
Valid Values: `ACTIVE | LOCKED | DELETED`

 ** [imageSetWorkflowStatus](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-imageSetWorkflowStatus"></a>
The image set workflow status.
Type: String
Valid Values: `CREATED | COPIED | COPYING | COPYING_WITH_READ_ONLY_ACCESS | COPY_FAILED | UPDATING | UPDATING_FOR_STUDY_CONSISTENCY | UPDATED | UPDATE_FAILED | DELETING | DELETED | IMPORTING | IMPORTED | IMPORT_FAILED`

 ** [latestVersionId](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-latestVersionId"></a>
The latest image set version identifier.
Type: String
Pattern: `\d+`

 ** [message](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-message"></a>
The error message thrown if an update image set metadata action fails.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Pattern: `[\w -:`]+`

 ** [updatedAt](#API_UpdateImageSetMetadata_ResponseSyntax) **   <a name="healthimaging-UpdateImageSetMetadata-response-updatedAt"></a>
The timestamp when image set metadata was updated.
Type: Timestamp

## Errors
<a name="API_UpdateImageSetMetadata_Errors"></a>

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

 ** ServiceQuotaExceededException **
The request caused a service quota to be exceeded.
HTTP Status Code: 402

 ** ThrottlingException **
The request was denied due to throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the constraints set by the service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateImageSetMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/UpdateImageSetMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/UpdateImageSetMetadata)

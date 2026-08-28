---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_CopyImageSet.html
---

# CopyImageSet
<a name="API_CopyImageSet"></a>

Copy an image set.

## Request Syntax
<a name="API_CopyImageSet_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/imageSet/{{sourceImageSetId}}/copyImageSet?force={{force}}&promoteToPrimary={{promoteToPrimary}} HTTP/1.1
Content-type: application/json

{
   "destinationImageSet": {
      "imageSetId": "{{string}}",
      "latestVersionId": "{{string}}"
   },
   "sourceImageSet": {
      "DICOMCopies": {
         "copiableAttributes": "{{string}}"
      },
      "latestVersionId": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CopyImageSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_CopyImageSet_RequestSyntax) **   <a name="healthimaging-CopyImageSet-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [force](#API_CopyImageSet_RequestSyntax) **   <a name="healthimaging-CopyImageSet-request-uri-force"></a>
Providing this parameter will force completion of the `CopyImageSet` operation, even if there are inconsistent Patient, Study, and/or Series level metadata elements between the `sourceImageSet` and `destinationImageSet`.

 ** [promoteToPrimary](#API_CopyImageSet_RequestSyntax) **   <a name="healthimaging-CopyImageSet-request-uri-promoteToPrimary"></a>
Providing this parameter will configure the `CopyImageSet` operation to promote the given image set to the primary DICOM hierarchy. If successful, a new primary image set ID will be returned as the destination image set.

 ** [sourceImageSetId](#API_CopyImageSet_RequestSyntax) **   <a name="healthimaging-CopyImageSet-request-uri-sourceImageSetId"></a>
The source image set identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

## Request Body
<a name="API_CopyImageSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [destinationImageSet](#API_CopyImageSet_RequestSyntax) **   <a name="healthimaging-CopyImageSet-request-destinationImageSet"></a>
The destination image set.
Type: [CopyDestinationImageSet](API_CopyDestinationImageSet.md) object
Required: No

 ** [sourceImageSet](#API_CopyImageSet_RequestSyntax) **   <a name="healthimaging-CopyImageSet-request-sourceImageSet"></a>
The source image set.
Type: [CopySourceImageSetInformation](API_CopySourceImageSetInformation.md) object
Required: Yes

## Response Syntax
<a name="API_CopyImageSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreId": "string",
   "destinationImageSetProperties": {
      "createdAt": number,
      "imageSetArn": "string",
      "imageSetId": "string",
      "imageSetState": "string",
      "imageSetWorkflowStatus": "string",
      "latestVersionId": "string",
      "updatedAt": number
   },
   "sourceImageSetProperties": {
      "createdAt": number,
      "imageSetArn": "string",
      "imageSetId": "string",
      "imageSetState": "string",
      "imageSetWorkflowStatus": "string",
      "latestVersionId": "string",
      "updatedAt": number
   }
}
```

## Response Elements
<a name="API_CopyImageSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreId](#API_CopyImageSet_ResponseSyntax) **   <a name="healthimaging-CopyImageSet-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [destinationImageSetProperties](#API_CopyImageSet_ResponseSyntax) **   <a name="healthimaging-CopyImageSet-response-destinationImageSetProperties"></a>
The properties of the destination image set.
Type: [CopyDestinationImageSetProperties](API_CopyDestinationImageSetProperties.md) object

 ** [sourceImageSetProperties](#API_CopyImageSet_ResponseSyntax) **   <a name="healthimaging-CopyImageSet-response-sourceImageSetProperties"></a>
The properties of the source image set.
Type: [CopySourceImageSetProperties](API_CopySourceImageSetProperties.md) object

## Errors
<a name="API_CopyImageSet_Errors"></a>

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
<a name="API_CopyImageSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/CopyImageSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/CopyImageSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthImaging. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthimaging` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

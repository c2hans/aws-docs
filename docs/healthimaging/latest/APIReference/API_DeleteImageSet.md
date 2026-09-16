---
source_url: https://docs.aws.amazon.com/healthimaging/latest/APIReference/API_DeleteImageSet.html
---

# DeleteImageSet
<a name="API_DeleteImageSet"></a>

Delete an image set.

## Request Syntax
<a name="API_DeleteImageSet_RequestSyntax"></a>

```
POST /datastore/{{datastoreId}}/imageSet/{{imageSetId}}/deleteImageSet HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteImageSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [datastoreId](#API_DeleteImageSet_RequestSyntax) **   <a name="healthimaging-DeleteImageSet-request-uri-datastoreId"></a>
The data store identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

 ** [imageSetId](#API_DeleteImageSet_RequestSyntax) **   <a name="healthimaging-DeleteImageSet-request-uri-imageSetId"></a>
The image set identifier.
Pattern: `[0-9a-z]{32}`
Required: Yes

## Request Body
<a name="API_DeleteImageSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteImageSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "datastoreId": "string",
   "imageSetId": "string",
   "imageSetState": "string",
   "imageSetWorkflowStatus": "string"
}
```

## Response Elements
<a name="API_DeleteImageSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [datastoreId](#API_DeleteImageSet_ResponseSyntax) **   <a name="healthimaging-DeleteImageSet-response-datastoreId"></a>
The data store identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [imageSetId](#API_DeleteImageSet_ResponseSyntax) **   <a name="healthimaging-DeleteImageSet-response-imageSetId"></a>
The image set identifier.
Type: String
Pattern: `[0-9a-z]{32}`

 ** [imageSetState](#API_DeleteImageSet_ResponseSyntax) **   <a name="healthimaging-DeleteImageSet-response-imageSetState"></a>
The image set state.
Type: String
Valid Values: `ACTIVE | LOCKED | DELETED`

 ** [imageSetWorkflowStatus](#API_DeleteImageSet_ResponseSyntax) **   <a name="healthimaging-DeleteImageSet-response-imageSetWorkflowStatus"></a>
The image set workflow status.
Type: String
Valid Values: `CREATED | COPIED | COPYING | COPYING_WITH_READ_ONLY_ACCESS | COPY_FAILED | UPDATING | UPDATING_FOR_STUDY_CONSISTENCY | UPDATED | UPDATE_FAILED | DELETING | DELETED | IMPORTING | IMPORTED | IMPORT_FAILED`

## Errors
<a name="API_DeleteImageSet_Errors"></a>

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
<a name="API_DeleteImageSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/medical-imaging-2023-07-19/DeleteImageSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/medical-imaging-2023-07-19/DeleteImageSet)

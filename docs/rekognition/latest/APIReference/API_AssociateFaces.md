---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_AssociateFaces.html
---

# AssociateFaces
<a name="API_AssociateFaces"></a>

Associates one or more faces with an existing UserID. Takes an array of `FaceIds`. Each `FaceId` that are present in the `FaceIds` list is associated with the provided UserID. The number of FaceIds that can be used as input in a single request is limited to 100.

Note that the total number of faces that can be associated with a single `UserID` is also limited to 100. Once a `UserID` has 100 faces associated with it, no additional faces can be added. If more API calls are made after the limit is reached, a `ServiceQuotaExceededException` will result.

The `UserMatchThreshold` parameter specifies the minimum user match confidence required for the face to be associated with a UserID that has at least one `FaceID` already associated. This ensures that the `FaceIds` are associated with the right UserID. The value ranges from 0-100 and default value is 75.

If successful, an array of `AssociatedFace` objects containing the associated `FaceIds` is returned. If a given face is already associated with the given `UserID`, it will be ignored and will not be returned in the response. If a given face is already associated to a different `UserID`, isn't found in the collection, doesn’t meet the `UserMatchThreshold`, or there are already 100 faces associated with the `UserID`, it will be returned as part of an array of `UnsuccessfulFaceAssociations.`

The `UserStatus` reflects the status of an operation which updates a UserID representation with a list of given faces. The `UserStatus` can be:
+ ACTIVE - All associations or disassociations of FaceID(s) for a UserID are complete.
+ CREATED - A UserID has been created, but has no FaceID(s) associated with it.
+ UPDATING - A UserID is being updated and there are current associations or disassociations of FaceID(s) taking place.

## Request Syntax
<a name="API_AssociateFaces_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CollectionId": "{{string}}",
   "FaceIds": [ "{{string}}" ],
   "UserId": "{{string}}",
   "UserMatchThreshold": {{number}}
}
```

## Request Parameters
<a name="API_AssociateFaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_AssociateFaces_RequestSyntax) **   <a name="rekognition-AssociateFaces-request-ClientRequestToken"></a>
Idempotent token used to identify the request to `AssociateFaces`. If you use the same token with multiple `AssociateFaces` requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [CollectionId](#API_AssociateFaces_RequestSyntax) **   <a name="rekognition-AssociateFaces-request-CollectionId"></a>
The ID of an existing collection containing the UserID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [FaceIds](#API_AssociateFaces_RequestSyntax) **   <a name="rekognition-AssociateFaces-request-FaceIds"></a>
An array of FaceIDs to associate with the UserID.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [UserId](#API_AssociateFaces_RequestSyntax) **   <a name="rekognition-AssociateFaces-request-UserId"></a>
The ID for the existing UserID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: Yes

 ** [UserMatchThreshold](#API_AssociateFaces_RequestSyntax) **   <a name="rekognition-AssociateFaces-request-UserMatchThreshold"></a>
An optional value specifying the minimum confidence in the UserID match to return. The default value is 75.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_AssociateFaces_ResponseSyntax"></a>

```
{
   "AssociatedFaces": [
      {
         "FaceId": "string"
      }
   ],
   "UnsuccessfulFaceAssociations": [
      {
         "Confidence": number,
         "FaceId": "string",
         "Reasons": [ "string" ],
         "UserId": "string"
      }
   ],
   "UserStatus": "string"
}
```

## Response Elements
<a name="API_AssociateFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AssociatedFaces](#API_AssociateFaces_ResponseSyntax) **   <a name="rekognition-AssociateFaces-response-AssociatedFaces"></a>
An array of AssociatedFace objects containing FaceIDs that have been successfully associated with the UserID. Returned if the AssociateFaces action is successful.
Type: Array of [AssociatedFace](API_AssociatedFace.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [UnsuccessfulFaceAssociations](#API_AssociateFaces_ResponseSyntax) **   <a name="rekognition-AssociateFaces-response-UnsuccessfulFaceAssociations"></a>
An array of UnsuccessfulAssociation objects containing FaceIDs that are not successfully associated along with the reasons. Returned if the AssociateFaces action is successful.
Type: Array of [UnsuccessfulFaceAssociation](API_UnsuccessfulFaceAssociation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

 ** [UserStatus](#API_AssociateFaces_ResponseSyntax) **   <a name="rekognition-AssociateFaces-response-UserStatus"></a>
The status of an update made to a UserID. Reflects if the UserID has been updated for every requested change.
Type: String
Valid Values: `ACTIVE | UPDATING | CREATING | CREATED`

## Errors
<a name="API_AssociateFaces_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** ConflictException **
 A User with the same Id already exists within the collection, or the update or deletion of the User caused an inconsistent state. \*\*
HTTP Status Code: 400

 ** IdempotentParameterMismatchException **
A `ClientRequestToken` input parameter was reused with an operation, but at least one of the other input parameters is different from the previous call to the operation.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidParameterException **
Input parameter violated a constraint. Validate your parameter before calling the API operation again.
HTTP Status Code: 400

 ** ProvisionedThroughputExceededException **
The number of requests exceeded your throughput limit. If you want to increase this limit, contact Amazon Rekognition.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The resource specified in the request cannot be found.
HTTP Status Code: 400

 ** ServiceQuotaExceededException **

The size of the resource exceeds the allowed limit. For more information, see [Guidelines and quotas in Amazon Rekognition](https://docs.aws.amazon.com/rekognition/latest/dg/limits.html).
HTTP Status Code: 400

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_AssociateFaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/AssociateFaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/AssociateFaces)

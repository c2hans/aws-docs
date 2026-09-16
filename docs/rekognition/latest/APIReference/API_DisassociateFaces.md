---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_DisassociateFaces.html
---

# DisassociateFaces
<a name="API_DisassociateFaces"></a>

Removes the association between a `Face` supplied in an array of `FaceIds` and the User. If the User is not present already, then a `ResourceNotFound` exception is thrown. If successful, an array of faces that are disassociated from the User is returned. If a given face is already disassociated from the given UserID, it will be ignored and not be returned in the response. If a given face is already associated with a different User or not found in the collection it will be returned as part of `UnsuccessfulDisassociations`. You can remove 1 - 100 face IDs from a user at one time.

## Request Syntax
<a name="API_DisassociateFaces_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CollectionId": "{{string}}",
   "FaceIds": [ "{{string}}" ],
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_DisassociateFaces_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_DisassociateFaces_RequestSyntax) **   <a name="rekognition-DisassociateFaces-request-ClientRequestToken"></a>
Idempotent token used to identify the request to `DisassociateFaces`. If you use the same token with multiple `DisassociateFaces` requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [CollectionId](#API_DisassociateFaces_RequestSyntax) **   <a name="rekognition-DisassociateFaces-request-CollectionId"></a>
The ID of an existing collection containing the UserID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [FaceIds](#API_DisassociateFaces_RequestSyntax) **   <a name="rekognition-DisassociateFaces-request-FaceIds"></a>
An array of face IDs to disassociate from the UserID.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 100 items.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [UserId](#API_DisassociateFaces_RequestSyntax) **   <a name="rekognition-DisassociateFaces-request-UserId"></a>
ID for the existing UserID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: Yes

## Response Syntax
<a name="API_DisassociateFaces_ResponseSyntax"></a>

```
{
   "DisassociatedFaces": [
      {
         "FaceId": "string"
      }
   ],
   "UnsuccessfulFaceDisassociations": [
      {
         "FaceId": "string",
         "Reasons": [ "string" ],
         "UserId": "string"
      }
   ],
   "UserStatus": "string"
}
```

## Response Elements
<a name="API_DisassociateFaces_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DisassociatedFaces](#API_DisassociateFaces_ResponseSyntax) **   <a name="rekognition-DisassociateFaces-response-DisassociatedFaces"></a>
An array of DissociatedFace objects containing FaceIds that are successfully disassociated with the UserID is returned. Returned if the DisassociatedFaces action is successful.
Type: Array of [DisassociatedFace](API_DisassociatedFace.md) objects
Array Members: Minimum number of 0 items. Maximum number of 100 items.

 ** [UnsuccessfulFaceDisassociations](#API_DisassociateFaces_ResponseSyntax) **   <a name="rekognition-DisassociateFaces-response-UnsuccessfulFaceDisassociations"></a>
An array of UnsuccessfulDisassociation objects containing FaceIds that are not successfully associated, along with the reasons for the failure to associate. Returned if the DisassociateFaces action is successful.
Type: Array of [UnsuccessfulFaceDisassociation](API_UnsuccessfulFaceDisassociation.md) objects
Array Members: Minimum number of 0 items. Maximum number of 500 items.

 ** [UserStatus](#API_DisassociateFaces_ResponseSyntax) **   <a name="rekognition-DisassociateFaces-response-UserStatus"></a>
The status of an update made to a User. Reflects if the User has been updated for every requested change.
Type: String
Valid Values: `ACTIVE | UPDATING | CREATING | CREATED`

## Errors
<a name="API_DisassociateFaces_Errors"></a>

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

 ** ThrottlingException **
Amazon Rekognition is temporarily unable to process the request. Try your call again.
HTTP Status Code: 500

## See Also
<a name="API_DisassociateFaces_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/DisassociateFaces)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/DisassociateFaces)

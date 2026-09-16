---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_SearchUsers.html
---

# SearchUsers
<a name="API_SearchUsers"></a>

Searches for UserIDs within a collection based on a `FaceId` or `UserId`. This API can be used to find the closest UserID (with a highest similarity) to associate a face. The request must be provided with either `FaceId` or `UserId`. The operation returns an array of UserID that match the `FaceId` or `UserId`, ordered by similarity score with the highest similarity first.

## Request Syntax
<a name="API_SearchUsers_RequestSyntax"></a>

```
{
   "CollectionId": "{{string}}",
   "FaceId": "{{string}}",
   "MaxUsers": {{number}},
   "UserId": "{{string}}",
   "UserMatchThreshold": {{number}}
}
```

## Request Parameters
<a name="API_SearchUsers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CollectionId](#API_SearchUsers_RequestSyntax) **   <a name="rekognition-SearchUsers-request-CollectionId"></a>
The ID of an existing collection containing the UserID, used with a UserId or FaceId. If a FaceId is provided, UserId isn’t required to be present in the Collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [FaceId](#API_SearchUsers_RequestSyntax) **   <a name="rekognition-SearchUsers-request-FaceId"></a>
ID for the existing face.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** [MaxUsers](#API_SearchUsers_RequestSyntax) **   <a name="rekognition-SearchUsers-request-MaxUsers"></a>
Maximum number of identities to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [UserId](#API_SearchUsers_RequestSyntax) **   <a name="rekognition-SearchUsers-request-UserId"></a>
ID for the existing User.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: No

 ** [UserMatchThreshold](#API_SearchUsers_RequestSyntax) **   <a name="rekognition-SearchUsers-request-UserMatchThreshold"></a>
Optional value that specifies the minimum confidence in the matched UserID to return. Default value of 80.
Type: Float
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

## Response Syntax
<a name="API_SearchUsers_ResponseSyntax"></a>

```
{
   "FaceModelVersion": "string",
   "SearchedFace": {
      "FaceId": "string"
   },
   "SearchedUser": {
      "UserId": "string"
   },
   "UserMatches": [
      {
         "Similarity": number,
         "User": {
            "UserId": "string",
            "UserStatus": "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FaceModelVersion](#API_SearchUsers_ResponseSyntax) **   <a name="rekognition-SearchUsers-response-FaceModelVersion"></a>
Version number of the face detection model associated with the input CollectionId.
Type: String

 ** [SearchedFace](#API_SearchUsers_ResponseSyntax) **   <a name="rekognition-SearchUsers-response-SearchedFace"></a>
Contains the ID of a face that was used to search for matches in a collection.
Type: [SearchedFace](API_SearchedFace.md) object

 ** [SearchedUser](#API_SearchUsers_ResponseSyntax) **   <a name="rekognition-SearchUsers-response-SearchedUser"></a>
Contains the ID of the UserID that was used to search for matches in a collection.
Type: [SearchedUser](API_SearchedUser.md) object

 ** [UserMatches](#API_SearchUsers_ResponseSyntax) **   <a name="rekognition-SearchUsers-response-UserMatches"></a>
An array of UserMatch objects that matched the input face along with the confidence in the match. Array will be empty if there are no matches.
Type: Array of [UserMatch](API_UserMatch.md) objects
Array Members: Maximum number of 500 items.

## Errors
<a name="API_SearchUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
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
<a name="API_SearchUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/SearchUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/SearchUsers)

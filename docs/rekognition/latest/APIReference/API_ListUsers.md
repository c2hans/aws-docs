---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_ListUsers.html
---

# ListUsers
<a name="API_ListUsers"></a>

Returns metadata of the User such as `UserID` in the specified collection. Anonymous User (to reserve faces without any identity) is not returned as part of this request. The results are sorted by system generated primary key ID. If the response is truncated, `NextToken` is returned in the response that can be used in the subsequent request to retrieve the next set of identities.

## Request Syntax
<a name="API_ListUsers_RequestSyntax"></a>

```
{
   "CollectionId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListUsers_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [CollectionId](#API_ListUsers_RequestSyntax) **   <a name="rekognition-ListUsers-request-CollectionId"></a>
The ID of an existing collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [MaxResults](#API_ListUsers_RequestSyntax) **   <a name="rekognition-ListUsers-request-MaxResults"></a>
Maximum number of UsersID to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 500.
Required: No

 ** [NextToken](#API_ListUsers_RequestSyntax) **   <a name="rekognition-ListUsers-request-NextToken"></a>
Pagingation token to receive the next set of UsersID.
Type: String
Length Constraints: Maximum length of 255.
Required: No

## Response Syntax
<a name="API_ListUsers_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "Users": [
      {
         "UserId": "string",
         "UserStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListUsers_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListUsers_ResponseSyntax) **   <a name="rekognition-ListUsers-response-NextToken"></a>
A pagination token to be used with the subsequent request if the response is truncated.
Type: String
Length Constraints: Maximum length of 255.

 ** [Users](#API_ListUsers_ResponseSyntax) **   <a name="rekognition-ListUsers-response-Users"></a>
List of UsersID associated with the specified collection.
Type: Array of [User](API_User.md) objects
Array Members: Maximum number of 500 items.

## Errors
<a name="API_ListUsers_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You are not authorized to perform the action.
HTTP Status Code: 400

 ** InternalServerError **
Amazon Rekognition experienced a service issue. Try your call again.
HTTP Status Code: 500

 ** InvalidPaginationTokenException **
Pagination token in the request is not valid.
HTTP Status Code: 400

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
<a name="API_ListUsers_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/ListUsers)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/ListUsers)

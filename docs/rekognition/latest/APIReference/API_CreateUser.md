---
source_url: https://docs.aws.amazon.com/rekognition/latest/APIReference/API_CreateUser.html
---

# CreateUser
<a name="API_CreateUser"></a>

Creates a new User within a collection specified by `CollectionId`. Takes `UserId` as a parameter, which is a user provided ID which should be unique within the collection. The provided `UserId` will alias the system generated UUID to make the `UserId` more user friendly.

Uses a `ClientToken`, an idempotency token that ensures a call to `CreateUser` completes only once. If the value is not supplied, the AWS SDK generates an idempotency token for the requests. This prevents retries after a network error results from making multiple `CreateUser` calls.

## Request Syntax
<a name="API_CreateUser_RequestSyntax"></a>

```
{
   "ClientRequestToken": "{{string}}",
   "CollectionId": "{{string}}",
   "UserId": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateUser_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientRequestToken](#API_CreateUser_RequestSyntax) **   <a name="rekognition-CreateUser-request-ClientRequestToken"></a>
Idempotent token used to identify the request to `CreateUser`. If you use the same token with multiple `CreateUser` requests, the same response is returned. Use ClientRequestToken to prevent the same request from being processed more than once.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9-_]+$`
Required: No

 ** [CollectionId](#API_CreateUser_RequestSyntax) **   <a name="rekognition-CreateUser-request-CollectionId"></a>
The ID of an existing collection to which the new UserID needs to be created.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9_.\-]+`
Required: Yes

 ** [UserId](#API_CreateUser_RequestSyntax) **   <a name="rekognition-CreateUser-request-UserId"></a>
ID for the UserID to be created. This ID needs to be unique within the collection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9_.\-:]+`
Required: Yes

## Response Elements
<a name="API_CreateUser_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_CreateUser_Errors"></a>

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
<a name="API_CreateUser_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/rekognition-2016-06-27/CreateUser)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/rekognition-2016-06-27/CreateUser)

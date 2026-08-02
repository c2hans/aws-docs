---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_UpdateTestSet.html
---

# UpdateTestSet
<a name="API_UpdateTestSet"></a>

The action to update the test set.

## Request Syntax
<a name="API_UpdateTestSet_RequestSyntax"></a>

```
PUT /testsets/{{testSetId}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "testSetName": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTestSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetId](#API_UpdateTestSet_RequestSyntax) **   <a name="lexv2-UpdateTestSet-request-uri-testSetId"></a>
The test set Id for which update test operation to be performed.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_UpdateTestSet_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateTestSet_RequestSyntax) **   <a name="lexv2-UpdateTestSet-request-description"></a>
The new test set description.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [testSetName](#API_UpdateTestSet_RequestSyntax) **   <a name="lexv2-UpdateTestSet-request-testSetName"></a>
The new test set name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

## Response Syntax
<a name="API_UpdateTestSet_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDateTime": number,
   "description": "string",
   "lastUpdatedDateTime": number,
   "modality": "string",
   "numTurns": number,
   "roleArn": "string",
   "status": "string",
   "storageLocation": {
      "kmsKeyArn": "string",
      "s3BucketName": "string",
      "s3Path": "string"
   },
   "testSetId": "string",
   "testSetName": "string"
}
```

## Response Elements
<a name="API_UpdateTestSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-creationDateTime"></a>
The creation date and time for the updated test set.
Type: Timestamp

 ** [description](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-description"></a>
The test set description for the updated test set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [lastUpdatedDateTime](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-lastUpdatedDateTime"></a>
 The date and time of the last update for the updated test set.
Type: Timestamp

 ** [modality](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-modality"></a>
Indicates whether audio or text is used for the updated test set.
Type: String
Valid Values: `Text | Audio`

 ** [numTurns](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-numTurns"></a>
The number of conversation turns from the updated test set.
Type: Integer

 ** [roleArn](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-roleArn"></a>
The roleARN used for any operation in the test set to access resources in the AWS account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

 ** [status](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-status"></a>
The status for the updated test set.
Type: String
Valid Values: `Importing | PendingAnnotation | Deleting | ValidationError | Ready`

 ** [storageLocation](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-storageLocation"></a>
The Amazon S3 storage location for the updated test set.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object

 ** [testSetId](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-testSetId"></a>
The test set Id for which update test operation to be performed.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetName](#API_UpdateTestSet_ResponseSyntax) **   <a name="lexv2-UpdateTestSet-response-testSetName"></a>
The test set name for the updated test set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

## Errors
<a name="API_UpdateTestSet_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** PreconditionFailedException **
Your request couldn't be completed because one or more request fields aren't valid. Check the fields in your request and try again.
HTTP Status Code: 412

 ** ServiceQuotaExceededException **
You have reached a quota for your bot.
HTTP Status Code: 402

 ** ThrottlingException **
Your request rate is too high. Reduce the frequency of requests.
 ** retryAfterSeconds **
The number of seconds after which the user can invoke the API again.
HTTP Status Code: 429

 ** ValidationException **
One of the input parameters in your request isn't valid. Check the parameters and try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateTestSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/UpdateTestSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/UpdateTestSet)

---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_StartTestSetGeneration.html
---

# StartTestSetGeneration
<a name="API_StartTestSetGeneration"></a>

The action to start the generation of test set.

## Request Syntax
<a name="API_StartTestSetGeneration_RequestSyntax"></a>

```
PUT /testsetgenerations HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "generationDataSource": {
      "conversationLogsDataSource": {
         "botAliasId": "{{string}}",
         "botId": "{{string}}",
         "filter": {
            "endTime": {{number}},
            "inputMode": "{{string}}",
            "startTime": {{number}}
         },
         "localeId": "{{string}}"
      }
   },
   "roleArn": "{{string}}",
   "storageLocation": {
      "kmsKeyArn": "{{string}}",
      "s3BucketName": "{{string}}",
      "s3Path": "{{string}}"
   },
   "testSetName": "{{string}}",
   "testSetTags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_StartTestSetGeneration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_StartTestSetGeneration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_StartTestSetGeneration_RequestSyntax) **   <a name="lexv2-StartTestSetGeneration-request-description"></a>
The test set description for the test set generation request.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.
Required: No

 ** [generationDataSource](#API_StartTestSetGeneration_RequestSyntax) **   <a name="lexv2-StartTestSetGeneration-request-generationDataSource"></a>
The data source for the test set generation.
Type: [TestSetGenerationDataSource](API_TestSetGenerationDataSource.md) object
Required: Yes

 ** [roleArn](#API_StartTestSetGeneration_RequestSyntax) **   <a name="lexv2-StartTestSetGeneration-request-roleArn"></a>
The roleARN used for any operation in the test set to access resources in the AWS account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`
Required: Yes

 ** [storageLocation](#API_StartTestSetGeneration_RequestSyntax) **   <a name="lexv2-StartTestSetGeneration-request-storageLocation"></a>
The Amazon S3 storage location for the test set generation.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object
Required: Yes

 ** [testSetName](#API_StartTestSetGeneration_RequestSyntax) **   <a name="lexv2-StartTestSetGeneration-request-testSetName"></a>
The test set name for the test set generation request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`
Required: Yes

 ** [testSetTags](#API_StartTestSetGeneration_RequestSyntax) **   <a name="lexv2-StartTestSetGeneration-request-testSetTags"></a>
A list of tags to add to the test set. You can only add tags when you import/generate a new test set. You can't use the `UpdateTestSet` operation to update tags. To update tags, use the `TagResource` operation.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_StartTestSetGeneration_ResponseSyntax"></a>

```
HTTP/1.1 202
Content-type: application/json

{
   "creationDateTime": number,
   "description": "string",
   "generationDataSource": {
      "conversationLogsDataSource": {
         "botAliasId": "string",
         "botId": "string",
         "filter": {
            "endTime": number,
            "inputMode": "string",
            "startTime": number
         },
         "localeId": "string"
      }
   },
   "roleArn": "string",
   "storageLocation": {
      "kmsKeyArn": "string",
      "s3BucketName": "string",
      "s3Path": "string"
   },
   "testSetGenerationId": "string",
   "testSetGenerationStatus": "string",
   "testSetName": "string",
   "testSetTags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_StartTestSetGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 202 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-creationDateTime"></a>
 The creation date and time for the test set generation.
Type: Timestamp

 ** [description](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-description"></a>
The description used for the test set generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [generationDataSource](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-generationDataSource"></a>
 The data source for the test set generation.
Type: [TestSetGenerationDataSource](API_TestSetGenerationDataSource.md) object

 ** [roleArn](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-roleArn"></a>
The roleARN used for any operation in the test set to access resources in the AWS account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

 ** [storageLocation](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-storageLocation"></a>
The Amazon S3 storage location for the test set generation.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object

 ** [testSetGenerationId](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-testSetGenerationId"></a>
The unique identifier of the test set generation to describe.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetGenerationStatus](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-testSetGenerationStatus"></a>
 The status for the test set generation.
Type: String
Valid Values: `Generating | Ready | Failed | Pending`

 ** [testSetName](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-testSetName"></a>
The test set name used for the test set generation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

 ** [testSetTags](#API_StartTestSetGeneration_ResponseSyntax) **   <a name="lexv2-StartTestSetGeneration-response-testSetTags"></a>
A list of tags that was used for the test set that is being generated.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

## Errors
<a name="API_StartTestSetGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The action that you tried to perform couldn't be completed because the resource is in a conflicting state. For example, deleting a bot that is in the CREATING state. Try your request again.
HTTP Status Code: 409

 ** InternalServerException **
The service encountered an unexpected condition. Try your request again.
HTTP Status Code: 500

 ** ResourceNotFoundException **
You asked to describe a resource that doesn't exist. Check the resource that you are requesting and try again.
HTTP Status Code: 404

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
<a name="API_StartTestSetGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/StartTestSetGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/StartTestSetGeneration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

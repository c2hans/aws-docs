---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestSetGeneration.html
---

# DescribeTestSetGeneration
<a name="API_DescribeTestSetGeneration"></a>

Gets metadata information about the test set generation.

## Request Syntax
<a name="API_DescribeTestSetGeneration_RequestSyntax"></a>

```
GET /testsetgenerations/{{testSetGenerationId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTestSetGeneration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetGenerationId](#API_DescribeTestSetGeneration_RequestSyntax) **   <a name="lexv2-DescribeTestSetGeneration-request-uri-testSetGenerationId"></a>
The unique identifier of the test set generation.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeTestSetGeneration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTestSetGeneration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDateTime": number,
   "description": "string",
   "failureReasons": [ "string" ],
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
   "lastUpdatedDateTime": number,
   "roleArn": "string",
   "storageLocation": {
      "kmsKeyArn": "string",
      "s3BucketName": "string",
      "s3Path": "string"
   },
   "testSetGenerationId": "string",
   "testSetGenerationStatus": "string",
   "testSetId": "string",
   "testSetName": "string"
}
```

## Response Elements
<a name="API_DescribeTestSetGeneration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-creationDateTime"></a>
The creation date and time for the test set generation.
Type: Timestamp

 ** [description](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-description"></a>
The test set description for the test set generation.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [failureReasons](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-failureReasons"></a>
The reasons the test set generation failed.
Type: Array of strings

 ** [generationDataSource](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-generationDataSource"></a>
The data source of the test set used for the test set generation.
Type: [TestSetGenerationDataSource](API_TestSetGenerationDataSource.md) object

 ** [lastUpdatedDateTime](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-lastUpdatedDateTime"></a>
The date and time of the last update for the test set generation.
Type: Timestamp

 ** [roleArn](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-roleArn"></a>
 The roleARN of the test set used for the test set generation.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

 ** [storageLocation](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-storageLocation"></a>
The Amazon S3 storage location for the test set generation.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object

 ** [testSetGenerationId](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-testSetGenerationId"></a>
The unique identifier of the test set generation.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetGenerationStatus](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-testSetGenerationStatus"></a>
The status for the test set generation.
Type: String
Valid Values: `Generating | Ready | Failed | Pending`

 ** [testSetId](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-testSetId"></a>
The unique identifier for the test set created for the generated test set.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetName](#API_DescribeTestSetGeneration_ResponseSyntax) **   <a name="lexv2-DescribeTestSetGeneration-response-testSetName"></a>
The test set name for the generated test set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

## Errors
<a name="API_DescribeTestSetGeneration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

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
<a name="API_DescribeTestSetGeneration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeTestSetGeneration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeTestSetGeneration)

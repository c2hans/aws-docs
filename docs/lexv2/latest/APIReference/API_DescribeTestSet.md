---
source_url: https://docs.aws.amazon.com/lexv2/latest/APIReference/API_DescribeTestSet.html
---

# DescribeTestSet
<a name="API_DescribeTestSet"></a>

Gets metadata information about the test set.

## Request Syntax
<a name="API_DescribeTestSet_RequestSyntax"></a>

```
GET /testsets/{{testSetId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTestSet_RequestParameters"></a>

The request uses the following URI parameters.

 ** [testSetId](#API_DescribeTestSet_RequestSyntax) **   <a name="lexv2-DescribeTestSet-request-uri-testSetId"></a>
The test set Id for the test set request.
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`
Required: Yes

## Request Body
<a name="API_DescribeTestSet_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTestSet_ResponseSyntax"></a>

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
<a name="API_DescribeTestSet_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDateTime](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-creationDateTime"></a>
The creation date and time for the test set data.
Type: Timestamp

 ** [description](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-description"></a>
The description of the test set.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 2000.

 ** [lastUpdatedDateTime](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-lastUpdatedDateTime"></a>
The date and time for the last update of the test set data.
Type: Timestamp

 ** [modality](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-modality"></a>
Indicates whether the test set is audio or text data.
Type: String
Valid Values: `Text | Audio`

 ** [numTurns](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-numTurns"></a>
The total number of agent and user turn in the test set.
Type: Integer

 ** [roleArn](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-roleArn"></a>
The roleARN used for any operation in the test set to access resources in the AWS account.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 2048.
Pattern: `^arn:aws:iam::[0-9]{12}:role/.*$`

 ** [status](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-status"></a>
The status of the test set.
Type: String
Valid Values: `Importing | PendingAnnotation | Deleting | ValidationError | Ready`

 ** [storageLocation](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-storageLocation"></a>
The Amazon S3 storage location for the test set data.
Type: [TestSetStorageLocation](API_TestSetStorageLocation.md) object

 ** [testSetId](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-testSetId"></a>
The test set Id for the test set response.
Type: String
Length Constraints: Fixed length of 10.
Pattern: `^[0-9a-zA-Z]+$`

 ** [testSetName](#API_DescribeTestSet_ResponseSyntax) **   <a name="lexv2-DescribeTestSet-response-testSetName"></a>
The test set name of the test set.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `^([0-9a-zA-Z][_-]?){1,100}$`

## Errors
<a name="API_DescribeTestSet_Errors"></a>

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
<a name="API_DescribeTestSet_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/models.lex.v2-2020-08-07/DescribeTestSet)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/models.lex.v2-2020-08-07/DescribeTestSet)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Lex. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query lexv2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

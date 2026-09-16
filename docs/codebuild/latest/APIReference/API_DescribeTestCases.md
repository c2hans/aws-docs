---
source_url: https://docs.aws.amazon.com/codebuild/latest/APIReference/API_DescribeTestCases.html
---

# DescribeTestCases
<a name="API_DescribeTestCases"></a>

 Returns a list of details about test cases for a report.

## Request Syntax
<a name="API_DescribeTestCases_RequestSyntax"></a>

```
{
   "filter": {
      "keyword": "{{string}}",
      "status": "{{string}}"
   },
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "reportArn": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeTestCases_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

**Note**
In the following list, the required parameters are described first.

 ** [reportArn](#API_DescribeTestCases_RequestSyntax) **   <a name="CodeBuild-DescribeTestCases-request-reportArn"></a>
 The ARN of the report for which test cases are returned.
Type: String
Required: Yes

 ** [filter](#API_DescribeTestCases_RequestSyntax) **   <a name="CodeBuild-DescribeTestCases-request-filter"></a>
 A `TestCaseFilter` object used to filter the returned reports.
Type: [TestCaseFilter](API_TestCaseFilter.md) object
Required: No

 ** [maxResults](#API_DescribeTestCases_RequestSyntax) **   <a name="CodeBuild-DescribeTestCases-request-maxResults"></a>
 The maximum number of paginated test cases returned per response. Use `nextToken` to iterate pages in the list of returned `TestCase` objects. The default value is 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_DescribeTestCases_RequestSyntax) **   <a name="CodeBuild-DescribeTestCases-request-nextToken"></a>
 During a previous call, the maximum number of items that can be returned is the value specified in `maxResults`. If there more items in the list, then a unique string called a *nextToken* is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String
Required: No

## Response Syntax
<a name="API_DescribeTestCases_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "testCases": [
      {
         "durationInNanoSeconds": number,
         "expired": number,
         "message": "string",
         "name": "string",
         "prefix": "string",
         "reportArn": "string",
         "status": "string",
         "testRawDataPath": "string",
         "testSuiteName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeTestCases_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_DescribeTestCases_ResponseSyntax) **   <a name="CodeBuild-DescribeTestCases-response-nextToken"></a>
 During a previous call, the maximum number of items that can be returned is the value specified in `maxResults`. If there more items in the list, then a unique string called a *nextToken* is returned. To get the next batch of items in the list, call this operation again, adding the next token to the call. To get all of the items in the list, keep calling this operation with each subsequent next token that is returned, until no more next tokens are returned.
Type: String

 ** [testCases](#API_DescribeTestCases_ResponseSyntax) **   <a name="CodeBuild-DescribeTestCases-response-testCases"></a>
 The returned list of test cases.
Type: Array of [TestCase](API_TestCase.md) objects

## Errors
<a name="API_DescribeTestCases_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInputException **
The input value that was provided is not valid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified AWS resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeTestCases_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/codebuild-2016-10-06/DescribeTestCases)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codebuild-2016-10-06/DescribeTestCases)

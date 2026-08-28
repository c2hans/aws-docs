---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_DescribeTestCase.html
---

# DescribeTestCase
<a name="API_DescribeTestCase"></a>

Describes the specified test case and allows you to get the content and metadata of the test case for the specified Amazon Connect instance.

## Request Syntax
<a name="API_DescribeTestCase_RequestSyntax"></a>

```
GET /test-cases/{{InstanceId}}/{{TestCaseId}}?status={{Status}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeTestCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_DescribeTestCase_RequestSyntax) **   <a name="connect-DescribeTestCase-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [Status](#API_DescribeTestCase_RequestSyntax) **   <a name="connect-DescribeTestCase-request-uri-Status"></a>
The status of the test case version to retrieve. If not specified, returns the published version if available, otherwise returns the saved version.
Valid Values: `PUBLISHED | SAVED`

 ** [TestCaseId](#API_DescribeTestCase_RequestSyntax) **   <a name="connect-DescribeTestCase-request-uri-TestCaseId"></a>
The identifier of the test case.
Length Constraints: Maximum length of 500.
Required: Yes

## Request Body
<a name="API_DescribeTestCase_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeTestCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TestCase": {
      "Arn": "string",
      "Content": "string",
      "Description": "string",
      "EntryPoint": {
         "ChatEntryPointParameters": {
            "FlowId": "string"
         },
         "Type": "string",
         "VoiceCallEntryPointParameters": {
            "DestinationPhoneNumber": "string",
            "FlowId": "string",
            "SourcePhoneNumber": "string"
         }
      },
      "Id": "string",
      "InitializationData": "string",
      "LastModifiedRegion": "string",
      "LastModifiedTime": number,
      "Name": "string",
      "Status": "string",
      "Tags": {
         "string" : "string"
      },
      "TestCaseSha256": "string"
   }
}
```

## Response Elements
<a name="API_DescribeTestCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TestCase](#API_DescribeTestCase_ResponseSyntax) **   <a name="connect-DescribeTestCase-response-TestCase"></a>
The test case object containing all test case information.
Type: [TestCase](API_TestCase.md) object

## Errors
<a name="API_DescribeTestCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/DescribeTestCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/DescribeTestCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

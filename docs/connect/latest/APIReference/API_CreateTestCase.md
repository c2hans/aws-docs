---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_CreateTestCase.html
---

# CreateTestCase
<a name="API_CreateTestCase"></a>

Creates a test case with its content and metadata for the specified Amazon Connect instance.

## Request Syntax
<a name="API_CreateTestCase_RequestSyntax"></a>

```
PUT /test-cases/{{InstanceId}} HTTP/1.1
x-amz-resource-id: {{TestCaseId}}
x-amz-last-modified-time: {{LastModifiedTime}}
x-amz-last-modified-region: {{LastModifiedRegion}}
Content-type: application/json

{
   "Content": "{{string}}",
   "Description": "{{string}}",
   "EntryPoint": {
      "ChatEntryPointParameters": {
         "FlowId": "{{string}}"
      },
      "Type": "{{string}}",
      "VoiceCallEntryPointParameters": {
         "DestinationPhoneNumber": "{{string}}",
         "FlowId": "{{string}}",
         "SourcePhoneNumber": "{{string}}"
      }
   },
   "InitializationData": "{{string}}",
   "Name": "{{string}}",
   "Status": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateTestCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [LastModifiedRegion](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-LastModifiedRegion"></a>
The region in which the resource was last modified
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-LastModifiedTime"></a>
The time at which the resource was last modified.

 ** [TestCaseId](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-TestCaseId"></a>
Id of the test case if you want to create it in a replica region using Amazon Connect Global Resiliency
Length Constraints: Maximum length of 500.

## Request Body
<a name="API_CreateTestCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Content](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-Content"></a>
The JSON string that represents the content of the test.
Type: String
Required: Yes

 ** [Description](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-Description"></a>
The description of the test.
Type: String
Required: No

 ** [EntryPoint](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-EntryPoint"></a>
Defines the starting point for your test.
Type: [TestCaseEntryPoint](API_TestCaseEntryPoint.md) object
Required: No

 ** [InitializationData](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-InitializationData"></a>
Defines the initial custom attributes for your test.
Type: String
Required: No

 ** [Name](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-Name"></a>
The name of the test.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

 ** [Status](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-Status"></a>
Indicates the test status as either SAVED or PUBLISHED. The PUBLISHED status will initiate validation on the content. The SAVED status does not initiate validation of the content.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

 ** [Tags](#API_CreateTestCase_RequestSyntax) **   <a name="connect-CreateTestCase-request-Tags"></a>
The tags used to organize, track, or control access for this resource.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_CreateTestCase_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "TestCaseArn": "string",
   "TestCaseId": "string"
}
```

## Response Elements
<a name="API_CreateTestCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [TestCaseArn](#API_CreateTestCase_ResponseSyntax) **   <a name="connect-CreateTestCase-response-TestCaseArn"></a>
The Amazon Resource Name (ARN) of the test.
Type: String

 ** [TestCaseId](#API_CreateTestCase_ResponseSyntax) **   <a name="connect-CreateTestCase-response-TestCaseId"></a>
The identifier of the test.
Type: String
Length Constraints: Maximum length of 500.

## Errors
<a name="API_CreateTestCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
HTTP Status Code: 409

 ** IdempotencyException **
An entity with the same name already exists.
HTTP Status Code: 409

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

 ** InvalidTestCaseException **
The test is not valid.
 ** Problems **
The problems with the test. Please fix before trying again.
HTTP Status Code: 400

 ** LimitExceededException **
The allowed limit for the resource has been exceeded.
 ** Message **
The message about the limit.
HTTP Status Code: 429

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ServiceQuotaExceededException **
The service quota has been exceeded.
 ** Reason **
The reason for the exception.
HTTP Status Code: 402

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_CreateTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/CreateTestCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/CreateTestCase)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

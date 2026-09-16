---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_UpdateTestCase.html
---

# UpdateTestCase
<a name="API_UpdateTestCase"></a>

Updates any of the metadata for a test case, such as the name, description, and status or content of an existing test case. This API doesn't allow customers to update the tags of the test case resource for the specified Amazon Connect instance.

## Request Syntax
<a name="API_UpdateTestCase_RequestSyntax"></a>

```
POST /test-cases/{{InstanceId}}/{{TestCaseId}} HTTP/1.1
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
   "Status": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateTestCase_RequestParameters"></a>

The request uses the following URI parameters.

 ** [InstanceId](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-uri-InstanceId"></a>
The identifier of the Amazon Connect instance.
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^(arn:(aws|aws-us-gov):connect:[a-z]{2}-[a-z]+-[0-9]{1}:[0-9]{1,20}:instance/)?[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$`
Required: Yes

 ** [LastModifiedRegion](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-LastModifiedRegion"></a>
The region in which the resource was last modified
Pattern: `[a-z]{2}(-[a-z]+){1,2}(-[0-9])?`

 ** [LastModifiedTime](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-LastModifiedTime"></a>
The time at which the resource was last modified.

 ** [TestCaseId](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-uri-TestCaseId"></a>
The identifier of the test case to update.
Length Constraints: Maximum length of 500.
Required: Yes

## Request Body
<a name="API_UpdateTestCase_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [Content](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-Content"></a>
The JSON string that represents the content of the test.
Type: String
Required: No

 ** [Description](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-Description"></a>
The description of the test case.
Type: String
Required: No

 ** [EntryPoint](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-EntryPoint"></a>
Defines the starting point for your test.
Type: [TestCaseEntryPoint](API_TestCaseEntryPoint.md) object
Required: No

 ** [InitializationData](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-InitializationData"></a>
Defines the test attributes for precise data representation.
Type: String
Required: No

 ** [Name](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-Name"></a>
The name of the test case.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** [Status](#API_UpdateTestCase_RequestSyntax) **   <a name="connect-UpdateTestCase-request-Status"></a>
Indicates the test status as either SAVED or PUBLISHED. The PUBLISHED status will initiate validation on the content. The SAVED status does not initiate validation of the content.
Type: String
Valid Values: `PUBLISHED | SAVED`
Required: No

## Response Syntax
<a name="API_UpdateTestCase_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateTestCase_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateTestCase_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action.
HTTP Status Code: 403

 ** DuplicateResourceException **
A resource with the specified name already exists.
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

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_UpdateTestCase_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/UpdateTestCase)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/UpdateTestCase)

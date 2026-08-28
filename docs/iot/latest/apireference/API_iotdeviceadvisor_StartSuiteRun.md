---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_StartSuiteRun.html
---

# StartSuiteRun
<a name="API_iotdeviceadvisor_StartSuiteRun"></a>

Starts a Device Advisor test suite run.

Requires permission to access the [StartSuiteRun](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_StartSuiteRun_RequestSyntax"></a>

```
POST /suiteDefinitions/{{suiteDefinitionId}}/suiteRuns HTTP/1.1
Content-type: application/json

{
   "suiteDefinitionVersion": "{{string}}",
   "suiteRunConfiguration": {
      "parallelRun": {{boolean}},
      "primaryDevice": {
         "certificateArn": "{{string}}",
         "deviceRoleArn": "{{string}}",
         "thingArn": "{{string}}"
      },
      "selectedTestList": [ "{{string}}" ]
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_StartSuiteRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_StartSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-request-uri-suiteDefinitionId"></a>
Suite definition ID of the test suite.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_iotdeviceadvisor_StartSuiteRun_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [suiteDefinitionVersion](#API_iotdeviceadvisor_StartSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-request-suiteDefinitionVersion"></a>
Suite definition version of the test suite.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.
Required: No

 ** [suiteRunConfiguration](#API_iotdeviceadvisor_StartSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-request-suiteRunConfiguration"></a>
Suite run configuration.
Type: [SuiteRunConfiguration](API_iotdeviceadvisor_SuiteRunConfiguration.md) object
Required: Yes

 ** [tags](#API_iotdeviceadvisor_StartSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-request-tags"></a>
The tags to be attached to the suite run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_iotdeviceadvisor_StartSuiteRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "endpoint": "string",
   "suiteRunArn": "string",
   "suiteRunId": "string"
}
```

## Response Elements
<a name="API_iotdeviceadvisor_StartSuiteRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_iotdeviceadvisor_StartSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-response-createdAt"></a>
Starts a Device Advisor test suite run based on suite create time.
Type: Timestamp

 ** [endpoint](#API_iotdeviceadvisor_StartSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-response-endpoint"></a>
The response of an Device Advisor test endpoint.
Type: String
Length Constraints: Minimum length of 45. Maximum length of 75.

 ** [suiteRunArn](#API_iotdeviceadvisor_StartSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-response-suiteRunArn"></a>
Amazon Resource Name (ARN) of the started suite run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [suiteRunId](#API_iotdeviceadvisor_StartSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_StartSuiteRun-response-suiteRunId"></a>
Suite Run ID of the started suite run.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.

## Errors
<a name="API_iotdeviceadvisor_StartSuiteRun_Errors"></a>

 ** ConflictException **
Sends a Conflict Exception.
 ** message **
Sends a Conflict Exception message.
HTTP Status Code: 400

 ** InternalServerException **
Sends an Internal Failure exception.
 ** message **
Sends an Internal Failure Exception message.
HTTP Status Code: 500

 ** ValidationException **
Sends a validation exception.
 ** message **
Sends a Validation Exception message.
HTTP Status Code: 400

## See Also
<a name="API_iotdeviceadvisor_StartSuiteRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/StartSuiteRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/StartSuiteRun)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

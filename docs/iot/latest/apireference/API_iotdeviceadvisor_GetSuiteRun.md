---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteRun.html
---

# GetSuiteRun
<a name="API_iotdeviceadvisor_GetSuiteRun"></a>

Gets information about a Device Advisor test suite run.

Requires permission to access the [GetSuiteRun](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_GetSuiteRun_RequestSyntax"></a>

```
GET /suiteDefinitions/{{suiteDefinitionId}}/suiteRuns/{{suiteRunId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_GetSuiteRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_GetSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-request-uri-suiteDefinitionId"></a>
Suite definition ID for the test suite run.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

 ** [suiteRunId](#API_iotdeviceadvisor_GetSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-request-uri-suiteRunId"></a>
Suite run ID for the test suite run.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_iotdeviceadvisor_GetSuiteRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "endTime": number,
   "errorReason": "string",
   "startTime": number,
   "status": "string",
   "suiteDefinitionId": "string",
   "suiteDefinitionVersion": "string",
   "suiteRunArn": "string",
   "suiteRunConfiguration": {
      "parallelRun": boolean,
      "primaryDevice": {
         "certificateArn": "string",
         "deviceRoleArn": "string",
         "thingArn": "string"
      },
      "selectedTestList": [ "string" ]
   },
   "suiteRunId": "string",
   "tags": {
      "string" : "string"
   },
   "testResult": {
      "groups": [
         {
            "groupId": "string",
            "groupName": "string",
            "tests": [
               {
                  "endTime": number,
                  "failure": "string",
                  "logUrl": "string",
                  "startTime": number,
                  "status": "string",
                  "testCaseDefinitionId": "string",
                  "testCaseDefinitionName": "string",
                  "testCaseRunId": "string",
                  "testScenarios": [
                     {
                        "failure": "string",
                        "status": "string",
                        "systemMessage": "string",
                        "testCaseScenarioId": "string",
                        "testCaseScenarioType": "string"
                     }
                  ],
                  "warnings": "string"
               }
            ]
         }
      ]
   }
}
```

## Response Elements
<a name="API_iotdeviceadvisor_GetSuiteRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [endTime](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-endTime"></a>
Date (in Unix epoch time) when the test suite run ended.
Type: Timestamp

 ** [errorReason](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-errorReason"></a>
Error reason for any test suite run failure.
Type: String

 ** [startTime](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-startTime"></a>
Date (in Unix epoch time) when the test suite run started.
Type: Timestamp

 ** [status](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-status"></a>
Status for the test suite run.
Type: String
Valid Values: `PASS | FAIL | CANCELED | PENDING | RUNNING | STOPPING | STOPPED | PASS_WITH_WARNINGS | ERROR`

 ** [suiteDefinitionId](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-suiteDefinitionId"></a>
Suite definition ID for the test suite run.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.

 ** [suiteDefinitionVersion](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-suiteDefinitionVersion"></a>
Suite definition version for the test suite run.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.

 ** [suiteRunArn](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-suiteRunArn"></a>
The ARN of the suite run.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [suiteRunConfiguration](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-suiteRunConfiguration"></a>
Suite run configuration for the test suite run.
Type: [SuiteRunConfiguration](API_iotdeviceadvisor_SuiteRunConfiguration.md) object

 ** [suiteRunId](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-suiteRunId"></a>
Suite run ID for the test suite run.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.

 ** [tags](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-tags"></a>
The tags attached to the suite run.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [testResult](#API_iotdeviceadvisor_GetSuiteRun_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRun-response-testResult"></a>
Test results for the test suite run.
Type: [TestResult](API_iotdeviceadvisor_TestResult.md) object

## Errors
<a name="API_iotdeviceadvisor_GetSuiteRun_Errors"></a>

 ** InternalServerException **
Sends an Internal Failure exception.
 ** message **
Sends an Internal Failure Exception message.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Sends a Resource Not Found exception.
 ** message **
Sends a Resource Not Found Exception message.
HTTP Status Code: 404

 ** ValidationException **
Sends a validation exception.
 ** message **
Sends a Validation Exception message.
HTTP Status Code: 400

## See Also
<a name="API_iotdeviceadvisor_GetSuiteRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/GetSuiteRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/GetSuiteRun)

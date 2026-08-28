---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteRunReport.html
---

# GetSuiteRunReport
<a name="API_iotdeviceadvisor_GetSuiteRunReport"></a>

Gets a report download link for a successful Device Advisor qualifying test suite run.

Requires permission to access the [GetSuiteRunReport](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_GetSuiteRunReport_RequestSyntax"></a>

```
GET /suiteDefinitions/{{suiteDefinitionId}}/suiteRuns/{{suiteRunId}}/report HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_GetSuiteRunReport_RequestParameters"></a>

The request uses the following URI parameters.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_GetSuiteRunReport_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRunReport-request-uri-suiteDefinitionId"></a>
Suite definition ID of the test suite.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

 ** [suiteRunId](#API_iotdeviceadvisor_GetSuiteRunReport_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRunReport-request-uri-suiteRunId"></a>
Suite run ID of the test suite run.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_iotdeviceadvisor_GetSuiteRunReport_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_GetSuiteRunReport_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "qualificationReportDownloadUrl": "string"
}
```

## Response Elements
<a name="API_iotdeviceadvisor_GetSuiteRunReport_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [qualificationReportDownloadUrl](#API_iotdeviceadvisor_GetSuiteRunReport_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteRunReport-response-qualificationReportDownloadUrl"></a>
Download URL of the qualification report.
Type: String

## Errors
<a name="API_iotdeviceadvisor_GetSuiteRunReport_Errors"></a>

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
<a name="API_iotdeviceadvisor_GetSuiteRunReport_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/GetSuiteRunReport)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

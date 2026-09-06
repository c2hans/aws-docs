---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_StopSuiteRun.html
---

# StopSuiteRun
<a name="API_iotdeviceadvisor_StopSuiteRun"></a>

Stops a Device Advisor test suite run that is currently running.

Requires permission to access the [StopSuiteRun](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_StopSuiteRun_RequestSyntax"></a>

```
POST /suiteDefinitions/{{suiteDefinitionId}}/suiteRuns/{{suiteRunId}}/stop HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_StopSuiteRun_RequestParameters"></a>

The request uses the following URI parameters.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_StopSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_StopSuiteRun-request-uri-suiteDefinitionId"></a>
Suite definition ID of the test suite run to be stopped.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

 ** [suiteRunId](#API_iotdeviceadvisor_StopSuiteRun_RequestSyntax) **   <a name="iot-iotdeviceadvisor_StopSuiteRun-request-uri-suiteRunId"></a>
Suite run ID of the test suite run to be stopped.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_iotdeviceadvisor_StopSuiteRun_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_StopSuiteRun_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_iotdeviceadvisor_StopSuiteRun_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_iotdeviceadvisor_StopSuiteRun_Errors"></a>

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
<a name="API_iotdeviceadvisor_StopSuiteRun_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/StopSuiteRun)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/StopSuiteRun)

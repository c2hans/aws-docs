---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_UpdateSuiteDefinition.html
---

# UpdateSuiteDefinition
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition"></a>

Updates a Device Advisor test suite.

Requires permission to access the [UpdateSuiteDefinition](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_RequestSyntax"></a>

```
PATCH /suiteDefinitions/{{suiteDefinitionId}} HTTP/1.1
Content-type: application/json

{
   "suiteDefinitionConfiguration": {
      "devicePermissionRoleArn": "{{string}}",
      "devices": [
         {
            "certificateArn": "{{string}}",
            "deviceRoleArn": "{{string}}",
            "thingArn": "{{string}}"
         }
      ],
      "intendedForQualification": {{boolean}},
      "isLongDurationTest": {{boolean}},
      "protocol": "{{string}}",
      "rootGroup": "{{string}}",
      "suiteDefinitionName": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_UpdateSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-request-uri-suiteDefinitionId"></a>
Suite definition ID of the test suite to be updated.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

## Request Body
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [suiteDefinitionConfiguration](#API_iotdeviceadvisor_UpdateSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-request-suiteDefinitionConfiguration"></a>
Updates a Device Advisor test suite with suite definition configuration.
Type: [SuiteDefinitionConfiguration](API_iotdeviceadvisor_SuiteDefinitionConfiguration.md) object
Required: Yes

## Response Syntax
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "lastUpdatedAt": number,
   "suiteDefinitionArn": "string",
   "suiteDefinitionId": "string",
   "suiteDefinitionName": "string",
   "suiteDefinitionVersion": "string"
}
```

## Response Elements
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-response-createdAt"></a>
Timestamp of when the test suite was created.
Type: Timestamp

 ** [lastUpdatedAt](#API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-response-lastUpdatedAt"></a>
Timestamp of when the test suite was updated.
Type: Timestamp

 ** [suiteDefinitionArn](#API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-response-suiteDefinitionArn"></a>
Amazon Resource Name (ARN) of the updated test suite.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-response-suiteDefinitionId"></a>
Suite definition ID of the updated test suite.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.

 ** [suiteDefinitionName](#API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-response-suiteDefinitionName"></a>
Updates the suite definition name. This is a required parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

 ** [suiteDefinitionVersion](#API_iotdeviceadvisor_UpdateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_UpdateSuiteDefinition-response-suiteDefinitionVersion"></a>
Suite definition version of the updated test suite.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.

## Errors
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_Errors"></a>

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
<a name="API_iotdeviceadvisor_UpdateSuiteDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/UpdateSuiteDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

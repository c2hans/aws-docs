---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_GetSuiteDefinition.html
---

# GetSuiteDefinition
<a name="API_iotdeviceadvisor_GetSuiteDefinition"></a>

Gets information about a Device Advisor test suite.

Requires permission to access the [GetSuiteDefinition](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_GetSuiteDefinition_RequestSyntax"></a>

```
GET /suiteDefinitions/{{suiteDefinitionId}}?suiteDefinitionVersion={{suiteDefinitionVersion}} HTTP/1.1
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_GetSuiteDefinition_RequestParameters"></a>

The request uses the following URI parameters.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_GetSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-request-uri-suiteDefinitionId"></a>
Suite definition ID of the test suite to get.
Length Constraints: Minimum length of 12. Maximum length of 36.
Required: Yes

 ** [suiteDefinitionVersion](#API_iotdeviceadvisor_GetSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-request-uri-suiteDefinitionVersion"></a>
Suite definition version of the test suite to get.
Length Constraints: Minimum length of 2. Maximum length of 255.

## Request Body
<a name="API_iotdeviceadvisor_GetSuiteDefinition_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "lastModifiedAt": number,
   "latestVersion": "string",
   "suiteDefinitionArn": "string",
   "suiteDefinitionConfiguration": {
      "devicePermissionRoleArn": "string",
      "devices": [
         {
            "certificateArn": "string",
            "deviceRoleArn": "string",
            "thingArn": "string"
         }
      ],
      "intendedForQualification": boolean,
      "isLongDurationTest": boolean,
      "protocol": "string",
      "rootGroup": "string",
      "suiteDefinitionName": "string"
   },
   "suiteDefinitionId": "string",
   "suiteDefinitionVersion": "string",
   "tags": {
      "string" : "string"
   }
}
```

## Response Elements
<a name="API_iotdeviceadvisor_GetSuiteDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-createdAt"></a>
Date (in Unix epoch time) when the suite definition was created.
Type: Timestamp

 ** [lastModifiedAt](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-lastModifiedAt"></a>
Date (in Unix epoch time) when the suite definition was last modified.
Type: Timestamp

 ** [latestVersion](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-latestVersion"></a>
Latest suite definition version of the suite definition.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.

 ** [suiteDefinitionArn](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-suiteDefinitionArn"></a>
The ARN of the suite definition.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [suiteDefinitionConfiguration](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-suiteDefinitionConfiguration"></a>
Suite configuration of the suite definition.
Type: [SuiteDefinitionConfiguration](API_iotdeviceadvisor_SuiteDefinitionConfiguration.md) object

 ** [suiteDefinitionId](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-suiteDefinitionId"></a>
Suite definition ID of the suite definition.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.

 ** [suiteDefinitionVersion](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-suiteDefinitionVersion"></a>
Suite definition version of the suite definition.
Type: String
Length Constraints: Minimum length of 2. Maximum length of 255.

 ** [tags](#API_iotdeviceadvisor_GetSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_GetSuiteDefinition-response-tags"></a>
Tags attached to the suite definition.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_iotdeviceadvisor_GetSuiteDefinition_Errors"></a>

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
<a name="API_iotdeviceadvisor_GetSuiteDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/GetSuiteDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_iotdeviceadvisor_CreateSuiteDefinition.html
---

# CreateSuiteDefinition
<a name="API_iotdeviceadvisor_CreateSuiteDefinition"></a>

Creates a Device Advisor test suite.

Requires permission to access the [CreateSuiteDefinition](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_RequestSyntax"></a>

```
POST /suiteDefinitions HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
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
   },
   "tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_iotdeviceadvisor_CreateSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-request-clientToken"></a>
A unique case-sensitive identifier that you can provide to ensure the idempotency of the request. Don't reuse this client token if a new idempotent request is required.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[\u0021-\u007E]+$`
Required: No

 ** [suiteDefinitionConfiguration](#API_iotdeviceadvisor_CreateSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-request-suiteDefinitionConfiguration"></a>
Creates a Device Advisor test suite with suite definition configuration.
Type: [SuiteDefinitionConfiguration](API_iotdeviceadvisor_SuiteDefinitionConfiguration.md) object
Required: Yes

 ** [tags](#API_iotdeviceadvisor_CreateSuiteDefinition_RequestSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-request-tags"></a>
The tags to be attached to the suite definition.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 1. Maximum length of 256.
Required: No

## Response Syntax
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "createdAt": number,
   "suiteDefinitionArn": "string",
   "suiteDefinitionId": "string",
   "suiteDefinitionName": "string"
}
```

## Response Elements
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [createdAt](#API_iotdeviceadvisor_CreateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-response-createdAt"></a>
The timestamp of when the test suite was created.
Type: Timestamp

 ** [suiteDefinitionArn](#API_iotdeviceadvisor_CreateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-response-suiteDefinitionArn"></a>
The Amazon Resource Name (ARN) of the test suite.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [suiteDefinitionId](#API_iotdeviceadvisor_CreateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-response-suiteDefinitionId"></a>
The UUID of the test suite created.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 36.

 ** [suiteDefinitionName](#API_iotdeviceadvisor_CreateSuiteDefinition_ResponseSyntax) **   <a name="iot-iotdeviceadvisor_CreateSuiteDefinition-response-suiteDefinitionName"></a>
The suite definition name of the test suite. This is a required parameter.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.

## Errors
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_Errors"></a>

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
<a name="API_iotdeviceadvisor_CreateSuiteDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotdeviceadvisor-2020-09-18/CreateSuiteDefinition)

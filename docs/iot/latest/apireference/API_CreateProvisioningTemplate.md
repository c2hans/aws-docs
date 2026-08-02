---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html
---

# CreateProvisioningTemplate
<a name="API_CreateProvisioningTemplate"></a>

Creates a provisioning template.

Requires permission to access the [CreateProvisioningTemplate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateProvisioningTemplate_RequestSyntax"></a>

```
POST /provisioning-templates HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "enabled": {{boolean}},
   "preProvisioningHook": {
      "payloadVersion": "{{string}}",
      "targetArn": "{{string}}"
   },
   "provisioningRoleArn": "{{string}}",
   "tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "templateBody": "{{string}}",
   "templateName": "{{string}}",
   "type": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateProvisioningTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateProvisioningTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-description"></a>
The description of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[^\p{C}]*`
Required: No

 ** [enabled](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-enabled"></a>
True to enable the provisioning template, otherwise false.
Type: Boolean
Required: No

 ** [preProvisioningHook](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-preProvisioningHook"></a>
Creates a pre-provisioning hook template. Only supports template of type `FLEET_PROVISIONING`. For more information about provisioning template types, see [type](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html#iot-CreateProvisioningTemplate-request-type).
Type: [ProvisioningHook](API_ProvisioningHook.md) object
Required: No

 ** [provisioningRoleArn](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-provisioningRoleArn"></a>
The role ARN for the role associated with the provisioning template. This IoT role grants permission to provision a device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: Yes

 ** [tags](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-tags"></a>
Metadata which can be used to manage the provisioning template.
For URI Request parameters use format: ...key1=value1&key2=value2...
For the CLI command-line parameter use format: &&tags "key1=value1&key2=value2..."
For the cli-input-json file use format: "tags": "key1=value1&key2=value2..."
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** [templateBody](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-templateBody"></a>
The JSON formatted contents of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`
Required: Yes

 ** [templateName](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-templateName"></a>
The name of the provisioning template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

 ** [type](#API_CreateProvisioningTemplate_RequestSyntax) **   <a name="iot-CreateProvisioningTemplate-request-type"></a>
The type you define in a provisioning template. You can create a template with only one type. You can't change the template type after its creation. The default value is `FLEET_PROVISIONING`. For more information about provisioning template, see: [Provisioning template](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html).
Type: String
Valid Values: `FLEET_PROVISIONING | JITP`
Required: No

## Response Syntax
<a name="API_CreateProvisioningTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "defaultVersionId": number,
   "templateArn": "string",
   "templateName": "string"
}
```

## Response Elements
<a name="API_CreateProvisioningTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [defaultVersionId](#API_CreateProvisioningTemplate_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplate-response-defaultVersionId"></a>
The default version of the provisioning template.
Type: Integer

 ** [templateArn](#API_CreateProvisioningTemplate_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplate-response-templateArn"></a>
The ARN that identifies the provisioning template.
Type: String

 ** [templateName](#API_CreateProvisioningTemplate_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplate-response-templateName"></a>
The name of the provisioning template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`

## Errors
<a name="API_CreateProvisioningTemplate_Errors"></a>

 ** InternalFailureException **
An unexpected error has occurred.
 ** message **
The message for the exception.
HTTP Status Code: 500

 ** InvalidRequestException **
The request is not valid.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit has been exceeded.
 ** message **
The message for the exception.
HTTP Status Code: 410

 ** ResourceAlreadyExistsException **
The resource already exists.
 ** message **
The message for the exception.
 ** resourceArn **
The ARN of the resource that caused the exception.
 ** resourceId **
The ID of the resource that caused the exception.
HTTP Status Code: 409

 ** ThrottlingException **
The rate exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 400

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_CreateProvisioningTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateProvisioningTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateProvisioningTemplate)

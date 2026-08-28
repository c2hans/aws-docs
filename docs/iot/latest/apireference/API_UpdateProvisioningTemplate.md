---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_UpdateProvisioningTemplate.html
---

# UpdateProvisioningTemplate
<a name="API_UpdateProvisioningTemplate"></a>

Updates a provisioning template.

Requires permission to access the [UpdateProvisioningTemplate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_UpdateProvisioningTemplate_RequestSyntax"></a>

```
PATCH /provisioning-templates/{{templateName}} HTTP/1.1
Content-type: application/json

{
   "defaultVersionId": {{number}},
   "description": "{{string}}",
   "enabled": {{boolean}},
   "preProvisioningHook": {
      "payloadVersion": "{{string}}",
      "targetArn": "{{string}}"
   },
   "provisioningRoleArn": "{{string}}",
   "removePreProvisioningHook": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateProvisioningTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateName](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-uri-templateName"></a>
The name of the provisioning template.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

## Request Body
<a name="API_UpdateProvisioningTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [defaultVersionId](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-defaultVersionId"></a>
The ID of the default provisioning template version.
Type: Integer
Required: No

 ** [description](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-description"></a>
The description of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[^\p{C}]*`
Required: No

 ** [enabled](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-enabled"></a>
True to enable the provisioning template, otherwise false.
Type: Boolean
Required: No

 ** [preProvisioningHook](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-preProvisioningHook"></a>
Updates the pre-provisioning hook template. Only supports template of type `FLEET_PROVISIONING`. For more information about provisioning template types, see [type](https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplate.html#iot-CreateProvisioningTemplate-request-type).
Type: [ProvisioningHook](API_ProvisioningHook.md) object
Required: No

 ** [provisioningRoleArn](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-provisioningRoleArn"></a>
The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Required: No

 ** [removePreProvisioningHook](#API_UpdateProvisioningTemplate_RequestSyntax) **   <a name="iot-UpdateProvisioningTemplate-request-removePreProvisioningHook"></a>
Removes pre-provisioning hook template.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateProvisioningTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateProvisioningTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateProvisioningTemplate_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

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

 ** ResourceNotFoundException **
The specified resource does not exist.
 ** message **
The message for the exception.
HTTP Status Code: 404

 ** UnauthorizedException **
You are not authorized to perform this operation.
 ** message **
The message for the exception.
HTTP Status Code: 401

## See Also
<a name="API_UpdateProvisioningTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/UpdateProvisioningTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/UpdateProvisioningTemplate)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

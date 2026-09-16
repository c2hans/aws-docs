---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DescribeProvisioningTemplate.html
---

# DescribeProvisioningTemplate
<a name="API_DescribeProvisioningTemplate"></a>

Returns information about a provisioning template.

Requires permission to access the [DescribeProvisioningTemplate](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DescribeProvisioningTemplate_RequestSyntax"></a>

```
GET /provisioning-templates/{{templateName}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeProvisioningTemplate_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateName](#API_DescribeProvisioningTemplate_RequestSyntax) **   <a name="iot-DescribeProvisioningTemplate-request-uri-templateName"></a>
The name of the provisioning template.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

## Request Body
<a name="API_DescribeProvisioningTemplate_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeProvisioningTemplate_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "creationDate": number,
   "defaultVersionId": number,
   "description": "string",
   "enabled": boolean,
   "lastModifiedDate": number,
   "preProvisioningHook": {
      "payloadVersion": "string",
      "targetArn": "string"
   },
   "provisioningRoleArn": "string",
   "templateArn": "string",
   "templateBody": "string",
   "templateName": "string",
   "type": "string"
}
```

## Response Elements
<a name="API_DescribeProvisioningTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [creationDate](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-creationDate"></a>
The date when the provisioning template was created.
Type: Timestamp

 ** [defaultVersionId](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-defaultVersionId"></a>
The default fleet template version ID.
Type: Integer

 ** [description](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-description"></a>
The description of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[^\p{C}]*`

 ** [enabled](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-enabled"></a>
True if the provisioning template is enabled, otherwise false.
Type: Boolean

 ** [lastModifiedDate](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-lastModifiedDate"></a>
The date when the provisioning template was last modified.
Type: Timestamp

 ** [preProvisioningHook](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-preProvisioningHook"></a>
Gets information about a pre-provisioned hook.
Type: [ProvisioningHook](API_ProvisioningHook.md) object

 ** [provisioningRoleArn](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-provisioningRoleArn"></a>
The ARN of the role associated with the provisioning template. This IoT role grants permission to provision a device.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.

 ** [templateArn](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-templateArn"></a>
The ARN of the provisioning template.
Type: String

 ** [templateBody](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-templateBody"></a>
The JSON formatted contents of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`

 ** [templateName](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-templateName"></a>
The name of the provisioning template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`

 ** [type](#API_DescribeProvisioningTemplate_ResponseSyntax) **   <a name="iot-DescribeProvisioningTemplate-response-type"></a>
The type you define in a provisioning template. You can create a template with only one type. You can't change the template type after its creation. The default value is `FLEET_PROVISIONING`. For more information about provisioning template, see: [Provisioning template](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html).
Type: String
Valid Values: `FLEET_PROVISIONING | JITP`

## Errors
<a name="API_DescribeProvisioningTemplate_Errors"></a>

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
<a name="API_DescribeProvisioningTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DescribeProvisioningTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DescribeProvisioningTemplate)

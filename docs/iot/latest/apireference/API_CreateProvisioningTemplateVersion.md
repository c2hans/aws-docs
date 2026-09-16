---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_CreateProvisioningTemplateVersion.html
---

# CreateProvisioningTemplateVersion
<a name="API_CreateProvisioningTemplateVersion"></a>

Creates a new version of a provisioning template.

Requires permission to access the [CreateProvisioningTemplateVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_CreateProvisioningTemplateVersion_RequestSyntax"></a>

```
POST /provisioning-templates/{{templateName}}/versions?setAsDefault={{setAsDefault}} HTTP/1.1
Content-type: application/json

{
   "templateBody": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateProvisioningTemplateVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [setAsDefault](#API_CreateProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-request-uri-setAsDefault"></a>
Sets a fleet provision template version as the default version.

 ** [templateName](#API_CreateProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-request-uri-templateName"></a>
The name of the provisioning template.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

## Request Body
<a name="API_CreateProvisioningTemplateVersion_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [templateBody](#API_CreateProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-request-templateBody"></a>
The JSON formatted contents of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 10240.
Pattern: `[\s\S]*`
Required: Yes

## Response Syntax
<a name="API_CreateProvisioningTemplateVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "isDefaultVersion": boolean,
   "templateArn": "string",
   "templateName": "string",
   "versionId": number
}
```

## Response Elements
<a name="API_CreateProvisioningTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [isDefaultVersion](#API_CreateProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-response-isDefaultVersion"></a>
True if the provisioning template version is the default version, otherwise false.
Type: Boolean

 ** [templateArn](#API_CreateProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-response-templateArn"></a>
The ARN that identifies the provisioning template.
Type: String

 ** [templateName](#API_CreateProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-response-templateName"></a>
The name of the provisioning template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`

 ** [versionId](#API_CreateProvisioningTemplateVersion_ResponseSyntax) **   <a name="iot-CreateProvisioningTemplateVersion-response-versionId"></a>
The version of the provisioning template.
Type: Integer

## Errors
<a name="API_CreateProvisioningTemplateVersion_Errors"></a>

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

 ** VersionsLimitExceededException **
The number of policy versions exceeds the limit.
 ** message **
The message for the exception.
HTTP Status Code: 409

## See Also
<a name="API_CreateProvisioningTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/CreateProvisioningTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/CreateProvisioningTemplateVersion)

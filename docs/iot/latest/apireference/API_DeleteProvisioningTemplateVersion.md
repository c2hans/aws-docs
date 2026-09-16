---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_DeleteProvisioningTemplateVersion.html
---

# DeleteProvisioningTemplateVersion
<a name="API_DeleteProvisioningTemplateVersion"></a>

Deletes a provisioning template version.

Requires permission to access the [DeleteProvisioningTemplateVersion](https://docs.aws.amazon.com/service-authorization/latest/reference/list_awsiot.html#awsiot-actions-as-permissions) action.

## Request Syntax
<a name="API_DeleteProvisioningTemplateVersion_RequestSyntax"></a>

```
DELETE /provisioning-templates/{{templateName}}/versions/{{versionId}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteProvisioningTemplateVersion_RequestParameters"></a>

The request uses the following URI parameters.

 ** [templateName](#API_DeleteProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-DeleteProvisioningTemplateVersion-request-uri-templateName"></a>
The name of the provisioning template version to delete.
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: Yes

 ** [versionId](#API_DeleteProvisioningTemplateVersion_RequestSyntax) **   <a name="iot-DeleteProvisioningTemplateVersion-request-uri-versionId"></a>
The provisioning template version ID to delete.
Required: Yes

## Request Body
<a name="API_DeleteProvisioningTemplateVersion_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteProvisioningTemplateVersion_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_DeleteProvisioningTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_DeleteProvisioningTemplateVersion_Errors"></a>

 ** ConflictingResourceUpdateException **
A conflicting resource update exception. This exception is thrown when two pending updates cause a conflict.
 ** message **
The message for the exception.
HTTP Status Code: 409

 ** DeleteConflictException **
You can't delete the resource because it is attached to one or more resources.
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

## See Also
<a name="API_DeleteProvisioningTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iot-2015-05-28/DeleteProvisioningTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/DeleteProvisioningTemplateVersion)

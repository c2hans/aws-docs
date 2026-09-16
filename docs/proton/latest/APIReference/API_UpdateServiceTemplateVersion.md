---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateServiceTemplateVersion.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateServiceTemplateVersion
<a name="API_UpdateServiceTemplateVersion"></a>

Update a major or minor version of a service template.

## Request Syntax
<a name="API_UpdateServiceTemplateVersion_RequestSyntax"></a>

```
{
   "compatibleEnvironmentTemplates": [
      {
         "majorVersion": "{{string}}",
         "templateName": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "majorVersion": "{{string}}",
   "minorVersion": "{{string}}",
   "status": "{{string}}",
   "supportedComponentSources": [ "{{string}}" ],
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateServiceTemplateVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [compatibleEnvironmentTemplates](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-compatibleEnvironmentTemplates"></a>
An array of environment template objects that are compatible with this service template version. A service instance based on this service template version can run in environments based on compatible templates.
Type: Array of [CompatibleEnvironmentTemplateInput](API_CompatibleEnvironmentTemplateInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** [description](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-description"></a>
A description of a service template version to update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [majorVersion](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-majorVersion"></a>
To update a major version of a service template, include `major Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [minorVersion](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-minorVersion"></a>
To update a minor version of a service template, include `minorVersion`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [status](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-status"></a>
The status of the service template minor version to update.
Type: String
Valid Values: `REGISTRATION_IN_PROGRESS | REGISTRATION_FAILED | DRAFT | PUBLISHED`
Required: No

 ** [supportedComponentSources](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-supportedComponentSources"></a>
An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.
A change to `supportedComponentSources` doesn't impact existing component attachments to instances based on this template version. A change only affects later associations.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: Array of strings
Valid Values: `DIRECTLY_DEFINED`
Required: No

 ** [templateName](#API_UpdateServiceTemplateVersion_RequestSyntax) **   <a name="proton-UpdateServiceTemplateVersion-request-templateName"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_UpdateServiceTemplateVersion_ResponseSyntax"></a>

```
{
   "serviceTemplateVersion": {
      "arn": "string",
      "compatibleEnvironmentTemplates": [
         {
            "majorVersion": "string",
            "templateName": "string"
         }
      ],
      "createdAt": number,
      "description": "string",
      "lastModifiedAt": number,
      "majorVersion": "string",
      "minorVersion": "string",
      "recommendedMinorVersion": "string",
      "schema": "string",
      "status": "string",
      "statusMessage": "string",
      "supportedComponentSources": [ "string" ],
      "templateName": "string"
   }
}
```

## Response Elements
<a name="API_UpdateServiceTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceTemplateVersion](#API_UpdateServiceTemplateVersion_ResponseSyntax) **   <a name="proton-UpdateServiceTemplateVersion-response-serviceTemplateVersion"></a>
The service template version detail data that's returned by AWS Proton.
Type: [ServiceTemplateVersion](API_ServiceTemplateVersion.md) object

## Errors
<a name="API_UpdateServiceTemplateVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
There *isn't* sufficient access for performing this action.
HTTP Status Code: 400

 ** ConflictException **
The request *couldn't* be made due to a conflicting operation or resource.
HTTP Status Code: 400

 ** InternalServerException **
The request failed to register with the service.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource *wasn't* found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_UpdateServiceTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateServiceTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateServiceTemplateVersion)

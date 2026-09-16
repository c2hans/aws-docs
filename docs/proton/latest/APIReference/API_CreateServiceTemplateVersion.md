---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_CreateServiceTemplateVersion.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# CreateServiceTemplateVersion
<a name="API_CreateServiceTemplateVersion"></a>

Create a new major or minor version of a service template. A major version of a service template is a version that *isn't* backward compatible. A minor version of a service template is a version that's backward compatible within its major version.

## Request Syntax
<a name="API_CreateServiceTemplateVersion_RequestSyntax"></a>

```
{
   "clientToken": "{{string}}",
   "compatibleEnvironmentTemplates": [
      {
         "majorVersion": "{{string}}",
         "templateName": "{{string}}"
      }
   ],
   "description": "{{string}}",
   "majorVersion": "{{string}}",
   "source": { ... },
   "supportedComponentSources": [ "{{string}}" ],
   "tags": [
      {
         "key": "{{string}}",
         "value": "{{string}}"
      }
   ],
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateServiceTemplateVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [clientToken](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-clientToken"></a>
When included, if two identical requests are made with the same client token, AWS Proton returns the service template version that the first request created.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 64.
Pattern: `[!-~]*`
Required: No

 ** [compatibleEnvironmentTemplates](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-compatibleEnvironmentTemplates"></a>
An array of environment template objects that are compatible with the new service template version. A service instance based on this service template version can run in environments based on compatible templates.
Type: Array of [CompatibleEnvironmentTemplateInput](API_CompatibleEnvironmentTemplateInput.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: Yes

 ** [description](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-description"></a>
A description of the new version of a service template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [majorVersion](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-majorVersion"></a>
To create a new minor version of the service template, include a `major Version`.
To create a new major and minor version of the service template, *exclude* `major Version`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: No

 ** [source](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-source"></a>
An object that includes the template bundle S3 bucket path and name for the new version of a service template.
Type: [TemplateVersionSourceInput](API_TemplateVersionSourceInput.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [supportedComponentSources](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-supportedComponentSources"></a>
An array of supported component sources. Components with supported sources can be attached to service instances based on this service template version.
For more information about components, see [AWS Proton components](https://docs.aws.amazon.com/proton/latest/userguide/ag-components.html) in the * AWS Proton User Guide*.
Type: Array of strings
Valid Values: `DIRECTLY_DEFINED`
Required: No

 ** [tags](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-tags"></a>
An optional list of metadata items that you can associate with the AWS Proton service template version. A tag is a key-value pair.
For more information, see [AWS Proton resources and tagging](https://docs.aws.amazon.com/proton/latest/userguide/resources.html) in the * AWS Proton User Guide*.
Type: Array of [Tag](API_Tag.md) objects
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 ** [templateName](#API_CreateServiceTemplateVersion_RequestSyntax) **   <a name="proton-CreateServiceTemplateVersion-request-templateName"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_CreateServiceTemplateVersion_ResponseSyntax"></a>

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
<a name="API_CreateServiceTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceTemplateVersion](#API_CreateServiceTemplateVersion_ResponseSyntax) **   <a name="proton-CreateServiceTemplateVersion-response-serviceTemplateVersion"></a>
The service template version summary of detail data that's returned by AWS Proton.
Type: [ServiceTemplateVersion](API_ServiceTemplateVersion.md) object

## Errors
<a name="API_CreateServiceTemplateVersion_Errors"></a>

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

 ** ServiceQuotaExceededException **
A quota was exceeded. For more information, see [AWS Proton Quotas](https://docs.aws.amazon.com/proton/latest/userguide/ag-limits.html) in the * AWS Proton User Guide*.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input is invalid or an out-of-range value was supplied for the input parameter.
HTTP Status Code: 400

## See Also
<a name="API_CreateServiceTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/CreateServiceTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/CreateServiceTemplateVersion)

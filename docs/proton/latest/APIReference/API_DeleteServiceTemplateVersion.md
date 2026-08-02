---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_DeleteServiceTemplateVersion.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# DeleteServiceTemplateVersion
<a name="API_DeleteServiceTemplateVersion"></a>

If no other minor versions of a service template exist, delete a major version of the service template if it's not the `Recommended` version. Delete the `Recommended` version of the service template if no other major versions or minor versions of the service template exist. A major version of a service template is a version that *isn't* backwards compatible.

Delete a minor version of a service template if it's not the `Recommended` version. Delete a `Recommended` minor version of the service template if no other minor versions of the service template exist. A minor version of a service template is a version that's backwards compatible.

## Request Syntax
<a name="API_DeleteServiceTemplateVersion_RequestSyntax"></a>

```
{
   "majorVersion": "{{string}}",
   "minorVersion": "{{string}}",
   "templateName": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteServiceTemplateVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [majorVersion](#API_DeleteServiceTemplateVersion_RequestSyntax) **   <a name="proton-DeleteServiceTemplateVersion-request-majorVersion"></a>
The service template major version to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [minorVersion](#API_DeleteServiceTemplateVersion_RequestSyntax) **   <a name="proton-DeleteServiceTemplateVersion-request-minorVersion"></a>
The service template minor version to delete.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 20.
Pattern: `(0|([1-9]{1}\d*))`
Required: Yes

 ** [templateName](#API_DeleteServiceTemplateVersion_RequestSyntax) **   <a name="proton-DeleteServiceTemplateVersion-request-templateName"></a>
The name of the service template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_DeleteServiceTemplateVersion_ResponseSyntax"></a>

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
<a name="API_DeleteServiceTemplateVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [serviceTemplateVersion](#API_DeleteServiceTemplateVersion_ResponseSyntax) **   <a name="proton-DeleteServiceTemplateVersion-response-serviceTemplateVersion"></a>
The detailed data of the service template version being deleted.
Type: [ServiceTemplateVersion](API_ServiceTemplateVersion.md) object

## Errors
<a name="API_DeleteServiceTemplateVersion_Errors"></a>

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
<a name="API_DeleteServiceTemplateVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/DeleteServiceTemplateVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/DeleteServiceTemplateVersion)

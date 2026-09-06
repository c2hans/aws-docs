---
source_url: https://docs.aws.amazon.com/proton/latest/APIReference/API_UpdateEnvironmentTemplate.html
---

AWS has decided to discontinue AWS Proton, with support ending on October 7, 2026. New customers will not be able to sign up after October 7, 2025, but existing customers can continue to use the service until October 7, 2026.For more information, see [AWS Proton Service Deprecation and Migration Guide](https://docs.aws.amazon.com/proton/latest/userguide/proton-end-of-support.html).

# UpdateEnvironmentTemplate
<a name="API_UpdateEnvironmentTemplate"></a>

Update an environment template.

## Request Syntax
<a name="API_UpdateEnvironmentTemplate_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "displayName": "{{string}}",
   "name": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateEnvironmentTemplate_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_UpdateEnvironmentTemplate_RequestSyntax) **   <a name="proton-UpdateEnvironmentTemplate-request-description"></a>
A description of the environment template update.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Required: No

 ** [displayName](#API_UpdateEnvironmentTemplate_RequestSyntax) **   <a name="proton-UpdateEnvironmentTemplate-request-displayName"></a>
The name of the environment template to update as displayed in the developer interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** [name](#API_UpdateEnvironmentTemplate_RequestSyntax) **   <a name="proton-UpdateEnvironmentTemplate-request-name"></a>
The name of the environment template to update.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `[0-9A-Za-z]+[0-9A-Za-z_\-]*`
Required: Yes

## Response Syntax
<a name="API_UpdateEnvironmentTemplate_ResponseSyntax"></a>

```
{
   "environmentTemplate": {
      "arn": "string",
      "createdAt": number,
      "description": "string",
      "displayName": "string",
      "encryptionKey": "string",
      "lastModifiedAt": number,
      "name": "string",
      "provisioning": "string",
      "recommendedVersion": "string"
   }
}
```

## Response Elements
<a name="API_UpdateEnvironmentTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [environmentTemplate](#API_UpdateEnvironmentTemplate_ResponseSyntax) **   <a name="proton-UpdateEnvironmentTemplate-response-environmentTemplate"></a>
The environment template detail data that's returned by AWS Proton.
Type: [EnvironmentTemplate](API_EnvironmentTemplate.md) object

## Errors
<a name="API_UpdateEnvironmentTemplate_Errors"></a>

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
<a name="API_UpdateEnvironmentTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/proton-2020-07-20/UpdateEnvironmentTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/proton-2020-07-20/UpdateEnvironmentTemplate)

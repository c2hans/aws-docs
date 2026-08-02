---
source_url: https://docs.aws.amazon.com/panorama/latest/api/API_CreateApplicationInstance.html
---

# CreateApplicationInstance
<a name="API_CreateApplicationInstance"></a>

**Important**
End of support notice: On May 31, 2026, AWS will end support for AWS Panorama. After May 31, 2026, you will no longer be able to access the AWS Panorama console or AWS Panorama resources. For more information, see [AWS Panorama end of support](https://docs.aws.amazon.com/panorama/latest/dev/panorama-end-of-support.html).

Creates an application instance and deploys it to a device.

## Request Syntax
<a name="API_CreateApplicationInstance_RequestSyntax"></a>

```
POST /application-instances HTTP/1.1
Content-type: application/json

{
   "ApplicationInstanceIdToReplace": "{{string}}",
   "DefaultRuntimeContextDevice": "{{string}}",
   "Description": "{{string}}",
   "ManifestOverridesPayload": { ... },
   "ManifestPayload": { ... },
   "Name": "{{string}}",
   "RuntimeRoleArn": "{{string}}",
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_CreateApplicationInstance_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateApplicationInstance_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ApplicationInstanceIdToReplace](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-ApplicationInstanceIdToReplace"></a>
The ID of an application instance to replace with the new instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** [DefaultRuntimeContextDevice](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-DefaultRuntimeContextDevice"></a>
A device's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: Yes

 ** [Description](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-Description"></a>
A description for the application instance.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `.*`
Required: No

 ** [ManifestOverridesPayload](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-ManifestOverridesPayload"></a>
Setting overrides for the application manifest.
Type: [ManifestOverridesPayload](API_ManifestOverridesPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** [ManifestPayload](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-ManifestPayload"></a>
The application's manifest document.
Type: [ManifestPayload](API_ManifestPayload.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: Yes

 ** [Name](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-Name"></a>
A name for the application instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`
Required: No

 ** [RuntimeRoleArn](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-RuntimeRoleArn"></a>
The ARN of a runtime role for the application instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `arn:[a-z0-9][-.a-z0-9]{0,62}:iam::[0-9]{12}:role/.+`
Required: No

 ** [Tags](#API_CreateApplicationInstance_RequestSyntax) **   <a name="panorama-CreateApplicationInstance-request-Tags"></a>
Tags for the application instance.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `.+`
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Value Pattern: `.*`
Required: No

## Response Syntax
<a name="API_CreateApplicationInstance_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApplicationInstanceId": "string"
}
```

## Response Elements
<a name="API_CreateApplicationInstance_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApplicationInstanceId](#API_CreateApplicationInstance_ResponseSyntax) **   <a name="panorama-CreateApplicationInstance-response-ApplicationInstanceId"></a>
The application instance's ID.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z0-9\-\_]+`

## Errors
<a name="API_CreateApplicationInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The requestor does not have permission to access the target action or resource.
HTTP Status Code: 403

 ** InternalServerException **
An internal error occurred.
 ** RetryAfterSeconds **
The number of seconds a client should wait before retrying the call.
HTTP Status Code: 500

 ** ServiceQuotaExceededException **
The request would cause a limit to be exceeded.
 ** QuotaCode **
The name of the limit.
 ** ResourceId **
The target resource's ID.
 ** ResourceType **
The target resource's type.
 ** ServiceCode **
The name of the service.
HTTP Status Code: 402

 ** ValidationException **
The request contains an invalid parameter value.
 ** ErrorArguments **
A list of attributes that led to the exception and their values.
 ** ErrorId **
A unique ID for the error.
 ** Fields **
A list of request parameters that failed validation.
 ** Reason **
The reason that validation failed.
HTTP Status Code: 400

## See Also
<a name="API_CreateApplicationInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/panorama-2019-07-24/CreateApplicationInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/panorama-2019-07-24/CreateApplicationInstance)

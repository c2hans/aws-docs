---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_CreateInstanceProfile.html
---

# CreateInstanceProfile
<a name="API_CreateInstanceProfile"></a>

Creates a profile that can be applied to one or more private fleet device instances.

## Request Syntax
<a name="API_CreateInstanceProfile_RequestSyntax"></a>

```
{
   "description": "{{string}}",
   "excludeAppPackagesFromCleanup": [ "{{string}}" ],
   "name": "{{string}}",
   "packageCleanup": {{boolean}},
   "rebootAfterUse": {{boolean}}
}
```

## Request Parameters
<a name="API_CreateInstanceProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [description](#API_CreateInstanceProfile_RequestSyntax) **   <a name="devicefarm-CreateInstanceProfile-request-description"></a>
The description of your instance profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** [excludeAppPackagesFromCleanup](#API_CreateInstanceProfile_RequestSyntax) **   <a name="devicefarm-CreateInstanceProfile-request-excludeAppPackagesFromCleanup"></a>
An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run.
The list of packages is considered only if you set `packageCleanup` to `true`.
Type: Array of strings
Required: No

 ** [name](#API_CreateInstanceProfile_RequestSyntax) **   <a name="devicefarm-CreateInstanceProfile-request-name"></a>
The name of your instance profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: Yes

 ** [packageCleanup](#API_CreateInstanceProfile_RequestSyntax) **   <a name="devicefarm-CreateInstanceProfile-request-packageCleanup"></a>
When set to `true`, Device Farm removes app packages after a test run. The default value is `false` for private devices.
Type: Boolean
Required: No

 ** [rebootAfterUse](#API_CreateInstanceProfile_RequestSyntax) **   <a name="devicefarm-CreateInstanceProfile-request-rebootAfterUse"></a>
When set to `true`, Device Farm reboots the instance after a test run. The default value is `true`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_CreateInstanceProfile_ResponseSyntax"></a>

```
{
   "instanceProfile": {
      "arn": "string",
      "description": "string",
      "excludeAppPackagesFromCleanup": [ "string" ],
      "name": "string",
      "packageCleanup": boolean,
      "rebootAfterUse": boolean
   }
}
```

## Response Elements
<a name="API_CreateInstanceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceProfile](#API_CreateInstanceProfile_ResponseSyntax) **   <a name="devicefarm-CreateInstanceProfile-response-instanceProfile"></a>
An object that contains information about your instance profile.
Type: [InstanceProfile](API_InstanceProfile.md) object

## Errors
<a name="API_CreateInstanceProfile_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ArgumentException **
An invalid argument was specified.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** LimitExceededException **
A limit was exceeded.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** NotFoundException **
The specified entity was not found.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

 ** ServiceAccountException **
There was a problem with the service account.
 ** message **
Any additional information about the exception.
HTTP Status Code: 400

## See Also
<a name="API_CreateInstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/CreateInstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/CreateInstanceProfile)

---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_UpdateInstanceProfile.html
---

# UpdateInstanceProfile
<a name="API_UpdateInstanceProfile"></a>

Updates information about an existing private device instance profile.

## Request Syntax
<a name="API_UpdateInstanceProfile_RequestSyntax"></a>

```
{
   "arn": "{{string}}",
   "description": "{{string}}",
   "excludeAppPackagesFromCleanup": [ "{{string}}" ],
   "name": "{{string}}",
   "packageCleanup": {{boolean}},
   "rebootAfterUse": {{boolean}}
}
```

## Request Parameters
<a name="API_UpdateInstanceProfile_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [arn](#API_UpdateInstanceProfile_RequestSyntax) **   <a name="devicefarm-UpdateInstanceProfile-request-arn"></a>
The Amazon Resource Name (ARN) of the instance profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: Yes

 ** [description](#API_UpdateInstanceProfile_RequestSyntax) **   <a name="devicefarm-UpdateInstanceProfile-request-description"></a>
The updated description for your instance profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** [excludeAppPackagesFromCleanup](#API_UpdateInstanceProfile_RequestSyntax) **   <a name="devicefarm-UpdateInstanceProfile-request-excludeAppPackagesFromCleanup"></a>
An array of strings that specifies the list of app packages that should not be cleaned up from the device after a test run is over.
The list of packages is only considered if you set `packageCleanup` to `true`.
Type: Array of strings
Required: No

 ** [name](#API_UpdateInstanceProfile_RequestSyntax) **   <a name="devicefarm-UpdateInstanceProfile-request-name"></a>
The updated name for your instance profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [packageCleanup](#API_UpdateInstanceProfile_RequestSyntax) **   <a name="devicefarm-UpdateInstanceProfile-request-packageCleanup"></a>
The updated choice for whether you want to specify package cleanup. The default value is `false` for private devices.
Type: Boolean
Required: No

 ** [rebootAfterUse](#API_UpdateInstanceProfile_RequestSyntax) **   <a name="devicefarm-UpdateInstanceProfile-request-rebootAfterUse"></a>
The updated choice for whether you want to reboot the device after use. The default value is `true`.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateInstanceProfile_ResponseSyntax"></a>

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
<a name="API_UpdateInstanceProfile_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [instanceProfile](#API_UpdateInstanceProfile_ResponseSyntax) **   <a name="devicefarm-UpdateInstanceProfile-response-instanceProfile"></a>
An object that contains information about your instance profile.
Type: [InstanceProfile](API_InstanceProfile.md) object

## Errors
<a name="API_UpdateInstanceProfile_Errors"></a>

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
<a name="API_UpdateInstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/devicefarm-2015-06-23/UpdateInstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/UpdateInstanceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

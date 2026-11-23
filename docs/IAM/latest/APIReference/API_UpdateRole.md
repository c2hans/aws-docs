---
source_url: https://docs.aws.amazon.com/IAM/latest/APIReference/API_UpdateRole.html
---

# UpdateRole

Updates the description, maximum session duration, or maximum sign-in session duration of a role. You cannot change the maximum sign-in session duration of a service-linked role.

## Request Parameters
<a name="API_UpdateRole_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** Description **
The new description that you want to apply to the specified role.
Type: String
Length Constraints: Maximum length of 1000.
Pattern: `[\u0009\u000A\u000D\u0020-\u007E\u00A1-\u00FF]*`
Required: No

 ** MaxSessionDuration **
The maximum session duration (in seconds) that you want to set for the specified role. If you do not specify a value for this setting, the default value of one hour is applied. This setting can have a value from 1 hour to 12 hours.
Anyone who assumes the role from the AWS CLI or API can use the `DurationSeconds` API parameter or the `duration-seconds` AWS CLI parameter to request a longer session. The `MaxSessionDuration` setting determines the maximum duration that can be requested using the `DurationSeconds` parameter. If users don't specify a value for the `DurationSeconds` parameter, their security credentials are valid for one hour by default. This applies when you use the `AssumeRole*` API operations or the `assume-role*` AWS CLI operations but does not apply when you use those operations to create a console URL. For more information, see [Using IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_use.html) in the *IAM User Guide*.
IAM role credentials provided by Amazon EC2 instances assigned to the role are not subject to the specified maximum session duration.
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 43200.
Required: No

 ** MaxSigninSessionDuration **
The maximum AWS Sign-In duration (in seconds) for users who authenticate with the specified role through OAuth-based flows (`signin:CreateOAuth2Token`), such as the AWS CLI (`aws login`), AWS SDKs, and MCP clients. This setting does not affect AWS Management Console browser sessions or traditional STS sessions. This setting can have a value from 1 hour (3600 seconds) to 90 days (7776000 seconds), inclusive, and overrides any value currently configured for the role. This setting is independent of `MaxSessionDuration`. If this parameter is not set, the default session duration equals the role's `MaxSessionDuration`.
If you omit both this parameter and `ResetMaxSigninSessionDuration`, the current setting is unchanged. You cannot specify this parameter and set `ResetMaxSigninSessionDuration` to `true` in the same request.
Changes to this setting apply to new sign-in sessions. Sessions that are already established are not affected.
You cannot set this value on a service-linked role.
Type: Integer
Valid Range: Minimum value of 3600. Maximum value of 7776000.
Required: No

 ** ResetMaxSigninSessionDuration **
Specifies whether to clear the role's maximum sign-in session duration. Set this value to `true` to return the setting to its unset state, so that the existing sign-in session behavior applies.
If you set this value to `false` or omit it, the current setting is not cleared. You cannot set this value to `true` and specify `MaxSigninSessionDuration` in the same request. Clearing a setting that is already unset has no effect.
You cannot reset this value on a service-linked role.
Type: Boolean
Required: No

 ** RoleName **
The name of the role that you want to modify.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[\w+=,.@-]+`
Required: Yes

## Errors
<a name="API_UpdateRole_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidInput **
The request was rejected because an invalid or out-of-range value was supplied for an input parameter.
HTTP Status Code: 400

 ** NoSuchEntity **
The request was rejected because it referenced a resource entity that does not exist. The error message describes the resource.
HTTP Status Code: 404

 ** ServiceFailure **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** UnmodifiableEntity **
The request was rejected because service-linked roles are protected AWS resources. Only the service that depends on the service-linked role can modify or delete the role on your behalf. The error message includes the name of the service that depends on this service-linked role. You must request the change through that service.
HTTP Status Code: 400

## See Also
<a name="API_UpdateRole_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/iam-2010-05-08/UpdateRole)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/iam-2010-05-08/UpdateRole)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iam-2010-05-08/UpdateRole)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/iam-2010-05-08/UpdateRole)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iam-2010-05-08/UpdateRole)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/iam-2010-05-08/UpdateRole)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/iam-2010-05-08/UpdateRole)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/iam-2010-05-08/UpdateRole)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/iam-2010-05-08/UpdateRole)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iam-2010-05-08/UpdateRole)

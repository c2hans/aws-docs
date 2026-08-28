---
source_url: https://docs.aws.amazon.com/devicefarm/latest/APIReference/API_InstanceProfile.html
---

# InstanceProfile
<a name="API_InstanceProfile"></a>

Represents the instance profile.

## Contents
<a name="API_InstanceProfile_Contents"></a>

 ** arn **   <a name="devicefarm-Type-InstanceProfile-arn"></a>
The Amazon Resource Name (ARN) of the instance profile.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 1011.
Pattern: `^arn:aws:devicefarm:.+`
Required: No

 ** description **   <a name="devicefarm-Type-InstanceProfile-description"></a>
The description of the instance profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 16384.
Required: No

 ** excludeAppPackagesFromCleanup **   <a name="devicefarm-Type-InstanceProfile-excludeAppPackagesFromCleanup"></a>
An array of strings containing the list of app packages that should not be cleaned up from the device after a test run completes.
The list of packages is considered only if you set `packageCleanup` to `true`.
Type: Array of strings
Required: No

 ** name **   <a name="devicefarm-Type-InstanceProfile-name"></a>
The name of the instance profile.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** packageCleanup **   <a name="devicefarm-Type-InstanceProfile-packageCleanup"></a>
When set to `true`, Device Farm removes app packages after a test run. The default value is `false` for private devices.
Type: Boolean
Required: No

 ** rebootAfterUse **   <a name="devicefarm-Type-InstanceProfile-rebootAfterUse"></a>
When set to `true`, Device Farm reboots the instance after a test run. The default value is `true`.
Type: Boolean
Required: No

## See Also
<a name="API_InstanceProfile_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/devicefarm-2015-06-23/InstanceProfile)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/devicefarm-2015-06-23/InstanceProfile)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/devicefarm-2015-06-23/InstanceProfile)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Device Farm Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query devicefarm` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

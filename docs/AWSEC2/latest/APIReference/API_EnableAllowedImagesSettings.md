---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableAllowedImagesSettings.html
---

# EnableAllowedImagesSettings
<a name="API_EnableAllowedImagesSettings"></a>

Enables Allowed AMIs for your account in the specified AWS Region. Two values are accepted:
+  `enabled`: The image criteria in your Allowed AMIs settings are applied. As a result, only AMIs matching these criteria are discoverable and can be used by your account to launch instances.
+  `audit-mode`: The image criteria in your Allowed AMIs settings are not applied. No restrictions are placed on AMI discoverability or usage. Users in your account can launch instances using any public AMI or AMI shared with your account.

  The purpose of `audit-mode` is to indicate which AMIs will be affected when Allowed AMIs is `enabled`. In `audit-mode`, each AMI displays either `"ImageAllowed": true` or `"ImageAllowed": false` to indicate whether the AMI will be discoverable and available to users in the account when Allowed AMIs is enabled.

**Note**
The Allowed AMIs feature does not restrict the AMIs owned by your account. Regardless of the criteria you set, the AMIs created by your account will always be discoverable and usable by users in your account.

For more information, see [Control the discovery and use of AMIs in Amazon EC2 with Allowed AMIs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-allowed-amis.html) in *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_EnableAllowedImagesSettings_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllowedImagesSettingsState**
Specify `enabled` to apply the image criteria specified by the Allowed AMIs settings. Specify `audit-mode` so that you can check which AMIs will be allowed or not allowed by the image criteria.
Type: String
Valid Values: `enabled | audit-mode`
Required: Yes

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

## Response Elements
<a name="API_EnableAllowedImagesSettings_ResponseElements"></a>

The following elements are returned by the service.

 **allowedImagesSettingsState**
Returns `enabled` or `audit-mode` if the request succeeds; otherwise, it returns an error.
Type: String
Valid Values: `enabled | audit-mode`

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_EnableAllowedImagesSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_EnableAllowedImagesSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableAllowedImagesSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableAllowedImagesSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

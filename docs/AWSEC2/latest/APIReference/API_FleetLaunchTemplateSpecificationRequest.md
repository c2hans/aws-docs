---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_FleetLaunchTemplateSpecificationRequest.html
---

# FleetLaunchTemplateSpecificationRequest
<a name="API_FleetLaunchTemplateSpecificationRequest"></a>

The Amazon EC2 launch template that can be used by an EC2 Fleet to configure Amazon EC2 instances. You must specify either the ID or name of the launch template in the request, but not both.

For information about launch templates, see [Launch an instance from a launch template](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html) in the *Amazon EC2 User Guide*.

## Contents
<a name="API_FleetLaunchTemplateSpecificationRequest_Contents"></a>

 ** LaunchTemplateId **
The ID of the launch template.
You must specify the `LaunchTemplateId` or the `LaunchTemplateName`, but not both.
Type: String
Required: No

 ** LaunchTemplateName **
The name of the launch template.
You must specify the `LaunchTemplateName` or the `LaunchTemplateId`, but not both.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 128.
Pattern: `[a-zA-Z0-9\(\)\.\-/_]+`
Required: No

 ** LaunchTemplateSpecificationUserData **
The base64-encoded user data for instances launched by the fleet. User data is limited to 16 KB, in raw form, before it is base64-encoded.
Supported only for fleets of type `instant`.
Type: String
Required: No

 ** Version **
The launch template version number, `$Latest`, or `$Default`. You must specify a value, otherwise the request fails.
If the value is `$Latest`, Amazon EC2 uses the latest version of the launch template.
If the value is `$Default`, Amazon EC2 uses the default version of the launch template.
Type: String
Required: No

## See Also
<a name="API_FleetLaunchTemplateSpecificationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/FleetLaunchTemplateSpecificationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/FleetLaunchTemplateSpecificationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/FleetLaunchTemplateSpecificationRequest)

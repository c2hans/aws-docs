---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_Ec2LaunchTemplate.html
---

# Ec2LaunchTemplate
<a name="API_Ec2LaunchTemplate"></a>

Contains information about the Amazon EC2 launch template involved in a GuardDuty finding, including unique identifiers of the Amazon EC2 instances.

## Contents
<a name="API_Ec2LaunchTemplate_Contents"></a>

 ** ec2InstanceUids **   <a name="guardduty-Type-Ec2LaunchTemplate-ec2InstanceUids"></a>
A list of unique identifiers for the compromised Amazon EC2 instances that share the same Amazon EC2 launch template.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** version **   <a name="guardduty-Type-Ec2LaunchTemplate-version"></a>
Version of the EC2 launch template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Ec2LaunchTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/Ec2LaunchTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/Ec2LaunchTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/Ec2LaunchTemplate)

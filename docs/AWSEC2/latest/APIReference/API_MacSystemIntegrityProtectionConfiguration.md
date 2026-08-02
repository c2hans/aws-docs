---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MacSystemIntegrityProtectionConfiguration.html
---

# MacSystemIntegrityProtectionConfiguration
<a name="API_MacSystemIntegrityProtectionConfiguration"></a>

Describes the configuration for a System Integrity Protection (SIP) modification task.

## Contents
<a name="API_MacSystemIntegrityProtectionConfiguration_Contents"></a>

 ** appleInternal **
Indicates whether Apple Internal was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** baseSystem **
Indicates whether Base System was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** debuggingRestrictions **
Indicates whether Debugging Restrictions was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** dTraceRestrictions **
Indicates whether Dtrace Restrictions was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** filesystemProtections **
Indicates whether Filesystem Protections was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** kextSigning **
Indicates whether Kext Signing was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** nvramProtections **
Indicates whether NVRAM Protections was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** status **
Indicates SIP was enabled or disabled by the task.
Type: String
Valid Values: `enabled | disabled`
Required: No

## See Also
<a name="API_MacSystemIntegrityProtectionConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MacSystemIntegrityProtectionConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MacSystemIntegrityProtectionConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MacSystemIntegrityProtectionConfiguration)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MacSystemIntegrityProtectionConfigurationRequest.html
---

# MacSystemIntegrityProtectionConfigurationRequest
<a name="API_MacSystemIntegrityProtectionConfigurationRequest"></a>

Describes a custom configuration for a System Integrity Protection (SIP) modification task.

## Contents
<a name="API_MacSystemIntegrityProtectionConfigurationRequest_Contents"></a>

 ** AppleInternal **
Enables or disables Apple Internal.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** BaseSystem **
Enables or disables Base System.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** DebuggingRestrictions **
Enables or disables Debugging Restrictions.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** DTraceRestrictions **
Enables or disables Dtrace Restrictions.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** FilesystemProtections **
Enables or disables Filesystem Protections.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** KextSigning **
Enables or disables Kext Signing.
Type: String
Valid Values: `enabled | disabled`
Required: No

 ** NvramProtections **
Enables or disables Nvram Protections.
Type: String
Valid Values: `enabled | disabled`
Required: No

## See Also
<a name="API_MacSystemIntegrityProtectionConfigurationRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/MacSystemIntegrityProtectionConfigurationRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/MacSystemIntegrityProtectionConfigurationRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/MacSystemIntegrityProtectionConfigurationRequest)

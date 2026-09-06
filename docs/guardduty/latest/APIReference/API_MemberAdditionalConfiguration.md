---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_MemberAdditionalConfiguration.html
---

# MemberAdditionalConfiguration
<a name="API_MemberAdditionalConfiguration"></a>

Information about the additional configuration for the member account.

## Contents
<a name="API_MemberAdditionalConfiguration_Contents"></a>

 ** name **   <a name="guardduty-Type-MemberAdditionalConfiguration-name"></a>
Name of the additional configuration.
Type: String
Valid Values: `EKS_ADDON_MANAGEMENT | ECS_FARGATE_AGENT_MANAGEMENT | EC2_AGENT_MANAGEMENT`
Required: No

 ** status **   <a name="guardduty-Type-MemberAdditionalConfiguration-status"></a>
Status of the additional configuration.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_MemberAdditionalConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/MemberAdditionalConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/MemberAdditionalConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/MemberAdditionalConfiguration)

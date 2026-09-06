---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_ComplianceByConfigRule.html
---

# ComplianceByConfigRule
<a name="API_ComplianceByConfigRule"></a>

Indicates whether an AWS Config rule is compliant. A rule is compliant if all of the resources that the rule evaluated comply with it. A rule is noncompliant if any of these resources do not comply.

## Contents
<a name="API_ComplianceByConfigRule_Contents"></a>

 ** Compliance **   <a name="config-Type-ComplianceByConfigRule-Compliance"></a>
Indicates whether the AWS Config rule is compliant.
Type: [Compliance](API_Compliance.md) object
Required: No

 ** ConfigRuleName **   <a name="config-Type-ComplianceByConfigRule-ConfigRuleName"></a>
The name of the AWS Config rule.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_ComplianceByConfigRule_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/ComplianceByConfigRule)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/ComplianceByConfigRule)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/ComplianceByConfigRule)

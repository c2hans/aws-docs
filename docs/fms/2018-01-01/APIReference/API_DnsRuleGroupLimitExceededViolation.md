---
source_url: https://docs.aws.amazon.com/fms/2018-01-01/APIReference/API_DnsRuleGroupLimitExceededViolation.html
---

# DnsRuleGroupLimitExceededViolation
<a name="API_DnsRuleGroupLimitExceededViolation"></a>

The VPC that Firewall Manager was applying a DNS Fireall policy to reached the limit for associated DNS Firewall rule groups. Firewall Manager tried to associate another rule group with the VPC and failed due to the limit.

## Contents
<a name="API_DnsRuleGroupLimitExceededViolation_Contents"></a>

 ** NumberOfRuleGroupsAlreadyAssociated **   <a name="fms-Type-DnsRuleGroupLimitExceededViolation-NumberOfRuleGroupsAlreadyAssociated"></a>
The number of rule groups currently associated with the VPC.
Type: Integer
Valid Range: Minimum value of -2147483648. Maximum value of 2147483647.
Required: No

 ** ViolationTarget **   <a name="fms-Type-DnsRuleGroupLimitExceededViolation-ViolationTarget"></a>
Information about the VPC ID.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `.*`
Required: No

 ** ViolationTargetDescription **   <a name="fms-Type-DnsRuleGroupLimitExceededViolation-ViolationTargetDescription"></a>
A description of the violation that specifies the rule group and VPC.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Required: No

## See Also
<a name="API_DnsRuleGroupLimitExceededViolation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/fms-2018-01-01/DnsRuleGroupLimitExceededViolation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/fms-2018-01-01/DnsRuleGroupLimitExceededViolation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/fms-2018-01-01/DnsRuleGroupLimitExceededViolation)

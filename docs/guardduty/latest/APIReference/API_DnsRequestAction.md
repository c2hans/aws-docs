---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DnsRequestAction.html
---

# DnsRequestAction
<a name="API_DnsRequestAction"></a>

Contains information about the DNS\_REQUEST action described in this finding.

## Contents
<a name="API_DnsRequestAction_Contents"></a>

 ** blocked **   <a name="guardduty-Type-DnsRequestAction-blocked"></a>
Indicates whether the targeted port is blocked.
Type: Boolean
Required: No

 ** domain **   <a name="guardduty-Type-DnsRequestAction-domain"></a>
The domain information for the DNS query.
Type: String
Required: No

 ** domainWithSuffix **   <a name="guardduty-Type-DnsRequestAction-domainWithSuffix"></a>
The second and top level domain involved in the activity that potentially prompted GuardDuty to generate this finding. For a list of top-level and second-level domains, see [public suffix list](https://publicsuffix.org/).
Type: String
Required: No

 ** protocol **   <a name="guardduty-Type-DnsRequestAction-protocol"></a>
The network connection protocol observed in the activity that prompted GuardDuty to generate the finding.
Type: String
Required: No

 ** vpcOwnerAccountId **   <a name="guardduty-Type-DnsRequestAction-vpcOwnerAccountId"></a>
The AWS account ID that owns the VPC through which the DNS request was made.
Type: String
Length Constraints: Fixed length of 12.
Required: No

## See Also
<a name="API_DnsRequestAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DnsRequestAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DnsRequestAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DnsRequestAction)

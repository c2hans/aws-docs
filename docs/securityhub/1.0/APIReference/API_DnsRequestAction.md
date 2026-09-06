---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DnsRequestAction.html
---

# DnsRequestAction
<a name="API_DnsRequestAction"></a>

Provided if `ActionType` is `DNS_REQUEST`. It provides details about the DNS request that was detected.

## Contents
<a name="API_DnsRequestAction_Contents"></a>

 ** Blocked **   <a name="securityhub-Type-DnsRequestAction-Blocked"></a>
Indicates whether the DNS request was blocked.
Type: Boolean
Required: No

 ** Domain **   <a name="securityhub-Type-DnsRequestAction-Domain"></a>
The DNS domain that is associated with the DNS request.
Length Constraints: 128.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Protocol **   <a name="securityhub-Type-DnsRequestAction-Protocol"></a>
The protocol that was used for the DNS request.
Length Constraints: Minimum length of 1. Maximum length of 64.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_DnsRequestAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DnsRequestAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DnsRequestAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DnsRequestAction)

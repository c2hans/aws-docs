---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_ThreatIntelIndicator.html
---

# ThreatIntelIndicator
<a name="API_ThreatIntelIndicator"></a>

Details about the threat intelligence related to a finding.

## Contents
<a name="API_ThreatIntelIndicator_Contents"></a>

 ** Category **   <a name="securityhub-Type-ThreatIntelIndicator-Category"></a>
The category of a threat intelligence indicator.
Type: String
Valid Values: `BACKDOOR | CARD_STEALER | COMMAND_AND_CONTROL | DROP_SITE | EXPLOIT_SITE | KEYLOGGER`
Required: No

 ** LastObservedAt **   <a name="securityhub-Type-ThreatIntelIndicator-LastObservedAt"></a>
Indicates when the most recent instance of a threat intelligence indicator was observed.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** Source **   <a name="securityhub-Type-ThreatIntelIndicator-Source"></a>
The source of the threat intelligence indicator.
Length Constraints: Minimum of 1 length. Maximum of 64 length.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceUrl **   <a name="securityhub-Type-ThreatIntelIndicator-SourceUrl"></a>
The URL to the page or site where you can get more information about the threat intelligence indicator.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Type **   <a name="securityhub-Type-ThreatIntelIndicator-Type"></a>
The type of threat intelligence indicator.
Type: String
Valid Values: `DOMAIN | EMAIL_ADDRESS | HASH_MD5 | HASH_SHA1 | HASH_SHA256 | HASH_SHA512 | IPV4_ADDRESS | IPV6_ADDRESS | MUTEX | PROCESS | URL`
Required: No

 ** Value **   <a name="securityhub-Type-ThreatIntelIndicator-Value"></a>
The value of a threat intelligence indicator.
Length Constraints: Minimum of 1 length. Maximum of 512 length.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_ThreatIntelIndicator_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/ThreatIntelIndicator)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/ThreatIntelIndicator)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/ThreatIntelIndicator)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AnalysisPacketHeader.html
---

# AnalysisPacketHeader
<a name="API_AnalysisPacketHeader"></a>

Describes a header. Reflects any changes made by a component as traffic passes through. The fields of an inbound header are null except for the first component of a path.

## Contents
<a name="API_AnalysisPacketHeader_Contents"></a>

 ** DestinationAddressSet.N **
The destination addresses.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** DestinationPortRangeSet.N **
The destination port ranges.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

 ** protocol **
The protocol.
Type: String
Required: No

 ** SourceAddressSet.N **
The source addresses.
Type: Array of strings
Length Constraints: Minimum length of 0. Maximum length of 15.
Pattern: `^([0-9]{1,3}.){3}[0-9]{1,3}$`
Required: No

 ** SourcePortRangeSet.N **
The source port ranges.
Type: Array of [PortRange](API_PortRange.md) objects
Required: No

## See Also
<a name="API_AnalysisPacketHeader_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AnalysisPacketHeader)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AnalysisPacketHeader)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AnalysisPacketHeader)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

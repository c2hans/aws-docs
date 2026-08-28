---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_AsnAssociation.html
---

# AsnAssociation
<a name="API_AsnAssociation"></a>

An Autonomous System Number (ASN) and BYOIP CIDR association.

## Contents
<a name="API_AsnAssociation_Contents"></a>

 ** asn **
The association's ASN.
Type: String
Required: No

 ** cidr **
The association's CIDR.
Type: String
Required: No

 ** state **
The association's state.
Type: String
Valid Values: `disassociated | failed-disassociation | failed-association | pending-disassociation | pending-association | associated`
Required: No

 ** statusMessage **
The association's status message.
Type: String
Required: No

## See Also
<a name="API_AsnAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/AsnAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/AsnAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/AsnAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

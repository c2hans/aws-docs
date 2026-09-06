---
source_url: https://docs.aws.amazon.com/networkmanager/latest/APIReference/API_ProposedSegmentChange.html
---

# ProposedSegmentChange
<a name="API_ProposedSegmentChange"></a>

Describes a proposed segment change. In some cases, the segment change must first be evaluated and accepted.

## Contents
<a name="API_ProposedSegmentChange_Contents"></a>

 ** AttachmentPolicyRuleNumber **   <a name="networkmanager-Type-ProposedSegmentChange-AttachmentPolicyRuleNumber"></a>
The rule number in the policy document that applies to this change.
Type: Integer
Required: No

 ** SegmentName **   <a name="networkmanager-Type-ProposedSegmentChange-SegmentName"></a>
The name of the segment to change.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[\s\S]*`
Required: No

 ** Tags **   <a name="networkmanager-Type-ProposedSegmentChange-Tags"></a>
The list of key-value tags that changed for the segment.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## See Also
<a name="API_ProposedSegmentChange_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/networkmanager-2019-07-05/ProposedSegmentChange)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/networkmanager-2019-07-05/ProposedSegmentChange)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/networkmanager-2019-07-05/ProposedSegmentChange)

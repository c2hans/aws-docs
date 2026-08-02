---
source_url: https://docs.aws.amazon.com/AmazonSynthetics/latest/APIReference/API_GroupSummary.html
---

# GroupSummary
<a name="API_GroupSummary"></a>

A structure containing some information about a group.

## Contents
<a name="API_GroupSummary_Contents"></a>

 ** Arn **   <a name="synthetics-Type-GroupSummary-Arn"></a>
The ARN of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `arn:(aws[a-zA-Z-]*)?:synthetics:[a-z]{2,4}(-[a-z]{2,4})?-[a-z]+-\d{1}:\d{12}:group:[0-9a-z]+`
Required: No

 ** Id **   <a name="synthetics-Type-GroupSummary-Id"></a>
The unique ID of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** Name **   <a name="synthetics-Type-GroupSummary-Name"></a>
The name of the group.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## See Also
<a name="API_GroupSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/synthetics-2017-10-11/GroupSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/synthetics-2017-10-11/GroupSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/synthetics-2017-10-11/GroupSummary)

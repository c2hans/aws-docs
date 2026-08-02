---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_LensShareSummary.html
---

# LensShareSummary
<a name="API_LensShareSummary"></a>

A lens share summary return object.

## Contents
<a name="API_LensShareSummary_Contents"></a>

 ** SharedWith **   <a name="wellarchitected-Type-LensShareSummary-SharedWith"></a>
The AWS account ID, organization ID, or organizational unit (OU) ID with which the workload, lens, profile, or review template is shared.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 2048.
Required: No

 ** ShareId **   <a name="wellarchitected-Type-LensShareSummary-ShareId"></a>
The ID associated with the share.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Status **   <a name="wellarchitected-Type-LensShareSummary-Status"></a>
The status of the share request.
Type: String
Valid Values: `ACCEPTED | REJECTED | PENDING | REVOKED | EXPIRED | ASSOCIATING | ASSOCIATED | FAILED`
Required: No

 ** StatusMessage **   <a name="wellarchitected-Type-LensShareSummary-StatusMessage"></a>
Optional message to compliment the Status field.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Required: No

## See Also
<a name="API_LensShareSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/LensShareSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/LensShareSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/LensShareSummary)

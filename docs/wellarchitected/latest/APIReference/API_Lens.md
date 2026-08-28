---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/APIReference/API_Lens.html
---

# Lens
<a name="API_Lens"></a>

A lens return object.

## Contents
<a name="API_Lens_Contents"></a>

 ** Description **   <a name="wellarchitected-Type-Lens-Description"></a>
The description of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

 ** LensArn **   <a name="wellarchitected-Type-Lens-LensArn"></a>
The ARN of a lens.
Type: String
Required: No

 ** LensVersion **   <a name="wellarchitected-Type-Lens-LensVersion"></a>
The version of a lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Required: No

 ** Name **   <a name="wellarchitected-Type-Lens-Name"></a>
The full name of the lens.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** Owner **   <a name="wellarchitected-Type-Lens-Owner"></a>
The AWS account ID that owns the lens.
Type: String
Required: No

 ** ShareInvitationId **   <a name="wellarchitected-Type-Lens-ShareInvitationId"></a>
The ID assigned to the share invitation.
Type: String
Pattern: `[0-9a-f]{32}`
Required: No

 ** Tags **   <a name="wellarchitected-Type-Lens-Tags"></a>
The tags assigned to the lens.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_Lens_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wellarchitected-2020-03-31/Lens)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wellarchitected-2020-03-31/Lens)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wellarchitected-2020-03-31/Lens)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected Tool. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

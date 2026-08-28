---
source_url: https://docs.aws.amazon.com/interconnect/latest/api/API_RemoteAccountIdentifier.html
---

# RemoteAccountIdentifier
<a name="API_RemoteAccountIdentifier"></a>

The types of identifiers that may be needed for remote account specification.

## Contents
<a name="API_RemoteAccountIdentifier_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** identifier **   <a name="interconnect-Type-RemoteAccountIdentifier-identifier"></a>
A generic bit of identifying information. Can be used in place of any of the more specific types.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[-a-zA-Z0-9_@\.]+`
Required: No

## See Also
<a name="API_RemoteAccountIdentifier_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/interconnect-2022-07-26/RemoteAccountIdentifier)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/interconnect-2022-07-26/RemoteAccountIdentifier)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/interconnect-2022-07-26/RemoteAccountIdentifier)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Interconnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query interconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

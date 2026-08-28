---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SecurityProfileSearchSummary.html
---

# SecurityProfileSearchSummary
<a name="API_SecurityProfileSearchSummary"></a>

Information about the returned security profiles.

## Contents
<a name="API_SecurityProfileSearchSummary_Contents"></a>

 ** Arn **   <a name="connect-Type-SecurityProfileSearchSummary-Arn"></a>
The Amazon Resource Name (ARN) of the security profile.
Type: String
Required: No

 ** Description **   <a name="connect-Type-SecurityProfileSearchSummary-Description"></a>
The description of the security profile.
Type: String
Length Constraints: Maximum length of 250.
Required: No

 ** Id **   <a name="connect-Type-SecurityProfileSearchSummary-Id"></a>
The identifier of the security profile.
Type: String
Required: No

 ** OrganizationResourceId **   <a name="connect-Type-SecurityProfileSearchSummary-OrganizationResourceId"></a>
The organization resource identifier.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: No

 ** SecurityProfileName **   <a name="connect-Type-SecurityProfileSearchSummary-SecurityProfileName"></a>
The name of the security profile.
Type: String
Required: No

 ** Tags **   <a name="connect-Type-SecurityProfileSearchSummary-Tags"></a>
The tags used to organize, track, or control access for this resource. For example, { "Tags": {"key1":"value1", "key2":"value2"} }.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[\p{L}\p{Z}\p{N}_.:/=+\-@]*$`
Value Length Constraints: Maximum length of 256.
Required: No

## See Also
<a name="API_SecurityProfileSearchSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SecurityProfileSearchSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SecurityProfileSearchSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SecurityProfileSearchSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

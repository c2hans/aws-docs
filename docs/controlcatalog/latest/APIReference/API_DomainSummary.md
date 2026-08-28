---
source_url: https://docs.aws.amazon.com/controlcatalog/latest/APIReference/API_DomainSummary.html
---

# DomainSummary
<a name="API_DomainSummary"></a>

A summary of metadata for a domain.

## Contents
<a name="API_DomainSummary_Contents"></a>

 ** Arn **   <a name="controlcatalog-Type-DomainSummary-Arn"></a>
The Amazon Resource Name (ARN) that identifies the domain.
Type: String
Length Constraints: Minimum length of 33. Maximum length of 2048.
Pattern: `arn:(aws(?:[-a-z]*)?):controlcatalog:::domain/[0-9a-z]+`
Required: Yes

 ** CreateTime **   <a name="controlcatalog-Type-DomainSummary-CreateTime"></a>
The time when the domain was created.
Type: Timestamp
Required: Yes

 ** Description **   <a name="controlcatalog-Type-DomainSummary-Description"></a>
The description of the domain.
Type: String
Required: Yes

 ** LastUpdateTime **   <a name="controlcatalog-Type-DomainSummary-LastUpdateTime"></a>
The time when the domain was most recently updated.
Type: Timestamp
Required: Yes

 ** Name **   <a name="controlcatalog-Type-DomainSummary-Name"></a>
The name of the domain.
Type: String
Required: Yes

## See Also
<a name="API_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controlcatalog-2018-05-10/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controlcatalog-2018-05-10/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controlcatalog-2018-05-10/DomainSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Control Catalog. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query controlcatalog` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-cases_DomainSummary.html
---

# DomainSummary
<a name="API_connect-cases_DomainSummary"></a>

Object for the summarized details of the domain.

## Contents
<a name="API_connect-cases_DomainSummary_Contents"></a>

 ** domainArn **   <a name="connect-Type-connect-cases_DomainSummary-domainArn"></a>
The Amazon Resource Name (ARN) of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** domainId **   <a name="connect-Type-connect-cases_DomainSummary-domainId"></a>
The unique identifier of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 500.
Required: Yes

 ** name **   <a name="connect-Type-connect-cases_DomainSummary-name"></a>
The name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `.*[\S]`
Required: Yes

## See Also
<a name="API_connect-cases_DomainSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connectcases-2022-10-03/DomainSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connectcases-2022-10-03/DomainSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connectcases-2022-10-03/DomainSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

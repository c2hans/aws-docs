---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_CspmProviderDetail.html
---

# CspmProviderDetail
<a name="API_CspmProviderDetail"></a>

The detailed cloud provider configuration for a connector. This is a union type that currently supports Azure.

## Contents
<a name="API_CspmProviderDetail_Contents"></a>

**Important**
This data type is a UNION, so only one of the following members can be specified when used or returned.

 ** Azure **   <a name="securityhub-Type-CspmProviderDetail-Azure"></a>
The Azure provider detail.
Type: [AzureDetail](API_AzureDetail.md) object
Required: No

## See Also
<a name="API_CspmProviderDetail_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/CspmProviderDetail)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/CspmProviderDetail)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/CspmProviderDetail)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_DiversityConfig.html
---

# DiversityConfig
<a name="API_connect-customer-profiles_DiversityConfig"></a>

Configuration that controls diversity of recommendation results by capping the representation of specified item columns.

## Contents
<a name="API_connect-customer-profiles_DiversityConfig_Contents"></a>

 ** DiversityColumns **   <a name="connect-Type-connect-customer-profiles_DiversityConfig-DiversityColumns"></a>
A list of up to two diversity columns. Each column defines a cap on the number or percentage of recommended items that share the same value for that column.
Type: Array of [DiversityColumn](API_connect-customer-profiles_DiversityColumn.md) objects
Array Members: Minimum number of 0 items. Maximum number of 2 items.
Required: No

## See Also
<a name="API_connect-customer-profiles_DiversityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/DiversityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/DiversityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/DiversityConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_marketplace-agreements_Sort.html
---

# Sort
<a name="API_marketplace-agreements_Sort"></a>

An object that contains the `SortBy` and `SortOrder` attributes.

## Contents
<a name="API_marketplace-agreements_Sort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** sortBy **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Sort-sortBy"></a>
The attribute on which the data is grouped, which can be by `StartTime` and `EndTime`. The default value is `EndTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[A-Za-z_]+`
Required: No

 ** sortOrder **   <a name="AWSMarketplaceService-Type-marketplace-agreements_Sort-sortOrder"></a>
The sorting order, which can be `ASCENDING` or `DESCENDING`. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_marketplace-agreements_Sort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-agreement-2020-03-01/Sort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-agreement-2020-03-01/Sort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-agreement-2020-03-01/Sort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

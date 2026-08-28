---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_Sort.html
---

# Sort
<a name="API_Sort"></a>

An object that contains two attributes, `SortBy` and `SortOrder`.

## Contents
<a name="API_Sort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSMarketplaceService-Type-Sort-SortBy"></a>
For `ListEntities`, supported attributes include `LastModifiedDate` (default) and `EntityId`. In addition to `LastModifiedDate` and `EntityId`, each `EntityType` might support additional fields.
For `ListChangeSets`, supported attributes include `StartTime` and `EndTime`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z]+$`
Required: No

 ** SortOrder **   <a name="AWSMarketplaceService-Type-Sort-SortOrder"></a>
The sorting order. Can be `ASCENDING` or `DESCENDING`. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_Sort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/Sort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/Sort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/Sort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

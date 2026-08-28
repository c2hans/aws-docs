---
source_url: https://docs.aws.amazon.com/marketplace/latest/APIReference/API_AmiProductSort.html
---

# AmiProductSort
<a name="API_AmiProductSort"></a>

Objects that allows sorting on AMI products based on certain fields and sorting order.

## Contents
<a name="API_AmiProductSort_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** SortBy **   <a name="AWSMarketplaceService-Type-AmiProductSort-SortBy"></a>
Field to sort the AMI products by.
Type: String
Valid Values: `EntityId | LastModifiedDate | ProductTitle | Visibility`
Required: No

 ** SortOrder **   <a name="AWSMarketplaceService-Type-AmiProductSort-SortOrder"></a>
The sorting order. Can be `ASCENDING` or `DESCENDING`. The default value is `DESCENDING`.
Type: String
Valid Values: `ASCENDING | DESCENDING`
Required: No

## See Also
<a name="API_AmiProductSort_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/marketplace-catalog-2018-09-17/AmiProductSort)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/marketplace-catalog-2018-09-17/AmiProductSort)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/marketplace-catalog-2018-09-17/AmiProductSort)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Marketplace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query marketplace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

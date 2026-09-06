---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_Index.html
---

# Index
<a name="API_Index"></a>

An index is the data store used by AWS Resource Explorer to hold information about your AWS resources that the service discovers. Creating an index in an AWS Region turns on Resource Explorer and lets it discover your resources.

By default, an index is *local*, meaning that it contains information about resources in only the same Region as the index. However, you can promote the index of one Region in the account by calling [UpdateIndexType](API_UpdateIndexType.md) to convert it into an aggregator index. The aggregator index receives a replicated copy of the index information from all other Regions where Resource Explorer is turned on. This allows search operations in that Region to return results from all Regions in the account.

## Contents
<a name="API_Index_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="resourceexplorer-Type-Index-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index.
Type: String
Required: No

 ** Region **   <a name="resourceexplorer-Type-Index-Region"></a>
The AWS Region in which the index exists.
Type: String
Required: No

 ** Type **   <a name="resourceexplorer-Type-Index-Type"></a>
The type of index. It can be one of the following values:
+  `LOCAL` – The index contains information about resources from only the same AWS Region.
+  `AGGREGATOR` – Resource Explorer replicates copies of the indexed information about resources in all other AWS Regions to the aggregator index. This lets search results in the Region with the aggregator index to include resources from all Regions in the account where Resource Explorer is turned on.
Type: String
Valid Values: `LOCAL | AGGREGATOR`
Required: No

## See Also
<a name="API_Index_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/Index)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/Index)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/Index)

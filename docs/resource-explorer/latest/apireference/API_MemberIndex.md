---
source_url: https://docs.aws.amazon.com/resource-explorer/latest/apireference/API_MemberIndex.html
---

# MemberIndex
<a name="API_MemberIndex"></a>

An index is the data store used by AWS Resource Explorer to hold information about your AWS resources that the service discovers.

## Contents
<a name="API_MemberIndex_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccountId **   <a name="resourceexplorer-Type-MemberIndex-AccountId"></a>
The account ID for the index.
Type: String
Required: No

 ** Arn **   <a name="resourceexplorer-Type-MemberIndex-Arn"></a>
The [Amazon resource name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the index.
Type: String
Required: No

 ** Region **   <a name="resourceexplorer-Type-MemberIndex-Region"></a>
The AWS Region in which the index exists.
Type: String
Required: No

 ** Type **   <a name="resourceexplorer-Type-MemberIndex-Type"></a>
The type of index. It can be one of the following values:
+  `LOCAL` – The index contains information about resources from only the same AWS Region.
+  `AGGREGATOR` – Resource Explorer replicates copies of the indexed information about resources in all other AWS Regions to the aggregator index. This lets search results in the Region with the aggregator index to include resources from all Regions in the account where Resource Explorer is turned on.
Type: String
Valid Values: `LOCAL | AGGREGATOR`
Required: No

## See Also
<a name="API_MemberIndex_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/resource-explorer-2-2022-07-28/MemberIndex)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/resource-explorer-2-2022-07-28/MemberIndex)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/resource-explorer-2-2022-07-28/MemberIndex)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Resource Explorer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query resource-explorer` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

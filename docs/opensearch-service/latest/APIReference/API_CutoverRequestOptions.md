---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CutoverRequestOptions.html
---

# CutoverRequestOptions
<a name="API_CutoverRequestOptions"></a>

The cutover to perform for a cloned blue/green upgrade.

## Contents
<a name="API_CutoverRequestOptions_Contents"></a>

 ** Target **   <a name="opensearchservice-Type-CutoverRequestOptions-Target"></a>
The cluster to cut over to. `ClonedCluster` makes the cloned cluster serve the domain. `PrimaryCluster` keeps the primary cluster and ends the upgrade.
Type: String
Valid Values: `ClonedCluster | PrimaryCluster`
Required: Yes

## See Also
<a name="API_CutoverRequestOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CutoverRequestOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CutoverRequestOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CutoverRequestOptions)

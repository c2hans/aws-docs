---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_CutoverOptions.html
---

# CutoverOptions
<a name="API_CutoverOptions"></a>

The cutover target and status for a cloned blue/green upgrade.

## Contents
<a name="API_CutoverOptions_Contents"></a>

 ** Status **   <a name="opensearchservice-Type-CutoverOptions-Status"></a>
The status of the cutover.
Type: String
Valid Values: `InProgress | Completed | Failed`
Required: Yes

 ** Target **   <a name="opensearchservice-Type-CutoverOptions-Target"></a>
The cluster that the domain is cutting over to.
Type: String
Valid Values: `ClonedCluster | PrimaryCluster`
Required: Yes

## See Also
<a name="API_CutoverOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/CutoverOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/CutoverOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/CutoverOptions)

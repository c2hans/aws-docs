---
source_url: https://docs.aws.amazon.com/keyspaces/latest/APIReference/API_ClusteringKey.html
---

# ClusteringKey
<a name="API_ClusteringKey"></a>

The optional clustering column portion of your primary key determines how the data is clustered and sorted within each partition.

## Contents
<a name="API_ClusteringKey_Contents"></a>

 ** name **   <a name="keyspaces-Type-ClusteringKey-name"></a>
The name(s) of the clustering column(s).
Type: String
Required: Yes

 ** orderBy **   <a name="keyspaces-Type-ClusteringKey-orderBy"></a>
Sets the ascendant (`ASC`) or descendant (`DESC`) order modifier.
Type: String
Valid Values: `ASC | DESC`
Required: Yes

## See Also
<a name="API_ClusteringKey_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/keyspaces-2022-02-10/ClusteringKey)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/keyspaces-2022-02-10/ClusteringKey)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/keyspaces-2022-02-10/ClusteringKey)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Keyspaces (for Apache Cassandra). To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query keyspaces` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

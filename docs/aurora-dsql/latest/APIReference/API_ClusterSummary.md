---
source_url: https://docs.aws.amazon.com/aurora-dsql/latest/APIReference/API_ClusterSummary.html
---

# ClusterSummary
<a name="API_ClusterSummary"></a>

A summary of the properties of a cluster.

## Contents
<a name="API_ClusterSummary_Contents"></a>

 ** arn **   <a name="auroradsql-Type-ClusterSummary-arn"></a>
The ARN of the cluster.
Type: String
Pattern: `arn:aws(-[^:]+)?:dsql:[a-z0-9-]{1,20}:[0-9]{12}:cluster/[a-z0-9]{26}`
Required: Yes

 ** identifier **   <a name="auroradsql-Type-ClusterSummary-identifier"></a>
The ID of the cluster.
Type: String
Pattern: `[a-z0-9]{26}`
Required: Yes

## See Also
<a name="API_ClusterSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/dsql-2018-05-10/ClusterSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/dsql-2018-05-10/ClusterSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/dsql-2018-05-10/ClusterSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Aurora DSQL. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aurora-dsql` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

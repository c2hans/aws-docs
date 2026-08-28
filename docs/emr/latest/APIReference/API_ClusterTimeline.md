---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_ClusterTimeline.html
---

# ClusterTimeline
<a name="API_ClusterTimeline"></a>

Represents the timeline of the cluster's lifecycle.

## Contents
<a name="API_ClusterTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-ClusterTimeline-CreationDateTime"></a>
The creation date and time of the cluster.
Type: Timestamp
Required: No

 ** EndDateTime **   <a name="EMR-Type-ClusterTimeline-EndDateTime"></a>
The date and time when the cluster was terminated.
Type: Timestamp
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-ClusterTimeline-ReadyDateTime"></a>
The date and time when the cluster was ready to run steps.
Type: Timestamp
Required: No

## See Also
<a name="API_ClusterTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/ClusterTimeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/ClusterTimeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/ClusterTimeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

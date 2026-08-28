---
source_url: https://docs.aws.amazon.com/emr/latest/APIReference/API_InstanceFleetTimeline.html
---

# InstanceFleetTimeline
<a name="API_InstanceFleetTimeline"></a>

Provides historical timestamps for the instance fleet, including the time of creation, the time it became ready to run jobs, and the time of termination.

**Note**
The instance fleet configuration is available only in Amazon EMR releases 4.8.0 and later, excluding 5.0.x versions.

## Contents
<a name="API_InstanceFleetTimeline_Contents"></a>

 ** CreationDateTime **   <a name="EMR-Type-InstanceFleetTimeline-CreationDateTime"></a>
The time and date the instance fleet was created.
Type: Timestamp
Required: No

 ** EndDateTime **   <a name="EMR-Type-InstanceFleetTimeline-EndDateTime"></a>
The time and date the instance fleet terminated.
Type: Timestamp
Required: No

 ** ReadyDateTime **   <a name="EMR-Type-InstanceFleetTimeline-ReadyDateTime"></a>
The time and date the instance fleet was ready to run jobs.
Type: Timestamp
Required: No

## See Also
<a name="API_InstanceFleetTimeline_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticmapreduce-2009-03-31/InstanceFleetTimeline)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticmapreduce-2009-03-31/InstanceFleetTimeline)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticmapreduce-2009-03-31/InstanceFleetTimeline)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

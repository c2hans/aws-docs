---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/api/API_FailoverConfig.html
---

# FailoverConfig
<a name="API_FailoverConfig"></a>

 The settings for source failover.

## Contents
<a name="API_FailoverConfig_Contents"></a>

 ** failoverMode **   <a name="mediaconnect-Type-FailoverConfig-failoverMode"></a>
 The type of failover you choose for this flow. MERGE combines the source streams into a single stream, allowing graceful recovery from any single-source loss. FAILOVER allows switching between different streams.
Type: String
Valid Values: `MERGE | FAILOVER`
Required: No

 ** recoveryWindow **   <a name="mediaconnect-Type-FailoverConfig-recoveryWindow"></a>
 Search window time to look for dash-7 packets.
Type: Integer
Required: No

 ** sourcePriority **   <a name="mediaconnect-Type-FailoverConfig-sourcePriority"></a>
 The priority you want to assign to a source. You can have a primary stream and a backup stream or two equally prioritized streams.
Type: [SourcePriority](API_SourcePriority.md) object
Required: No

 ** state **   <a name="mediaconnect-Type-FailoverConfig-state"></a>
The state of source failover on the flow. If the state is inactive, the flow can have only one source. If the state is active, the flow can have one or two sources.
Type: String
Valid Values: `ENABLED | DISABLED`
Required: No

## See Also
<a name="API_FailoverConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mediaconnect-2018-11-14/FailoverConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mediaconnect-2018-11-14/FailoverConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mediaconnect-2018-11-14/FailoverConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

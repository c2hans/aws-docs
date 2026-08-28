---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_WorkerResourceConfig.html
---

# WorkerResourceConfig
<a name="API_WorkerResourceConfig"></a>

The cumulative configuration requirements for every worker instance of the worker type.

## Contents
<a name="API_WorkerResourceConfig_Contents"></a>

 ** cpu **   <a name="emrserverless-Type-WorkerResourceConfig-cpu"></a>
The CPU requirements for every worker instance of the worker type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[1-9][0-9]*(\s)?(vCPU|vcpu|VCPU)?`
Required: Yes

 ** memory **   <a name="emrserverless-Type-WorkerResourceConfig-memory"></a>
The memory requirements for every worker instance of the worker type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[1-9][0-9]*(\s)?(GB|gb|gB|Gb)?`
Required: Yes

 ** disk **   <a name="emrserverless-Type-WorkerResourceConfig-disk"></a>
The disk requirements for every worker instance of the worker type.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 15.
Pattern: `[1-9][0-9]*(\s)?(GB|gb|gB|Gb)`
Required: No

 ** diskType **   <a name="emrserverless-Type-WorkerResourceConfig-diskType"></a>
The disk type for every worker instance of the work type. Shuffle optimized disks have higher performance characteristics and are better for shuffle heavy workloads. Default is `STANDARD`.
Type: String
Pattern: `(SHUFFLE_OPTIMIZED|[Ss]huffle_[Oo]ptimized|STANDARD|[Ss]tandard)`
Required: No

## See Also
<a name="API_WorkerResourceConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/WorkerResourceConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/WorkerResourceConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/WorkerResourceConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

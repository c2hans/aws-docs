---
source_url: https://docs.aws.amazon.com/emr-serverless/latest/APIReference/API_InitialCapacityConfig.html
---

# InitialCapacityConfig
<a name="API_InitialCapacityConfig"></a>

The initial capacity configuration per worker.

## Contents
<a name="API_InitialCapacityConfig_Contents"></a>

 ** workerCount **   <a name="emrserverless-Type-InitialCapacityConfig-workerCount"></a>
The number of workers in the initial capacity configuration.
Type: Long
Valid Range: Minimum value of 1. Maximum value of 1000000.
Required: Yes

 ** workerConfiguration **   <a name="emrserverless-Type-InitialCapacityConfig-workerConfiguration"></a>
The resource configuration of the initial capacity configuration.
Type: [WorkerResourceConfig](API_WorkerResourceConfig.md) object
Required: No

## See Also
<a name="API_InitialCapacityConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/emr-serverless-2021-07-13/InitialCapacityConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/emr-serverless-2021-07-13/InitialCapacityConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/emr-serverless-2021-07-13/InitialCapacityConfig)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Serverless. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr-serverless` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

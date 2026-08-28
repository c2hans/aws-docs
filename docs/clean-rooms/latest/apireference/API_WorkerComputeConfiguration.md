---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_WorkerComputeConfiguration.html
---

# WorkerComputeConfiguration
<a name="API_WorkerComputeConfiguration"></a>

 The configuration of the compute resources for workers running an analysis with the AWS Clean Rooms SQL analytics engine.

## Contents
<a name="API_WorkerComputeConfiguration_Contents"></a>

 ** number **   <a name="API-Type-WorkerComputeConfiguration-number"></a>
 The number of workers.
SQL queries support a minimum value of 2 and a maximum value of 400.
PySpark jobs support a minimum value of 4 and a maximum value of 128.
Type: Integer
Valid Range: Minimum value of 2. Maximum value of 1024.
Required: No

 ** properties **   <a name="API-Type-WorkerComputeConfiguration-properties"></a>
The configuration properties for the worker compute environment. These properties allow you to customize the compute settings for your AWS Clean Rooms workloads.
Type: [WorkerComputeConfigurationProperties](API_WorkerComputeConfigurationProperties.md) object
 **Note: **This object is a Union. Only one member of this object can be specified or returned.
Required: No

 ** type **   <a name="API-Type-WorkerComputeConfiguration-type"></a>
 The worker compute configuration type.
Type: String
Valid Values: `CR.1X | CR.4X | CR.8X`
Required: No

## See Also
<a name="API_WorkerComputeConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/WorkerComputeConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/WorkerComputeConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/WorkerComputeConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query clean-rooms` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

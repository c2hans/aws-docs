---
source_url: https://docs.aws.amazon.com/pcs/latest/APIReference/API_SchedulerRequest.html
---

# SchedulerRequest
<a name="API_SchedulerRequest"></a>

The cluster management and job scheduling software associated with the cluster.

## Contents
<a name="API_SchedulerRequest_Contents"></a>

 ** type **   <a name="PCS-Type-SchedulerRequest-type"></a>
The software AWS PCS uses to manage cluster scaling and job scheduling.
Type: String
Valid Values: `SLURM`
Required: Yes

 ** version **   <a name="PCS-Type-SchedulerRequest-version"></a>
The version of the specified scheduling software that AWS PCS uses to manage cluster scaling and job scheduling. For more information, see [Slurm versions in AWS PCS](https://docs.aws.amazon.com/pcs/latest/userguide/slurm-versions.html) in the * AWS PCS User Guide*.
Valid Values: `24.11 | 25.05 | 25.11`
Type: String
Required: Yes

## See Also
<a name="API_SchedulerRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pcs-2023-02-10/SchedulerRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pcs-2023-02-10/SchedulerRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pcs-2023-02-10/SchedulerRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS PCS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pcs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

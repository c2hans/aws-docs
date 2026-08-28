---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_DiskResourceUtilization.html
---

# DiskResourceUtilization
<a name="API_DiskResourceUtilization"></a>

The field that contains a list of disk (local storage) metrics that are associated with the current instance.

## Contents
<a name="API_DiskResourceUtilization_Contents"></a>

 ** DiskReadBytesPerSecond **   <a name="awscostmanagement-Type-DiskResourceUtilization-DiskReadBytesPerSecond"></a>
The maximum read throughput operations per second.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DiskReadOpsPerSecond **   <a name="awscostmanagement-Type-DiskResourceUtilization-DiskReadOpsPerSecond"></a>
The maximum number of read operations per second.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DiskWriteBytesPerSecond **   <a name="awscostmanagement-Type-DiskResourceUtilization-DiskWriteBytesPerSecond"></a>
The maximum write throughput operations per second.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** DiskWriteOpsPerSecond **   <a name="awscostmanagement-Type-DiskResourceUtilization-DiskWriteOpsPerSecond"></a>
The maximum number of write operations per second.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_DiskResourceUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/DiskResourceUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/DiskResourceUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/DiskResourceUtilization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

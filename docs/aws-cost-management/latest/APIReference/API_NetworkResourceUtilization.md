---
source_url: https://docs.aws.amazon.com/aws-cost-management/latest/APIReference/API_NetworkResourceUtilization.html
---

# NetworkResourceUtilization
<a name="API_NetworkResourceUtilization"></a>

The network field that contains a list of network metrics that are associated with the current instance.

## Contents
<a name="API_NetworkResourceUtilization_Contents"></a>

 ** NetworkInBytesPerSecond **   <a name="awscostmanagement-Type-NetworkResourceUtilization-NetworkInBytesPerSecond"></a>
The network inbound throughput utilization measured in Bytes per second (Bps).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NetworkOutBytesPerSecond **   <a name="awscostmanagement-Type-NetworkResourceUtilization-NetworkOutBytesPerSecond"></a>
The network outbound throughput utilization measured in Bytes per second (Bps).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NetworkPacketsInPerSecond **   <a name="awscostmanagement-Type-NetworkResourceUtilization-NetworkPacketsInPerSecond"></a>
The network inbound packets that are measured in packets per second.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

 ** NetworkPacketsOutPerSecond **   <a name="awscostmanagement-Type-NetworkResourceUtilization-NetworkPacketsOutPerSecond"></a>
The network outbound packets that are measured in packets per second.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 1024.
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_NetworkResourceUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ce-2017-10-25/NetworkResourceUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ce-2017-10-25/NetworkResourceUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ce-2017-10-25/NetworkResourceUtilization)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Billing and Cost Management. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query aws-cost-management` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

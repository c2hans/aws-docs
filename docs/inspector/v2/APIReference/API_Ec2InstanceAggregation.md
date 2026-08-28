---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_Ec2InstanceAggregation.html
---

# Ec2InstanceAggregation
<a name="API_Ec2InstanceAggregation"></a>

The details that define an aggregation based on Amazon EC2 instances.

## Contents
<a name="API_Ec2InstanceAggregation_Contents"></a>

 ** amis **   <a name="inspector2-Type-Ec2InstanceAggregation-amis"></a>
The AMI IDs associated with the Amazon EC2 instances to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** instanceIds **   <a name="inspector2-Type-Ec2InstanceAggregation-instanceIds"></a>
The Amazon EC2 instance IDs to aggregate findings for.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** instanceTags **   <a name="inspector2-Type-Ec2InstanceAggregation-instanceTags"></a>
The Amazon EC2 instance tags to aggregate findings for.
Type: Array of [MapFilter](API_MapFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** operatingSystems **   <a name="inspector2-Type-Ec2InstanceAggregation-operatingSystems"></a>
The operating system types to aggregate findings for. Valid values must be uppercase and underscore separated, examples are `ORACLE_LINUX_7` and `ALPINE_LINUX_3_8`.
Type: Array of [StringFilter](API_StringFilter.md) objects
Array Members: Minimum number of 1 item. Maximum number of 10 items.
Required: No

 ** sortBy **   <a name="inspector2-Type-Ec2InstanceAggregation-sortBy"></a>
The value to sort results by.
Type: String
Valid Values: `NETWORK_FINDINGS | CRITICAL | HIGH | ALL`
Required: No

 ** sortOrder **   <a name="inspector2-Type-Ec2InstanceAggregation-sortOrder"></a>
The order to sort results by.
Type: String
Valid Values: `ASC | DESC`
Required: No

## See Also
<a name="API_Ec2InstanceAggregation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/Ec2InstanceAggregation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/Ec2InstanceAggregation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/Ec2InstanceAggregation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Inspector. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query inspector` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

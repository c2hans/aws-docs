---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParameters.html
---

# ScalingParameters
<a name="API_ScalingParameters"></a>

## Description
<a name="API_ScalingParameters_Description"></a>

The desired instance type and desired number of replicas of each index partition.

## Contents
<a name="API_ScalingParameters_Contents"></a>

 **DesiredInstanceType**
The instance type that you want to preconfigure for your domain. For example, `search.medium`.
Type: String
Valid Values: `search.small | search.medium | search.large | search.xlarge | search.2xlarge`
For older domains, valid values might also include `search.m1.small`, `search.m1.large`, `search.m2.xlarge`, `search.m2.2xlarge`, `search.m3.medium`, `search.m3.large`, `search.m3.xlarge`, and `search.m3.2xlarge`.
Required: No

 **DesiredPartitionCount**
The number of partitions you want to preconfigure for your domain. Only valid when you select `search.2xlarge` as the instance type.
Type: Integer
Required: No

 **DesiredReplicationCount**
The number of replicas you want to preconfigure for each index partition.
Type: Integer
Required: No

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

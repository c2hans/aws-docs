---
source_url: https://docs.aws.amazon.com/cloudsearch/latest/developerguide/API_ScalingParametersStatus.html
---

# ScalingParametersStatus
<a name="API_ScalingParametersStatus"></a>

## Description
<a name="API_ScalingParametersStatus_Description"></a>

The status and configuration of a search domain's scaling parameters.

## Contents
<a name="API_ScalingParametersStatus_Contents"></a>

 **Options**
The desired instance type and desired number of replicas of each index partition.
Type: [ScalingParameters](API_ScalingParameters.md)
 Required: Yes

 **Status**
The status of domain configuration option.
Type: [OptionStatus](API_OptionStatus.md)
 Required: Yes

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Cloud Search. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cloudsearch` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

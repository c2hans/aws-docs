---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-codeguruprofiler-profilinggroup-agentpermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CodeGuruProfiler::ProfilingGroup AgentPermissions
<a name="aws-properties-codeguruprofiler-profilinggroup-agentpermissions"></a>

The agent permissions attached to a profiling group. Granting `AgentPermissions` to a role or user allows that role or user to perform actions required by the profiling agent, `ConfigureAgent` and `PostAgentProfile`. For more information, see [Resource-based policies in CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/resource-based-policies.html) in the *Amazon CodeGuru Profiler User Guide*.

## Syntax
<a name="aws-properties-codeguruprofiler-profilinggroup-agentpermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-codeguruprofiler-profilinggroup-agentpermissions-syntax.json"></a>

```
{
  "[Principals](#cfn-codeguruprofiler-profilinggroup-agentpermissions-principals)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-codeguruprofiler-profilinggroup-agentpermissions-syntax.yaml"></a>

```
  [Principals](#cfn-codeguruprofiler-profilinggroup-agentpermissions-principals): {{
    - String}}
```

## Properties
<a name="aws-properties-codeguruprofiler-profilinggroup-agentpermissions-properties"></a>

`Principals`  <a name="cfn-codeguruprofiler-profilinggroup-agentpermissions-principals"></a>
A list of string ARNs for the roles and users you want to grant access to the profiling group. Wildcards are not supported in the ARNs. You are allowed to provide up to 50 ARNs. An empty list is not permitted.
*Required*: Yes
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

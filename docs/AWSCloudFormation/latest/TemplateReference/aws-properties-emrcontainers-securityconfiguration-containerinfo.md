---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-securityconfiguration-containerinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::SecurityConfiguration ContainerInfo
<a name="aws-properties-emrcontainers-securityconfiguration-containerinfo"></a>

The information about the container used for a job run or a managed endpoint.

## Syntax
<a name="aws-properties-emrcontainers-securityconfiguration-containerinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-securityconfiguration-containerinfo-syntax.json"></a>

```
{
  "[EksInfo](#cfn-emrcontainers-securityconfiguration-containerinfo-eksinfo)" : {{EksInfo}}
}
```

### YAML
<a name="aws-properties-emrcontainers-securityconfiguration-containerinfo-syntax.yaml"></a>

```
  [EksInfo](#cfn-emrcontainers-securityconfiguration-containerinfo-eksinfo): {{
    EksInfo}}
```

## Properties
<a name="aws-properties-emrcontainers-securityconfiguration-containerinfo-properties"></a>

`EksInfo`  <a name="cfn-emrcontainers-securityconfiguration-containerinfo-eksinfo"></a>
The information about the Amazon EKS cluster.
*Required*: No
*Type*: [EksInfo](aws-properties-emrcontainers-securityconfiguration-eksinfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

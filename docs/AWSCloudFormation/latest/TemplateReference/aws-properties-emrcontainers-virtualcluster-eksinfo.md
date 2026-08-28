---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-emrcontainers-virtualcluster-eksinfo.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EMRContainers::VirtualCluster EksInfo
<a name="aws-properties-emrcontainers-virtualcluster-eksinfo"></a>

The information about the Amazon EKS cluster.

## Syntax
<a name="aws-properties-emrcontainers-virtualcluster-eksinfo-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-emrcontainers-virtualcluster-eksinfo-syntax.json"></a>

```
{
  "[Namespace](#cfn-emrcontainers-virtualcluster-eksinfo-namespace)" : {{String}}
}
```

### YAML
<a name="aws-properties-emrcontainers-virtualcluster-eksinfo-syntax.yaml"></a>

```
  [Namespace](#cfn-emrcontainers-virtualcluster-eksinfo-namespace): {{String}}
```

## Properties
<a name="aws-properties-emrcontainers-virtualcluster-eksinfo-properties"></a>

`Namespace`  <a name="cfn-emrcontainers-virtualcluster-eksinfo-namespace"></a>
The namespaces of the EKS cluster.
*Minimum*: 1
*Maximum*: 63
*Pattern*: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
*Required*: Yes
*Type*: String
*Pattern*: `[a-z0-9]([-a-z0-9]*[a-z0-9])?`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

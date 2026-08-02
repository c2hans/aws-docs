---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-serviceaccesssecuritygroups.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment ServiceAccessSecurityGroups
<a name="aws-properties-evs-environment-serviceaccesssecuritygroups"></a>

The security groups that allow traffic between the Amazon EVS control plane and your VPC for Amazon EVS service access. If a security group is not specified, Amazon EVS uses the default security group in your account for service access.

## Syntax
<a name="aws-properties-evs-environment-serviceaccesssecuritygroups-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-serviceaccesssecuritygroups-syntax.json"></a>

```
{
  "[SecurityGroups](#cfn-evs-environment-serviceaccesssecuritygroups-securitygroups)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-evs-environment-serviceaccesssecuritygroups-syntax.yaml"></a>

```
  [SecurityGroups](#cfn-evs-environment-serviceaccesssecuritygroups-securitygroups): {{
    - String}}
```

## Properties
<a name="aws-properties-evs-environment-serviceaccesssecuritygroups-properties"></a>

`SecurityGroups`  <a name="cfn-evs-environment-serviceaccesssecuritygroups-securitygroups"></a>
The security groups that allow service access.
*Required*: No
*Type*: Array of String
*Update requires*: Updates are not supported.

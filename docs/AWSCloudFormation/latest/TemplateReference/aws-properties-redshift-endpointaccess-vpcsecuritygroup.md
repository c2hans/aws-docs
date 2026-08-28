---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-redshift-endpointaccess-vpcsecuritygroup.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Redshift::EndpointAccess VpcSecurityGroup
<a name="aws-properties-redshift-endpointaccess-vpcsecuritygroup"></a>

The security groups associated with the endpoint.

## Syntax
<a name="aws-properties-redshift-endpointaccess-vpcsecuritygroup-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-redshift-endpointaccess-vpcsecuritygroup-syntax.json"></a>

```
{
  "[Status](#cfn-redshift-endpointaccess-vpcsecuritygroup-status)" : {{String}},
  "[VpcSecurityGroupId](#cfn-redshift-endpointaccess-vpcsecuritygroup-vpcsecuritygroupid)" : {{String}}
}
```

### YAML
<a name="aws-properties-redshift-endpointaccess-vpcsecuritygroup-syntax.yaml"></a>

```
  [Status](#cfn-redshift-endpointaccess-vpcsecuritygroup-status): {{String}}
  [VpcSecurityGroupId](#cfn-redshift-endpointaccess-vpcsecuritygroup-vpcsecuritygroupid): {{String}}
```

## Properties
<a name="aws-properties-redshift-endpointaccess-vpcsecuritygroup-properties"></a>

`Status`  <a name="cfn-redshift-endpointaccess-vpcsecuritygroup-status"></a>
The status of the endpoint.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`VpcSecurityGroupId`  <a name="cfn-redshift-endpointaccess-vpcsecuritygroup-vpcsecuritygroupid"></a>
The identifier of the VPC security group.
*Required*: No
*Type*: String
*Maximum*: `2147483647`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

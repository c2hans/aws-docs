---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-vpcendpointservicepermissions.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::VPCEndpointServicePermissions
<a name="aws-resource-ec2-vpcendpointservicepermissions"></a>

Grant or revoke permissions for service consumers (users, IAM roles, and AWS accounts) to connect to a VPC endpoint service.

If you grant permissions to all principals, the service is public. Any users who know the name of a public service can send a request to attach an endpoint. If the service does not require manual approval, attachments are automatically approved.

## Syntax
<a name="aws-resource-ec2-vpcendpointservicepermissions-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-vpcendpointservicepermissions-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::VPCEndpointServicePermissions",
  "Properties" : {
      "[AllowedPrincipals](#cfn-ec2-vpcendpointservicepermissions-allowedprincipals)" : {{[ String, ... ]}},
      "[ServiceId](#cfn-ec2-vpcendpointservicepermissions-serviceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ec2-vpcendpointservicepermissions-syntax.yaml"></a>

```
Type: AWS::EC2::VPCEndpointServicePermissions
Properties:
  [AllowedPrincipals](#cfn-ec2-vpcendpointservicepermissions-allowedprincipals): {{
    - String}}
  [ServiceId](#cfn-ec2-vpcendpointservicepermissions-serviceid): {{String}}
```

## Properties
<a name="aws-resource-ec2-vpcendpointservicepermissions-properties"></a>

`AllowedPrincipals`  <a name="cfn-ec2-vpcendpointservicepermissions-allowedprincipals"></a>
The Amazon Resource Names (ARN) of one or more principals (for example, users, IAM roles, and AWS accounts). Permissions are granted to the principals in this list. To grant permissions to all principals, specify an asterisk (\*). Permissions are revoked for principals not in this list. If the list is empty, then all permissions are revoked.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceId`  <a name="cfn-ec2-vpcendpointservicepermissions-serviceid"></a>
The ID of the service.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ec2-vpcendpointservicepermissions-return-values"></a>

### Ref
<a name="aws-resource-ec2-vpcendpointservicepermissions-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ID of the VPC endpoint service permissions.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

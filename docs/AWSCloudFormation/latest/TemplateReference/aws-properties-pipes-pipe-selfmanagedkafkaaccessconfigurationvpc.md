---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Pipes::Pipe SelfManagedKafkaAccessConfigurationVpc
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc"></a>

This structure specifies the VPC subnets and security groups for the stream, and whether a public IP address is to be used.

## Syntax
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-syntax.json"></a>

```
{
  "[SecurityGroup](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-securitygroup)" : {{[ String, ... ]}},
  "[Subnets](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-subnets)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-syntax.yaml"></a>

```
  [SecurityGroup](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-securitygroup): {{
    - String}}
  [Subnets](#cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-subnets): {{
    - String}}
```

## Properties
<a name="aws-properties-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-properties"></a>

`SecurityGroup`  <a name="cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-securitygroup"></a>
Specifies the security groups associated with the stream. These security groups must all be in the same VPC. You can specify as many as five security groups.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `1024 | 5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Subnets`  <a name="cfn-pipes-pipe-selfmanagedkafkaaccessconfigurationvpc-subnets"></a>
Specifies the subnets associated with the stream. These subnets must all be in the same VPC. You can specify as many as 16 subnets.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `1024 | 16`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

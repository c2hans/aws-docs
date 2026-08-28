---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-lambda-capacityprovider-instancerequirements.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Lambda::CapacityProvider InstanceRequirements
<a name="aws-properties-lambda-capacityprovider-instancerequirements"></a>

Specifications that define the characteristics and constraints for compute instances used by the capacity provider.

## Syntax
<a name="aws-properties-lambda-capacityprovider-instancerequirements-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-lambda-capacityprovider-instancerequirements-syntax.json"></a>

```
{
  "[AllowedInstanceTypes](#cfn-lambda-capacityprovider-instancerequirements-allowedinstancetypes)" : {{[ String, ... ]}},
  "[Architectures](#cfn-lambda-capacityprovider-instancerequirements-architectures)" : {{[ String, ... ]}},
  "[ExcludedInstanceTypes](#cfn-lambda-capacityprovider-instancerequirements-excludedinstancetypes)" : {{[ String, ... ]}}
}
```

### YAML
<a name="aws-properties-lambda-capacityprovider-instancerequirements-syntax.yaml"></a>

```
  [AllowedInstanceTypes](#cfn-lambda-capacityprovider-instancerequirements-allowedinstancetypes): {{
    - String}}
  [Architectures](#cfn-lambda-capacityprovider-instancerequirements-architectures): {{
    - String}}
  [ExcludedInstanceTypes](#cfn-lambda-capacityprovider-instancerequirements-excludedinstancetypes): {{
    - String}}
```

## Properties
<a name="aws-properties-lambda-capacityprovider-instancerequirements-properties"></a>

`AllowedInstanceTypes`  <a name="cfn-lambda-capacityprovider-instancerequirements-allowedinstancetypes"></a>
A list of EC2 instance types that the capacity provider is allowed to use. If not specified, all compatible instance types are allowed.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `30 | 400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Architectures`  <a name="cfn-lambda-capacityprovider-instancerequirements-architectures"></a>
A list of supported CPU architectures for compute instances. Valid values include `x86_64` and `arm64`.
*Required*: No
*Type*: Array of String
*Minimum*: `1`
*Maximum*: `1`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ExcludedInstanceTypes`  <a name="cfn-lambda-capacityprovider-instancerequirements-excludedinstancetypes"></a>
A list of EC2 instance types that the capacity provider should not use, even if they meet other requirements.
*Required*: No
*Type*: Array of String
*Minimum*: `1 | 0`
*Maximum*: `30 | 400`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Examples
<a name="aws-properties-lambda-capacityprovider-instancerequirements--examples"></a>

### Instance requirement configuration
<a name="aws-properties-lambda-capacityprovider-instancerequirements--examples--Instance_requirement_configuration"></a>

Configure instance types and architecture.

#### YAML
<a name="aws-properties-lambda-capacityprovider-instancerequirements--examples--Instance_requirement_configuration--yaml"></a>

```

InstanceRequirements:
    AllowedInstanceTypes:
        - c5.4xlarge
    ExcludedInstanceTypes:
        - r6g.xlarge
    Architecture:
        - x86_64
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

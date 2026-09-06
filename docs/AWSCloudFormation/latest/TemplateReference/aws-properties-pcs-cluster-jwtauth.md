---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-pcs-cluster-jwtauth.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::PCS::Cluster JwtAuth
<a name="aws-properties-pcs-cluster-jwtauth"></a>

The JWT authentication configuration for Slurm REST API access.

## Syntax
<a name="aws-properties-pcs-cluster-jwtauth-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-pcs-cluster-jwtauth-syntax.json"></a>

```
{
  "[JwtKey](#cfn-pcs-cluster-jwtauth-jwtkey)" : {{JwtKey}}
}
```

### YAML
<a name="aws-properties-pcs-cluster-jwtauth-syntax.yaml"></a>

```
  [JwtKey](#cfn-pcs-cluster-jwtauth-jwtkey): {{
    JwtKey}}
```

## Properties
<a name="aws-properties-pcs-cluster-jwtauth-properties"></a>

`JwtKey`  <a name="cfn-pcs-cluster-jwtauth-jwtkey"></a>
The JWT key for Slurm REST API authentication.
*Required*: No
*Type*: [JwtKey](aws-properties-pcs-cluster-jwtkey.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

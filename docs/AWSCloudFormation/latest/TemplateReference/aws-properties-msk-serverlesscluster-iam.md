---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-msk-serverlesscluster-iam.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::MSK::ServerlessCluster Iam
<a name="aws-properties-msk-serverlesscluster-iam"></a>

Details for SASL/IAM client authentication.

## Syntax
<a name="aws-properties-msk-serverlesscluster-iam-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-msk-serverlesscluster-iam-syntax.json"></a>

```
{
  "[Enabled](#cfn-msk-serverlesscluster-iam-enabled)" : {{Boolean}}
}
```

### YAML
<a name="aws-properties-msk-serverlesscluster-iam-syntax.yaml"></a>

```
  [Enabled](#cfn-msk-serverlesscluster-iam-enabled): {{Boolean}}
```

## Properties
<a name="aws-properties-msk-serverlesscluster-iam-properties"></a>

`Enabled`  <a name="cfn-msk-serverlesscluster-iam-enabled"></a>
SASL/IAM authentication is enabled or not.
*Required*: Yes
*Type*: Boolean
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

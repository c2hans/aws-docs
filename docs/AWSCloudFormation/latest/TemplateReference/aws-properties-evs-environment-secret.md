---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-evs-environment-secret.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EVS::Environment Secret
<a name="aws-properties-evs-environment-secret"></a>

A managed secret that contains the credentials for installing vCenter Server, NSX, and SDDC Manager. During environment creation, the Amazon EVS control plane uses AWS Secrets Manager to create, encrypt, validate, and store secrets. If you choose to delete your environment, Amazon EVS also deletes the secrets that are associated with your environment. Amazon EVS does not provide managed rotation of secrets. We recommend that you rotate secrets regularly to ensure that secrets are not long-lived.

## Syntax
<a name="aws-properties-evs-environment-secret-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-evs-environment-secret-syntax.json"></a>

```
{
  "[SecretArn](#cfn-evs-environment-secret-secretarn)" : {{String}}
}
```

### YAML
<a name="aws-properties-evs-environment-secret-syntax.yaml"></a>

```
  [SecretArn](#cfn-evs-environment-secret-secretarn): {{String}}
```

## Properties
<a name="aws-properties-evs-environment-secret-properties"></a>

`SecretArn`  <a name="cfn-evs-environment-secret-secretarn"></a>
 The Amazon Resource Name (ARN) of the secret.
*Required*: No
*Type*: String
*Update requires*: Updates are not supported.

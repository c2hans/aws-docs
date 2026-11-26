---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-config-conformancepack-source.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Config::ConformancePack Source

Provides the identifier of the managed conformance pack that AWS Config deploys in your account.

## Syntax
<a name="aws-properties-config-conformancepack-source-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-config-conformancepack-source-syntax.json"></a>

```json
{
  "[SourceIdentifier](#cfn-config-conformancepack-source-sourceidentifier)" : {{String}}
}
```

### YAML
<a name="aws-properties-config-conformancepack-source-syntax.yaml"></a>

```yaml
  [SourceIdentifier](#cfn-config-conformancepack-source-sourceidentifier): {{String}}
```

## Properties
<a name="aws-properties-config-conformancepack-source-properties"></a>

`SourceIdentifier`  <a name="cfn-config-conformancepack-source-sourceidentifier"></a>
A predefined identifier for a managed conformance pack, such as `NIST-SP-800-53_R5`. The identifier specifies which framework's managed conformance pack AWS Config deploys in your account. For the identifier of each managed conformance pack, see the [Managed Conformance Pack Catalog](https://docs.aws.amazon.com/config/latest/developerguide/managed-conformance-pack-catalog.html) in the *AWS Config Developer Guide*.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

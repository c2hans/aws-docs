---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Integration
<a name="aws-resource-cloudwatch-integration"></a>

<a name="aws-resource-cloudwatch-integration-description"></a>The `AWS::CloudWatch::Integration` resource Property description not available. for CloudWatch.

## Syntax
<a name="aws-resource-cloudwatch-integration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cloudwatch-integration-syntax.json"></a>

```
{
  "Type" : "AWS::CloudWatch::Integration",
  "Properties" : {
      "[Credential](#cfn-cloudwatch-integration-credential)" : {{IntegrationCredential}},
      "[IntegrationAttributes](#cfn-cloudwatch-integration-integrationattributes)" : {{{{{Key}}: {{Value}}, ...}}},
      "[IntegrationType](#cfn-cloudwatch-integration-integrationtype)" : {{String}},
      "[Name](#cfn-cloudwatch-integration-name)" : {{String}},
      "[RoleArn](#cfn-cloudwatch-integration-rolearn)" : {{String}},
      "[Tags](#cfn-cloudwatch-integration-tags)" : {{[ TagsItems, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cloudwatch-integration-syntax.yaml"></a>

```
Type: AWS::CloudWatch::Integration
Properties:
  [Credential](#cfn-cloudwatch-integration-credential): {{
    IntegrationCredential}}
  [IntegrationAttributes](#cfn-cloudwatch-integration-integrationattributes): {{
    {{Key}}: {{Value}}}}
  [IntegrationType](#cfn-cloudwatch-integration-integrationtype): {{String}}
  [Name](#cfn-cloudwatch-integration-name): {{String}}
  [RoleArn](#cfn-cloudwatch-integration-rolearn): {{String}}
  [Tags](#cfn-cloudwatch-integration-tags): {{
    - TagsItems}}
```

## Properties
<a name="aws-resource-cloudwatch-integration-properties"></a>

`Credential`  <a name="cfn-cloudwatch-integration-credential"></a>
Property description not available.
*Required*: No
*Type*: [IntegrationCredential](aws-properties-cloudwatch-integration-integrationcredential.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationAttributes`  <a name="cfn-cloudwatch-integration-integrationattributes"></a>
Property description not available.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationType`  <a name="cfn-cloudwatch-integration-integrationtype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_CONFIG_SLREC | AWS_INTEGRATION | EXTERNAL_AGENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloudwatch-integration-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-cloudwatch-integration-rolearn"></a>
Property description not available.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-integration-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-cloudwatch-integration-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-integration-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-integration-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-cloudwatch-integration-return-values-fn--getatt"></a>

####
<a name="aws-resource-cloudwatch-integration-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Property description not available.

`IntegrationArn`  <a name="IntegrationArn-fn::getatt"></a>
Property description not available.

`IntegrationId`  <a name="IntegrationId-fn::getatt"></a>
Property description not available.

`Status`  <a name="Status-fn::getatt"></a>
Property description not available.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
Property description not available.

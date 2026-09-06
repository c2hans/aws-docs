---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-inspectorv2-codesecurityintegration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::InspectorV2::CodeSecurityIntegration
<a name="aws-resource-inspectorv2-codesecurityintegration"></a>

Creates a code security integration with a source code repository provider.

## Syntax
<a name="aws-resource-inspectorv2-codesecurityintegration-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-inspectorv2-codesecurityintegration-syntax.json"></a>

```
{
  "Type" : "AWS::InspectorV2::CodeSecurityIntegration",
  "Properties" : {
      "[CreateIntegrationDetails](#cfn-inspectorv2-codesecurityintegration-createintegrationdetails)" : {{CreateDetails}},
      "[Name](#cfn-inspectorv2-codesecurityintegration-name)" : {{String}},
      "[Tags](#cfn-inspectorv2-codesecurityintegration-tags)" : {{{{{Key}}: {{Value}}, ...}}},
      "[Type](#cfn-inspectorv2-codesecurityintegration-type)" : {{String}},
      "[UpdateIntegrationDetails](#cfn-inspectorv2-codesecurityintegration-updateintegrationdetails)" : {{UpdateDetails}}
    }
}
```

### YAML
<a name="aws-resource-inspectorv2-codesecurityintegration-syntax.yaml"></a>

```
Type: AWS::InspectorV2::CodeSecurityIntegration
Properties:
  [CreateIntegrationDetails](#cfn-inspectorv2-codesecurityintegration-createintegrationdetails): {{
    CreateDetails}}
  [Name](#cfn-inspectorv2-codesecurityintegration-name): {{String}}
  [Tags](#cfn-inspectorv2-codesecurityintegration-tags): {{
    {{Key}}: {{Value}}}}
  [Type](#cfn-inspectorv2-codesecurityintegration-type): {{String}}
  [UpdateIntegrationDetails](#cfn-inspectorv2-codesecurityintegration-updateintegrationdetails): {{
    UpdateDetails}}
```

## Properties
<a name="aws-resource-inspectorv2-codesecurityintegration-properties"></a>

`CreateIntegrationDetails`  <a name="cfn-inspectorv2-codesecurityintegration-createintegrationdetails"></a>
Contains details required to create a code security integration with a specific repository provider.
*Required*: No
*Type*: [CreateDetails](aws-properties-inspectorv2-codesecurityintegration-createdetails.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-inspectorv2-codesecurityintegration-name"></a>
The name of the code security integration.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9-_$:.]*$`
*Minimum*: `1`
*Maximum*: `60`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-inspectorv2-codesecurityintegration-tags"></a>
The tags to apply to the code security integration.
*Required*: No
*Type*: Object of String
*Pattern*: `^.{2,127}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-inspectorv2-codesecurityintegration-type"></a>
The type of repository provider for the integration.
*Required*: No
*Type*: String
*Allowed values*: `GITLAB_SELF_MANAGED | GITHUB`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`UpdateIntegrationDetails`  <a name="cfn-inspectorv2-codesecurityintegration-updateintegrationdetails"></a>
The updated integration details specific to the repository provider type.
*Required*: No
*Type*: [UpdateDetails](aws-properties-inspectorv2-codesecurityintegration-updatedetails.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-inspectorv2-codesecurityintegration-return-values"></a>

### Ref
<a name="aws-resource-inspectorv2-codesecurityintegration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the ARN of the code security integration.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-inspectorv2-codesecurityintegration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-inspectorv2-codesecurityintegration-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the code security integration.

`AuthorizationUrl`  <a name="AuthorizationUrl-fn::getatt"></a>
The URL used to authorize the integration with the repository provider.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the code security integration was created.

`LastUpdatedAt`  <a name="LastUpdatedAt-fn::getatt"></a>
The timestamp when the code security integration was last updated.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the integration.

`StatusReason`  <a name="StatusReason-fn::getatt"></a>
The reason for the current status of the code security integration.

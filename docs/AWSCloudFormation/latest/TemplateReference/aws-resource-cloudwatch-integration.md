---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cloudwatch-integration.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CloudWatch::Integration
<a name="aws-resource-cloudwatch-integration"></a>

Resource Type definition for `AWS::CloudWatch::Integration`. Manages a CloudWatch (Amazon CloudWatch Observability / Omni) account-scoped integration. V1 supports AWS\_CONFIG\_SLREC, AWS\_INTEGRATION, and EXTERNAL\_AGENT.

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
Type-specific configuration attributes (max 50 entries). EXTERNAL\_AGENT requires 'catalogId'. On update, supplied attributes merge into the existing map; omitting a key does not remove it.
*Required*: No
*Type*: Object of String
*Pattern*: `^.+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`IntegrationType`  <a name="cfn-cloudwatch-integration-integrationtype"></a>
The type of integration. Immutable after creation.
*Required*: Yes
*Type*: String
*Allowed values*: `AWS_CONFIG_SLREC | AWS_INTEGRATION | EXTERNAL_AGENT`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cloudwatch-integration-name"></a>
The customer-supplied name of the integration. Unique per account.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RoleArn`  <a name="cfn-cloudwatch-integration-rolearn"></a>
IAM role ARN the integration assumes. Required for AWS\_INTEGRATION (a valid, service-assumable IAM role ARN). Not used by AWS\_CONFIG\_SLREC or EXTERNAL\_AGENT.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-cloudwatch-integration-tags"></a>
Tags associated with the integration.
*Required*: No
*Type*: Array of [TagsItems](aws-properties-cloudwatch-integration-tagsitems.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cloudwatch-integration-return-values"></a>

### Ref
<a name="aws-resource-cloudwatch-integration-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `IntegrationArn` property.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cloudwatch-integration-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cloudwatch-integration-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The time at which the integration was created.

`IntegrationArn`  <a name="IntegrationArn-fn::getatt"></a>
The ARN of the integration. arn:aws:cloudwatch:{region}:{account}:integration/{integrationId}.

`IntegrationId`  <a name="IntegrationId-fn::getatt"></a>
The service-generated unique identifier (UUID) of the integration.

`Status`  <a name="Status-fn::getatt"></a>
Lifecycle status of the integration.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The time at which the integration was last updated.

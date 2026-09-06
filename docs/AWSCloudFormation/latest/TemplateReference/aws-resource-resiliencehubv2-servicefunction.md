---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-resiliencehubv2-servicefunction.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ResilienceHubV2::ServiceFunction
<a name="aws-resource-resiliencehubv2-servicefunction"></a>

Represents a logical component of a service.

## Syntax
<a name="aws-resource-resiliencehubv2-servicefunction-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-resiliencehubv2-servicefunction-syntax.json"></a>

```
{
  "Type" : "AWS::ResilienceHubV2::ServiceFunction",
  "Properties" : {
      "[Criticality](#cfn-resiliencehubv2-servicefunction-criticality)" : {{String}},
      "[Description](#cfn-resiliencehubv2-servicefunction-description)" : {{String}},
      "[Name](#cfn-resiliencehubv2-servicefunction-name)" : {{String}},
      "[ServiceArn](#cfn-resiliencehubv2-servicefunction-servicearn)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-resiliencehubv2-servicefunction-syntax.yaml"></a>

```
Type: AWS::ResilienceHubV2::ServiceFunction
Properties:
  [Criticality](#cfn-resiliencehubv2-servicefunction-criticality): {{String}}
  [Description](#cfn-resiliencehubv2-servicefunction-description): {{String}}
  [Name](#cfn-resiliencehubv2-servicefunction-name): {{String}}
  [ServiceArn](#cfn-resiliencehubv2-servicefunction-servicearn): {{String}}
```

## Properties
<a name="aws-resource-resiliencehubv2-servicefunction-properties"></a>

`Criticality`  <a name="cfn-resiliencehubv2-servicefunction-criticality"></a>
The criticality level of the service function.
*Required*: Yes
*Type*: String
*Allowed values*: `PRIMARY | SUPPLEMENTAL`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Description`  <a name="cfn-resiliencehubv2-servicefunction-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Maximum*: `500`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-resiliencehubv2-servicefunction-name"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Pattern*: `^[A-Za-z0-9][A-Za-z0-9_\-]{1,59}$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ServiceArn`  <a name="cfn-resiliencehubv2-servicefunction-servicearn"></a>
ARN identifier.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:(aws|aws-cn|aws-iso|aws-iso-[a-z]{1}|aws-us-gov):[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:([a-z]{2}-((iso[a-z]{0,1}-)|(gov-)){0,1}[a-z]+-[0-9]):[0-9]{12}:[A-Za-z0-9/][A-Za-z0-9:_/+.-]{0,1023}$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-resiliencehubv2-servicefunction-return-values"></a>

### Ref
<a name="aws-resource-resiliencehubv2-servicefunction-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-resiliencehubv2-servicefunction-return-values-fn--getatt"></a>

####
<a name="aws-resource-resiliencehubv2-servicefunction-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The timestamp when the service function was created.

`ResourceCount`  <a name="ResourceCount-fn::getatt"></a>
The number of resources associated with the service function.

`ServiceFunctionId`  <a name="ServiceFunctionId-fn::getatt"></a>
The unique identifier of the service function.

`Source`  <a name="Source-fn::getatt"></a>
The source of the service function.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The timestamp when the service function was last updated.

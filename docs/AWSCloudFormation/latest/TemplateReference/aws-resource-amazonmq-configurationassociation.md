---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-amazonmq-configurationassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AmazonMQ::ConfigurationAssociation
<a name="aws-resource-amazonmq-configurationassociation"></a>

<a name="aws-resource-amazonmq-configurationassociation-description"></a>The `AWS::AmazonMQ::ConfigurationAssociation` resource Property description not available. for AmazonMQ.

## Syntax
<a name="aws-resource-amazonmq-configurationassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-amazonmq-configurationassociation-syntax.json"></a>

```
{
  "Type" : "AWS::AmazonMQ::ConfigurationAssociation",
  "Properties" : {
      "[Broker](#cfn-amazonmq-configurationassociation-broker)" : {{String}},
      "[Configuration](#cfn-amazonmq-configurationassociation-configuration)" : {{ConfigurationId}}
    }
}
```

### YAML
<a name="aws-resource-amazonmq-configurationassociation-syntax.yaml"></a>

```
Type: AWS::AmazonMQ::ConfigurationAssociation
Properties:
  [Broker](#cfn-amazonmq-configurationassociation-broker): {{String}}
  [Configuration](#cfn-amazonmq-configurationassociation-configuration): {{
    ConfigurationId}}
```

## Properties
<a name="aws-resource-amazonmq-configurationassociation-properties"></a>

`Broker`  <a name="cfn-amazonmq-configurationassociation-broker"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Configuration`  <a name="cfn-amazonmq-configurationassociation-configuration"></a>
Returns information about all configurations.
*Required*: Yes
*Type*: [ConfigurationId](aws-properties-amazonmq-configurationassociation-configurationid.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-amazonmq-configurationassociation-return-values"></a>

### Ref
<a name="aws-resource-amazonmq-configurationassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon MQ configurationassociation ID. For example:

 `c-1234a5b6-78cd-901e-2fgh-3i45j6k178l9`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-amazonmq-configurationassociation-return-values-fn--getatt"></a>

## Examples
<a name="aws-resource-amazonmq-configurationassociation--examples"></a>

### ConfigurationAssociation
<a name="aws-resource-amazonmq-configurationassociation--examples--ConfigurationAssociation"></a>

The following example creates an Amazon MQ for ActiveMQ ConfigurationAssociation.

#### JSON
<a name="aws-resource-amazonmq-configurationassociation--examples--ConfigurationAssociation--json"></a>

```
"ConfigurationAssociation1": {
		"Type": "AWS::AmazonMQ::ConfigurationAssociation",
		"Properties": {
			"Broker": {
				"Ref": "Broker1"
			},
			"Configuration": {
				"Id": {
					"Ref": "Configuration1"
				},
				"Revision": {
					"Fn::GetAtt": [
						"Configuration1",
						"Revision"
					]
				}
			}
		}
	}
```

#### YAML
<a name="aws-resource-amazonmq-configurationassociation--examples--ConfigurationAssociation--yaml"></a>

```
 ConfigurationAssociation1:
    Type: AWS::AmazonMQ::ConfigurationAssociation
    Properties:
      Broker: {Ref: Broker1}
      Configuration:
        Id: {Ref: Configuration1}
        Revision: {'Fn::GetAtt': [Configuration1, Revision]}
```

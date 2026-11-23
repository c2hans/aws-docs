---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-agentregistry-publisher.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::AgentRegistry::Publisher

AWS Agent Registry lets you register and discover agents, tools, and related resources. A Publisher is a verified public identity under which your organization publishes records for public discovery. The `AWS::AgentRegistry::Publisher` resource specifies a publisher for a domain that you control.

## Syntax
<a name="aws-resource-agentregistry-publisher-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-agentregistry-publisher-syntax.json"></a>

```json
{
  "Type" : "AWS::AgentRegistry::Publisher",
  "Properties" : {
      "[Tags](#cfn-agentregistry-publisher-tags)" : {{[ Tag, ... ]}},
      "[Value](#cfn-agentregistry-publisher-value)" : {{Identifier}}
    }
}
```

### YAML
<a name="aws-resource-agentregistry-publisher-syntax.yaml"></a>

```yaml
Type: AWS::AgentRegistry::Publisher
Properties:
  [Tags](#cfn-agentregistry-publisher-tags): {{
    - Tag}}
  [Value](#cfn-agentregistry-publisher-value): {{
    Identifier}}
```

## Properties
<a name="aws-resource-agentregistry-publisher-properties"></a>

`Tags`  <a name="cfn-agentregistry-publisher-tags"></a>
A list of key-value pairs that contain metadata for the publisher. For more information, see [Tagging AWS resources](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html) in the *AWS General Reference Guide*.
*Required*: No
*Type*: Array of [Tag](aws-properties-agentregistry-publisher-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Value`  <a name="cfn-agentregistry-publisher-value"></a>
The `Value` property specifies the publisher identifier. The only supported identifier is a domain, which you specify with the `Domain` property. For instructions on verifying the domain during resource creation, see [Creating a Publisher with AWS CloudFormation](https://docs.aws.amazon.com/bedrock-agentcore/latest/devguide/registry-publishers.html#registry-publishers-create-cloudformation) in the *AWS Agent Registry Developer Guide*.
*Required*: Yes
*Type*: [Identifier](aws-properties-agentregistry-publisher-identifier.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-agentregistry-publisher-return-values"></a>

### Ref
<a name="aws-resource-agentregistry-publisher-return-values-ref"></a>

 When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns

The Amazon Resource Name (ARN) of the publisher.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-agentregistry-publisher-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-agentregistry-publisher-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The `CreatedAt` attribute contains the timestamp when the publisher was created.

`PublisherArn`  <a name="PublisherArn-fn::getatt"></a>
The `PublisherArn` attribute contains the ARN of the publisher. The ARN does not include an AWS Region because the publisher applies across all AWS Regions.

`Status`  <a name="Status-fn::getatt"></a>
The `Status` attribute indicates the publisher verification state. It can have one of the following values:
+ `ACTION_REQUIRED` – The Publisher requires domain verification. You can retrieve the challenge through `GetPublisher`, and publish the returned Domain Name System (DNS) TXT record.
+ `ACTIVE` – Domain verification succeeded. The Publisher can accept new registry record associations.
+ `FAILED` – Domain verification failed. Confirm that the DNS TXT record matches the expected name and value before retrying.
+ `SUSPENDED` – The previously verified DNS TXT record is missing. Restore the expected record to allow domain verification to succeed again.
+ `DELETING` – The Publisher is being deleted.

`UpdatedAt`  <a name="UpdatedAt-fn::getatt"></a>
The `UpdatedAt` attribute contains the timestamp when the publisher was last updated.

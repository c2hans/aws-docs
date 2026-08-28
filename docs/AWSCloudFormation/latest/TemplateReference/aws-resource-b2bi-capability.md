---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-b2bi-capability.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Capability
<a name="aws-resource-b2bi-capability"></a>

Instantiates a capability based on the specified parameters. A trading capability contains the information required to transform incoming EDI documents into JSON or XML outputs.

## Syntax
<a name="aws-resource-b2bi-capability-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-b2bi-capability-syntax.json"></a>

```
{
  "Type" : "AWS::B2BI::Capability",
  "Properties" : {
      "[Configuration](#cfn-b2bi-capability-configuration)" : {{CapabilityConfiguration}},
      "[InstructionsDocuments](#cfn-b2bi-capability-instructionsdocuments)" : {{[ S3Location, ... ]}},
      "[Name](#cfn-b2bi-capability-name)" : {{String}},
      "[Tags](#cfn-b2bi-capability-tags)" : {{[ Tag, ... ]}},
      "[Type](#cfn-b2bi-capability-type)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-b2bi-capability-syntax.yaml"></a>

```
Type: AWS::B2BI::Capability
Properties:
  [Configuration](#cfn-b2bi-capability-configuration): {{
    CapabilityConfiguration}}
  [InstructionsDocuments](#cfn-b2bi-capability-instructionsdocuments): {{
    - S3Location}}
  [Name](#cfn-b2bi-capability-name): {{String}}
  [Tags](#cfn-b2bi-capability-tags): {{
    - Tag}}
  [Type](#cfn-b2bi-capability-type): {{String}}
```

## Properties
<a name="aws-resource-b2bi-capability-properties"></a>

`Configuration`  <a name="cfn-b2bi-capability-configuration"></a>
Specifies a structure that contains the details for a capability.
*Required*: Yes
*Type*: [CapabilityConfiguration](aws-properties-b2bi-capability-capabilityconfiguration.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstructionsDocuments`  <a name="cfn-b2bi-capability-instructionsdocuments"></a>
Specifies one or more locations in Amazon S3, each specifying an EDI document that can be used with this capability. Each item contains the name of the bucket and the key, to identify the document's location.
*Required*: No
*Type*: Array of [S3Location](aws-properties-b2bi-capability-s3location.md)
*Minimum*: `0`
*Maximum*: `5`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-b2bi-capability-name"></a>
The display name of the capability.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-b2bi-capability-tags"></a>
Specifies the key-value pairs assigned to ARNs that you can use to group and search for resources by type. You can attach this metadata to resources (capabilities, partnerships, and so on) for any purpose.
*Required*: No
*Type*: Array of [Tag](aws-properties-b2bi-capability-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Type`  <a name="cfn-b2bi-capability-type"></a>
Returns the type of the capability. Currently, only `edi` is supported.
*Required*: Yes
*Type*: String
*Allowed values*: `edi`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-b2bi-capability-return-values"></a>

### Ref
<a name="aws-resource-b2bi-capability-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-b2bi-capability-return-values-fn--getatt"></a>

####
<a name="aws-resource-b2bi-capability-return-values-fn--getatt-fn--getatt"></a>

`CapabilityArn`  <a name="CapabilityArn-fn::getatt"></a>
Returns an Amazon Resource Name (ARN) for a specific AWS resource, such as a capability, partnership, profile, or transformer.

`CapabilityId`  <a name="CapabilityId-fn::getatt"></a>
Returns a system-assigned unique identifier for the capability.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Returns a timestamp for creation date and time of the capability.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
Returns a timestamp that identifies the most recent date and time that the capability was modified.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

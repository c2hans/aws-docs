---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-b2bi-transformer.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Transformer
<a name="aws-resource-b2bi-transformer"></a>

Creates a transformer. AWS B2B Data Interchange currently supports two scenarios:
+ *Inbound EDI*: the AWS customer receives an EDI file from their trading partner. AWS B2B Data Interchange converts this EDI file into a JSON or XML file with a service-defined structure. A mapping template provided by the customer, in JSONata or XSLT format, is optionally applied to this file to produce a JSON or XML file with the structure the customer requires.
+ *Outbound EDI*: the AWS customer has a JSON or XML file containing data that they wish to use in an EDI file. A mapping template, provided by the customer (in either JSONata or XSLT format) is applied to this file to generate a JSON or XML file in the service-defined structure. This file is then converted to an EDI file.

**Note**
The following fields are provided for backwards compatibility only: `fileFormat`, `mappingTemplate`, `ediType`, and `sampleDocument`.
Use the `mapping` data type in place of `mappingTemplate` and `fileFormat`
Use the `sampleDocuments` data type in place of `sampleDocument`
Use either the `inputConversion` or `outputConversion` in place of `ediType`

## Syntax
<a name="aws-resource-b2bi-transformer-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-b2bi-transformer-syntax.json"></a>

```
{
  "Type" : "AWS::B2BI::Transformer",
  "Properties" : {
      "[InputConversion](#cfn-b2bi-transformer-inputconversion)" : {{InputConversion}},
      "[Mapping](#cfn-b2bi-transformer-mapping)" : {{Mapping}},
      "[Name](#cfn-b2bi-transformer-name)" : {{String}},
      "[OutputConversion](#cfn-b2bi-transformer-outputconversion)" : {{OutputConversion}},
      "[SampleDocuments](#cfn-b2bi-transformer-sampledocuments)" : {{SampleDocuments}},
      "[Status](#cfn-b2bi-transformer-status)" : {{String}},
      "[Tags](#cfn-b2bi-transformer-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-b2bi-transformer-syntax.yaml"></a>

```
Type: AWS::B2BI::Transformer
Properties:
  [InputConversion](#cfn-b2bi-transformer-inputconversion): {{
    InputConversion}}
  [Mapping](#cfn-b2bi-transformer-mapping): {{
    Mapping}}
  [Name](#cfn-b2bi-transformer-name): {{String}}
  [OutputConversion](#cfn-b2bi-transformer-outputconversion): {{
    OutputConversion}}
  [SampleDocuments](#cfn-b2bi-transformer-sampledocuments): {{
    SampleDocuments}}
  [Status](#cfn-b2bi-transformer-status): {{String}}
  [Tags](#cfn-b2bi-transformer-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-b2bi-transformer-properties"></a>

`InputConversion`  <a name="cfn-b2bi-transformer-inputconversion"></a>
Returns a structure that contains the format options for the transformation.
*Required*: No
*Type*: [InputConversion](aws-properties-b2bi-transformer-inputconversion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Mapping`  <a name="cfn-b2bi-transformer-mapping"></a>
Returns the structure that contains the mapping template and its language (either XSLT or JSONATA).
*Required*: No
*Type*: [Mapping](aws-properties-b2bi-transformer-mapping.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-b2bi-transformer-name"></a>
Returns the descriptive name for the transformer.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9_-]{1,512}$`
*Minimum*: `1`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`OutputConversion`  <a name="cfn-b2bi-transformer-outputconversion"></a>
Returns the `OutputConversion` object, which contains the format options for the outbound transformation.
*Required*: No
*Type*: [OutputConversion](aws-properties-b2bi-transformer-outputconversion.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`SampleDocuments`  <a name="cfn-b2bi-transformer-sampledocuments"></a>
Returns a structure that contains the Amazon S3 bucket and an array of the corresponding keys used to identify the location for your sample documents.
*Required*: No
*Type*: [SampleDocuments](aws-properties-b2bi-transformer-sampledocuments.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-b2bi-transformer-status"></a>
Returns the state of the newly created transformer. The transformer can be either `active` or `inactive`. For the transformer to be used in a capability, its status must `active`.
*Required*: Yes
*Type*: String
*Allowed values*: `active | inactive`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-b2bi-transformer-tags"></a>
A key-value pair for a specific transformer. Tags are metadata that you can use to search for and group capabilities for various purposes.
*Required*: No
*Type*: Array of [Tag](aws-properties-b2bi-transformer-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-b2bi-transformer-return-values"></a>

### Ref
<a name="aws-resource-b2bi-transformer-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-b2bi-transformer-return-values-fn--getatt"></a>

####
<a name="aws-resource-b2bi-transformer-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Returns a timestamp indicating when the transformer was created. For example, `2023-07-20T19:58:44.624Z`.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
Returns a timestamp representing the date and time for the most recent change for the transformer object.

`TransformerArn`  <a name="TransformerArn-fn::getatt"></a>
Returns an Amazon Resource Name (ARN) for a specific transformer.

`TransformerId`  <a name="TransformerId-fn::getatt"></a>
The system-assigned unique identifier for the transformer.

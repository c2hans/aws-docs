---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-sdb-domain.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SDB::Domain
<a name="aws-resource-sdb-domain"></a>

 Use the `AWS::SDB::Domain` resource to declare a SimpleDB domain. When you specify `AWS::SDB::Domain` as an argument in a `Ref` function, AWS CloudFormation returns the value of the `DomainName`.

**Important**
 The `AWS::SDB::Domain` resource does not allow any updates, including metadata updates.

## Syntax
<a name="aws-resource-sdb-domain-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-sdb-domain-syntax.json"></a>

```
{
  "Type" : "AWS::SDB::Domain",
  "Properties" : {
      "[Description](#cfn-sdb-domain-description)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-sdb-domain-syntax.yaml"></a>

```
Type: AWS::SDB::Domain
Properties:
  [Description](#cfn-sdb-domain-description): {{String}}
```

## Properties
<a name="aws-resource-sdb-domain-properties"></a>

`Description`  <a name="cfn-sdb-domain-description"></a>
Information about the SimpleDB domain.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-sdb-domain-return-values"></a>

### Ref
<a name="aws-resource-sdb-domain-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the value of the `DomainName`, such as: `Domain1-123456789012`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-sdb-domain-return-values-fn--getatt"></a>

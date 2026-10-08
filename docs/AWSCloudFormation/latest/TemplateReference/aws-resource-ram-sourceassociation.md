---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ram-sourceassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::RAM::SourceAssociation
<a name="aws-resource-ram-sourceassociation"></a>

Associates a specified source account with a resource share.

## Syntax
<a name="aws-resource-ram-sourceassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ram-sourceassociation-syntax.json"></a>

```
{
  "Type" : "AWS::RAM::SourceAssociation",
  "Properties" : {
      "[ResourceShareArn](#cfn-ram-sourceassociation-resourcesharearn)" : {{String}},
      "[SourceId](#cfn-ram-sourceassociation-sourceid)" : {{String}}
    }
}
```

### YAML
<a name="aws-resource-ram-sourceassociation-syntax.yaml"></a>

```
Type: AWS::RAM::SourceAssociation
Properties:
  [ResourceShareArn](#cfn-ram-sourceassociation-resourcesharearn): {{String}}
  [SourceId](#cfn-ram-sourceassociation-sourceid): {{String}}
```

## Properties
<a name="aws-resource-ram-sourceassociation-properties"></a>

`ResourceShareArn`  <a name="cfn-ram-sourceassociation-resourcesharearn"></a>
Specifies the [Amazon Resource Name (ARN)](https://docs.aws.amazon.com/general/latest/gr/aws-arns-and-namespaces.html) of the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SourceId`  <a name="cfn-ram-sourceassociation-sourceid"></a>
Specifies the ID of the source account to associate with the resource share.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

## Return values
<a name="aws-resource-ram-sourceassociation-return-values"></a>

### Ref
<a name="aws-resource-ram-sourceassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource share ARN and source ID in the format `resource-share-arn|source-id`. For example: `arn:aws:ram:us-east-1:999999999999:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2|999999999999`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ram-sourceassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ram-sourceassociation-return-values-fn--getatt-fn--getatt"></a>

`CreationTime`  <a name="CreationTime-fn::getatt"></a>
The date and time when the association was created.

`LastUpdatedTime`  <a name="LastUpdatedTime-fn::getatt"></a>
The date and time when the association was last updated.

`SourceType`  <a name="SourceType-fn::getatt"></a>
The type of the source. This value is always `SOURCE` for this resource type.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the association. Possible values include `ASSOCIATING`, `ASSOCIATED`, `FAILED`, `DISASSOCIATING`, `DISASSOCIATED`, `SUSPENDED`, `SUSPENDING`, and `RESTORING`.

## Examples
<a name="aws-resource-ram-sourceassociation--examples"></a>

### Associating a source account with a resource share
<a name="aws-resource-ram-sourceassociation--examples--Associating_a_source_account_with_a_resource_share"></a>

The following example associates a source account with a resource share.

#### YAML
<a name="aws-resource-ram-sourceassociation--examples--Associating_a_source_account_with_a_resource_share--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MySourceAssociation:
    Type: AWS::RAM::SourceAssociation
    Properties:
      ResourceShareArn: !Sub arn:aws:ram:${AWS::Region}:${AWS::AccountId}:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2
      SourceId: '999999999999'
```

#### JSON
<a name="aws-resource-ram-sourceassociation--examples--Associating_a_source_account_with_a_resource_share--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MySourceAssociation": {
      "Type": "AWS::RAM::SourceAssociation",
      "Properties": {
        "ResourceShareArn": {
          "Fn::Sub": "arn:aws:ram:${AWS::Region}:${AWS::AccountId}:resource-share/27d09b4b-5e12-41d1-a4f2-19ded10982e2"
        },
        "SourceId": "999999999999"
      }
    }
  }
}
```

## See also
<a name="aws-resource-ram-sourceassociation--seealso"></a>
+ [AssociateResourceShare](https://docs.aws.amazon.com/ram/latest/APIReference/API_AssociateResourceShare.html) in the *AWS Resource Access Manager API Reference*
+  [AWS Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide)

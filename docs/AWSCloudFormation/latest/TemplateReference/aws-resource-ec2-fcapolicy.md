---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-fcapolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy
<a name="aws-resource-ec2-fcapolicy"></a>

<a name="aws-resource-ec2-fcapolicy-description"></a>The `AWS::EC2::FcaPolicy` resource Property description not available. for EC2.

## Syntax
<a name="aws-resource-ec2-fcapolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-fcapolicy-syntax.json"></a>

```
{
  "Type" : "AWS::EC2::FcaPolicy",
  "Properties" : {
      "[Description](#cfn-ec2-fcapolicy-description)" : {{String}},
      "[InstanceFcaPolicyDocument](#cfn-ec2-fcapolicy-instancefcapolicydocument)" : {{InstanceFcaPolicyDocument}},
      "[NatFcaPolicyDocument](#cfn-ec2-fcapolicy-natfcapolicydocument)" : {{NatFcaPolicyDocument}},
      "[NetworkResourceType](#cfn-ec2-fcapolicy-networkresourcetype)" : {{String}},
      "[PcxFcaPolicyDocument](#cfn-ec2-fcapolicy-pcxfcapolicydocument)" : {{PcxFcaPolicyDocument}},
      "[ShowBackEnabled](#cfn-ec2-fcapolicy-showbackenabled)" : {{Boolean}},
      "[Tags](#cfn-ec2-fcapolicy-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-ec2-fcapolicy-syntax.yaml"></a>

```
Type: AWS::EC2::FcaPolicy
Properties:
  [Description](#cfn-ec2-fcapolicy-description): {{String}}
  [InstanceFcaPolicyDocument](#cfn-ec2-fcapolicy-instancefcapolicydocument): {{
    InstanceFcaPolicyDocument}}
  [NatFcaPolicyDocument](#cfn-ec2-fcapolicy-natfcapolicydocument): {{
    NatFcaPolicyDocument}}
  [NetworkResourceType](#cfn-ec2-fcapolicy-networkresourcetype): {{String}}
  [PcxFcaPolicyDocument](#cfn-ec2-fcapolicy-pcxfcapolicydocument): {{
    PcxFcaPolicyDocument}}
  [ShowBackEnabled](#cfn-ec2-fcapolicy-showbackenabled): {{Boolean}}
  [Tags](#cfn-ec2-fcapolicy-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-ec2-fcapolicy-properties"></a>

`Description`  <a name="cfn-ec2-fcapolicy-description"></a>
Property description not available.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceFcaPolicyDocument`  <a name="cfn-ec2-fcapolicy-instancefcapolicydocument"></a>
Property description not available.
*Required*: No
*Type*: [InstanceFcaPolicyDocument](aws-properties-ec2-fcapolicy-instancefcapolicydocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatFcaPolicyDocument`  <a name="cfn-ec2-fcapolicy-natfcapolicydocument"></a>
Property description not available.
*Required*: No
*Type*: [NatFcaPolicyDocument](aws-properties-ec2-fcapolicy-natfcapolicydocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkResourceType`  <a name="cfn-ec2-fcapolicy-networkresourcetype"></a>
Property description not available.
*Required*: Yes
*Type*: String
*Allowed values*: `natgw | pcx | ec2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PcxFcaPolicyDocument`  <a name="cfn-ec2-fcapolicy-pcxfcapolicydocument"></a>
Property description not available.
*Required*: No
*Type*: [PcxFcaPolicyDocument](aws-properties-ec2-fcapolicy-pcxfcapolicydocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShowBackEnabled`  <a name="cfn-ec2-fcapolicy-showbackenabled"></a>
Property description not available.
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-fcapolicy-tags"></a>
Property description not available.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-fcapolicy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-fcapolicy-return-values"></a>

### Ref
<a name="aws-resource-ec2-fcapolicy-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-ec2-fcapolicy-return-values-fn--getatt"></a>

####
<a name="aws-resource-ec2-fcapolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
Property description not available.

`FcaPolicyId`  <a name="FcaPolicyId-fn::getatt"></a>
Property description not available.

`LatestVersion`  <a name="LatestVersion-fn::getatt"></a>
Property description not available.

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
Property description not available.

`PolicyCreatedAt`  <a name="PolicyCreatedAt-fn::getatt"></a>
Property description not available.

`VersionExpectedEffectiveAt`  <a name="VersionExpectedEffectiveAt-fn::getatt"></a>
Property description not available.

---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-ec2-fcapolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::EC2::FcaPolicy

Networking Flexible Cost Allocation (FCA) is a feature of Amazon VPC that lets you specify an FCA policy. An FCA policy defines how shared network costs, such as data transfer and data processing, are allocated and reported for network resources such as NAT gateways, Amazon EC2 instances, and VPC peering connections.

## Syntax
<a name="aws-resource-ec2-fcapolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-ec2-fcapolicy-syntax.json"></a>

```json
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

```yaml
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
The description of the FCA policy.
*Required*: No
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`InstanceFcaPolicyDocument`  <a name="cfn-ec2-fcapolicy-instancefcapolicydocument"></a>
The FCA policy document for EC2 instance cost allocation. This property is required when `NetworkResourceType` is `ec2`, and you can't specify it for other resource types.
*Required*: No
*Type*: [InstanceFcaPolicyDocument](aws-properties-ec2-fcapolicy-instancefcapolicydocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NatFcaPolicyDocument`  <a name="cfn-ec2-fcapolicy-natfcapolicydocument"></a>
The FCA policy document for NAT gateway cost allocation. This property is required when `NetworkResourceType` is `natgw`, and you can't specify it for other resource types.
*Required*: No
*Type*: [NatFcaPolicyDocument](aws-properties-ec2-fcapolicy-natfcapolicydocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`NetworkResourceType`  <a name="cfn-ec2-fcapolicy-networkresourcetype"></a>
The type of network resource that the FCA policy applies to.
Specify the policy document that matches the resource type: `NatFcaPolicyDocument` for `natgw`, `InstanceFcaPolicyDocument` for `ec2`, or `PcxFcaPolicyDocument` for `pcx`. Don't specify a policy document for a different resource type.
*Required*: Yes
*Type*: String
*Allowed values*: `natgw | pcx | ec2`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PcxFcaPolicyDocument`  <a name="cfn-ec2-fcapolicy-pcxfcapolicydocument"></a>
The FCA policy document for VPC peering connection cost allocation. This property is required when `NetworkResourceType` is `pcx`, and you can't specify it for other resource types.
*Required*: No
*Type*: [PcxFcaPolicyDocument](aws-properties-ec2-fcapolicy-pcxfcapolicydocument.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ShowBackEnabled`  <a name="cfn-ec2-fcapolicy-showbackenabled"></a>
Specifies whether showback reporting is enabled for the FCA policy.
Default: `true`
*Required*: No
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-ec2-fcapolicy-tags"></a>
The tags to apply to the FCA policy.
*Required*: No
*Type*: Array of [Tag](aws-properties-ec2-fcapolicy-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-ec2-fcapolicy-return-values"></a>

### Ref
<a name="aws-resource-ec2-fcapolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the FCA policy.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-ec2-fcapolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-ec2-fcapolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the FCA policy.

`FcaPolicyId`  <a name="FcaPolicyId-fn::getatt"></a>
The ID of the FCA policy, such as `fcap-1234567890abcdef0`.

`LatestVersion`  <a name="LatestVersion-fn::getatt"></a>
The latest version number of the FCA policy.

`OwnerAccount`  <a name="OwnerAccount-fn::getatt"></a>
The ID of the AWS account that owns the FCA policy.

`PolicyCreatedAt`  <a name="PolicyCreatedAt-fn::getatt"></a>
The timestamp when the FCA policy was created.

`VersionExpectedEffectiveAt`  <a name="VersionExpectedEffectiveAt-fn::getatt"></a>
The timestamp when the latest version of the FCA policy is expected to take effect.

## Examples
<a name="aws-resource-ec2-fcapolicy--examples"></a>

### Create an FCA policy for a NAT gateway
<a name="aws-resource-ec2-fcapolicy--examples--Create_an_FCA_policy_for_a_NAT_gateway"></a>

The following example creates a Flex Cost Allocation policy that allocates NAT gateway data transfer and data processing costs, reported at the subnet level.

#### YAML
<a name="aws-resource-ec2-fcapolicy--examples--Create_an_FCA_policy_for_a_NAT_gateway--yaml"></a>

```yaml
MyFcaPolicy:
  Type: AWS::EC2::FcaPolicy
  Properties:
    NetworkResourceType: natgw
    Description: Allocate NAT gateway costs by subnet
    ShowBackEnabled: true
    NatFcaPolicyDocument:
      ReportingGranularity:
        - subnet
      Dimensions:
        - data-transfer
        - data-processing
    Tags:
      - Key: Team
        Value: Networking
```

#### JSON
<a name="aws-resource-ec2-fcapolicy--examples--Create_an_FCA_policy_for_a_NAT_gateway--json"></a>

```json
{
    "MyFcaPolicy": {
        "Type": "AWS::EC2::FcaPolicy",
        "Properties": {
            "NetworkResourceType": "natgw",
            "Description": "Allocate NAT gateway costs by subnet",
            "ShowBackEnabled": true,
            "NatFcaPolicyDocument": {
                "ReportingGranularity": [ "subnet" ],
                "Dimensions": [ "data-transfer", "data-processing" ]
            },
            "Tags": [
                { "Key": "Team", "Value": "Networking" }
            ]
        }
    }
}
```

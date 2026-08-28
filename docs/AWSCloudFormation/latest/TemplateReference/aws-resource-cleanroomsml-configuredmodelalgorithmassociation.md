---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanroomsml-configuredmodelalgorithmassociation.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation"></a>

Associates a configured model algorithm to a collaboration for use by any member of the collaboration.

## Syntax
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation",
  "Properties" : {
      "[ConfiguredModelAlgorithmArn](#cfn-cleanroomsml-configuredmodelalgorithmassociation-configuredmodelalgorithmarn)" : {{String}},
      "[Description](#cfn-cleanroomsml-configuredmodelalgorithmassociation-description)" : {{String}},
      "[MembershipIdentifier](#cfn-cleanroomsml-configuredmodelalgorithmassociation-membershipidentifier)" : {{String}},
      "[Name](#cfn-cleanroomsml-configuredmodelalgorithmassociation-name)" : {{String}},
      "[PrivacyConfiguration](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration)" : {{PrivacyConfiguration}},
      "[Tags](#cfn-cleanroomsml-configuredmodelalgorithmassociation-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-syntax.yaml"></a>

```
Type: AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation
Properties:
  [ConfiguredModelAlgorithmArn](#cfn-cleanroomsml-configuredmodelalgorithmassociation-configuredmodelalgorithmarn): {{String}}
  [Description](#cfn-cleanroomsml-configuredmodelalgorithmassociation-description): {{String}}
  [MembershipIdentifier](#cfn-cleanroomsml-configuredmodelalgorithmassociation-membershipidentifier): {{String}}
  [Name](#cfn-cleanroomsml-configuredmodelalgorithmassociation-name): {{String}}
  [PrivacyConfiguration](#cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration): {{
    PrivacyConfiguration}}
  [Tags](#cfn-cleanroomsml-configuredmodelalgorithmassociation-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-properties"></a>

`ConfiguredModelAlgorithmArn`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-configuredmodelalgorithmarn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm that is associated to the collaboration.
*Required*: Yes
*Type*: String
*Pattern*: `^arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+$`
*Minimum*: `20`
*Maximum*: `2048`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Description`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-description"></a>
The description of the configured model algorithm association.
*Required*: No
*Type*: String
*Pattern*: `^[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*$`
*Maximum*: `255`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MembershipIdentifier`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-membershipidentifier"></a>
The membership ID of the member that created the configured model algorithm association.
*Required*: Yes
*Type*: String
*Pattern*: `^[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}$`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-name"></a>
The name of the configured model algorithm association.
*Required*: Yes
*Type*: String
*Pattern*: `^(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*$`
*Minimum*: `1`
*Maximum*: `63`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PrivacyConfiguration`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration"></a>
Information about the privacy configuration for a configured model algorithm association.
*Required*: No
*Type*: [PrivacyConfiguration](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-privacyconfiguration.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanroomsml-configuredmodelalgorithmassociation-tags"></a>
The optional metadata that you apply to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use `aws:`, `AWS:`, or any upper or lowercase combination of such as a prefix for keys as it is reserved. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has `aws` as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of `aws` do not count against your tags per resource limit.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanroomsml-configuredmodelalgorithmassociation-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-return-values"></a>

### Ref
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN. For example:

 `{ "Ref": "myConfiguredModelAlgorithmAssociation" }`

For the Clean Rooms ML configured model algorithm association, `Ref` returns the ARN of the configured model algorithm association.

Example: `arn:aws:cleanrooms-ml:us-east-1:123456789012:membership/a1b2c3d4-e5f6-7890-abcd-ef1234567890/configured-model-algorithm-association/a1b2c3d4e5f6`

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation-return-values-fn--getatt-fn--getatt"></a>

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
The collaboration ID of the collaboration that contains the configured model algorithm association.

`ConfiguredModelAlgorithmAssociationArn`  <a name="ConfiguredModelAlgorithmAssociationArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association.

## Examples
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation--examples"></a>

### Create a configured model algorithm association
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation--examples--Create_a_configured_model_algorithm_association"></a>

The following example creates a configured model algorithm association with privacy configuration policies.

#### JSON
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation--examples--Create_a_configured_model_algorithm_association--json"></a>

```
{
  "AWSTemplateFormatVersion": "2010-09-09",
  "Resources": {
    "MyConfiguredModelAlgorithmAssociation": {
      "Type": "AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation",
      "Properties": {
        "Name": "MyMLAssociation",
        "MembershipIdentifier": "12345678-1234-1234-1234-123456789012",
        "ConfiguredModelAlgorithmArn": "arn:aws:cleanrooms-ml:us-east-1:123456789012:configured-model-algorithm/my-algorithm",
        "Description": "Association for collaborative ML training",
        "PrivacyConfiguration": {
          "Policies": {
            "TrainedModels": {
              "ContainerLogs": [
                {
                  "AllowedAccountIds": ["123456789012"],
                  "LogType": "ERROR_SUMMARY"
                }
              ],
              "ContainerMetrics": {
                "NoiseLevel": "HIGH"
              }
            },
            "TrainedModelExports": {
              "MaxSize": {
                "Unit": "GB",
                "Value": 10
              },
              "FilesToExport": ["MODEL", "OUTPUT"]
            }
          }
        },
        "Tags": [
          {
            "Key": "Project",
            "Value": "CollaborativeML"
          }
        ]
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-cleanroomsml-configuredmodelalgorithmassociation--examples--Create_a_configured_model_algorithm_association--yaml"></a>

```
AWSTemplateFormatVersion: '2010-09-09'
Resources:
  MyConfiguredModelAlgorithmAssociation:
    Type: AWS::CleanRoomsML::ConfiguredModelAlgorithmAssociation
    Properties:
      Name: MyMLAssociation
      MembershipIdentifier: 12345678-1234-1234-1234-123456789012
      ConfiguredModelAlgorithmArn: arn:aws:cleanrooms-ml:us-east-1:123456789012:configured-model-algorithm/my-algorithm
      Description: Association for collaborative ML training
      PrivacyConfiguration:
        Policies:
          TrainedModels:
            ContainerLogs:
              - AllowedAccountIds:
                  - '123456789012'
                LogType: ERROR_SUMMARY
            ContainerMetrics:
              NoiseLevel: HIGH
          TrainedModelExports:
            MaxSize:
              Unit: GB
              Value: 10
            FilesToExport:
              - MODEL
              - OUTPUT
      Tags:
        - Key: Project
          Value: CollaborativeML
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

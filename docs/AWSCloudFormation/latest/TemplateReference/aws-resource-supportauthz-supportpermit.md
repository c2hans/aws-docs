---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-supportauthz-supportpermit.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SupportAuthZ::SupportPermit
<a name="aws-resource-supportauthz-supportpermit"></a>

The `AWS::SupportAuthZ::SupportPermit` resource creates a support permit that authorizes AWS Support to perform a specific set of actions on one or more of your resources for a bounded period of time. You define which actions are allowed, which resources they apply to, and optional time-window conditions that control when the permit is active.

Each permit is cryptographically signed with a customer managed AWS KMS key so that the authorization is non-repudiable. You can optionally associate a permit with an AWS Support case. For more information, see [Managing support permits](https://docs.aws.amazon.com/awssupport/latest/user/support-authorization-permits.html) in the *AWS Support User Guide*.

**Note**
You can't modify a support permit after you create it. Changing any property other than `Tags` requires replacement: CloudFormation deletes the existing permit and creates a new one.

## Syntax
<a name="aws-resource-supportauthz-supportpermit-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-supportauthz-supportpermit-syntax.json"></a>

```
{
  "Type" : "AWS::SupportAuthZ::SupportPermit",
  "Properties" : {
      "[Description](#cfn-supportauthz-supportpermit-description)" : {{String}},
      "[Name](#cfn-supportauthz-supportpermit-name)" : {{String}},
      "[Permit](#cfn-supportauthz-supportpermit-permit)" : {{Permit}},
      "[SigningKeyInfo](#cfn-supportauthz-supportpermit-signingkeyinfo)" : {{SigningKeyInfo}},
      "[SupportCaseDisplayId](#cfn-supportauthz-supportpermit-supportcasedisplayid)" : {{String}},
      "[Tags](#cfn-supportauthz-supportpermit-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-supportauthz-supportpermit-syntax.yaml"></a>

```
Type: AWS::SupportAuthZ::SupportPermit
Properties:
  [Description](#cfn-supportauthz-supportpermit-description): {{String}}
  [Name](#cfn-supportauthz-supportpermit-name): {{String}}
  [Permit](#cfn-supportauthz-supportpermit-permit): {{
    Permit}}
  [SigningKeyInfo](#cfn-supportauthz-supportpermit-signingkeyinfo): {{
    SigningKeyInfo}}
  [SupportCaseDisplayId](#cfn-supportauthz-supportpermit-supportcasedisplayid): {{String}}
  [Tags](#cfn-supportauthz-supportpermit-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-supportauthz-supportpermit-properties"></a>

`Description`  <a name="cfn-supportauthz-supportpermit-description"></a>
An optional description of the support permit.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-supportauthz-supportpermit-name"></a>
The name of the support permit. The name must be unique within your AWS account in the current Region.
You can't change the name after the permit is created. Specifying a different name replaces the permit.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9]{1,256}$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Permit`  <a name="cfn-supportauthz-supportpermit-permit"></a>
The grant definition for the permit: the actions that AWS Support is authorized to perform, the resources they apply to, and optional time-window conditions.
*Required*: Yes
*Type*: [Permit](aws-properties-supportauthz-supportpermit-permit.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SigningKeyInfo`  <a name="cfn-supportauthz-supportpermit-signingkeyinfo"></a>
The customer managed AWS KMS key used to cryptographically sign the permit.
*Required*: Yes
*Type*: [SigningKeyInfo](aws-properties-supportauthz-supportpermit-signingkeyinfo.md)
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`SupportCaseDisplayId`  <a name="cfn-supportauthz-supportpermit-supportcasedisplayid"></a>
The display identifier of the AWS Support case to associate with the permit. When you specify this value, the permit is linked to the specified support case.
*Required*: No
*Type*: String
*Pattern*: `^[a-zA-Z0-9:/-]{1,512}$`
*Minimum*: `1`
*Maximum*: `512`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-supportauthz-supportpermit-tags"></a>
An array of key-value pairs to apply to this resource.
For more information, see [Tag](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-resource-tags.html).
*Required*: No
*Type*: Array of [Tag](aws-properties-supportauthz-supportpermit-tag.md)
*Maximum*: `50`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-supportauthz-supportpermit-return-values"></a>

### Ref
<a name="aws-resource-supportauthz-supportpermit-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the Amazon Resource Name (ARN) of the support permit, such as `arn:aws:supportauthz:us-east-1:123456789012:supportpermit/2494ccf5-d7b5-434a-adef-79e15e1e3191`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-supportauthz-supportpermit-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-supportauthz-supportpermit-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the support permit.

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
The date and time when the support permit was created, in ISO 8601 format.

`PermitId`  <a name="PermitId-fn::getatt"></a>
The service-generated identifier of the support permit, which is the resource segment of the ARN.

`Status`  <a name="Status-fn::getatt"></a>
The current status of the support permit:
+ `ACTIVE` – The permit is in effect and authorizes the granted actions, subject to any time-window conditions.
+ `INACTIVE` – The permit exists but does not currently authorize any actions.
+ `DELETING` – The permit is being deleted and no longer authorizes any actions.

## Examples
<a name="aws-resource-supportauthz-supportpermit--examples"></a>

**Topics**
+ [Grant time-bounded access to specific actions on specific resources](#aws-resource-supportauthz-supportpermit--examples--Grant_time-bounded_access_to_specific_actions_on_specific_resources)
+ [Grant all actions on all resources in the Region within a time window](#aws-resource-supportauthz-supportpermit--examples--Grant_all_actions_on_all_resources_in_the_Region_within_a_time_window)

### Grant time-bounded access to specific actions on specific resources
<a name="aws-resource-supportauthz-supportpermit--examples--Grant_time-bounded_access_to_specific_actions_on_specific_resources"></a>

The following example creates a support permit that allows two Amazon EC2 read actions on a single instance, active only before a specified time, and signed with a customer managed AWS KMS key.

#### JSON
<a name="aws-resource-supportauthz-supportpermit--examples--Grant_time-bounded_access_to_specific_actions_on_specific_resources--json"></a>

```
{
  "Resources": {
    "ExampleSupportPermit": {
      "Type": "AWS::SupportAuthZ::SupportPermit",
      "Properties": {
        "Name": "ExampleTroubleshootingPermit",
        "Description": "Temporary EC2 read access for support case investigation",
        "SupportCaseDisplayId": "1234567890",
        "Permit": {
          "Actions": { "Actions": [ "ec2:DescribeInstances", "ec2:GetConsoleOutput" ] },
          "Resources": { "Resources": [ "arn:aws:ec2:us-east-1:111122223333:instance/i-0abcd1234efgh5678" ] },
          "Conditions": [ { "AllowBefore": "2026-12-31T23:59:59Z" } ]
        },
        "SigningKeyInfo": {
          "KmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-supportauthz-supportpermit--examples--Grant_time-bounded_access_to_specific_actions_on_specific_resources--yaml"></a>

```
Resources:
  ExampleSupportPermit:
    Type: AWS::SupportAuthZ::SupportPermit
    Properties:
      Name: ExampleTroubleshootingPermit
      Description: Temporary EC2 read access for support case investigation
      SupportCaseDisplayId: "1234567890"
      Permit:
        Actions:
          Actions:
            - ec2:DescribeInstances
            - ec2:GetConsoleOutput
        Resources:
          Resources:
            - arn:aws:ec2:us-east-1:111122223333:instance/i-0abcd1234efgh5678
        Conditions:
          - AllowBefore: "2026-12-31T23:59:59Z"
      SigningKeyInfo:
        KmsKey: arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
```

### Grant all actions on all resources in the Region within a time window
<a name="aws-resource-supportauthz-supportpermit--examples--Grant_all_actions_on_all_resources_in_the_Region_within_a_time_window"></a>

The following example creates a support permit that grants all supported actions on every resource in the current Region during a specific time window, and is signed with a customer managed AWS KMS key.

#### JSON
<a name="aws-resource-supportauthz-supportpermit--examples--Grant_all_actions_on_all_resources_in_the_Region_within_a_time_window--json"></a>

```
{
  "Resources": {
    "BroadSupportPermit": {
      "Type": "AWS::SupportAuthZ::SupportPermit",
      "Properties": {
        "Name": "FullRegionSupportPermit",
        "Description": "Broad time-bounded access for an escalation",
        "Permit": {
          "Actions": { "AllActions": {} },
          "Resources": { "AllResourcesInRegion": {} },
          "Conditions": [
            { "AllowAfter": "2026-09-01T00:00:00Z" },
            { "AllowBefore": "2026-09-08T00:00:00Z" }
          ]
        },
        "SigningKeyInfo": {
          "KmsKey": "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
        }
      }
    }
  }
}
```

#### YAML
<a name="aws-resource-supportauthz-supportpermit--examples--Grant_all_actions_on_all_resources_in_the_Region_within_a_time_window--yaml"></a>

```
Resources:
  BroadSupportPermit:
    Type: AWS::SupportAuthZ::SupportPermit
    Properties:
      Name: FullRegionSupportPermit
      Description: Broad time-bounded access for an escalation
      Permit:
        Actions:
          AllActions: {}
        Resources:
          AllResourcesInRegion: {}
        Conditions:
          - AllowAfter: "2026-09-01T00:00:00Z"
          - AllowBefore: "2026-09-08T00:00:00Z"
      SigningKeyInfo:
        KmsKey: arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab
```

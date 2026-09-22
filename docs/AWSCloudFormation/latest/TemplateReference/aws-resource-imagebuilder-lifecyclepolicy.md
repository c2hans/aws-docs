---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-imagebuilder-lifecyclepolicy.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::ImageBuilder::LifecyclePolicy
<a name="aws-resource-imagebuilder-lifecyclepolicy"></a>

Creates a lifecycle policy resource.

## Syntax
<a name="aws-resource-imagebuilder-lifecyclepolicy-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-imagebuilder-lifecyclepolicy-syntax.json"></a>

```
{
  "Type" : "AWS::ImageBuilder::LifecyclePolicy",
  "Properties" : {
      "[Description](#cfn-imagebuilder-lifecyclepolicy-description)" : {{String}},
      "[ExecutionRole](#cfn-imagebuilder-lifecyclepolicy-executionrole)" : {{String}},
      "[Name](#cfn-imagebuilder-lifecyclepolicy-name)" : {{String}},
      "[PolicyDetails](#cfn-imagebuilder-lifecyclepolicy-policydetails)" : {{[ PolicyDetail, ... ]}},
      "[ResourceSelection](#cfn-imagebuilder-lifecyclepolicy-resourceselection)" : {{ResourceSelection}},
      "[ResourceType](#cfn-imagebuilder-lifecyclepolicy-resourcetype)" : {{String}},
      "[Status](#cfn-imagebuilder-lifecyclepolicy-status)" : {{String}},
      "[Tags](#cfn-imagebuilder-lifecyclepolicy-tags)" : {{{{{Key}}: {{Value}}, ...}}}
    }
}
```

### YAML
<a name="aws-resource-imagebuilder-lifecyclepolicy-syntax.yaml"></a>

```
Type: AWS::ImageBuilder::LifecyclePolicy
Properties:
  [Description](#cfn-imagebuilder-lifecyclepolicy-description): {{String}}
  [ExecutionRole](#cfn-imagebuilder-lifecyclepolicy-executionrole): {{String}}
  [Name](#cfn-imagebuilder-lifecyclepolicy-name): {{String}}
  [PolicyDetails](#cfn-imagebuilder-lifecyclepolicy-policydetails): {{
    - PolicyDetail}}
  [ResourceSelection](#cfn-imagebuilder-lifecyclepolicy-resourceselection): {{
    ResourceSelection}}
  [ResourceType](#cfn-imagebuilder-lifecyclepolicy-resourcetype): {{String}}
  [Status](#cfn-imagebuilder-lifecyclepolicy-status): {{String}}
  [Tags](#cfn-imagebuilder-lifecyclepolicy-tags): {{
    {{Key}}: {{Value}}}}
```

## Properties
<a name="aws-resource-imagebuilder-lifecyclepolicy-properties"></a>

`Description`  <a name="cfn-imagebuilder-lifecyclepolicy-description"></a>
Optional description for the lifecycle policy.
*Required*: No
*Type*: String
*Minimum*: `1`
*Maximum*: `1024`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExecutionRole`  <a name="cfn-imagebuilder-lifecyclepolicy-executionrole"></a>
The name or Amazon Resource Name (ARN) for the IAM role you create that grants Image Builder access to run lifecycle actions. You must have permission to pass the role, and the role's trust policy must allow the Image Builder service principal to assume it.
*Required*: Yes
*Type*: String
*Pattern*: `^(?:arn:aws(?:-[a-z]+)*:iam::[0-9]{12}:role/)?[a-zA-Z_0-9+=,.@\-_/]+$`
*Minimum*: `1`
*Maximum*: `2048`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Name`  <a name="cfn-imagebuilder-lifecyclepolicy-name"></a>
The name of the lifecycle policy to create. Policy names must be unique to your account in each AWS Region. Image Builder generates the policy ARN from a normalized form of the name, so names that differ only in case, spaces, or underscores count as the same name. You can't change the name after creation.
*Required*: Yes
*Type*: String
*Pattern*: `^[-_A-Za-z-0-9][-_A-Za-z0-9 ]{1,126}[-_A-Za-z-0-9]$`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`PolicyDetails`  <a name="cfn-imagebuilder-lifecyclepolicy-policydetails"></a>
Configuration details for the lifecycle policy rules. A policy can contain at most one rule per action type: one `DELETE`, one `DEPRECATE`, and one `DISABLE`.
*Required*: Yes
*Type*: Array of [PolicyDetail](aws-properties-imagebuilder-lifecyclepolicy-policydetail.md)
*Minimum*: `1`
*Maximum*: `3`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceSelection`  <a name="cfn-imagebuilder-lifecyclepolicy-resourceselection"></a>
Selection criteria for the resources that the lifecycle policy applies to. You must specify exactly one selection criteria: either recipes or a tag map, not both.
*Required*: Yes
*Type*: [ResourceSelection](aws-properties-imagebuilder-lifecyclepolicy-resourceselection.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResourceType`  <a name="cfn-imagebuilder-lifecyclepolicy-resourcetype"></a>
The type of Image Builder resource that the lifecycle policy applies to. The resource type determines the allowed rule actions: policies for AMI-based Image Builder images support `DELETE`, `DEPRECATE`, and `DISABLE`, and policies for container-based Image Builder images support only `DELETE`. You can't change the resource type after creation.
*Required*: Yes
*Type*: String
*Allowed values*: `AMI_IMAGE | CONTAINER_IMAGE`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Status`  <a name="cfn-imagebuilder-lifecyclepolicy-status"></a>
Indicates whether the lifecycle policy resource is enabled. If you don't specify a status, it defaults to `ENABLED`. Only enabled policies run on their schedule.
*Required*: No
*Type*: String
*Allowed values*: `DISABLED | ENABLED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-imagebuilder-lifecyclepolicy-tags"></a>
Tags to apply to the lifecycle policy resource.
*Required*: No
*Type*: Object of String
*Pattern*: `.{1,}`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-imagebuilder-lifecyclepolicy-return-values"></a>

### Ref
<a name="aws-resource-imagebuilder-lifecyclepolicy-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN, such as `arn:aws:imagebuilder:us-west-2:111122223333:lifecycle-policy/my-example-policy`.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-imagebuilder-lifecyclepolicy-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-imagebuilder-lifecyclepolicy-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the lifecycle policy resource.

## Examples
<a name="aws-resource-imagebuilder-lifecyclepolicy--examples"></a>

### Create a lifecycle policy that deletes AMIs older than 90 days
<a name="aws-resource-imagebuilder-lifecyclepolicy--examples--Create_a_lifecycle_policy_that_deletes_AMIs_older_than_90_days"></a>

The following example creates a lifecycle policy that deletes AMIs older than 90 days, while retaining the three most recent images. The policy applies to images produced by a specific image recipe.

#### YAML
<a name="aws-resource-imagebuilder-lifecyclepolicy--examples--Create_a_lifecycle_policy_that_deletes_AMIs_older_than_90_days--yaml"></a>

```
Resources:
  LifecyclePolicyExample:
    Type: AWS::ImageBuilder::LifecyclePolicy
    Properties:
      Name: delete-old-amis-policy
      Description: Delete AMIs older than 90 days
      Status: ENABLED
      ResourceType: AMI_IMAGE
      ExecutionRole: !GetAtt LifecyclePolicyRole.Arn
      PolicyDetails:
        - Action:
            Type: DELETE
            IncludeResources:
              Amis: true
              Snapshots: true
          Filter:
            Type: AGE
            Value: 90
            Unit: DAYS
            RetainAtLeast: 3
          ExclusionRules:
            Amis:
              IsPublic: true
              TagMap:
                DoNotDelete: 'true'
      ResourceSelection:
        Recipes:
          - Name: my-image-recipe
            SemanticVersion: '1.0.0'
      Tags:
        Purpose: cleanup
```

#### JSON
<a name="aws-resource-imagebuilder-lifecyclepolicy--examples--Create_a_lifecycle_policy_that_deletes_AMIs_older_than_90_days--json"></a>

```
{
    "Resources": {
        "LifecyclePolicyExample": {
            "Type": "AWS::ImageBuilder::LifecyclePolicy",
            "Properties": {
                "Name": "delete-old-amis-policy",
                "Description": "Delete AMIs older than 90 days",
                "Status": "ENABLED",
                "ResourceType": "AMI_IMAGE",
                "ExecutionRole": {
                    "Fn::GetAtt": ["LifecyclePolicyRole", "Arn"]
                },
                "PolicyDetails": [
                    {
                        "Action": {
                            "Type": "DELETE",
                            "IncludeResources": {
                                "Amis": true,
                                "Snapshots": true
                            }
                        },
                        "Filter": {
                            "Type": "AGE",
                            "Value": 90,
                            "Unit": "DAYS",
                            "RetainAtLeast": 3
                        },
                        "ExclusionRules": {
                            "Amis": {
                                "IsPublic": true,
                                "TagMap": {
                                    "DoNotDelete": "true"
                                }
                            }
                        }
                    }
                ],
                "ResourceSelection": {
                    "Recipes": [
                        {
                            "Name": "my-image-recipe",
                            "SemanticVersion": "1.0.0"
                        }
                    ]
                },
                "Tags": {
                    "Purpose": "cleanup"
                }
            }
        }
    }
}
```

## See also
<a name="aws-resource-imagebuilder-lifecyclepolicy--seealso"></a>
+ [Manage image lifecycles](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-image-lifecycles.html) in the *Image Builder User Guide*.

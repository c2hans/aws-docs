---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-b2bi-profile.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::B2BI::Profile
<a name="aws-resource-b2bi-profile"></a>

Creates a customer profile. You can have up to five customer profiles, each representing a distinct private network. A profile is the mechanism used to create the concept of a private network.

## Syntax
<a name="aws-resource-b2bi-profile-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-b2bi-profile-syntax.json"></a>

```
{
  "Type" : "AWS::B2BI::Profile",
  "Properties" : {
      "[BusinessName](#cfn-b2bi-profile-businessname)" : {{String}},
      "[Email](#cfn-b2bi-profile-email)" : {{String}},
      "[Logging](#cfn-b2bi-profile-logging)" : {{String}},
      "[Name](#cfn-b2bi-profile-name)" : {{String}},
      "[Phone](#cfn-b2bi-profile-phone)" : {{String}},
      "[Tags](#cfn-b2bi-profile-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-b2bi-profile-syntax.yaml"></a>

```
Type: AWS::B2BI::Profile
Properties:
  [BusinessName](#cfn-b2bi-profile-businessname): {{String}}
  [Email](#cfn-b2bi-profile-email): {{String}}
  [Logging](#cfn-b2bi-profile-logging): {{String}}
  [Name](#cfn-b2bi-profile-name): {{String}}
  [Phone](#cfn-b2bi-profile-phone): {{String}}
  [Tags](#cfn-b2bi-profile-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-b2bi-profile-properties"></a>

`BusinessName`  <a name="cfn-b2bi-profile-businessname"></a>
Returns the name for the business associated with this profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Email`  <a name="cfn-b2bi-profile-email"></a>
Property description not available.
*Required*: No
*Type*: String
*Pattern*: `^[\w\.\-]+@[\w\.\-]+$`
*Minimum*: `5`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Logging`  <a name="cfn-b2bi-profile-logging"></a>
Specifies whether or not logging is enabled for this profile.
*Required*: Yes
*Type*: String
*Allowed values*: `ENABLED | DISABLED`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Name`  <a name="cfn-b2bi-profile-name"></a>
Returns the display name for profile.
*Required*: Yes
*Type*: String
*Minimum*: `1`
*Maximum*: `254`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Phone`  <a name="cfn-b2bi-profile-phone"></a>
Specifies the phone number associated with the profile.
*Required*: Yes
*Type*: String
*Pattern*: `^\+?([0-9 \t\-()\/]{7,})(?:\s*(?:#|x\.?|ext\.?|extension) \t*(\d+))?$`
*Minimum*: `7`
*Maximum*: `22`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Tags`  <a name="cfn-b2bi-profile-tags"></a>
A key-value pair for a specific profile. Tags are metadata that you can use to search for and group capabilities for various purposes.
*Required*: No
*Type*: Array of [Tag](aws-properties-b2bi-profile-tag.md)
*Minimum*: `0`
*Maximum*: `200`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-b2bi-profile-return-values"></a>

### Ref
<a name="aws-resource-b2bi-profile-return-values-ref"></a>

### Fn::GetAtt
<a name="aws-resource-b2bi-profile-return-values-fn--getatt"></a>

####
<a name="aws-resource-b2bi-profile-return-values-fn--getatt-fn--getatt"></a>

`CreatedAt`  <a name="CreatedAt-fn::getatt"></a>
Returns the timestamp for creation date and time of the profile.

`LogGroupName`  <a name="LogGroupName-fn::getatt"></a>
Returns the name of the logging group.

`ModifiedAt`  <a name="ModifiedAt-fn::getatt"></a>
Returns the timestamp that identifies the most recent date and time that the profile was modified.

`ProfileArn`  <a name="ProfileArn-fn::getatt"></a>
Returns an Amazon Resource Name (ARN) for the profile.

`ProfileId`  <a name="ProfileId-fn::getatt"></a>
Property description not available.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

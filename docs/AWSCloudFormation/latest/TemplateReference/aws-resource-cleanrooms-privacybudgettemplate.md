---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-cleanrooms-privacybudgettemplate.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CleanRooms::PrivacyBudgetTemplate
<a name="aws-resource-cleanrooms-privacybudgettemplate"></a>

An object that defines the privacy budget template.

## Syntax
<a name="aws-resource-cleanrooms-privacybudgettemplate-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-cleanrooms-privacybudgettemplate-syntax.json"></a>

```
{
  "Type" : "AWS::CleanRooms::PrivacyBudgetTemplate",
  "Properties" : {
      "[AutoRefresh](#cfn-cleanrooms-privacybudgettemplate-autorefresh)" : {{String}},
      "[MembershipIdentifier](#cfn-cleanrooms-privacybudgettemplate-membershipidentifier)" : {{String}},
      "[Parameters](#cfn-cleanrooms-privacybudgettemplate-parameters)" : {{Parameters}},
      "[PrivacyBudgetType](#cfn-cleanrooms-privacybudgettemplate-privacybudgettype)" : {{String}},
      "[Tags](#cfn-cleanrooms-privacybudgettemplate-tags)" : {{[ Tag, ... ]}}
    }
}
```

### YAML
<a name="aws-resource-cleanrooms-privacybudgettemplate-syntax.yaml"></a>

```
Type: AWS::CleanRooms::PrivacyBudgetTemplate
Properties:
  [AutoRefresh](#cfn-cleanrooms-privacybudgettemplate-autorefresh): {{String}}
  [MembershipIdentifier](#cfn-cleanrooms-privacybudgettemplate-membershipidentifier): {{String}}
  [Parameters](#cfn-cleanrooms-privacybudgettemplate-parameters): {{
    Parameters}}
  [PrivacyBudgetType](#cfn-cleanrooms-privacybudgettemplate-privacybudgettype): {{String}}
  [Tags](#cfn-cleanrooms-privacybudgettemplate-tags): {{
    - Tag}}
```

## Properties
<a name="aws-resource-cleanrooms-privacybudgettemplate-properties"></a>

`AutoRefresh`  <a name="cfn-cleanrooms-privacybudgettemplate-autorefresh"></a>
How often the privacy budget refreshes.
If you plan to regularly bring new data into the collaboration, use `CALENDAR_MONTH` to automatically get a new privacy budget for the collaboration every calendar month. Choosing this option allows arbitrary amounts of information to be revealed about rows of the data when repeatedly queried across refreshes. Avoid choosing this if the same rows will be repeatedly queried between privacy budget refreshes.
*Required*: Yes
*Type*: String
*Allowed values*: `CALENDAR_MONTH | NONE`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`MembershipIdentifier`  <a name="cfn-cleanrooms-privacybudgettemplate-membershipidentifier"></a>
The identifier for a membership resource.
*Required*: Yes
*Type*: String
*Pattern*: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
*Minimum*: `36`
*Maximum*: `36`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Parameters`  <a name="cfn-cleanrooms-privacybudgettemplate-parameters"></a>
Specifies the epsilon and noise parameters for the privacy budget template.
*Required*: Yes
*Type*: [Parameters](aws-properties-cleanrooms-privacybudgettemplate-parameters.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`PrivacyBudgetType`  <a name="cfn-cleanrooms-privacybudgettemplate-privacybudgettype"></a>
Specifies the type of the privacy budget template.
*Required*: Yes
*Type*: String
*Allowed values*: `DIFFERENTIAL_PRIVACY | ACCESS_BUDGET`
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`Tags`  <a name="cfn-cleanrooms-privacybudgettemplate-tags"></a>
An optional label that you can assign to a resource when you create it. Each tag consists of a key and an optional value, both of which you define. When you use tagging, you can also use tag-based access control in IAM policies to control access to this resource.
*Required*: No
*Type*: Array of [Tag](aws-properties-cleanrooms-privacybudgettemplate-tag.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-cleanrooms-privacybudgettemplate-return-values"></a>

### Ref
<a name="aws-resource-cleanrooms-privacybudgettemplate-return-values-ref"></a>

When you pass the logical ID of this resource to the intrinsic `Ref` function, `Ref` returns the resource ARN. For example:

 `{ "Ref": "myPrivacyBudgetTemplate" }`

For the Clean Rooms privacy budget template, `Ref` returns the ARN of the privacy budget template.

For more information about using the `Ref` function, see [`Ref`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-ref.html).

### Fn::GetAtt
<a name="aws-resource-cleanrooms-privacybudgettemplate-return-values-fn--getatt"></a>

The `Fn::GetAtt` intrinsic function returns a value for a specified attribute of this type. The following are the available attributes and sample return values.

For more information about using the `Fn::GetAtt` intrinsic function, see [`Fn::GetAtt`](https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/intrinsic-function-reference-getatt.html).

####
<a name="aws-resource-cleanrooms-privacybudgettemplate-return-values-fn--getatt-fn--getatt"></a>

`Arn`  <a name="Arn-fn::getatt"></a>
The ARN of the privacy budget template.

`CollaborationArn`  <a name="CollaborationArn-fn::getatt"></a>
The ARN of the collaboration that contains this privacy budget template.

`CollaborationIdentifier`  <a name="CollaborationIdentifier-fn::getatt"></a>
The unique ID of the collaboration that contains this privacy budget template.

`MembershipArn`  <a name="MembershipArn-fn::getatt"></a>
The Amazon Resource Name (ARN) of the member who created the privacy budget template.

`PrivacyBudgetTemplateIdentifier`  <a name="PrivacyBudgetTemplateIdentifier-fn::getatt"></a>
A unique identifier for one of your memberships for a collaboration. The privacy budget template is created in the collaboration that this membership belongs to. Accepts a membership ID.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

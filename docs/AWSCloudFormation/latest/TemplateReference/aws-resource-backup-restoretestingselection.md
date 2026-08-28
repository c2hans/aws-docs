---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-resource-backup-restoretestingselection.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::Backup::RestoreTestingSelection
<a name="aws-resource-backup-restoretestingselection"></a>

This request can be sent after CreateRestoreTestingPlan request returns successfully. This is the second part of creating a resource testing plan, and it must be completed sequentially.

This consists of `RestoreTestingSelectionName`, `ProtectedResourceType`, and one of the following:
+  `ProtectedResourceArns`
+  `ProtectedResourceConditions`

Each protected resource type can have one single value.

A restore testing selection can include a wildcard value ("\*") for `ProtectedResourceArns` along with `ProtectedResourceConditions`. Alternatively, you can include up to 30 specific protected resource ARNs in `ProtectedResourceArns`.

Cannot select by both protected resource types AND specific ARNs. Request will fail if both are included.

## Syntax
<a name="aws-resource-backup-restoretestingselection-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-resource-backup-restoretestingselection-syntax.json"></a>

```
{
  "Type" : "AWS::Backup::RestoreTestingSelection",
  "Properties" : {
      "[IamRoleArn](#cfn-backup-restoretestingselection-iamrolearn)" : {{String}},
      "[ProtectedResourceArns](#cfn-backup-restoretestingselection-protectedresourcearns)" : {{[ String, ... ]}},
      "[ProtectedResourceConditions](#cfn-backup-restoretestingselection-protectedresourceconditions)" : {{ProtectedResourceConditions}},
      "[ProtectedResourceType](#cfn-backup-restoretestingselection-protectedresourcetype)" : {{String}},
      "[RestoreMetadataOverrides](#cfn-backup-restoretestingselection-restoremetadataoverrides)" : {{{{{Key}}: {{Value}}, ...}}},
      "[RestoreTestingPlanName](#cfn-backup-restoretestingselection-restoretestingplanname)" : {{String}},
      "[RestoreTestingSelectionName](#cfn-backup-restoretestingselection-restoretestingselectionname)" : {{String}},
      "[ValidationWindowHours](#cfn-backup-restoretestingselection-validationwindowhours)" : {{Integer}}
    }
}
```

### YAML
<a name="aws-resource-backup-restoretestingselection-syntax.yaml"></a>

```
Type: AWS::Backup::RestoreTestingSelection
Properties:
  [IamRoleArn](#cfn-backup-restoretestingselection-iamrolearn): {{String}}
  [ProtectedResourceArns](#cfn-backup-restoretestingselection-protectedresourcearns): {{
    - String}}
  [ProtectedResourceConditions](#cfn-backup-restoretestingselection-protectedresourceconditions): {{
    ProtectedResourceConditions}}
  [ProtectedResourceType](#cfn-backup-restoretestingselection-protectedresourcetype): {{String}}
  [RestoreMetadataOverrides](#cfn-backup-restoretestingselection-restoremetadataoverrides): {{
    {{Key}}: {{Value}}}}
  [RestoreTestingPlanName](#cfn-backup-restoretestingselection-restoretestingplanname): {{String}}
  [RestoreTestingSelectionName](#cfn-backup-restoretestingselection-restoretestingselectionname): {{String}}
  [ValidationWindowHours](#cfn-backup-restoretestingselection-validationwindowhours): {{Integer}}
```

## Properties
<a name="aws-resource-backup-restoretestingselection-properties"></a>

`IamRoleArn`  <a name="cfn-backup-restoretestingselection-iamrolearn"></a>
The Amazon Resource Name (ARN) of the IAM role that AWS Backup uses to create the target resource; for example:`arn:aws:iam::123456789012:role/S3Access`.
*Required*: Yes
*Type*: String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectedResourceArns`  <a name="cfn-backup-restoretestingselection-protectedresourcearns"></a>
You can include specific ARNs, such as `ProtectedResourceArns: ["arn:aws:...", "arn:aws:..."]` or you can include a wildcard: `ProtectedResourceArns: ["*"]`, but not both.
*Required*: No
*Type*: Array of String
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectedResourceConditions`  <a name="cfn-backup-restoretestingselection-protectedresourceconditions"></a>
In a resource testing selection, this parameter filters by specific conditions such as `StringEquals` or `StringNotEquals`.
*Required*: No
*Type*: [ProtectedResourceConditions](aws-properties-backup-restoretestingselection-protectedresourceconditions.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ProtectedResourceType`  <a name="cfn-backup-restoretestingselection-protectedresourcetype"></a>
The type of AWS resource included in a resource testing selection; for example, an Amazon EBS volume or an Amazon RDS database.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestoreMetadataOverrides`  <a name="cfn-backup-restoretestingselection-restoremetadataoverrides"></a>
You can override certain restore metadata keys by including the parameter `RestoreMetadataOverrides` in the body of `RestoreTestingSelection`. Key values are not case sensitive.
See the complete list of [restore testing inferred metadata](https://docs.aws.amazon.com/aws-backup/latest/devguide/restore-testing-inferred-metadata.html).
*Required*: No
*Type*: Object of String
*Pattern*: `.+`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`RestoreTestingPlanName`  <a name="cfn-backup-restoretestingselection-restoretestingplanname"></a>
Unique string that is the name of the restore testing plan.
The name cannot be changed after creation. The name must consist of only alphanumeric characters and underscores. Maximum length is 50.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`RestoreTestingSelectionName`  <a name="cfn-backup-restoretestingselection-restoretestingselectionname"></a>
The unique name of the restore testing selection that belongs to the related restore testing plan.
The name consists of only alphanumeric characters and underscores. Maximum length is 50.
*Required*: Yes
*Type*: String
*Update requires*: [Replacement](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-replacement)

`ValidationWindowHours`  <a name="cfn-backup-restoretestingselection-validationwindowhours"></a>
This is amount of hours (1 to 168) available to run a validation script on the data. The data will be deleted upon the completion of the validation script or the end of the specified retention period, whichever comes first.
*Required*: No
*Type*: Integer
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## Return values
<a name="aws-resource-backup-restoretestingselection-return-values"></a>

### Ref
<a name="aws-resource-backup-restoretestingselection-return-values-ref"></a>

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

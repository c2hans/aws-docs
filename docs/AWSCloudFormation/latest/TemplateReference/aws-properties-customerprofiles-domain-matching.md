---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-customerprofiles-domain-matching.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::CustomerProfiles::Domain Matching
<a name="aws-properties-customerprofiles-domain-matching"></a>

The process of matching duplicate profiles. If `Matching = true`, Connect Customer Customer Profiles starts a weekly batch process called *Identity Resolution Job*. If you do not specify a date and time for the *Identity Resolution Job* to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains. After the *Identity Resolution Job* completes, use the `GetMatches` API to return and review the results. Or, if you have configured `ExportingConfig` in the `MatchingRequest`, you can download the results from S3.

## Syntax
<a name="aws-properties-customerprofiles-domain-matching-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-customerprofiles-domain-matching-syntax.json"></a>

```
{
  "[AutoMerging](#cfn-customerprofiles-domain-matching-automerging)" : {{AutoMerging}},
  "[Enabled](#cfn-customerprofiles-domain-matching-enabled)" : {{Boolean}},
  "[ExportingConfig](#cfn-customerprofiles-domain-matching-exportingconfig)" : {{ExportingConfig}},
  "[JobSchedule](#cfn-customerprofiles-domain-matching-jobschedule)" : {{JobSchedule}}
}
```

### YAML
<a name="aws-properties-customerprofiles-domain-matching-syntax.yaml"></a>

```
  [AutoMerging](#cfn-customerprofiles-domain-matching-automerging): {{
    AutoMerging}}
  [Enabled](#cfn-customerprofiles-domain-matching-enabled): {{Boolean}}
  [ExportingConfig](#cfn-customerprofiles-domain-matching-exportingconfig): {{
    ExportingConfig}}
  [JobSchedule](#cfn-customerprofiles-domain-matching-jobschedule): {{
    JobSchedule}}
```

## Properties
<a name="aws-properties-customerprofiles-domain-matching-properties"></a>

`AutoMerging`  <a name="cfn-customerprofiles-domain-matching-automerging"></a>
Configuration information about the auto-merging process.
*Required*: No
*Type*: [AutoMerging](aws-properties-customerprofiles-domain-automerging.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`Enabled`  <a name="cfn-customerprofiles-domain-matching-enabled"></a>
The flag that enables the matching process of duplicate profiles.
*Required*: Yes
*Type*: Boolean
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ExportingConfig`  <a name="cfn-customerprofiles-domain-matching-exportingconfig"></a>
The S3 location where Identity Resolution Jobs write result files.
*Required*: No
*Type*: [ExportingConfig](aws-properties-customerprofiles-domain-exportingconfig.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`JobSchedule`  <a name="cfn-customerprofiles-domain-matching-jobschedule"></a>
The day and time when do you want to start the Identity Resolution Job every week.
*Required*: No
*Type*: [JobSchedule](aws-properties-customerprofiles-domain-jobschedule.md)
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

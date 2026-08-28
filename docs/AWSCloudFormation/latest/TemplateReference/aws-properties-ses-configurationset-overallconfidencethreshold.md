---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-configurationset-overallconfidencethreshold.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::ConfigurationSet OverallConfidenceThreshold
<a name="aws-properties-ses-configurationset-overallconfidencethreshold"></a>

Defines the validation threshold settings. This object determines the minimum score required for SES to allow an email to be sent.

## Syntax
<a name="aws-properties-ses-configurationset-overallconfidencethreshold-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-configurationset-overallconfidencethreshold-syntax.json"></a>

```
{
  "[ConfidenceVerdictThreshold](#cfn-ses-configurationset-overallconfidencethreshold-confidenceverdictthreshold)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-configurationset-overallconfidencethreshold-syntax.yaml"></a>

```
  [ConfidenceVerdictThreshold](#cfn-ses-configurationset-overallconfidencethreshold-confidenceverdictthreshold): {{String}}
```

## Properties
<a name="aws-properties-ses-configurationset-overallconfidencethreshold-properties"></a>

`ConfidenceVerdictThreshold`  <a name="cfn-ses-configurationset-overallconfidencethreshold-confidenceverdictthreshold"></a>
The validation threshold that determines the minimum score required for SES to allow an email to be sent.
Valid Values:
+ `HIGH` – Allows emails to be sent only to addresses with high delivery likelihood. This provides maximum protection for your sender reputation but may suppress some legitimate addresses with medium delivery confidence.
+ `MEDIUM` – Allows emails to be sent to addresses with medium or high delivery likelihood. This balances reputation protection with delivery reach by allowing addresses with medium and high delivery confidence. This suppresses delivery to email addresses with low delivery confidence.
+ `MANAGED` – Amazon SES automatically manages the threshold to suppress invalid addresses. This option allows Amazon SES to optimize the validation threshold based on your sending patterns and reputation.
*Required*: Yes
*Type*: String
*Pattern*: `MEDIUM|HIGH|MANAGED`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

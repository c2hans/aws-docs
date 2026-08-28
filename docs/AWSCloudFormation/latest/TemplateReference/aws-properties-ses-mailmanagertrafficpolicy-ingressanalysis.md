---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::SES::MailManagerTrafficPolicy IngressAnalysis
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis"></a>

The Add On ARN and its returned value that is evaluated in a policy statement's conditional expression to either deny or block the incoming email.

## Syntax
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis-syntax.json"></a>

```
{
  "[Analyzer](#cfn-ses-mailmanagertrafficpolicy-ingressanalysis-analyzer)" : {{String}},
  "[ResultField](#cfn-ses-mailmanagertrafficpolicy-ingressanalysis-resultfield)" : {{String}}
}
```

### YAML
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis-syntax.yaml"></a>

```
  [Analyzer](#cfn-ses-mailmanagertrafficpolicy-ingressanalysis-analyzer): {{String}}
  [ResultField](#cfn-ses-mailmanagertrafficpolicy-ingressanalysis-resultfield): {{String}}
```

## Properties
<a name="aws-properties-ses-mailmanagertrafficpolicy-ingressanalysis-properties"></a>

`Analyzer`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressanalysis-analyzer"></a>
The Amazon Resource Name (ARN) of an Add On.
*Required*: Yes
*Type*: String
*Pattern*: `^[a-zA-Z0-9:_/+=,@.#-]+$`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

`ResultField`  <a name="cfn-ses-mailmanagertrafficpolicy-ingressanalysis-resultfield"></a>
The returned value from an Add On.
*Required*: Yes
*Type*: String
*Pattern*: `^(addon\.)?[\sa-zA-Z0-9_]+$`
*Minimum*: `1`
*Maximum*: `256`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

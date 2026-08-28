---
source_url: https://docs.aws.amazon.com/AWSCloudFormation/latest/TemplateReference/aws-properties-vpclattice-rule-fixedresponse.html
---

This is the new *CloudFormation Template Reference Guide*. Please update your bookmarks and links. For help getting started with CloudFormation, see the [AWS CloudFormation User Guide](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html).

# AWS::VpcLattice::Rule FixedResponse
<a name="aws-properties-vpclattice-rule-fixedresponse"></a>

Describes an action that returns a custom HTTP response.

## Syntax
<a name="aws-properties-vpclattice-rule-fixedresponse-syntax"></a>

To declare this entity in your CloudFormation template, use the following syntax:

### JSON
<a name="aws-properties-vpclattice-rule-fixedresponse-syntax.json"></a>

```
{
  "[StatusCode](#cfn-vpclattice-rule-fixedresponse-statuscode)" : {{Integer}}
}
```

### YAML
<a name="aws-properties-vpclattice-rule-fixedresponse-syntax.yaml"></a>

```
  [StatusCode](#cfn-vpclattice-rule-fixedresponse-statuscode): {{Integer}}
```

## Properties
<a name="aws-properties-vpclattice-rule-fixedresponse-properties"></a>

`StatusCode`  <a name="cfn-vpclattice-rule-fixedresponse-statuscode"></a>
The HTTP response code. Only `404` and `500` status codes are supported.
*Required*: Yes
*Type*: Integer
*Minimum*: `100`
*Maximum*: `599`
*Update requires*: [No interruption](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/using-cfn-updating-stacks-update-behaviors.html#update-no-interrupt)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS CloudFormation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSCloudFormation` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-statemachine-statemachinetarget.html
---

# Target
<a name="sam-property-statemachine-statemachinetarget"></a>

Configures the AWS resource that EventBridge invokes when a rule is triggered.

## Syntax
<a name="sam-property-statemachine-statemachinetarget-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-statemachine-statemachinetarget-syntax.yaml"></a>

```
  [Id](#sam-statemachine-statemachinetarget-id): {{String}}
```

## Properties
<a name="sam-property-statemachine-statemachinetarget-properties"></a>

 `Id`   <a name="sam-statemachine-statemachinetarget-id"></a>
The logical ID of the target.
The value of `Id` can include alphanumeric characters, periods (`.`), hyphens (`-`), and underscores (`_`).
*Type*: String
*Required*: Yes
*CloudFormation compatibility*: This property is passed directly to the `[Id](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-properties-events-rule-target.html#cfn-events-rule-target-id)` property of the `AWS::Events::Rule` `Target` data type.

## Examples
<a name="sam-property-statemachine-statemachinetarget--examples"></a>

### Target
<a name="sam-property-statemachine-statemachinetarget--examples--target"></a>

#### YAML
<a name="sam-property-statemachine-statemachinetarget--examples--target--yaml"></a>

```
EBRule:
  Type: EventBridgeRule
  Properties:
    Target:
      Id: MyTarget
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

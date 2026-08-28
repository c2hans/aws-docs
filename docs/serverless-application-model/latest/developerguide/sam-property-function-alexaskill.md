---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-property-function-alexaskill.html
---

# AlexaSkill
<a name="sam-property-function-alexaskill"></a>

The object describing an `AlexaSkill` event source type.

## Syntax
<a name="sam-property-function-alexaskill-syntax"></a>

To declare this entity in your AWS Serverless Application Model (AWS SAM) template, use the following syntax.

### YAML
<a name="sam-property-function-alexaskill-syntax.yaml"></a>

```
  [SkillId](#sam-function-alexaskill-skillid): {{String}}
```

## Properties
<a name="sam-property-function-alexaskill-properties"></a>

 `SkillId`   <a name="sam-function-alexaskill-skillid"></a>
The Alexa Skill ID for your Alexa Skill. For more information about Skill ID see [Configure the trigger for a Lambda function](https://developer.amazon.com/docs/custom-skills/host-a-custom-skill-as-an-aws-lambda-function.html#configuring-the-alexa-skills-kit-trigger) in the Alexa Skills Kit documentation.
*Type*: String
*Required*: No
*CloudFormation compatibility*: This property is unique to AWS SAM and doesn't have an CloudFormation equivalent.

## Examples
<a name="sam-property-function-alexaskill--examples"></a>

### AlexaSkillTrigger
<a name="sam-property-function-alexaskill--examples--alexaskilltrigger"></a>

Alexa Skill Event Example

#### YAML
<a name="sam-property-function-alexaskill--examples--alexaskilltrigger--yaml"></a>

```
AlexaSkillEvent:
  Type: AlexaSkill
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

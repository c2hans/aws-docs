---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-statemachine.html
---

# CloudFormation resources generated when AWS::Serverless::StateMachine is specified
<a name="sam-specification-generated-resources-statemachine"></a>

When an `AWS::Serverless::StateMachine` is specified, AWS Serverless Application Model (AWS SAM) generates an `AWS::StepFunctions::StateMachine` base CloudFormation resource.

**`AWS::StepFunctions::StateMachine`**
*`LogicalId`: *`{{<statemachine‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::StateMachine` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [Role property is not specified](#sam-specification-generated-resources-statemachine-not-role)
+ [An API event source is specified](#sam-specification-generated-resources-statemachine-api)
+ [An event bridge (or event bus) event source is specified](#sam-specification-generated-resources-statemachine-eventbridge)

## Role property is not specified
<a name="sam-specification-generated-resources-statemachine-not-role"></a>

When the `Role` property of an `AWS::Serverless::StateMachine` is *not* specified, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource.

**`AWS::IAM::Role`**
*`LogicalId`: *`{{<statemachine‑LogicalId>}}Role`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## An API event source is specified
<a name="sam-specification-generated-resources-statemachine-api"></a>

When the `Event` property of an `AWS::Serverless::StateMachine` is set to `Api`, but the `RestApiId` property is *not* specified, AWS SAM generates the `AWS::ApiGateway::RestApi` CloudFormation resource.

**`AWS::ApiGateway::RestApi`**
*`LogicalId`: *`ServerlessRestApi`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## An event bridge (or event bus) event source is specified
<a name="sam-specification-generated-resources-statemachine-eventbridge"></a>

When the `Event` property of an `AWS::Serverless::StateMachine` is set to one of the event bridge (or event bus) types, AWS SAM generates the `AWS::Events::Rule` CloudFormation resource. This applies to the following types: `EventBridgeRule`, `Schedule`, and `CloudWatchEvents`.

**`AWS::Events::Rule`**
*`LogicalId`: *`{{<statemachine‑LogicalId><event‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

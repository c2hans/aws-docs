---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-capacityprovider.html
---

# CloudFormation resources generated when AWS::Serverless::CapacityProvider is specified
<a name="sam-specification-generated-resources-capacityprovider"></a>

When an `AWS::Serverless::CapacityProvider` is specified, AWS Serverless Application Model (AWS SAM) generates an `AWS::Lambda::CapacityProvider` base CloudFormation resource.

**`AWS::Lambda::CapacityProvider`**
*`LogicalId`: *`{{<capacityprovider‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::CapacityProvider` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [OperatorRole property is not specified](#sam-specification-generated-resources-capacityprovider-iam-role)

## OperatorRole property is not specified
<a name="sam-specification-generated-resources-capacityprovider-iam-role"></a>

When the `OperatorRole` property of an `AWS::Serverless::CapacityProvider` is *not* specified, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource with the `AWSLambdaManagedEC2ResourceOperator` managed policy attached.

**`AWS::IAM::Role`**
*`LogicalId`: *`{{<capacityprovider‑LogicalId>}}OperatorRole`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

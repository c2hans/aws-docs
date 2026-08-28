---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-networkconnector.html
---

# CloudFormation resources generated when AWS::Serverless::NetworkConnector is specified
<a name="sam-specification-generated-resources-networkconnector"></a>

When you specify an `AWS::Serverless::NetworkConnector`, AWS Serverless Application Model (AWS SAM) generates an `AWS::Lambda::NetworkConnector` base CloudFormation resource.

**`AWS::Lambda::NetworkConnector`**
*`LogicalId`: *`{{<networkconnector‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::NetworkConnector` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [OperatorRole property is not specified](#sam-specification-generated-resources-networkconnector-iam-role)

## OperatorRole property is not specified
<a name="sam-specification-generated-resources-networkconnector-iam-role"></a>

When you don't specify the `OperatorRole` property of an `AWS::Serverless::NetworkConnector`, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource with the `AWSLambdaNetworkConnectorOperatorPolicy` AWS managed policy attached.

The role trust policy allows the `lambda.amazonaws.com` service principal to assume the role.

**`AWS::IAM::Role`**
*`LogicalId`: *`{{<networkconnector‑LogicalId>}}OperatorRole`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

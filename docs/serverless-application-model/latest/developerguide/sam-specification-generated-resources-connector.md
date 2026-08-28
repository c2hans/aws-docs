---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-connector.html
---

# CloudFormation resources generated when you specify AWS::Serverless::Connector
<a name="sam-specification-generated-resources-connector"></a>

**Note**
When you define connectors through the embedded `Connectors` property, it is first transformed into an `AWS::Serverless::Connector` resource before generating these resources.

When you specify an `AWS::Serverless::Connector` resource in an AWS SAM template, AWS SAM generates the following AWS CloudFormation resources as needed.

**`AWS::IAM::ManagedPolicy`**
 *`LogicalId`:*`{{<connector‑LogicalId>}}Policy`
 *Referenceable property:* N/A (To reference this CloudFormation resource, you must use the `LogicalId`.)

**`AWS::SNS::TopicPolicy`**
 *`LogicalId`:*`{{<connector‑LogicalId>}}TopicPolicy`
 *Referenceable property:* N/A (To reference this CloudFormation resource, you must use the `LogicalId`.)

**`AWS::SQS::QueuePolicy`**
 *`LogicalId`:*`{{<connector‑LogicalId>}}QueuePolicy`
 *Referenceable property:* N/A (To reference this CloudFormation resource, you must use the `LogicalId`.)

**`AWS::Lambda::Permission`**
 *`LogicalId`:*`{{<connector‑LogicalId>}}{{<permission>}}LambdaPermission`
 `{{<permission>}}` is a permission specified by the `Permissions` property. For example, `Write`.
*Referenceable property:* N/A (To reference this CloudFormation resource, you must use the `LogicalId`.)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

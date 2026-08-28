---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-microvmimage.html
---

# CloudFormation resources generated when AWS::Serverless::MicrovmImage is specified
<a name="sam-specification-generated-resources-microvmimage"></a>

When you specify an `AWS::Serverless::MicrovmImage`, AWS Serverless Application Model (AWS SAM) generates an `AWS::Lambda::MicrovmImage` base CloudFormation resource.

**`AWS::Lambda::MicrovmImage`**
*`LogicalId`: *`{{<microvmimage‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::MicrovmImage` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [BuildRoleArn property is not specified](#sam-specification-generated-resources-microvmimage-iam-role)

## BuildRoleArn property is not specified
<a name="sam-specification-generated-resources-microvmimage-iam-role"></a>

When you don't specify the `BuildRoleArn` property of an `AWS::Serverless::MicrovmImage`, AWS SAM generates an `AWS::IAM::Role` CloudFormation resource with an inline policy granting the following permissions:
+ `s3:GetObject` — scoped to the Amazon S3 bucket from `CodeUri`
+ `logs:CreateLogGroup`, `logs:CreateLogStream`, `logs:PutLogEvents` — for build logs

The role trust policy allows the `lambda.amazonaws.com` service principal to assume the role.

**`AWS::IAM::Role`**
*`LogicalId`: *`{{<microvmimage‑LogicalId>}}BuildRole`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-httpapi.html
---

# CloudFormation resources generated when AWS::Serverless::HttpApi is specified
<a name="sam-specification-generated-resources-httpapi"></a>

When an `AWS::Serverless::HttpApi` is specified, AWS Serverless Application Model (AWS SAM) generates an `AWS::ApiGatewayV2::Api` base CloudFormation resource.

**`AWS::ApiGatewayV2::Api`**
*`LogicalId`: *`{{<httpapi‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

In addition to this CloudFormation resource, when `AWS::Serverless::HttpApi` is specified, AWS SAM also generates CloudFormation resources for the following scenarios:

**Topics**
+ [StageName property is specified](#sam-specification-generated-resources-httpapi-stage-name)
+ [StageName property is *not* specified](#sam-specification-generated-resources-httpapi-not-stage-name)
+ [DomainName property is specified](#sam-specification-generated-resources-httpapi-domain-name)

## StageName property is specified
<a name="sam-specification-generated-resources-httpapi-stage-name"></a>

When the `StageName` property of an `AWS::Serverless::HttpApi` is specified, AWS SAM generates the `AWS::ApiGatewayV2::Stage` CloudFormation resource.

**`AWS::ApiGatewayV2::Stage`**
*`LogicalId`: *`{{<httpapi‑LogicalId>}}{{<stage‑name>}}Stage`
`{{<stage‑name>}}` is the string that the `StageName` property is set to. For example, if you set `StageName` to `Gamma`, the `LogicalId` is: {{MyHttpApiGamma}}Stage.
*Referenceable property: *`{{<httpapi‑LogicalId>}}.Stage`

## StageName property is *not* specified
<a name="sam-specification-generated-resources-httpapi-not-stage-name"></a>

When the `StageName` property of an `AWS::Serverless::HttpApi` is *not* specified, AWS SAM generates the `AWS::ApiGatewayV2::Stage` CloudFormation resource.

**`AWS::ApiGatewayV2::Stage`**
*`LogicalId`: *`{{<httpapi‑LogicalId>}}ApiGatewayDefaultStage`
*Referenceable property: *`{{<httpapi‑LogicalId>}}.Stage`

## DomainName property is specified
<a name="sam-specification-generated-resources-httpapi-domain-name"></a>

When the `DomainName` property of the `Domain` property of an `AWS::Serverless::HttpApi` is specified, AWS SAM generates the `AWS::ApiGatewayV2::DomainName` CloudFormation resource.

**`AWS::ApiGatewayV2::DomainName`**
*`LogicalId`: *`ApiGatewayDomainNameV2{{<sha>}}`
`{{<sha>}}` is a unique hash value that is generated when the stack is created. For example, `ApiGatewayDomainNameV2`{{926eeb5ff1}}.
*Referenceable property: *`{{<httpapi‑LogicalId>}}.DomainName`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

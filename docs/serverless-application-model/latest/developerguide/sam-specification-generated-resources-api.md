---
source_url: https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/sam-specification-generated-resources-api.html
---

# CloudFormation resources generated when AWS::Serverless::Api is specified
<a name="sam-specification-generated-resources-api"></a>

When an `AWS::Serverless::Api` is specified, AWS Serverless Application Model (AWS SAM) always generates an `AWS::ApiGateway::RestApi` base CloudFormation resource. In addition, it also always generates an `AWS::ApiGateway::Stage` and an `AWS::ApiGateway::Deployment` resource.

**`AWS::ApiGateway::RestApi`**
*`LogicalId`: *`{{<api‑LogicalId>}}`
*Referenceable property: *N/A (you must use the `LogicalId` to reference this CloudFormation resource)

**`AWS::ApiGateway::Stage`**
*`LogicalId`: *`{{<api‑LogicalId>}}{{<stage‑name>}}Stage`
`{{<stage‑name>}}` is the string that the `StageName` property is set to. For example, if you set `StageName` to `Gamma`, the `LogicalId` is `{{MyRestApiGamma}}Stage`.
*Referenceable property: *`{{<api‑LogicalId>}}.Stage`

**`AWS::ApiGateway::Deployment`**
*`LogicalId`: *`{{<api‑LogicalId>}}Deployment{{<sha>}}`
`{{<sha>}}` is a unique hash value that is generated when the stack is created. For example, `{{MyRestApi}}Deployment{{926eeb5ff1}}`.
*Referenceable property: *`{{<api‑LogicalId>}}.Deployment`

In addition to these CloudFormation resources, when `AWS::Serverless::Api` is specified, AWS SAM generates additional CloudFormation resources for the following scenarios.

**Topics**
+ [DomainName property is specified](#sam-specification-generated-resources-api-domain-name)
+ [UsagePlan property is specified](#sam-specification-generated-resources-api-usage-plan)

## DomainName property is specified
<a name="sam-specification-generated-resources-api-domain-name"></a>

When the `DomainName` property of the `Domain` property of an `AWS::Serverless::Api` is specified, AWS SAM generates the `AWS::ApiGateway::DomainName` CloudFormation resource.

**`AWS::ApiGateway::DomainName`**
*`LogicalId`: *`ApiGatewayDomainName{{<sha>}}`
`{{<sha>}}` is a unique hash value that is generated when the stack is created. For example: `ApiGatewayDomainName{{926eeb5ff1}}`.
*Referenceable property: *`{{<api‑LogicalId>}}.DomainName`

## UsagePlan property is specified
<a name="sam-specification-generated-resources-api-usage-plan"></a>

When the `UsagePlan` property of the `Auth` property of an `AWS::Serverless::Api` is specified, AWS SAM generates the following CloudFormation resources: `AWS::ApiGateway::UsagePlan`, `AWS::ApiGateway::UsagePlanKey`, and `AWS::ApiGateway::ApiKey`.

**`AWS::ApiGateway::UsagePlan`**
*`LogicalId`: *`{{<api‑LogicalId>}}UsagePlan`
*Referenceable property: *`{{<api‑LogicalId>}}.UsagePlan`

**`AWS::ApiGateway::UsagePlanKey`**
*`LogicalId`: *`{{<api‑LogicalId>}}UsagePlanKey`
*Referenceable property: *`{{<api‑LogicalId>}}.UsagePlanKey`

**`AWS::ApiGateway::ApiKey`**
*`LogicalId`: *`{{<api‑LogicalId>}}ApiKey`
*Referenceable property: *`{{<api‑LogicalId>}}.ApiKey`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Serverless Application Model. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query serverless-application-model` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

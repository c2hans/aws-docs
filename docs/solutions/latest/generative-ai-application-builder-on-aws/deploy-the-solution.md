---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/deploy-the-solution.html
---

# Deploy the solution
<a name="deploy-the-solution"></a>

This solution uses [AWS CloudFormation templates and stacks](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-whatis-concepts.html) to automate its deployment. The CloudFormation template specifies the AWS resources included in this solution and their properties. The CloudFormation stack provisions the resources that are described in the template.

## Deployment process overview
<a name="deployment-process-overview"></a>

Before you launch the solution, review the [cost](cost.md), [architecture](architecture-overview.md), [security](security-1.md), and other considerations discussed in this guide.

**Important**
If you plan to use Amazon Bedrock, you must request access to models before they are available for use. Refer to [Model access](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the *Amazon Bedrock User Guide* for more details.

 **Time to deploy:** Approximately 10 minutes

 [Step 1: Launch the Deployment dashboard stack](step-1-launch-the-deployment-dashboard-stack.md)

 [Step 2: Deploy a use case](step-2-deploy-use-case.md)

 [Step 3: Deploy a use case using the Deployment dashboard wizard](step-3-deploy-a-use-case-using-deployment-dashboard-wizard.md)

 [Step 4: Post-deployment configuration](step-4-post-deployment-configuration.md)

Optionally, you can deploy the use cases separately from the solution, if you prefer not to have the Deployment dashboard UI or APIs.
+  [Deploying a standalone Text use case](deploying-the-text-use-case-stack-separately.md)
+  [Deploying a standalone Bedrock Agent use case](deploying-a-standalone-agent-use-case.md)

You can also [supply a DynamoDB chat configuration](#supplying-a-dynamo-db-chat-configuration).

**Important**
This solution sends operational metrics to AWS (the “Data”) about the use of this solution. We use this Data to better understand how customers use this solution and related services and products. AWS’s collection of this Data is subject to the [AWS Privacy Policy](https://aws.amazon.com/privacy/).

## Supplying a DynamoDB chat configuration
<a name="supplying-a-dynamo-db-chat-configuration"></a>

When deploying a use case, **UseCaseConfigRecordKey** and **UseCaseConfigTableName** are required CloudFormation parameters which are normally populated by the Deployment dashboard. The deployment dashboards stack handles the creation and configuration of this table, while calls to the deployment API trigger population of the parameters.

When performing a standalone deployment, you must do the following:

1. Create a DynamoDB table with a hash key of **key**.

1. Create a record in the table containing the configuration for the use case as a record of the format: `{key: some_use_case_key, config: {your_configuration}.`

1. Pass the chosen **UseCaseConfigTableName** and **UseCaseConfigRecordKey** (`some_use_case_key` in this example) parameters to the use case stack when deploying.

To create a suitable configuration for a standalone deployment, you can create a required use case from the Deployment dashboard, and copy record from the configuration table. Otherwise, you can craft your own configuration based on the following example for a Bedrock deployment:

```
{
 "UseCaseName": "SampleUseCase",
 "ConversationMemoryParams": {
 "ConversationMemoryType": "DynamoDB",
 "HumanPrefix": "H",
 "AiPrefix": "A",
 "ChatHistoryLength": 20
 },
 "KnowledgeBaseParams": {
 "KnowledgeBaseType": "Bedrock",
 "NumberOfDocs": 2,
 "ScoreThreshold": 0,
 "ReturnSourceDocs": false,
 "BedrockKnowledgeBaseParams": {
 "BedrockKnowledgeBaseId": "SOME_ID",
 "OverrideSearchType": null
 }
 },
 "LlmParams": {
 "ModelProvider": "Bedrock",
 "BedrockLlmParams": { "ModelId": "anthropic.claude-v2" },
 "PromptParams": {
 "PromptTemplate": "some prompt",
 "MaxPromptTemplateLength": 187500,
 "MaxInputTextLength": 187500,
 "UserPromptEditingEnabled": true,
 "DisambiguationEnabled": true,
 "DisambiguationPromptTemplate": "some prompt"
 },
 "ModelParams": {},
 "Temperature": 1,
 "RAGEnabled": true,
 "Streaming": true,
 "Verbose": false
 }
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Generative AI Application Builder on AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query solutions` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

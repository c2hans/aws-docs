---
source_url: https://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/accessing-and-analyzing-user-collected-feedback.html
---

# Accessing and analyzing user collected feedback
<a name="accessing-and-analyzing-user-collected-feedback"></a>

As of v3.0.0, the Deployment Dashboard deploys a nested feedback stack which allows Text and Bedrock Agent usecases deployed with the Dashboard to have the functionality of feedback collection for the responses that the LLM/Agent generates. Particularly, users can provide a positive or negative feedback along with an optional comment. If the user provides a negative feedback, they can further select one of these negative categories: 'Inaccurate', 'Incomplete or insufficient', 'Harmful' and/or 'Other'.

Once the user provides the feedback, the feedback is stored in an S3 bucket partitioned by Use Case ID, year and month. The Use Case ID can be found in the Deployment Dashboard and the Feedback S3 bucket can be found in the outputs of the feedback nested stack of the Deployment Dashboard stack:

 **Depicts Deployment stack - Finding Feedback Bucket Name**

![feedback bucket output](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/feedback-bucket-output.png)

The user feedback is sent as an API request containing a minimal set of information:

```
{
  "useCaseRecordKey": "a1b2c3d4-e5f6g7h8",
  "conversationId": "12345678-1234-1234-1234-123456789012",
  "messageId": "87654321-4321-4321-4321-210987654321",
  "rephrasedQuery": "What are the key features of the Generative AI Application Builder on AWS?",
  "sourceDocuments": [
    "s3://bucket-name/document1.pdf",
    "s3://bucket-name/document2.pdf"
  ],
  "feedback": "positive",
  "feedbackReason": [
    "Incomplete or insufficient"
  ],
  "comment": "The response was helpful but could include more details about important features."
}
```

This payload is then processed by a lambda using the `useCaseRecordKey` which identifies the correct configuration of a usecase at the time of deployment. This configuration is used to get specific details for the feedback such as the ConversationTable’s name (contains all the conversations and human and AI message sequences) which is further used to retrieve the the actual `userInput` and `llmResponse`. Additional details are also attached to this feedback record such as the `agentId` and `agentAliasId` for a Bedrock Agent usecase, and `modelProvider`, `bedrockModelId`, etc. for a Text usecase using this configuration. For details on how to access this configuration, see [Custom Feedback Mappings](#custom-feedback-mappings) section below. Each incoming feedback request is stored as a JSON object and a sample feedback record can look like this for a Text usecase:

```
{
   "useCaseId": "12345678-1234-1234-1234-123456789012",
   "useCaseRecordKey": "c07a2e3b-2f31b1e0",
   "userId": "22345678-1234-1234-1234-123456789012",
   "conversationId": "dd51de5d-5af1-4ec6-91d2-aadf14352109",
   "messageId": "32345678-1234-1234-1234-123456789012",
   "userInput": "What are its key features?",
   "rephrasedQuery": "What are the key features of the Generative AI Application Builder on AWS?",
   "llmResponse": "Generative AI Application Builder on AWS can help you build production ready enterprise chatbots rapidly.",
   "feedback": "negative",
   "feedbackReason": [
      "Incomplete or insufficient"
   ],
   "comment": "The response was helpful but could include more details about important features.",
   "timestamp": "2025-05-22T18:48:08.340Z",
   "feedbackId": "42345678-1234-1234-1234-123456789012",
   "useCaseType": "Text",
   "modelProvider": "Bedrock",
   "bedrockModelId": "amazon.nova-lite-v1:0",
   "ragEnabled": "false"
}
```

or like this for a Bedrock Agent usecase:

```
{
   "useCaseId": "12345678-1234-1234-1234-123456789012",
   "useCaseRecordKey": "c07a2e3b-2f31b1e0",
   "userId": "22345678-1234-1234-1234-123456789012",
   "conversationId": "dd51de5d-5af1-4ec6-91d2-aadf14352109",
   "messageId": "32345678-1234-1234-1234-123456789012",
   "userInput": "What are its key features?",
   "llmResponse": "Generative AI Application Builder on AWS can help you build production ready enterprise chatbots rapidly.",
   "feedback": "negative",
   "feedbackReason": [
      "Incomplete or insufficient"
   ],
   "comment": "The response was helpful but could include more details about important features.",
   "timestamp": "2025-05-22T18:48:08.340Z",
   "feedbackId": "42345678-1234-1234-1234-123456789012",
   "useCaseType": "Agent",
   "agentId": "AHFXUJCAK1",
   "agentAliasId": "KSEDKOS0BL"
}
```

This feedback can then be used for further processing, analyzing and model re-training/feedback loops. You can also add custom mappings to enhance the feedback record being stored in the feedback lambda.

## Custom Feedback Mappings
<a name="custom-feedback-mappings"></a>

The Deployment Dashboard contains a `LLMConfigTable` which can be found in the stack outputs of the Deployment Dashboard stack with the key `LLMConfigTableName`. `LLMConfigTable` contains the configurations for each usecase based on the settings selected by the admin while deploying the usecase through the Deployment Dashboard wizard. Each usecase configuration is identified by its `useCaseRecordKey`. Here is a sample usecase configuration record in the `LLMConfigTable`:

```
{
   "key": "2dd76cfa-bc1a14da",
   "config": {
      "ConversationMemoryParams": {
        ...
      },
      "FeedbackParams": {
         "CustomMappings": {
            "NumberOfDocs": "$.KnowledgeBaseParams.NumberOfDocs",
            "ScoreThreshold": "$.KnowledgeBaseParams.ScoreThreshold"
         },
         "FeedbackEnabled": true
      },
      "IsInternalUser": "true",
      "KnowledgeBaseParams": {
         "KendraKnowledgeBaseParams": {
            "ExistingKendraIndexId": "d2831033-667f-4539-ab28-e6c7c7c5988b",
            "RoleBasedAccessControlEnabled": false
         },
         "KnowledgeBaseType": "Kendra",
         "NumberOfDocs": 5,
         "ReturnSourceDocs": false,
         "ScoreThreshold": 0.3
      },
      "LlmParams": {
         "BedrockLlmParams": {
            "BedrockInferenceType": "QUICK_START",
            "ModelId": "amazon.nova-lite-v1:0"
         },
         "ModelParams": {},
         "ModelProvider": "Bedrock",
         "PromptParams": {
            ...
         },
         "RAGEnabled": true,
         "Streaming": false,
         "Temperature": 0.1,
         "Verbose": false
      },
      "UseCaseName": "test-rag-usecase",
      "UseCaseType": "Text"
   }
}
```

If feedback is enabled for a usecase, this configuration will contain a `FeedbackParams` object which allows a `CustomMappings` object inside it that can specify the JSONPaths for all the additional fields to be added to the feedback JSON record stored in the feedback S3 bucket. For example, for the above sample usecase configuration, the CustomMappings contains `NumberOfDocs` and `ScoreThreshold` JSONPaths additionally in the `CustomMappings` object which start with `config` as the root of the JSONPath. With this configuration, each JSON record stored in the feedback S3 bucket will start getting these 2 additional values apart from the fields that have already been provided.

## Analyzing feedback data
<a name="analyzing-feedback-data"></a>

The feedback data is stored in S3 as JSON objects. Here are some approaches to make this feedback data more accessible and actionable:

### Using AWS Glue and Amazon Athena
<a name="using-aws-glue-and-amazon-athena"></a>

 [AWS Glue](https://aws.amazon.com/glue) and [Amazon Athena](https://aws.amazon.com/athena) provide a serverless way to catalog, query, and analyze your feedback data.

AWS Glue allows you to create an [AWS Glue crawler](https://docs.aws.amazon.com/glue/latest/dg/add-crawler.html) that inspects the data in an S3 bucket, infers its schema, and records all the relevant metadata in a catalog. Post that, services like Amazon Athena can be used to query the data.

You can refer [AWS Athena Documentation](https://docs.aws.amazon.com/athena/latest/ug/data-sources-glue.html) on steps for connecting the feedback S3 bucket with Amazon Athena using AWS Glue Data Catalog. You can also use some of Glue’s more powerful features to perform Extract Transform & Load (ETL) jobs on this data and transform it into a format that suits your analytics or model re-training use cases. With Glue, you can perform operations such as filtering the records with certain feedback types, filling out any missing information, and you can also load this data into another storage location such as another S3 bucket or a different AWS data store.

**Note**
Depending upon your use case, consider scheduling the Glue crawler to run periodically (e.g., weekly) rather than nightly to optimize costs as feedback data can be sparse.

### Using the solution’s CloudWatch Dashboards
<a name="using-the-solutions-cloudwatch-dashboards"></a>

You also have access to a **CloudWatch Dashboard** packaged with the solution that can provide you trends for positive and negative feedback, negative feedback reason categories, etc. on a per use-case basis. You can find this dashboard using your usecase name in *Dashboards* inside the AWS CloudWatch console:

 **Depicts Usecase CloudWatch Dashboard**

![cloudwatch usecase dashboard](http://docs.aws.amazon.com/solutions/latest/generative-ai-application-builder-on-aws/images/cloudwatch-usecase-dashboard.png)

You can also build additional widgets in this Dashboard or create Amazon Quick Sight dashboards.

### Best practices for feedback data analysis
<a name="best-practices-for-feedback-data-analysis"></a>
+  **Implement data lifecycle policies** on your S3 bucket to archive older feedback data to lower-cost storage tiers
+  **Create separate analysis for each use case** to identify model-specific improvement opportunities
+  **Establish feedback thresholds** that trigger alerts when negative feedback exceeds acceptable levels
+  **Export critical insights** periodically for sharing with stakeholders and model improvement teams

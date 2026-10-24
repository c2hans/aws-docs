---
source_url: https://docs.aws.amazon.com/solutions/latest/qnabot-on-aws/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This section provides information about known issues with QnABot on AWS and instructions for resolving them.

## Amazon Bedrock model parameter errors (TopP and Temperature)
<a name="amazon-bedrock-model-parameter-errors"></a>

When using Amazon Bedrock large language models (LLMs) with QnABot on AWS, you might encounter errors if both the TopP and Temperature parameters are set simultaneously in the `LLM_GENERATE_QUERY_MODEL_PARAMS` or `LLM_QA_MODEL_PARAMS` settings. Certain Amazon Bedrock models do not support specifying both parameters in the same request, and invocations to those models will fail.

### Root causes
<a name="amazon-bedrock-model-parameter-errors-root-causes"></a>
+ The Amazon Bedrock model you are using does not accept both TopP and Temperature parameters in the same request. Not all models have this restriction—some models do accept both parameters.
+ The default QnABot on AWS settings may include both TopP and Temperature, which can cause invocation failures when the selected model does not support the combination.

### Resolution
<a name="amazon-bedrock-model-parameter-errors-resolution"></a>

1. Sign in to the QnABot Content Designer and navigate to the **Settings** page.

1. Locate the `LLM_GENERATE_QUERY_MODEL_PARAMS` and `LLM_QA_MODEL_PARAMS` settings.

1. Review the JSON object for each setting. If both `topP` and `temperature` are present, remove the parameter that is not supported by your model. For example, if your model does not support both, remove either `topP` or `temperature` from the JSON object.

1. Choose **Save** to apply the changes.

1. Test your QnABot on AWS deployment to confirm that LLM queries are processed successfully.

**Note**
Not all Amazon Bedrock models restrict the use of both TopP and Temperature simultaneously. Refer to the Amazon Bedrock inference parameters documentation to determine which parameters are supported by your chosen model. If you are unsure which parameter to remove, consult the model provider’s documentation for recommended inference settings.

For more information, see the related [GitHub issue \#892](https://github.com/aws-solutions/qnabot-on-aws/issues/892) in the QnABot on AWS GitHub repository.

## Unable to use Managed Knowledge Base with Amazon Bedrock
<a name="unable-to-use-managed-knowledge-base-with-amazon-bedrock"></a>

If you are using Amazon Bedrock Knowledge Bases with QnABot on AWS and the fulfillment Lambda function does not return a response, the issue may be related to the type of knowledge base in use.

### Root causes
<a name="unable-to-use-managed-knowledge-base-with-amazon-bedrock-root-causes"></a>
+ Amazon Bedrock has discontinued support for the RetrieveAndGenerate API with managed knowledge bases. QnABot on AWS uses this API to retrieve and generate responses from Amazon Bedrock Knowledge Bases.
+ If your knowledge base is configured as a managed knowledge base, API calls will fail and the fulfillment Lambda function will not return a response.

### Resolution
<a name="unable-to-use-managed-knowledge-base-with-amazon-bedrock-resolution"></a>

1. Sign in to the Amazon Bedrock console.

1. Navigate to **Knowledge bases** and identify the knowledge base that is associated with your QnABot on AWS deployment.

1. If the knowledge base is a managed knowledge base, create a new knowledge base using an unstructured vector store configuration. For instructions, see [Create a knowledge base](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base-create.html) in the *Amazon Bedrock User Guide*.

1. Update your QnABot on AWS settings to reference the new knowledge base ID.

1. Test your QnABot on AWS deployment to confirm that the knowledge base integration is functioning correctly.

**Note**
Existing knowledge bases that use an unstructured vector store configuration are not affected by this change. Only managed knowledge bases are impacted. If you are creating a new knowledge base for use with QnABot on AWS, ensure that you select the unstructured vector store option during creation.

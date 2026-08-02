---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/rag-fully-managed-sagemaker-canvas.html
---

# Amazon SageMaker AI Canvas
<a name="rag-fully-managed-sagemaker-canvas"></a>

[Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas.html) helps you use machine learning to generate predictions without needing to write any code. It provides a no-code visual interface that empowers you to prepare data, build, and deploy ML models, streamlining the end-to-end ML lifecycle in a unified environment. The complexities of data preparation, model development, bias detection, explainability, and monitoring are abstracted away behind an intuitive interface. Users don't need to be SageMaker AI or machine learning operations (MLOps) experts to develop, operationalize, and monitor models with SageMaker AI Canvas.

With SageMaker AI Canvas, the RAG functionality is provided through a no-code, document querying feature. You can enrich the chat experience in SageMaker AI Canvas by using an Amazon Kendra index as the underlying enterprise search. For more information, see [Extract information from documents with document querying](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat-query.html).

Connecting SageMaker AI Canvas to the Amazon Kendra index requires a one-time setup. As part of the domain configuration, a cloud administrator can choose one or more Kendra indexes that the user can query when interacting with SageMaker Canvas. For instructions about how to enable the document querying feature, see [Getting started with using Amazon SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-getting-started.html).

SageMaker AI Canvas manages the underlying communication between Amazon Kendra and the selected foundation model. For more information about the foundation models that SageMaker AI Canvas supports, see [Generative AI foundation models in SageMaker AI Canvas](https://docs.aws.amazon.com/sagemaker/latest/dg/canvas-fm-chat.html). The following diagram shows how the document querying feature works after the cloud administrator has connected SageMaker AI Canvas to an Amazon Kendra index.

![Workflow for the document querying feature in Amazon SageMaker Canvas.](http://docs.aws.amazon.com/prescriptive-guidance/latest/retrieval-augmented-generation-options/images/guide-img/22e94edd-d3e5-4e29-8c94-48e327306335/images/1aa440e8-131e-4bbb-a877-338cee073d4c.png)

The diagram shows the following workflow:

1. The user starts a new chat in SageMaker AI Canvas, turns on **Query documents**, selects the target index, and then submits a question.

1. SageMaker AI Canvas uses the query to search the Amazon Kendra index for relevant data.

1. SageMaker AI Canvas retrieves the data and its sources from the Amazon Kendra index.

1. SageMaker AI Canvas updates the prompt to include the retrieved context from the Amazon Kendra index and submits the prompt to the foundation model.

1. The foundation model uses the original question and the retrieved context to generate an answer.

1. SageMaker AI Canvas provides the generated answer to the user. It includes references to the data sources, such as documents, that were used to generate the response.

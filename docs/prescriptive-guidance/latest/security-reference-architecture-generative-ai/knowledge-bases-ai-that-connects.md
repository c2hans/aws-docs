---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/knowledge-bases-ai-that-connects.html
---

# Knowledge bases (AI that connects)

Retrieval-augmented generation (RAG) supplies external information to a model, such as company policy documents. The AWS AI Security Framework groups enterprise data and knowledge bases as **AI that connects**. A fixed retrieval sequence does not require an agent.

![AWS SRA of AI Security AWS OU and account structure with AWS service reference - Knowledge base connection](https://docs.aws.amazon.com/prescriptive-guidance/latest/security-reference-architecture-generative-ai/images/guide-img/a349f18f-a9fd-43a3-9a48-27534bf6412a/images/ef551a6f-d841-483f-83ce-6e9be90f21b5.png)

*** Fig 4:*** ***AWS SRA of AI Security AWS OU and account structure with AWS service reference - Knowledge base connection***

Apply [data and retrieval controls](https://dp8l2mfblnx2f.cloudfront.net/connects/data-and-retrieval/) alongside [model inference](https://dp8l2mfblnx2f.cloudfront.net/answers/model-inference/) and [application access](https://dp8l2mfblnx2f.cloudfront.net/answers/ai-applications/).

## When tools or agents are involved
<a name="when-tools-or-agents-are-involved"></a>

When an agent chooses tools or execution steps, also apply the [AI that acts](https://dp8l2mfblnx2f.cloudfront.net/acts/) guidance, including for read-only Model Context Protocol (MCP) tools. [Read-only tool access](https://dp8l2mfblnx2f.cloudfront.net/connects/tool-access/) covers information requests. Tools that change systems also require action authorization and recovery controls.

The [connected-workload reference diagram](https://dp8l2mfblnx2f.cloudfront.net/images/connects-generative-ai-account.png) shows the retrieval components, including [Amazon Bedrock Knowledge Bases](https://docs.aws.amazon.com/bedrock/latest/userguide/knowledge-base.html) and [Amazon OpenSearch Serverless](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/serverless-vector-search.html).

## Security considerations
<a name="security-considerations"></a>
+ Ingestion credentials can read more source data than the requesting user is entitled to retrieve.
+ Direct retrieval or untrusted filters can bypass document and tenant permissions.
+ Authorized documents can contain malicious instructions or poisoned content.
+ Source access changes can leave protected information in indexes, caches, or memory.

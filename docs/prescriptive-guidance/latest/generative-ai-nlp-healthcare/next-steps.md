---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/next-steps.html
---

# Next steps and resources
<a name="next-steps"></a>

This guide helps you use AWS services to automate medical NLP and generative AI tasks for real-world applications in production environments. It describes how you can use Amazon Comprehend Medical, supported LLMs in Amazon Bedrock, pretrained medical LLMs, or fine-tuned LLMs to achieve your healthcare and life science business objectives. This guide describes the advantages and limitations for the following approaches:
+ Using Amazon Comprehend Medical independently
+ Providing Amazon Comprehend Medical results to an LLM
+ Using a pretrained general LLM or a medical LLM in a Retrieval Augmented Generation (RAG) approach
+ Fine-tuning a general LLM or medical LLM

Use the [decision tree](choosing-approach.md) and the [business maturity considerations](choosing-approach.md#business-maturity) in this guide to choose between these approaches based on your organization's AI/ML maturity level. Although Amazon Comprehend Medical and Amazon Bedrock LLMs provide powerful capabilities, they are only successful if you properly implement and evaluate them. Use the [evaluation information](evaluation.md) and [metrics](evaluation.md#evaluation-metrics) described in this guide to validate the performance of your solution.

For next steps, we recommend that healthcare IT managers, architects, and technical leads work with AI/ML practitioners to identify their NLP medical task. Use this guide to choose a development path, and then use the appropriate AWS services and features to successfully implement an automated solution on AWS.

## AWS resources
<a name="aws-resources"></a>
+ Amazon Comprehend Medical documentation:
  + [Developer Guide](https://docs.aws.amazon.com/comprehend-medical/latest/dev/comprehendmedical-welcome.html)
  + [API Reference](https://docs.aws.amazon.com/comprehend-medical/latest/api/Welcome.html)
+ [Amazon Bedrock documentation](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html)
  + [Amazon Bedrock model evaluation](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation.html)
  + [Fine-tuning in Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/custom-model-fine-tuning.html)
+ [Fine-tune a model in Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/jumpstart-foundation-models-use-studio-updated-fine-tune.html)
+ [Amazon SageMaker Ground Truth](https://docs.aws.amazon.com/sagemaker/latest/dg/sms.html)
+ [Amazon Comprehend toxicity detection](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#toxicity-detection)
+ [AWS Healthcare Competency Partners](https://aws.amazon.com/health/healthcare-partner-solutions/)

## Other resources
<a name="other-resources"></a>
+ [Open Medical-LLM Leaderboard](https://huggingface.co/spaces/openlifescienceai/open_medical_llm_leaderboard)
+ [A Survey of Large Language Models for Healthcare: from Data, Technology, and Applications to Accountability and Ethics](https://arxiv.org/pdf/2310.05694)
+ [Large Language Models Are Poor Medical Coders — Benchmarking of Medical Code Querying](https://ai.nejm.org/doi/pdf/10.1056/AIdbp2300040)
+ [From Beginner to Expert: Modeling Medical Knowledge into General LLMs](https://arxiv.org/html/2312.01040v3)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

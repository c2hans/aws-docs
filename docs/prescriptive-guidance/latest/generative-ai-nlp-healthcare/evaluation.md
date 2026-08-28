---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/generative-ai-nlp-healthcare/evaluation.html
---

# Evaluating LLMs for healthcare and life science applications
<a name="evaluation"></a>

This section provides a comprehensive overview of the requirements and considerations for evaluating large language models (LLMs) in healthcare and life science use cases.

It is important to use ground truth data and SME feedback to mitigate bias and validate the accuracy of the LLM-generated response. This section describes best practices for collecting and curating training and test data. It also helps you implement guardrails and measure data bias and fairness. It also discusses the common medical natural language processing (NLP) tasks, such as text classification, named entity recognition, and text generation, and their associated evaluation metrics.

It also presents workflows for performing LLM evaluation during the training experimentation phase and post-production phase. Model monitoring and LLM operations are important elements of this evaluation process.

## Training and test data for medical NLP tasks
<a name="evaluation-test-data"></a>

Medical NLP tasks commonly use medical corpora (such as PubMed) or patient information (such as clinic patient visit notes) to classify, summarize, and generate insights. Medical personnel, such physicians, health care administrators, or technicians, vary in expertise and viewpoints. Due to subjectivity between these medical personnel, smaller training and test data sets pose a risk of bias. To mitigate this risk, we recommend the following best practices:
+ When using a pretrained LLM solution, make sure that you have an adequate amount of test data. The test data should closely resemble the actual medical data. Depending on the task, this can range from 20 to more than 100 records.
+ When fine-tuning an LLM, collect a sufficient number of labeled (ground truth) records from a variety of SMEs of the targeted medical domain. A general starting point is at least 100 high-quality records. However, given the complexity of the task and your accuracy acceptance criteria, more records might be required.
+ If required for your medical use case, implement guardrails and measure data bias and fairness. For example, make sure that the LLM prevents misdiagnosis due to racial profiles of patients. For more information, see *Security and guardrails* in the [Choosing an LLM](llms.md#llm-selection) section.

Many AI research and development companies, such as Anthropic, have already implemented guardrails in their foundation models to avoid toxicity. You can use toxicity detection to check input prompts and the output responses from LLMs. For more information, see [Toxicity detection](https://docs.aws.amazon.com/comprehend/latest/dg/trust-safety.html#toxicity-detection) in the Amazon Comprehend documentation and see [Guardrails](https://docs.aws.amazon.com/bedrock/latest/userguide/guardrails.html) in the Amazon Bedrock documentation.

In any generative AI task, there is a risk of hallucination. You can mitigate this risk by performing NLP tasks, such as classification. You can also use more advanced techniques, such as text similarity metrics. [BertScore](https://huggingface.co/spaces/evaluate-metric/bertscore) is a commonly adopted text similarity metric. For more information about techniques that you can use to mitigate hallucination, see [A Comprehensive Survey of Hallucination Mitigation Techniques in Large Language Models](https://arxiv.org/pdf/2401.01313).

## Metrics for medical NLP tasks
<a name="evaluation-metrics"></a>

You can create quantifiable metrics after you establish ground truth data and SME-provided labels for training and testing. Checking quality through qualitative processes, such as stress testing and reviewing LLM results, is helpful for quick development. However, metrics act as quantitative benchmarks that support future LLM operations and act as performance benchmarks for each production release.

Understanding the medical task is critical. Metrics typically map to one of the following general NLP tasks:
+ **Text classification** – The LLM categorizes the text into one or more predefined categories, based on the input prompt and provided context. An example is classifying a pain category by using a pain scale. Examples of text classification metrics include:
  + [Accuracy](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-accuracy-metric)
  + [Precision](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macroprecision-metric), also known as *macro precision*
  + [Recall](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macrorecall-metric), also known as *macro recall*
  + [F1 score](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macrof1score-metric), also known as *macro F1 score*
  + [Hamming loss](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-hammingloss-metric)
+ **Named entity recognition (NER)** – Also known as *text extraction*, named entity recognition is the process of locating and classifying named entities that are mentioned in unstructured text into predefined categories. An example is extracting the names of medications from patient records. Examples of NER metrics include:
  + [Accuracy](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-accuracy-metric)
  + [Precision](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macroprecision-metric)
  + [Recall](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macrorecall-metric)
  + [F1 score](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-macrof1score-metric)
  + [Hamming loss](https://docs.aws.amazon.com/comprehend/latest/dg/cer-doc-class.html#class-hammingloss-metric)
+ **Generation** – The LLM is generates new text by processing the prompt and provided context. Generation includes summarization tasks or question-answering tasks. Examples of generation metrics include:
  + [Recall-Oriented Understudy for Gisting Evaluation (ROUGE)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-accuracy-evaluation.html)
  + [Metric for Evaluation of Translation with Explicit ORdering (METEOR)](https://docs.aws.amazon.com/sagemaker/latest/dg/clarify-accuracy-evaluation.html)
  + [Bilingual evaluation understudy (BLEU)](https://en.wikipedia.org/wiki/BLEU) (for translations)
  + [String distance](https://en.wikipedia.org/wiki/Cosine_similarity), also known as *cosine similarity*

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

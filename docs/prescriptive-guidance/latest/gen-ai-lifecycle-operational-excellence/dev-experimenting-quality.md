---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-quality.html
---

# Evaluating quality and reliability in generated outputs
<a name="dev-experimenting-quality"></a>

Evaluation is the most critical and challenging part of the generative AI development loop. Because the outputs are often unstructured and subjective, a multi-faceted evaluation strategy is required. The evaluation system itself should be treated as a product, a complex software component that needs to be designed, versioned, and validated to make sure that it provides a reliable signal of application quality.

This section contains the following topics:
+ [Traits of a robust evaluation framework](#dev-experimenting-quality-traits)
+ [Evaluation datasets](#dev-experimenting-quality-datasets)
+ [Evaluation strategies and metrics](#dev-experimenting-quality-metrics)

## Traits of a robust evaluation framework
<a name="dev-experimenting-quality-traits"></a>

It is essential to establish a high-quality, human-curated set of question-answer pairs early in the PoC phase of a new generative AI application. These gold-standard examples form the foundation of the testing framework and directly influence the accuracy and relevance of model evaluation throughout the development lifecycle. To build a strong evaluation framework, it is essential to start with a set of (ideally human-curated) question-answer pairs that serve as the gold standard for model behavior. The quality of these questions directly impacts the entire application's quality. It is critical that these gold standard outputs are correct. If you use generative AI to synthetically create the evaluation dataset, it's critical that you take extreme care to validate the results.

Successful generative AI frameworks usually share the following traits:
+ **Use-case specificity** – The evaluation framework and the metrics chosen must be tailored to the specific business problem.
+ **Rapid iteration** – The evaluation runs in seconds, enabling engineers to test hundreds of possible improvements daily. This rapid feedback loop accelerates innovation by removing bottlenecks at development speed.
+ **Actionable feedback** – The generated score includes reasoned explanations, which provide engineers with precise insights into where the core application isn't functioning as expected. This transparency allows for targeted tuning of the evaluation system, uncovering hidden problems.
+ **Configurable measurement** – The evaluation produces tunable numeric results, providing objective comparisons that are tailored to the specific workload. This adaptability helps you make sure that the numeric score accurately reflects what matters most for each use case, such as the relative importance of spelling accuracy (strict for legal documents, lenient for brainstorming), formatting consistency, or factual precision.
+ **Comprehensive coverage** – The framework promotes reliable and consistent evaluation by using a high volume of diverse and categorized test cases. This broad coverage minimizes score variation and provides a trustworthy assessment across all possible scenarios, with results grouped by category for targeted feedback.
+ **Component-level insight** – The evaluation framework assesses every step in the application, not just the result. This segmented approach provides granular visibility so that engineers can apply feedback to the exact portion of the workload where it will have the most impact. This requires a high-quality dataset for each individual step.

## Evaluation datasets
<a name="dev-experimenting-quality-datasets"></a>

The quality of an evaluation is directly tied to the quality of its dataset. A robust evaluation dataset should be diverse and representative of real-world usage.

The best practice is to build a high-quality, sometimes called *golden*, evaluation dataset from one or more of the following sources:
+ **Real-world logs** – Extract examples from production or pilot user interactions, especially those that resulted in poor outcomes or received negative feedback. This makes sure that the evaluation focuses on real problems.
+ **Manually curated examples** – Domain experts should craft a set of canonical examples that test the core functionality and critical business requirements.
+ **Synthetically generated data** – Use an LLM to generate a wide variety of test cases, including edge cases, adversarial inputs (such as prompt injection attempts), and queries that are designed to test for specific biases.

The dataset must also cover a wide range of scenarios, including simple and complex queries, expected and unexpected usage patterns, and inputs with varying levels of ambiguity.

You can compare the outputs of the generative AI application to ground truth data. This helps you evaluate the quality and accuracy of the response. *Ground truth data* is data that is known to be accurate, verified, and representative of real-world outcomes.

For many generative tasks, defining a single, correct answer is impossible. This is a major departure from traditional machine learning, where labels are discrete. The following are two methods for handling ground truth data in generative AI evaluations:
+ **Reference text** – Provide a complete, ideal response. This is useful when the exact wording or structure is critical, such as in regulated domains.
+ **Expected facts** – A more flexible and robust approach is to list the key facts, entities, or concepts that must be present in a correct response. The evaluation system then checks for the presence of these facts, regardless of the specific phrasing. This accommodates the natural linguistic variability of LLMs.

## Evaluation strategies and metrics
<a name="dev-experimenting-quality-metrics"></a>

A generative AI evaluation strategy normally combines automated, model-based, and human evaluation approaches. The following table shows some metric options for each category.

|
|
| **Metric category ** | **Metric name** | **Description** | **Typical use case** | **Requires ground truth data** | **Advantages and disadvantages** |
| --- |--- |--- |--- |--- |--- |
|  Metric-based | [Recall-oriented understudy for gisting evaluation (ROUGE)](https://en.wikipedia.org/wiki/ROUGE_(metric)), such as ROUGE-L | Measures the [n-gram](https://en.wikipedia.org/wiki/N-gram) overlap between the generated text and the reference text, focusing on recall. | Summarization and question answering | Yes, as reference text | **Advantages**: Fast, cheap, and objective<br />**Disadvantages**: Misses semantic similarity and penalizes valid rephrasing |
| Metric-based | [Bilingual evaluation understudy (BLEU)](https://en.wikipedia.org/wiki/BLEU) | Measures n-gram overlap, focusing on precision. Penalizes outputs that are too short. | Machine translation | Yes, as reference text | **Advantages**: Correlates well with human judgment for translation<br />**Disadvantages**: Less suitable for creative or diverse text generation |
| Metric-based | [Bidirectional encoder representations from transformers (BERT)](https://en.wikipedia.org/wiki/BERT_(language_model)) score | Computes similarity between token embeddings of the generated text and the reference text. | General-purpose text generation | Yes, as reference text | **Advantages**: Captures semantic meaning better than n-gram overlap<br />**Disadvantages**: Computationally more expensive |
| Model-based | Faithfulness or groundedness | Assesses whether the generated output is factually consistent with the provided source context. | RAG and fact-based question answering | No, uses source context | **Advantages**: Crucial for mitigating hallucinations<br />**Disadvantages**: LLM-as-a-judge model can also hallucinate or be biased |
| Model-based | Relevance | Measures how well the response addresses the query or intent. | Chatbots and question answering | No | **Advantages**: Captures user-centric quality<br />**Disadvantages**: Can be subjective, so a well-defined rubric is required in the LLM-as-a-judge prompt |
| Model-based | Coherence or fluency | Evaluates the linguistic quality of the text, assessing whether it is well-written, logical, and easy to read. | All text generation | No | **Advantages**: Measures a key aspect of the user experience<br />**Disadvantages**: Highly dependent on the linguistic capabilities of the LLM-as-a-judge model |
| Model-based | Style or tone adherence | Checks if the output conforms to a specified style, such as whether it is professional, friendly, or in JSON format. | Brand voice and structured output | No | **Advantages**: Essential for brand consistency and system integration<br />**Disadvantages**: Requires a very clear and specific LLM-as-a-judge prompt |
| Human | Preference score | A human evaluator rates the output on a scale (such as 1–5) or compares two outputs (such as A/B testing). | All use cases | Optional | **Advantages**: Especially advantageous for subjective criteria<br />**Disadvantages**: Slow, expensive, and can be inconsistent |

### Model-based evaluation
<a name="model-based-evaluation.da6706f7-a220-5663-8cdc-db51cf549aea"></a>

The *LLM-as-a-judge* approach is a scalable method that uses an LLM to evaluate the outputs of generative AI system that uses a different LLM. It offers a cost-effective alternative to purely human evaluation, and it can accelerate development cycles. By reducing the need for human evaluation at every stage, which can be time-consuming, the automated process serves as a first filter to identify the most promising experiment results. This allows human reviewers to focus on the highest-value candidates, making reviews more efficient and speeding up decision-making.

However, it still requires careful prompt engineering and validation of the judge LLM against ground truth data, as it may inherit biases from the judge model. This makes it less reliable for highly subjective or safety-critical tasks. A human-in-the-loop approach is therefore recommended for critical decisions so that automated judgments are verified before deployment.

Just as human evaluation typically follows established criteria and converts subjective decisions into structured classifications, LLM-as-a-Judge transforms evaluation tasks into clear classification scenarios. Rather than seeking perfect score matches, the goal is achieving strong correlation with human judgment patterns.

A judge LLM receives evaluation prompts with specific criteria and assigns scores or classifications to system outputs. This works for single-output scoring (with or without reference) or pairwise comparisons. The key is framing evaluations as yes-or-no questions with explanations in order to validate alignment with human reasoning.

We recommend the following implementation best practices when using the LLM-as-a-judge approach:
+ **Keep humans in the loop for critical decisions** – Ensure that outputs from automated evaluation are reviewed by human evaluators before being used for critical decisions or production deployment.
+ **Validate against human patterns** – Test the performance of the judge LLM against human evaluation trends. Focus on correlation rather than exact matches.
+ **Use a judge from a different model family** – To mitigate *self-preference bias*, where models tend to favor outputs that resemble their own, use a judge from a different provider or architecture. This is especially important when using this approach for model comparison. For more information, see [Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena](https://arxiv.org/abs/2306.05685) (Arxiv).
+ **Define clear scenarios** – Precisely outline the evaluation context and what is being measured. Transform complex evaluations into structured yes-or-no decisions with required explanations. For example, use a rubric that defines specific key outcomes for each decision path, such as what qualifies a response as correct, partially correct, or incorrect. Describe how these outcomes determine whether the answer falls into the yes or no category.
+ **Use categories** – Assess performance using defined categories (such as *excellent*, *good*, or *needs improvement*) rather than solely numeric scores. This can provide clearer insights and avoid overemphasis on minor score differences.
+ **Prioritize models with strong reasoning capabilities** – To improve reliability and robustness, select judge models that have advanced reasoning skills. For more information, see [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) (Arxiv).
+ **Taking majority votes from repeated evaluations** – To mitigate bias and improve result reliability, run multiple evaluations and take the majority vote. For more information, see [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) (Arxiv).
+ **Use an ensemble of different models** – Combine the judgments of multiple models to enhance evaluation quality and reduce the risk of single-model bias. For more information, see [A Survey on LLM-as-a-Judge](https://arxiv.org/abs/2411.15594) (Arxiv).
+ **Iterate and refine** – Continuously evaluate and refine the judge model's performance against human benchmarks.

Cloud platforms are beginning to integrate this functionality directly. For instance, Amazon Bedrock provides a list of [built-in metric evaluator prompts](https://docs.aws.amazon.com/bedrock/latest/userguide/model-evaluation-type-judge-prompt.html) for LLM-as-a-judge evaluation jobs.

Applications that go into production without a proper evaluation system or pipeline often suffer in the production stage. This can result in the need for model changes, such as replacing an LLM version that was deprecated by a vendor or addressing performance degradation. These situations highlight that the challenge is not just in building an evaluation system, but also in overcoming the temptation to skip evaluation or rely solely on human review. Such shortcuts create technical debt and hinder scalability in the future.

A critical best practice is to treat the evaluation prompts used by the judge LLM as important software artifacts. These prompts contain the rubrics and instructions for the judge model, and they should be version-controlled and managed in a prompt registry, just like the application's main prompts. The reliability of the entire automated evaluation system hinges on how well the judge's assessments align with human preferences. Therefore, it is essential to periodically validate the judge's performance against a high-quality dataset that is evaluated by human experts. Use correlation metrics to validate consistency.

After the PoC stage, teams can maintain a balance between rapid release cycles and reliability by incorporating LLM-as-a-judge into a stage-gate testing process. This could involve setting a threshold score in predefined categories that must be met or exceeded before progressing in the release pipeline. You can pair this approach with blue-green deployment strategies to minimize production risk. For example, this automated stage-gate approach could be used for minor or patch releases, which promotes speed and efficiency without overburdening the process. Major releases, on the other hand, might still require full or partial human evaluation as part of the deployment process to provide the necessary guardrails for safe and high-quality releases to customer-facing environments.

### Human-based evaluation
<a name="human-based-evaluation.c63ec8bd-c92c-5300-a3f2-ef31ec3c8263"></a>

Human reviewers are generally considered the ultimate source of truth. Automated and model-based evaluations are powerful for scaling, but they must be calibrated and validated against human judgment. Human feedback is essential for creating the initial high-quality evaluation datasets and for periodically auditing the performance of the LLM-as-a-judge to make sure that it aligns with human preferences and hasn't drifted. Although implementing an automated evaluation system is critical for efficient generative AI solution development, retain a human review as the final quality gate. A human should check the quality of the generated output before promoting the solution to the next stage.

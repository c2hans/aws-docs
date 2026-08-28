---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/dev-experimenting-experimentation-loops.html
---

# Creating evaluation loops for generative AI experimentation
<a name="dev-experimenting-experimentation-loops"></a>

The core of any successful generative AI PoC is a robust and repeatable development loop. This loop is the engine room where ideas are tested, prompts are refined, and quality is measured. While it shares conceptual roots with traditional machine learning operations (MLOps), the unique nature of generative models necessitates a new set of practices and tools. The following diagram shows an experimentation and evaluation loop for generative AI.

![An experimentation and evaluation loop for generative AI.](http://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/images/guide-img/5b6a3e4a-ff13-48e9-83d7-177629049c97/images/55b0c3dd-c800-4320-959d-6d29df691dee.png)

The diagram shows the following workflow:

1. Each iteration begins with controlled variables, which are the generative AI application inputs.

1. The controlled variables are stored for experimental tracking.

1. The core generative AI application accepts the inputs and produces outputs.

1. SMEs provide feedback on the outputs.

1. Outputs and traces that are captured from the generative AI application are stored for experiment tracking purposes, and they are consumed by the evaluation system.

1. The evaluation system consumes the evaluation dataset.

1. The evaluation system generates evaluation metrics and stores them for experiment tracking purposes.

1. The experiment results and SME feedback are used to update the application inputs.

1. The controlled variables are updated.

Traditional machine learning experimentation follows a relatively straightforward cycle. Data scientists modify hyperparameters, retrain models, evaluate performance on validation sets, and then select the best-performing variant based on classification metrics (accuracy or F1 score), regression metrics (mean absolute error or mean squared error) or clustering metrics. The process is deterministic - given the same input data and hyperparameters, traditional ML models generate identical results. This makes experiment comparison and reproduction straightforward. Version control focuses primarily on code changes, dataset versions, and model checkpoints, with experimentation costs concentrated in the training phase.

Generative AI experimentation operates fundamentally differently. It requires a more nuanced approach to tracking and versioning. The experimentation process centers around iterative prompt engineering, where small prompt changes can dramatically affect output quality and consistency. Unlike traditional ML, generative AI experiments must account for the non-deterministic nature of LLM responses. This requires multiple runs and statistical analysis to establish meaningful performance baselines. The experimentation lifecycle extends beyond model training to encompass ongoing inference optimization, where teams continuously refine prompts, adjust temperature settings, and experiment with different model variants to balance cost, latency, and quality. This creates a complex web of interdependent variables that traditional versioning systems weren't designed to handle. It necessitates specialized tracking approaches that capture the full context of each experimental iteration.

To move beyond ad-hoc experimentation, a structured and automated development loop is essential for building reliable generative AI applications. The previous loop diagram offers an example of a practical blueprint for this process. It establishes a systematic workflow where every change can be tested, measured, and reproduced. Each component of this loop plays an important role in this systematic approach to quality and iteration. The following are the primary components of this loop:
+ **Controlled variables (inputs)** – Every scientific experiment begins with controlled variables. In generative AI, these are the versioned evaluation dataset, LLMs, hyperparameters, and the versioned prompt from the prompt management system. Treating the experiment variables as version-controlled inputs is beneficial for reproducibility. Changing any of the inputs creates a new experiment, and without strict versioning and tracking, it becomes difficult to compare results and determine if a change led to a genuine improvement.
+ **Core application** – This is the generative AI application itself, configured with a specific prompt version and LLM model ID for the current run. This application orchestrates the logic, which could be a simple LLM call or a complex RAG system or agentic AI pipeline. The key is that its configuration is precisely defined and logged as part of the experiment parameters.
+ **Experiment tracking** – This is the central hub where all experimental data is logged. It's the cornerstone of the entire loop. A single experiment is not just the output; it's a complete snapshot of the conditions that produce it. Tools like [MLflow](https://mlflow.org/docs/latest/genai/) or [Langfuse](https://langfuse.com/docs) are designed for this purpose because they capture a holistic view of each experiment. Track the following variables:
  + **Prompt template version** – The unique ID of the prompt is logged as an input parameter. Or, you can integrate the prompt template version directly into the application code.
  + **LLM model and hyperparameters** – The exact model used and its inference parameters, such as temperature and [top\_p sampling](https://en.wikipedia.org/wiki/Top-p_sampling), are logged. A change in any of these constitutes a new experiment. These parameters can also be tracked directly as part of the application code.
  + **Evaluation dataset version** – The version of the dataset used for the evaluation must be recorded to make sure that the test conditions are known.
  + **Outputs and metrics** – The raw text outputs from the model and the resulting performance scores from the evaluation system are logged as the experiment results.
  + **Execution traces** – For complex systems, such as RAG or agentic AI workflows, it's crucial to log the entire execution trace. This includes the retrieved documents, the final prompt sent to the LLM, and any tool calls made along the way. This provides deep observability for debugging and is a key differentiator from traditional ML tracking.

  For more information about experiment tracking, see [Role of Experiment Tracking in Llmops](https://www.larksuite.com/en_us/topics/ai-glossary/role-of-experiment-tracking-in-llmops) (Lark).
+ **Evaluation system** – This component takes the outputs from the application and compares them against the ground truth data, which is often curated by a human. This system is responsible for generating the quantitative and qualitative metrics that determine success. Given the nuanced nature of LLM outputs, this often includes model-based metrics, such as [LLM-as-a-judge](https://aws.amazon.com/blogs/machine-learning/llm-as-a-judge-on-amazon-bedrock-model-evaluation/). However, it can also include automatic (calculation-based) or human metrics to assess aspects such as relevance or faithfulness at scale.
+ **Optimization mechanism** – The final, most advanced stage of the loop involves feeding the evaluation results back into an automatic prompt-optimization component. This system can analyze failures and suggest or automatically generate a new, improved prompt version. You then check this prompt into the prompt management system to begin the next iteration. This creates a powerful, data-driven feedback mechanism that accelerates the path to a high-quality application. Automatic prompt optimization is discussed in more detail in the [Optimizing prompts](dev-experimenting-prompt-optimization.md) section of this guide.

For more information about developing rapid evaluation and experimentat loops, see [Generative AI app developer workflow](https://docs.databricks.com/aws/en/generative-ai/tutorials/ai-cookbook/genai-developer-workflow) (Databricks).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

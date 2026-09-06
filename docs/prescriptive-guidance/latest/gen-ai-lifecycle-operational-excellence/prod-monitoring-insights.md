---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/gen-ai-lifecycle-operational-excellence/prod-monitoring-insights.html
---

# Turning insights into improvements in generative AI applications
<a name="prod-monitoring-insights"></a>

Production monitoring of generative AI applications generates valuable data about system performance, user interactions, and failure patterns. This section describes systematic approaches for converting monitoring insights into concrete improvements. It examines key intervention mechanisms for handling application failures, methods for conducting root-cause analysis, and processes for implementing improvements through the GLOE lifecycle. The patterns and workflows presented help teams to establish robust feedback loops between production observations and system enhancements. This promotes continuous improvement of generative AI applications while maintaining operational reliability.

## Intervention mechanisms
<a name="prod-monitoring-insights-intervention"></a>

Occasionally, a generative AI application might not function as intended. It is important to be able to design for such failures through the implementation of an intervention mechanism. The following patterns are designed to handle such failures.

### Pattern 1: Intervention for repeat failures
<a name="pattern-1--intervention-for-repeat-failures.933eba22-ad3c-5e98-b7f4-ad05dd40db9a"></a>

Imagine that you have a chatbot where the user makes a request for information; however, after several attempts, the user still has not found the right information. The underlying issue could be the information is not available, or perhaps the model is struggling to interpret the user's request. By implementing an intervention mechanism, you can either redirect the request to a human agent who can better assist the user, or you can gracefully fail and send an alert that includes the logs and traces so that an engineering team can investigate. For both mechanisms, it is important to capture logs, traces, and feedback because this information helps engineering continuous improve the generative AI application.

### Pattern 2: Intervention for high-risk actions
<a name="pattern-2--intervention-for-high-risk-actions.ee32cb83-78ba-5d12-9b1e-5e183ab113a7"></a>

While using generative AI applications to automate actions can produce large efficiency gains, there are times where some actions can result in irreversible or detrimental outcomes. For example, it might approve a large fund transfer for the wrong item. To address this, you can implement a human-in-the-loop review process to help mitigate such risk. For more information, see [Human in the loop](prod-monitoring-feedback.md#prod-monitoring-feedback-human-in-loop) in this guide.

## Root-cause analysis and loopback to the GLOE lifecycle
<a name="prod-monitoring-insights-root-cause"></a>

When a performance issue is detected, either through a monitoring alert (such as a drift alarm) or a stream of negative user feedback, a systematic workflow needs to be developed to handle this. This process operationalizes the l*ooping cycle* at the heart of the GLOE framework. It makes sure that production insights are methodically channeled back into improvements. The following are the steps to resolve performance issues.

### Step 1: Triage and root-cause analysis
<a name="step-1--triage-and-root-cause-analysis.7ddf3fdc-b8e8-51aa-a101-47c286694105"></a>

The first step is to investigate the *why* behind the failure. Using the trace\_id associated with a negative feedback event or a failed evaluation, the team can retrieve the full context of the interaction from the observability platform. The root cause of a failure in a generative AI system might be one of the following:
+ **Prompt and orchestration failure** – The issue lies in the software layer of the generative AI application. This could be a poorly constructed prompt template, a flawed reasoning step in a chain-of-thought prompt, or incorrect logic in an agent's decision to use a tool. The underlying LLM and knowledge base might be perfectly capable, but they were given the wrong instructions.
+ **Knowledge and retrieval failure** – The issue lies in the data provided to the model. In a RAG system, this is the most common cause of factual errors. The retrieval system might have failed to find the relevant document or retrieved an outdated or incorrect document. Alternatively, the necessary information might not exist in the knowledge base.
+ **Core model limitation** – The issue lies with the inherent capabilities of the foundational model itself. Even with a perfect prompt and context, the model might lack the specialized knowledge, reasoning ability, or stylistic nuance to generate the desired output.

### Step 2: Looping back to the GLOE lifecycle
<a name="step-2--looping-back-to-the-gloe-lifecycle.2e4bd596-a5d1-5248-8a13-75928747d228"></a>

The diagnosed root cause dictates the appropriate remediation path, which creates a systematic and efficient loop back to the relevant stage of the GLOE lifecycle. This prevents wasted effort by making sure that the right team uses the right process to fix the problem. For the type of failure, do the following
+ **For prompt and orchestration failures, loop back to the development (PoC) stage** – This is fundamentally a software engineering or prompt engineering problem. The failing interaction, which includes the prompt, context, and the user's desired outcome (if available), is packaged as a new, failing test case. You add it to the version-controlled evaluation dataset. Engineers then return to the rapid, iterative experimentation loop of the PoC stage to refine the prompt template or the agent's orchestration logic until the new test case passes.
+ **For knowledge and retrieval failures, loop back to the data management (RAG) pipeline** – This is a data problem, not a code problem. The solution does not require developers to change the application. Instead, it is an operational task for data curators or domain experts to update the RAG system's knowledge base. This might involve adding new documents, correcting or updating existing ones, or improving the data processing pipeline. For example, you might adjust the document chunking or embedding strategy.
+ **For core model limitations, loop back to the development (PoC) stage for fine-tuning** – This is the most resource-intensive path. If the foundational model itself is the bottleneck, the solution is to enhance its capabilities. This requires collecting a curated dataset of failure cases that are derived from production feedback. Then you initiate a model improvement process by either selecting a more powerful model or by customizing the model through fine-tuning. Any new model is a major change, and it must be rigorously validated in the experiment environment against the full evaluation dataset before it can be considered for deployment.

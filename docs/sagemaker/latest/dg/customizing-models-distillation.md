---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/customizing-models-distillation.html
---

# Distillation
<a name="customizing-models-distillation"></a>

Distillation transfers knowledge from a *teacher* model to a *student* model. The result is a student that gains domain expertise from the teacher while operating at the inference cost, latency, and memory requirements of the smaller model.

## Key terminology
<a name="customizing-models-distillation-terminology"></a>

Teacher model
A more capable model, often larger, that provides the training signal. The teacher can be a model that you host yourself, for example on a Amazon SageMaker AI endpoint, or a model that you access through an API, such as Amazon Bedrock. This is the expert whose domain you want the student to learn.

Student model
The smaller model you are training to learn from the expert. After distillation, the student serves your inference workload.

## Distillation compared to other approaches
<a name="customizing-models-distillation-compared-to-other-approaches"></a>

Distillation is one of several ways to adapt a model's behavior. Which approach to use depends on *what you are trying to change* and *what resources you have*.

| Approach | What it does | Best when | Limitations |
| --- | --- | --- | --- |
| Prompt engineering / Context engineering | Provides instructions or examples in the prompt at inference time. No training required. | You need quick iteration, have no training data, or the task can be solved with a few examples in context. | Limited by the model's context window. Per-request cost increases with longer prompts. Cannot teach new knowledge or fundamentally change the model's behavior. |
| RAG (Retrieval-Augmented Generation) | Retrieves relevant documents at inference time and adds them to the prompt as context. | Your knowledge base changes frequently, you need citations or source attribution, or the knowledge is too large to fit in a training set. | Adds retrieval latency and cost per request. Quality depends on retrieval accuracy. The model still cannot learn new behaviors or reasoning patterns. |
| Fine-tuning | Updates the model's weights on your own training data to change its behavior or teach new patterns. The training signal can be labeled responses, preference pairs, or reward scores, depending on the technique. | You have high-quality training data, or a way to score responses, and want to change the model's style, format, or domain behavior permanently. | Requires your own training data or reward signal. Does not reduce model size or inference cost. |
| Distillation | Transfers knowledge from a capable teacher to a smaller student model. The teacher provides the training signal: generated responses, per-token probabilities, or both. | You want a smaller, more cost-efficient model, have a capable teacher but no labeled data, or want to transfer a post-trained teacher's skills to a smaller student. | Student quality is bounded by what it can represent: very large capability gaps reduce effectiveness. Requires access to a teacher model for data generation. |

These approaches are not mutually exclusive. A common pattern is to distill a smaller model for cost-efficient serving, then augment it with RAG for knowledge that changes frequently. Similarly, you can fine-tune a model and then distill the fine-tuned version into a smaller student for deployment.

## Distillation methods
<a name="customizing-models-distillation-methods"></a>

Distillation methods differ by *who generates the training sequences* and *what signal the teacher provides*.
+ **Logit-based (token-level) knowledge distillation** is a form of off-policy distillation that trains the student on the ground-truth responses in your dataset, with the teacher generating per-token log probabilities as an added signal. It requires the teacher's next-token distribution (its logits, or its log probabilities over the vocabulary), and the teacher and student must share a tokenizer.
+ **Sequence-level knowledge distillation** is the simplest form of off-policy distillation: it trains the student on the teacher's generated responses. The teacher's generated tokens are treated as the correct answers (one-hot labels), so the loss is the standard cross-entropy against these tokens. Because it does not require the teacher's log probabilities, it works even with a closed or API-only teacher. See [Sequence-level knowledge distillation](customizing-models-distillation-sequence-level-knowledge-distillation.md) for a step-by-step walkthrough.
+ **On-policy distillation** has the student generate its own responses, while the teacher provides a per-token signal for these responses: the teacher's log probabilities for the tokens that the student generated. It therefore requires a teacher that exposes log probabilities and shares the student's tokenizer. As the student trains on its own outputs, it learns to recover from the mistakes it actually makes at inference time. On-policy distillation is typically run after an off-policy warm start (for example, after sequence-level knowledge distillation).

## Best practices
<a name="customizing-models-distillation-best-practices"></a>
+ **Check for length inflation without accuracy gains.** If the student's responses grow longer (or frequently hit the token limit) while accuracy does not improve, the student may be reproducing the teacher's output structure without learning the underlying reasoning.
+ **Check for regressions outside the target task.** Specializing on teacher data can degrade unrelated capabilities such as instruction-following and general knowledge. Evaluate a small portfolio of held-out capabilities alongside your task metric. For example, you can use the [IFEval](https://huggingface.co/datasets/google/IFEval) metric to evaluate a model's instruction-following capability.
+ **Expect some forgetting with both LoRA and full fine-tuning.** Further training a post-trained student on narrow-domain data tends to degrade behaviors from its original post-training, such as instruction following. Full fine-tuning learns more of the new task but typically forgets more. LoRA reduces forgetting but does not prevent it, and it learns less of the new task. Start with LoRA, and use full fine-tuning when LoRA does not reach your task target and you can perform additional regression testing.

## Getting started
<a name="customizing-models-distillation-getting-started"></a>

For a step-by-step walkthrough, see [Sequence-level knowledge distillation](customizing-models-distillation-sequence-level-knowledge-distillation.md).

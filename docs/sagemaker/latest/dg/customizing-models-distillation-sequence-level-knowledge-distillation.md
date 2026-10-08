---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/customizing-models-distillation-sequence-level-knowledge-distillation.html
---

# Sequence-level knowledge distillation
<a name="customizing-models-distillation-sequence-level-knowledge-distillation"></a>

Sequence-level knowledge distillation is the simplest form of distillation. You use the teacher model to generate high-quality responses for a set of prompts, then fine-tune the student on those responses with supervised fine-tuning (SFT). The teacher's output responses can be persisted as a dataset and reused to train different students without regenerating the data.

## Use cases for sequence-level knowledge distillation
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-when-to-use"></a>
+ **You have prompts but no high-quality target outputs.** You supply the prompts, and the teacher writes the targets, so you can build a training set for a task or domain that has no existing labels. Targets can be single answers, full reasoning traces with chain-of-thought, or multi-turn tool-use trajectories.
+ **You want to transfer reasoning capability to a smaller model.** Sequence-level knowledge distillation on teacher-generated reasoning traces is an effective way to transfer reasoning skills.
+ **Your teacher is a closed or API-only model.** Sequence-level knowledge distillation needs only the teacher's generated output. It does not require access to the teacher's log probabilities. Once the student is trained, you no longer need to call the teacher at inference time.
+ **You need to serve a high-volume task at lower cost.** If you are currently calling a large model for a repetitive, well-defined task, sequence-level knowledge distillation lets you train a smaller student to handle that task at a fraction of the per-request cost.
+ **You want a reusable dataset that serves multiple students.** Because the teacher's responses persist as a dataset, you can reuse them to train different student models or experiment with different training configurations without regenerating the data.
+ **You want a starting point for more advanced methods.** Sequence-level knowledge distillation provides an effective warm start for on-policy distillation. This method typically requires an SFT-initialized student to work effectively.

## Steps to run sequence-level knowledge distillation
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-steps"></a>

The following steps describe how to run sequence-level knowledge distillation in Amazon SageMaker AI.

### Step 1: Prepare the distillation dataset
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-data"></a>

Generate teacher responses and assemble them into an SFT dataset:

1. Collect a set of prompts that represent your target task or domain.

1. Generate a response for each prompt by calling the teacher model. For a hosted foundation model, call the Amazon Bedrock [Converse](https://docs.aws.amazon.com/bedrock/latest/APIReference/API_runtime_Converse.html) API. For a self-hosted teacher, deploy it to a Amazon SageMaker AI endpoint and call that endpoint.

1. Filter and decontaminate the responses. For verifiable tasks such as math and code, reject-sample by checking the final answer, deduplicate the records, and remove any overlap with your evaluation sets.

1. Build the SFT dataset as (prompt, teacher response) pairs in JSONL format, using the `messages` format.

Each record pairs a user message (the prompt) with an assistant message (the teacher response). This is the same `messages` dataset format described on the [SFT](customizing-models-sft.md) page.

```
{
  "messages": [
    {"role": "user", "content": "What is the derivative of f(x) = 3x^2 + 2x?"},
    {"role": "assistant", "content": "The derivative is f'(x) = 6x + 2."}
  ]
}
```

The following Python example calls the Amazon Bedrock Converse API for a single prompt and writes one (prompt, teacher response) record to a JSONL file. Extend it to loop over your full set of prompts.

```
import json
import boto3

client = boto3.client("bedrock-runtime")

prompt = "What is the derivative of f(x) = 3x^2 + 2x?"

response = client.converse(
    modelId="<teacher-model-id>",  # for example, openai.gpt-oss-120b-1:0
    messages=
    [
        {"role": "user", "content": [{"text": prompt}]}
    ],
    inferenceConfig={"maxTokens": 1024, "temperature": 0.7, "topP": 0.9},
)

# Extract the teacher response from the Bedrock API response
blocks = response["output"]["message"]["content"]
teacher_response = next(b["text"] for b in blocks if "text" in b)

record = {
    "messages": [
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": teacher_response},
    ]
}

with open("training_dataset.jsonl", "a") as f:
    f.write(json.dumps(record) + "\n")
```

### Step 2: Train the student model
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-train"></a>

Train the student on the teacher-generated dataset using standard SFT. Because SFT masks the loss to the response tokens, the student learns to produce the teacher's responses.

You can run sequence-level knowledge distillation with either LoRA or full fine-tuning (FFT). For guidance on choosing between them, see [Training types](customizing-models-training-types.md).

#### Serverless training with the SFTTrainer
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-train-serverless"></a>

Use the Amazon SageMaker AI Python SDK `SFTTrainer`. You can override individual hyperparameters on the `hyperparameters` attribute; parameters that you don't set use the recipe default values.

```
from sagemaker.train import SFTTrainer
from sagemaker.train.common import TrainingType

trainer = SFTTrainer(
    model="<student-model-id>", # For example,"huggingface-vlm-qwen3-5-4b",
    training_type=TrainingType.LORA,
    model_package_group=model_package_group,   # Create a new or use an existing model package group ARN
    mlflow_experiment_name="<add-exp-name>",
    mlflow_run_name="<add-run-name>",
    training_dataset=TRAINING_DATASET,
    validation_dataset=VALIDATION_DATASET,
    s3_output_path="s3://<output-bucket>",
    accept_eula=True,
)

# Optionally set individual hyperparameters (otherwise the recipe defaults apply):
trainer.hyperparameters.global_batch_size = 64
trainer.hyperparameters.learning_rate = 8e-5
trainer.hyperparameters.max_epochs = 2
trainer.hyperparameters.lora_rank = 64
trainer.hyperparameters.lora_alpha = 128

trainer.train()
```

The serverless job emits a registered model package as its output, which you can deploy and evaluate directly in Step 3.

### Step 3: Deploy and evaluate the student model
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-deploy"></a>

After training, deploy the student model to a Amazon SageMaker AI endpoint and run benchmarks to evaluate the student model after distillation.

For the mechanics of deploying the student model, see [Deploying customized models](customizing-models-deployment.md). For evaluation guidance, see [Model evaluation job submission](model-customize-open-weight-evaluation.md) and [Evaluation](customizing-models-evaluation.md).

## Limitations
<a name="customizing-models-distillation-sequence-level-knowledge-distillation-limitations"></a>
+ **The capacity wall.** Distillation transfers a distribution the student can represent, not raw capability it lacks. If response length or truncation rate at the maximum sequence length increases while accuracy does not improve, the student is reproducing the surface structure of the teacher's output without the reasoning ability behind it. Match student size to task difficulty.
+ **The hardest-tail plateau.** Sequence-level knowledge distillation improves performance on easy and moderate problems but tends to plateau on the hardest ones. This happens because the student trains on the teacher's trajectories but generates from its own distribution at inference time. When the student makes an early mistake that the teacher never made, it enters a state it never saw during training, and subsequent errors can compound; particularly in multi-turn tasks. On-policy distillation methods address this by training on the student's own generations, which is why sequence-level knowledge distillation is commonly used as the first stage in a multi-stage distillation pipeline.
+ **Catastrophic forgetting.** The student trains only on teacher responses for your target task, so it can lose abilities it already had, such as following instructions, refusing unsafe requests, or answering questions outside that task.

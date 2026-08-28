---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/model-customize-mtrl-samples.html
---

# Sample datasets and tutorials
<a name="model-customize-mtrl-samples"></a>

## End-to-end example: Customer onboarding agent
<a name="model-customize-mtrl-samples-e2e"></a>

The following example demonstrates the complete workflow for multi-turn RL: training an agent, evaluating its performance, and deploying the trained model.

```
from sagemaker.train.multi_turn_rl_trainer import MultiTurnRLTrainer
from sagemaker.train.evaluate import MultiTurnRLEvaluator
from sagemaker.serve import ModelBuilder
from sagemaker.core.resources import ModelPackage

DATASET = "s3://my-bucket/prompts/prompts.parquet"
AGENT_ARN = "arn:aws:bedrock-agentcore:us-west-2:123456789012:runtime/my-agent"

# ── 1. Train ──────────────────────────────────────────────────────────────
trainer = MultiTurnRLTrainer(
    model="openai-reasoning-gpt-oss-20b",
    agent_env=AGENT_ARN,
    training_dataset=DATASET,
    s3_output_path="s3://my-bucket/train-output/",
    accept_eula=True,
)
trainer.hyperparameters.max_epochs = 1
trainer.hyperparameters.global_batch_size = 10

job = trainer.train(wait=True)
print(f"Training complete: {job.output_model_package_arn}")

# ── 2. Evaluate ───────────────────────────────────────────────────────────
evaluator = MultiTurnRLEvaluator(
    model=trainer,
    dataset=DATASET,
    s3_output_path="s3://my-bucket/eval-output/",
    evaluate_base_model=True,  # Compare base vs fine-tuned
)
execution = evaluator.evaluate()
execution.wait()
print(f"Evaluation: {execution.status.overall_status}")

# ── 3. Deploy ─────────────────────────────────────────────────────────────
model_package = ModelPackage.get(model_package_name=job.output_model_package_arn)

model_builder = ModelBuilder(
    model=model_package,
    instance_type="ml.g6e.48xlarge",
)
model_builder.accept_eula = True
model_builder.build()

endpoint = model_builder.deploy(
    endpoint_name="mtrl-production-endpoint",
    instance_type="ml.g6e.48xlarge",
    initial_instance_count=1,
)
print(f"Deployed: {endpoint.endpoint_name}")
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

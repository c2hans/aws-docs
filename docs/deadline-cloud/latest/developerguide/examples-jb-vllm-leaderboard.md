---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-jb-vllm-leaderboard.html
---

# Benchmark LLMs with vLLM and lm-evaluation-harness on Deadline Cloud
<a name="examples-jb-vllm-leaderboard"></a>

The [vllm\_lm\_eval\_leaderboard](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/job_bundles/vllm_lm_eval_leaderboard) job bundle evaluates multiple LLMs against multiple benchmarks in a single Deadline Cloud job. Each model becomes one task in a parameter sweep, and tasks run in parallel across workers. A final step aggregates per-model results into a ranked leaderboard (CSV and Markdown).

Each task in the `EvalModels` step starts a local [vLLM](https://github.com/vllm-project/vllm) server, runs every benchmark with [EleutherAI's lm-evaluation-harness](https://github.com/EleutherAI/lm-evaluation-harness) against the local endpoint, then stops vLLM. Models load directly from HuggingFace Hub, so job attachments are not required.

To run this bundle, deploy the [CUDA farm CloudFormation template](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm). The template provisions an NVIDIA GPU service-managed fleet (A10G or L4) and a queue with a conda queue environment that this bundle uses without modification. If you already have a farm, you need an SMF fleet with NVIDIA GPUs, at least 32 GB of RAM, and at least 4 vCPUs.

The default model list is a small, ungated, fast-loading mix that fits on a single A10G or L4: `Qwen/Qwen2.5-0.5B`, `Qwen/Qwen2.5-1.5B`, and `EleutherAI/pythia-1.4b`. To use other models, edit the `range` list under `parameterSpace.taskParameterDefinitions` in `template.yaml`.

The default benchmarks form a commonsense reasoning suite: `hellaswag,arc_easy,arc_challenge,winogrande`. Override at submit time:

```
deadline bundle submit ./job_bundles/vllm_lm_eval_leaderboard/ \
  --parameter Benchmarks="hellaswag,mmlu,gsm8k"
```

If your fleet does not scale up workers, the most common cause is an Deadline Cloud service quota. Confirm that you have headroom for *OnDemand G instance GPUs per region* and *OnDemand vCPUs per region* in the Service Quotas console.

For a complete walkthrough that covers prerequisites, farm setup, custom models and benchmarks, and cleanup, see [Benchmark LLMs with vLLM and lm-evaluation-harness](tutorial-vllm-leaderboard.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/developerguide/examples-cfn-cuda-farm.html
---

# Deploy a Deadline Cloud CUDA farm with CloudFormation
<a name="examples-cfn-cuda-farm"></a>

The [cuda\_farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/cuda_farm) CloudFormation template deploys a Deadline Cloud farm that you can use to run CUDA jobs. The default configuration includes a queue for CUDA jobs, a second queue for building conda packages, and a CUDA-capable fleet.

This template specializes the [Deploy a starter Deadline Cloud farm with CloudFormation](examples-cfn-starter-farm.md) template for the CUDA use case:
+ The default `CondaChannels` value is `deadline-cloud conda-forge`, which makes CUDA compilers, frameworks like PyTorch, and applications like COLMAP available.
+ The Linux CUDA fleet is required, and the Windows and Linux CPU fleets are removed.

This template provisions the infrastructure that the [Train 3D Gaussian Splatting from video on Deadline Cloud](examples-jb-gaussian-splatting.md) and [Benchmark LLMs with vLLM and lm-evaluation-harness on Deadline Cloud](examples-jb-vllm-leaderboard.md) job bundles need.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Deadline Cloud. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query deadline-cloud` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

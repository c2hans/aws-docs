---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/choose-dlami.html
---

# Choosing a DLAMI
<a name="choose-dlami"></a>

We offer a range of DLAMI options as mentioned in the [GPU DLAMI release notes](https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes.html#appendix-ami-release-notes-gpu). To help you select the correct DLAMI for your use case, we group images by the hardware type or functionality for which they were developed. Our top level groupings are:
+ **DLAMI Type:** Base, Single-Framework, Multi-Framework (Conda DLAMI)
+ **Compute Architecture:** x86-based, Arm64-based [AWS Graviton](https://aws.amazon.com/ec2/graviton/)
+ **Processor Type:** [GPU](https://docs.aws.amazon.com/dlami/latest/devguide/gpu), [CPU](https://docs.aws.amazon.com/dlami/latest/devguide/cpu), [Inferentia](https://docs.aws.amazon.com/dlami/latest/devguide/inferentia), [Trainium](https://docs.aws.amazon.com/dlami/latest/devguide/trainium)
+ **SDK:** [CUDA](https://developer.nvidia.com/cuda-toolkit), [AWS Neuron](https://awsdocs-neuron.readthedocs-hosted.com/en/latest/neuron-intro/get-started.html)
+ **OS:** Amazon Linux, Ubuntu

The rest of the topics in this guide help further inform you and go into more details.

**Topics**
+ [CUDA Installations and Framework Bindings](overview-cuda.md)
+ [Deep Learning Base AMI](overview-base.md)
+ [Deep Learning AMI with Conda](overview-conda.md)
+ [DLAMI Architecture Options](overview-architecture.md)
+ [DLAMI Operating System Options](overview-os.md)

**Next Up**
[Deep Learning AMI with Conda](overview-conda.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

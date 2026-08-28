---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-gpu-instances.html
---

# Performance acceleration with GPU instances
<a name="configure-gpu-instances"></a>

GPU-based instances provide access to NVIDIA GPUs with thousands of compute cores. You can use these instances to accelerate scientific, engineering, and rendering applications by leveraging the CUDA or Open Computing Language (OpenCL) parallel computing frameworks. You can also use them for graphics applications, including game streaming, 3-D application streaming, and other graphics workloads.

Before you can activate or optimize a GPU-based instance, you must install the appropriate drivers, as follows:
+ To install NVIDIA drivers on an instance with an attached NVIDIA GPU, such as a P3 or G4dn instance, see [NVIDIA drivers](install-nvidia-driver.md).
+ To install AMD drivers on an instance with an attached AMD GPU, such as a G4ad instance, see [AMD drivers](install-amd-driver.md).

**Topics**
+ [Activate NVIDIA GRID Virtual Applications](activate_grid.md)
+ [Optimize GPU settings](optimize_gpu.md)
+ [Set up dual 4K displays on G4ad](activate_g4ad_4k.md)
+ [Get started with GPU accelerated instances](gpu-instances-started.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

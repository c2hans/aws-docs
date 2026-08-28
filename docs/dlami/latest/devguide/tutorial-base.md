---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-base.html
---

# Using the Deep Learning Base AMI
<a name="tutorial-base"></a>

## Using the Deep Learning Base AMI
<a name="tutorial-base-overview"></a>

The Base AMI comes with a foundational platform of GPU drivers and acceleration libraries to deploy your own customized deep learning environment. By default the AMI is configured with any one NVIDIA CUDA version environment. You can also switch between different versions of CUDA. Refer to the following instructions for how to do this.

## Configuring CUDA Versions
<a name="tutorial-base-cuda"></a>

You can verify the CUDA version by running NVIDIA's `nvcc` program.

```
nvcc --version
```

You can select and verify a particular CUDA version with the following bash command:

```
sudo rm /usr/local/cuda
sudo ln -s /usr/local/{{cuda-12.0}} /usr/local/cuda
```

For more information, see the [Base DLAMI release notes](https://docs.aws.amazon.com/dlami/latest/devguide/appendix-ami-release-notes.html#appendix-ami-release-notes-base).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

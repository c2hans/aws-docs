---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-gpu-opt.html
---

# Optimization
<a name="tutorial-gpu-opt"></a>

To make the most of your GPUs, you can optimize your data pipeline and tune your deep learning network. As the following chart describes, a naive or basic implementation of a neural network might use the GPU inconsistently and not to its fullest potential. When you optimize your preprocessing and data loading, you can reduce the bottleneck from your CPU to your GPU. You can adjust the neural network itself, by using hybridization (when supported by the framework), adjusting batch size, and synchronizing calls. You can also use multiple-precision (float16 or int8) training in most frameworks, which can have a dramatic effect on improving throughput.

The following chart shows the cumulative performance gains when applying different optimizations. Your results will depend on the data you are processing and the network you are optimizing.

![Performance enhancements for GPUs](http://docs.aws.amazon.com/dlami/latest/devguide/images/performance-enhancements.png)

The following guides introduce options that will work with your DLAMI and help you boost GPU performance.

**Topics**
+ [Preprocessing](tutorial-gpu-opt-preprocessing.md)
+ [Training](tutorial-gpu-opt-training.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

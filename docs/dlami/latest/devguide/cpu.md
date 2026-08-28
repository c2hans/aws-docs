---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/cpu.html
---

# Recommended CPU Instances
<a name="cpu"></a>

Whether you're on a budget, learning about deep learning, or just want to run a prediction service, you have many affordable options in the CPU category. Some frameworks take advantage of Intel's MKL DNN, which speeds up training and inference on C5 (not available in all Regions) CPU instance types. For information about CPU instance types, see [EC2 Instance Types](https://aws.amazon.com/ec2/instance-types/) and select **Compute Optimized**.

**Note**
The size of your model should be a factor in choosing an instance. If your model exceeds an instance's available RAM, choose a different instance type with enough memory for your application.
+ [Amazon EC2 C5 Instances](https://aws.amazon.com/ec2/instance-types/c5/) have up to 72 Intel vCPUs. C5 instances excel at scientific modeling, batch processing, distributed analytics, high-performance computing (HPC), and machine and deep learning inference.

**Next Up**
[Recommended Inferentia Instances](inferentia.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

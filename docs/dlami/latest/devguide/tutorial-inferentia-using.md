---
source_url: https://docs.aws.amazon.com/dlami/latest/devguide/tutorial-inferentia-using.html
---

# Using the DLAMI with AWS Neuron
<a name="tutorial-inferentia-using"></a>

 A typical workflow with the AWS Neuron SDK is to compile a previously trained machine learning model on a compilation server. After this, distribute the artifacts to the Inf1 instances for execution. AWS Deep Learning AMIs (DLAMI) comes pre-installed with everything you need to compile and run inference in an Inf1 instance that uses Inferentia.

 The following sections describe how to use the DLAMI with Inferentia.

**Topics**
+ [Using TensorFlow-Neuron and the AWS Neuron Compiler](tutorial-inferentia-tf-neuron.md)
+ [Using AWS Neuron TensorFlow Serving](tutorial-inferentia-tf-neuron-serving.md)
+ [Using MXNet-Neuron and the AWS Neuron Compiler](tutorial-inferentia-mxnet-neuron.md)
+ [Using MXNet-Neuron Model Serving](tutorial-inferentia-mxnet-neuron-serving.md)
+ [Using PyTorch-Neuron and the AWS Neuron Compiler](tutorial-inferentia-pytorch-neuron.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Deep Learning AMI. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dlami` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

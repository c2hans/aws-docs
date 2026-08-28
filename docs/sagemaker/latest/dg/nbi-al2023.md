---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/nbi-al2023.html
---

# AL2023 notebook instances
<a name="nbi-al2023"></a>

SageMaker AI notebook instances support AL2023 operating systems. You can select the operating system that your notebook instance is based on when you create the notebook instance.

SageMaker AI supports notebook instances based on the following AL2023 operating systems.
+ **notebook-al2023-v1**: These notebook instances support JupyterLab version 4. For information about JupyterLab versions, see [JupyterLab versioning](nbi-jl.md).

**Topics**
+ [Supported instance types](#nbi-al2023-instances)
+ [Available kernels](#nbi-al2023-kernel)

## Supported instance types
<a name="nbi-al2023-instances"></a>

AL2023 supports instance types listed under **Notebook Instances** in [SageMaker AI Pricing](https://aws.amazon.com/sagemaker/pricing/), with the exception that AL2023 does not support `ml.p2`, `ml.p3`, `ml.p3dn`, `ml.inf1`, and `ml.g3` instances.

## Available kernels
<a name="nbi-al2023-kernel"></a>

The following table gives information about the available kernels for SageMaker notebook instances. All of these images are supported on notebook instances based on the `notebook-al2023-v1` operating system.

| Kernel name | Description |
| --- | --- |
| R | A kernel used to perform data analysis and visualization using R code from a Jupyter notebook. |
| Sparkmagic (PySpark) | A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Python programming language. This kernel comes with Python 3.10. |
| Sparkmagic (Spark) | A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the Scala programming language. This kernel comes with Python 3.10. |
| Sparkmagic (SparkR) | A kernel used to do data science with remote Spark clusters from Jupyter notebooks using the R programming language. This kernel comes with Python 3.10. |
| conda\_python3 | A conda environment that comes pre-installed with popular packages for data science and machine learning. This kernel comes with Python 3.10. |
| conda\_pytorch | A conda environment that comes pre-installed with PyTorch version 2.10.0, as well as popular data science and machine learning packages. This kernel comes with Python 3.10. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

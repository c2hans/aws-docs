---
source_url: https://docs.aws.amazon.com/emr/latest/ReleaseGuide/emr-spark-sagemaker.html
---

# Use Amazon SageMaker Spark for machine learning
<a name="emr-spark-sagemaker"></a>

When using Amazon EMR release 5.11.0 and later, the `aws-sagemaker-spark-sdk` component is installed along with Spark. This component installs Amazon SageMaker Spark and associated dependencies for Spark integration with [Amazon SageMaker](https://aws.amazon.com/sagemaker/). Please note, the `aws-sagemaker-spark-sdk` component is not available from Amazon EMR 7.x and higher. You can use Amazon SageMaker Spark to construct Spark machine learning (ML) pipelines using Amazon SageMaker stages. For more information, see the [Amazon SageMaker Spark README](https://github.com/aws/sagemaker-spark/blob/master/README.md) on GitHub and [Using Apache Spark with Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark.html) in the *Amazon SageMaker Developer Guide*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EMR Documentation. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query emr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

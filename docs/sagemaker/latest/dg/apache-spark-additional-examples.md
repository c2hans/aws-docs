---
source_url: https://docs.aws.amazon.com/sagemaker/latest/dg/apache-spark-additional-examples.html
---

# Resources for using SageMaker AI Spark for Python (PySpark) examples
<a name="apache-spark-additional-examples"></a>

Amazon SageMaker AI provides an Apache Spark Python library ([SageMaker AI PySpark](https://github.com/aws/sagemaker-spark/tree/master/sagemaker-pyspark-sdk)) that you can use to integrate your Apache Spark applications with SageMaker AI. This topic contains examples to help you get started with PySpark. For information about the SageMaker AI Apache Spark library, see [Apache Spark with Amazon SageMaker AI](apache-spark.md).

**Download PySpark**

You can download the source code for both Python Spark (PySpark) and Scala libraries from the [SageMaker AI Spark](https://github.com/aws/sagemaker-spark) GitHub repository.

For instructions on installing the SageMaker AI Spark library, use any the following options or visit [SageMaker AI PySpark](https://github.com/aws/sagemaker-spark/tree/master/sagemaker-pyspark-sdk).
+ Install using pip:

  ```
  pip install sagemaker_pyspark
  ```
+ Install from the source:

  ```
  git clone git@github.com:aws/sagemaker-spark.git
  cd sagemaker-pyspark-sdk
  python setup.py install
  ```
+ You can also create a new notebook in a notebook instance that uses either the `Sparkmagic (PySpark)` or the `Sparkmagic (PySpark3)` kernel and connect to a remote Amazon EMR cluster.
**Note**
The Amazon EMR cluster must be configured with an IAM role that has the `AmazonSageMakerFullAccess` policy attached. For information about configuring roles for an EMR cluster, see [Configure IAM Roles for Amazon EMR Permissions to AWS Services](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-iam-roles.html) in the *Amazon EMR Management Guide*.

**PySpark examples**

For examples on using SageMaker AI PySpark, see:
+ [Using Amazon SageMaker AI with Apache Spark](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-spark/index.html) in Read the Docs.
+ [SageMaker AI Spark](https://github.com/aws/sagemaker-spark) GitHub repository.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon SageMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sagemaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

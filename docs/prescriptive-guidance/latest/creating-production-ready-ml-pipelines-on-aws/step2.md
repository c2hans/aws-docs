---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/step2.html
---

# Step 2. Create the runtime scripts
<a name="step2"></a>

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/creating-production-ready-ml-pipelines-on-aws/images/guide-img/38c6f8a0-9908-46ce-9db4-ad6b4c4bc218/images/d94aee00-e81f-4673-a862-ae6fa562deae.png)

In this step, you integrate the model that you developed in step 1 and its associated helper code into an ML platform for production-ready training and inference. Specifically, this involves the development of runtime scripts so that the model can be incorporated into Amazon SageMaker. These standalone Python scripts include predefined SageMaker callback functions and environment variables. They are run inside a SageMaker container that is hosted on an Amazon Elastic Compute Cloud (Amazon EC2) instance. The [Amazon SageMaker Python SDK documentation](https://sagemaker.readthedocs.io/en/stable/index.html) provides detailed information about how these callbacks and auxiliary setup work together for training and inference. (For example, see [Prepare a scikit-learn training script](https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/using_sklearn.html#prepare-a-scikit-learn-training-script) and [Deploy a scikit-learn model](https://sagemaker.readthedocs.io/en/stable/frameworks/sklearn/using_sklearn.html#deploy-a-scikit-learn-model) in the SageMaker documentation.) The following sections provide additional recommendations for developing ML runtime scripts, based on our experience working with AWS customers.

## Using processing jobs
<a name="proc-job"></a>

SageMaker provides two options for performing batch-mode model inference. You can use a SageMaker *processing job* or a *batch transform job*. Each option has advantages and disadvantages.

A processing job consists of a Python file that runs inside a SageMaker container. The processing job consists of whatever logic you put in your Python file. It has these advantages:
+ When you understand the basic logic of a training job, processing jobs are straightforward to set up and easy to understand. They share the same abstractions as training jobs (for example, tuning the instance count and data distribution).
+ Data scientists and ML engineers have full control over  data manipulation options.
+ The data scientist doesn't have to manage any I/O component logic except for familiar read/write functionality.
+ It's somewhat easier to run the files in non-SageMaker environments, which aids rapid development and local testing.
+ If there is an error, a processing job fails as soon as the script fails, and there is no unexpected waiting for retry.

On the other hand, batch transform jobs are an extension of the concept of a SageMaker endpoint. At runtime, these jobs import callback functions, which then handle the I/O for reading the data, loading the model, and making the predictions. Batch transform jobs have these advantages:
+ They use a data distribution abstraction that differs from the abstraction used by training jobs.
+ They use the same core file and function structure for both batch inference and realtime inference, which is convenient.
+ They have a built-in, retry-based fault-tolerance mechanism. For example, if an error occurs on a batch of records, it will retry multiple times before the job is terminated as a failure.

Because of its transparency, its ease of use in multiple environments, and its shared abstraction with training jobs, we decided to use the processing job instead of the batch transform job in the reference architecture presented in this guide.

You should run Python runtime scripts locally before you deploy them in the cloud. Specifically, we recommend that you use the main guard clause when you structure your Python scripts, and perform unit testing.

## Using the main guard clause
<a name="main-guard"></a>

Use a main guard clause to support module import and to run your Python script. Running Python scripts individually is beneficial for debugging and isolating issues in the ML pipeline. We recommend the following steps:
+ Use an argument parser in the Python processing files to specify input/output files and their locations.
+ Provide a main guide and test functions for each Python file.
+ After you test a Python file, incorporate it into the different stages of the ML pipeline, whether you're using an AWS Step Functions model or a SageMaker processing job.
+ Use **Assert** statements in critical sections of the script to facilitate testing and debugging. For example, you can use an **Assert** statement to ensure that the number of dataset features is consistent after loading.

## Unit testing
<a name="unit-test"></a>

Unit testing of runtime scripts** **that were written for the pipeline is an important task that's frequently ignored in ML pipeline development. This is because machine learning and data science are relatively new fields and have been slow to adopt well-established software engineering practices such as unit testing. Because the ML pipeline will be used in the production environment, it is essential to test the pipeline code before applying the ML model to real-world applications.

Unit testing the runtime script also provides the following unique benefits for ML models:
+ It prevents unexpected data transformations. Most ML pipelines involve many data transformations, so it's critical for these transformations to perform as expected.
+ It validates the reproducibility of the code. Any randomness in the code can be detected by unit testing with different use cases.
+ It enforces the modularity of the code. Unit tests are usually associated with the *test*** ***coverage* measure, which is the degree to which a particular test suite (a collection of test cases) runs the [source code](https://en.wikipedia.org/wiki/Source_code) of a [program](https://en.wikipedia.org/wiki/Computer_program). To achieve high test coverage, developers modularize the code, because it's difficult to write unit tests for a large amount of code without breaking it down into functions or classes.
+ It prevents low-quality code or errors from being introduced into production.

We recommend that you use a mature unit testing framework such as [pytest](https://docs.pytest.org/en/stable/) to write the unit test cases, because it is easier to manage extensive unit tests within a framework.

**Important**
Unit testing cannot guarantee that all corner cases are tested, but it can help you proactively avoid mistakes before you deploy the model. We recommend that you also monitor the model after deployment, to ensure operational excellence.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function.html
---

# Run parallel reads of S3 objects by using Python in an AWS Lambda function
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function"></a>

*Eduardo Bortoluzzi, Amazon Web Services*

## Summary
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-summary"></a>

You can use this pattern to retrieve and summarize a list of documents from Amazon Simple Storage Service (Amazon S3) buckets in real time. The pattern provides example code to parallel read objects from S3 buckets on Amazon Web Services (AWS). The pattern showcases how to efficiently run I/O bound tasks with AWS Lambda functions using Python.

A financial company used this pattern in an interactive solution to manually approve or reject correlated financial transactions in real time. The financial transaction documents were stored in an S3 bucket related to the market. An operator selected a list of documents from the S3 bucket, analyzed the total value of the transactions that the solution calculated, and decided to approve or reject the selected batch.

I/O bound tasks support multiple threads. In this example code, the [concurrent.futures.ThreadPoolExecutor](https://docs.python.org/3.13/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) is used with a maximum of 30 simultaneous threads, even though Lambda functions support up to 1,024 threads (with one of those threads being your main process). This limit is because too many threads create latency issues due to context switching and utilization of computing resources. You also need to increase the maximum pool connections in `botocore` so that all threads can perform the S3 object download simultaneously.

The example code uses one 8.3 KB object, with JSON data, in an S3 bucket. The object is read multiple times. After the Lambda function reads the object, the JSON data is decoded to a Python object. In December 2024, the result after running this example was 1,000 reads processed in 2.3 seconds and 10,000 reads processed in 27 seconds using a Lambda function configured with 2,304 MB of memory. AWS Lambda supports memory configurations from 128 MB to 10,240 MB (10 GB), though increasing the Lambdamemory beyond 2,304 MB didn't help to decrease the time to run this particular I/O-bound task.

The [AWS Lambda Power Tuning](https://github.com/alexcasalboni/aws-lambda-power-tuning) tool was used to test different Lambda memory configurations and verify the best performance-to-cost ratio for the task. For test results, see the [Additional information](#run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-additional) section.

## Prerequisites and limitations
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Proficiency with Python development

**Limitations **
+ A Lambda function can have at most [1,024 execution processes or threads](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#function-configuration-deployment-and-execution).
+ New AWS accounts have a Lambda memory limit of 3,008 MB. Adjust the AWS Lambda Power Tuning tool accordingly. For more information, see the [Troubleshooting](#run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-troubleshooting) section.
+ Amazon S3 has a limit of [5,500 GET/HEAD requests per second per partitioned prefix](https://docs.aws.amazon.com/AmazonS3/latest/userguide/optimizing-performance.html).

**Product versions**
+ Python 3.9 or later
+ AWS Cloud Development Kit (AWS CDK) v2
+ AWS Command Line Interface (AWS CLI) version 2
+ AWS Lambda Power Tuning 4.3.6 (optional)

## Architecture
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-architecture"></a>

**Target technology stack  **
+ AWS Lambda
+ Amazon S3
+ AWS Step Functions (if AWS Lambda Power Tuning is deployed)

**Target architecture **

The following diagram shows a Lambda function that reads objects from an S3 bucket in parallel. The diagram also has a Step Functions workflow for the AWS Lambda Power Tuning tool to fine-tune the Lambda function memory. This fine-tuning helps to achieve a good balance between cost and performance.

![Diagram showing Lambda function, S3 bucket, and AWS Step Functions.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b46e9b16-9842-4291-adfa-3ef012b89aec/images/828696e2-6df7-4536-9205-951c99449f4e.png)

**Automation and scale**

The Lambda functions scale fast when required. To avoid 503 Slow Down errors from Amazon S3 during high demand, we recommend putting some limits on the scaling.

## Tools
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK) v2](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code. The example infrastructure was created to be deployed with AWS CDK.
+ [AWS Command Line InterfaceAWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell. In this pattern, AWS CLI version 2 is used to upload an example JSON file.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon Simple Storage Service Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.

**Other tools**
+ [Python](https://www.python.org/) is a general-purpose computer programming language. The [reuse of idle worker threads](https://docs.python.org/3.8/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor) was introduced in Python version 3.8, and the Lambda function code in this pattern was created for Python version 3.9 and later.

**Code repository**

The code for this pattern is available in the [aws-lambda-parallel-download](https://github.com/aws-samples/aws-lambda-parallel-download) GitHub repository.

## Best practices
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-best-practices"></a>
+ This AWS CDK construct relies on your AWS account's user permissions to deploy the infrastructure. If you plan to use AWS CDK Pipelines or cross-account deployments, see [Stack synthesizers](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping.html#bootstrapping-synthesizers).
+ This example application doesn't have the access logs enabled at the S3 bucket. It's a best practice to enable access logs in production code.

## Epics
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-epics"></a>

### Prepare the development environment
<a name="prepare-the-development-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Check the Python installed version. | This code has been tested specifically on Python 3.9 and Python 3.13, and it should work on all versions between these releases. To check your Python version, run `python3 -V` in your terminal, and install a newer version if needed.<br />To verify that the required modules are installed, run `python3 -c "import pip, venv"`. No error message means the modules are properly installed and you're ready to run this example.  | Cloud architect |
| Install AWS CDK. | To install the AWS CDK if it isn't already installed, follow the instructions at [Getting started with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html). To confirm that the installed AWS CDK version is 2.0 or later, run `cdk –version`. | Cloud architect |
| Bootstrap your environment. | To bootstrap your environment, if it hasn’t already been done, follow the instructions at [Bootstrap your environment for use with the AWS CDK](https://docs.aws.amazon.com/cdk/v2/guide/bootstrapping-env.html). | Cloud architect |

### Clone the example repository
<a name="clone-the-example-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone the latest version of the repository, run the following command:<pre>git clone --depth 1 --branch v1.2.0 \<br />git@github.com:aws-samples/aws-lambda-parallel-download.git</pre> | Cloud architect |
| Change the working directory to the cloned repository. | Run the following command:<pre>cd aws-lambda-parallel-download</pre> | Cloud architect |
| Create the Python virtual environment. | To create a Python virtual environment, run the following command:<pre>python3 -m venv .venv</pre> | Cloud architect |
| Activate the virtual environment. | To activate the virtual environment, run the following command:<pre>source .venv/bin/activate</pre> | Cloud architect |
| Install the dependencies. | To install the Python dependencies, run the `pip` command:<pre>pip install -r requirements.txt</pre> | Cloud architect |
| Browse the code. | (Optional) The example code that downloads an object from the S3 bucket is at `resources/parallel.py`.<br />The infrastructure code is in the `parallel_download` folder. | Cloud architect |

### Deploy and test the app
<a name="deploy-and-test-the-app"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the app. | Run `cdk deploy`.<br />Write down the AWS CDK outputs:+ `ParallelDownloadStack.LambdaFunctionARN`<br />+ `ParallelDownloadStack.SampleS3BucketName`<br />+ `ParallelDownloadStack.StateMachineARN` | Cloud architect |
| Upload an example JSON file. | The repository contains an example JSON file of about 9 KB. To upload the file to the S3 bucket of the created stack, run the following command:<pre>aws s3 cp sample.json s3://<ParallelDownloadStack.SampleS3BucketName></pre><br />Replace `<ParallelDownloadStack.SampleS3BucketName>` with the corresponding value from the AWS CDK output. | Cloud architect |
| Run the app. | To run the app, do the following:1. Sign in to the AWS Management Console, navigate to the [Lambda console](https://console.aws.amazon.com/lambda/home), and locate the Lambda function that has the ARN from the AWS CDK output `ParallelDownloadStack.LambdaFunctionARN`.<br />2. On the **Test** tab, change the **Event JSON** to the following:<pre>{"objectKey": "sample.json"}</pre><br />3. Choose **Test**.<br />4. To see the result, choose **details**. The details will show the statistics of the parallel download, the information of the run, and the logs. | Cloud architect |
| Add the number of downloads. | (Optional) To run 1,500 get object calls, use the following JSON in **Event JSON** of the `Test` parameter:<pre>{"repeat": 1500, "objectKey": "sample.json"}</pre> | Cloud architect |

### Optional: Run AWS Lambda Power Tuning
<a name="optional-run-lamlong-power-tuning"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run the AWS Lambda Power Tuning tool. | 1. Sign in to the console, and navigate to [Step Functions](https://console.aws.amazon.com/states/home).<br />2. Locate the state machine with the ARN from the AWS CDK output `ParallelDownloadStack.StateMachineARN`.<br />3. Choose **Start execution**, and paste the following JSON:<pre>{<br />  "lambdaARN": "<ParallelDownloadStack.LambdaFunctionARN>",<br />  "num": 10,<br />  "strategy": "balanced",<br />  "payload": {"repeat": 2000, "objectKey": "sample.json"}<br />}</pre><br />Remember to replace `<ParallelDownloadStack.LambdaFunctionARN>` with the value from the AWS CDK output.At the end of the run, the result will be on the **Execution input and output** tab. | Cloud architect |
| View the AWS Lambda Power Tuning results in a graph. | On the **Execution input and output** tab, copy the `visualization` property link, and paste it in a new browser tab. | Cloud architect |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Remove the objects from the S3 bucket. | Before you destroy the deployed resources, you remove all the objects from the S3 bucket:<pre>aws s3 rm s3://<ParallelDownloadStack.SampleS3BucketName> \<br />--recursive</pre><br />Remember to replace `<ParallelDownloadStack.SampleS3BucketName>` with the value from the AWS CDK outputs. | Cloud architect |
| Destroy the resources. | To destroy all the resources that were created for this pilot, run the following command:<pre>cdk destroy</pre> | Cloud architect |

## Troubleshooting
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| `'MemorySize' value failed to satisfy constraint: Member must have value less than or equal to 3008` | For new accounts, you might not be able to configure more than 3,008 MB in your Lambda functions. To test using AWS Lambda Power Tuning, add the following property at the input JSON when you are starting the Step Functions execution:<pre>"powerValues": [<br />    512,<br />    1024,<br />    1536,<br />    2048,<br />    2560,<br />    3008<br />  ]</pre> |

## Related resources
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-resources"></a>
+ [Python – concurrent.futures.ThreadPoolExecutor](https://docs.python.org/3/library/concurrent.futures.html#concurrent.futures.ThreadPoolExecutor)
+ [Lambda quotas – Function configuration, deployment, and execution](https://docs.aws.amazon.com/lambda/latest/dg/gettingstarted-limits.html#function-configuration-deployment-and-execution)
+ [Working with the AWS CDK in Python](https://docs.aws.amazon.com/cdk/v2/guide/work-with-cdk-python.html)
+ [Profiling functions with AWS Lambda Power Tuning](https://docs.aws.amazon.com/lambda/latest/operatorguide/profile-functions.html)

## Additional information
<a name="run-parallel-reads-of-s3-objects-by-using-python-in-an-aws-lambda-function-additional"></a>

**Code**

The following code snippet performs the parallel I/O processing:

```
with ThreadPoolExecutor(max_workers=MAX_WORKERS) as executor:
  for result in executor.map(a_function, (the_arguments)):
    ...
```

The `ThreadPoolExecutor` reuses the threads when they become available.

**Testing and results**

These tests were conducted in December 2024.

The first test processed 2,500 object reads, with the following result.

![Invocation time falling and invocation cost rising as memory increases.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b46e9b16-9842-4291-adfa-3ef012b89aec/images/f6743412-1e52-4c4c-a51c-ac0f75b3b998.png)

Starting at 3,009 MB, the processing-time level stayed almost the same for any memory increase, but the cost increased as the memory size increased.

Another test investigated the range between 1,536 MB and 3,072 MB of memory, using values that were multiples of 256 MB and processing 10,000 object reads, with the following results.

![Decreased difference between invocation time falling and invocation cost rising.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b46e9b16-9842-4291-adfa-3ef012b89aec/images/c75d4443-74d8-4b93-9b4d-b2640869381e.png)

The best performance-to-cost ratio was with the 2,304 MB memory Lambda configuration.

For comparison, a sequential process of 2,500 object reads took 47 seconds. The parallel process using the 2,304 MB Lambda configuration took 7 seconds, which is 85 percent less.

![Chart showing the decrease in time when switching from sequential to parallel processing.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b46e9b16-9842-4291-adfa-3ef012b89aec/images/f3dcc44d-ac20-4b75-897d-1d71f0d59781.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

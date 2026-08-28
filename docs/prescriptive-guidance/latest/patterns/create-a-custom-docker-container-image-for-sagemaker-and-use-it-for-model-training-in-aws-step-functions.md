---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions.html
---

# Create a custom Docker container image for SageMaker and use it for model training in AWS Step Functions
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions"></a>

*Julia Bluszcz, Aubrey Oosthuizen, Mohan Gowda Purushothama, Neha Sharma, and Mateusz Zaremba, Amazon Web Services*

## Summary
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions-summary"></a>

This pattern shows how to create a Docker container image for [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) and use it for a training model in [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html). By packaging custom algorithms in a container, you can run almost any code in the SageMaker environment, regardless of programming language, framework, or dependencies.

In the example [SageMaker notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/nbi.html) provided, the custom Docker container image is stored in [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html). Step Functions then uses the container that’s stored in Amazon ECR to run a Python processing script for SageMaker. Then, the container exports the model to [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

## Prerequisites and limitations
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An [AWS Identity and Access Management (IAM) role for SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/sagemaker-roles.html) with Amazon S3 permissions
+ An [IAM role for Step Functions](https://sagemaker-examples.readthedocs.io/en/latest/step-functions-data-science-sdk/step_functions_mlworkflow_processing/step_functions_mlworkflow_scikit_learn_data_processing_and_model_evaluation.html#Create-an-Execution-Role-for-Step-Functions)
+ Familiarity with Python
+ Familiarity with the Amazon SageMaker Python SDK
+ Familiarity with the AWS Command Line Interface (AWS CLI)
+ Familiarity with AWS SDK for Python (Boto3)
+ Familiarity with Amazon ECR
+ Familiarity with Docker

**Product versions**
+ AWS Step Functions Data Science SDK version 2.3.0
+ Amazon SageMaker Python SDK version 2.78.0

## Architecture
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions-architecture"></a>

The following diagram shows an example workflow for creating a Docker container image for SageMaker, then using it for a training model in Step Functions:

![Workflow to create Docker container image for SageMaker to use as a Step Functions training model.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/7857d57f-3077-4b06-8971-fb5846387693/images/37755e38-0bc4-4dd0-90c7-135d95b00053.png)

The diagram shows the following workflow:

1. A data scientist or DevOps engineer uses a Amazon SageMaker notebook to create a custom Docker container image.

1. A data scientist or DevOps engineer stores the Docker container image in an Amazon ECR private repository that’s in a private registry.

1. A data scientist or DevOps engineer uses the Docker container to run a Python SageMaker processing job in a Step Functions workflow.

**Automation and scale**

The example SageMaker notebook in this pattern uses an `ml.m5.xlarge` notebook instance type. You can change the instance type to fit your use case. For more information about SageMaker notebook instance types, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/).

## Tools
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions-tools"></a>
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is a managed machine learning (ML) service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [Amazon SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk) is an open source library for training and deploying machine-learning models on SageMaker.
+ [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) is a serverless orchestration service that helps you combine AWS Lambda functions and other AWS services to build business-critical applications.
+ [AWS Step Functions Data Science Python SDK](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/index.html) is an open source library that helps you create Step Functions workflows that process and publish machine learning models.

## Epics
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions-epics"></a>

### Create a custom Docker container image and store it in Amazon ECR
<a name="create-a-custom-docker-container-image-and-store-it-in-amazon-ecr"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Setup Amazon ECR and create a new private registry. | If you haven’t already, set up Amazon ECR by following the instructions in [Setting up with Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/get-set-up-for-amazon-ecr.html) in the *Amazon ECR User Guide*. Each AWS account is provided with a default private Amazon ECR registry. | DevOps engineer |
| Create an Amazon ECR private repository. | Follow the instructions in [Creating a private repository](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the *Amazon ECR User Guide*.The repository that you create is where you’ll store your custom Docker container images. | DevOps engineer |
| Create a Dockerfile that includes the specifications needed to run your SageMaker processing job.  | Create a Dockerfile that includes the specifications needed to run your SageMaker processing job by configuring a Dockerfile. For instructions, see [Adapting your own training container](https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-training-container.html) in the *Amazon SageMaker Developer Guide*.<br />For more information about Dockerfiles, see the [Dockerfile Reference](https://docs.docker.com/engine/reference/builder/) in the Docker documentation.<br />**Example Jupyter notebook code cells to create a Dockerfile**<br />*Cell 1*<pre># Make docker folder<br />!mkdir -p docker</pre><br />*Cell 2*<pre>%%writefile docker/Dockerfile<br /><br />FROM python:3.7-slim-buster<br /><br />RUN pip3 install pandas==0.25.3 scikit-learn==0.21.3<br />ENV PYTHONUNBUFFERED=TRUE<br /><br />ENTRYPOINT ["python3"]</pre> | DevOps engineer |
| Build your Docker container image and push it to Amazon ECR. | 1. Build the container image using the Dockerfile that you created by running the `docker build` command in the AWS CLI.<br />2. Push the container image to Amazon ECR by running the `docker push` command.For more information, see [Building and registering the container](https://sagemaker-examples.readthedocs.io/en/latest/advanced_functionality/scikit_bring_your_own/scikit_bring_your_own.html#Building-and-registering-the-container) in *Building your own algorithm container* on GitHub.<br />**Example Jupyter notebook code cells to build and register a Docker image**Before running the following cells, make sure that you’ve created a Dockerfile and stored it in the directory called `docker`. Also, make sure that you’ve created an Amazon ECR repository, and that you replace the `ecr_repository` value in the first cell with your repository’s name.<br />*Cell 1*<pre>import boto3<br />tag = ':latest'<br />account_id = boto3.client('sts').get_caller_identity().get('Account')<br />region = boto3.Session().region_name<br />ecr_repository = 'byoc'<br /><br />image_uri = '{}.dkr.ecr.{}.amazonaws.com/{}'.format(account_id, region, ecr_repository + tag)</pre><br />*Cell 2*<pre># Build docker image<br />!docker build -t $image_uri docker</pre><br />*Cell 3*<pre># Authenticate to ECR<br />!aws ecr get-login-password --region {region} | docker login --username AWS --password-stdin {account_id}.dkr.ecr.{region}.amazonaws.com</pre><br />*Cell 4*<pre># Push docker image<br />!docker push $image_uri</pre>You must [authenticate your Docker client to your private registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html) so that you can use the `docker push` and `docker pull` commands. These commands push and pull images to and from the repositories in your registry. | DevOps engineer |

### Create a Step Functions workflow that uses your custom Docker container image
<a name="create-a-step-functions-workflow-that-uses-your-custom-docker-container-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Python script that includes your custom processing and model training logic. | Write custom processing logic to run in your data processing script. Then, save it as a Python script named `training.py`.<br />For more information, see [Bring your own model with SageMaker Script Mode](https://sagemaker-examples.readthedocs.io/en/latest/sagemaker-script-mode/sagemaker-script-mode.html) on GitHub.<br />**Example Python script that includes custom processing and model training logic**<pre>%%writefile training.py<br />from numpy import empty<br />import pandas as pd<br />import os<br />from sklearn import datasets, svm<br />from joblib import dump, load<br /><br /><br />if __name__ == '__main__':<br />    digits = datasets.load_digits()<br />    #create classifier object<br />    clf = svm.SVC(gamma=0.001, C=100.)<br />    <br />    #fit the model<br />    clf.fit(digits.data[:-1], digits.target[:-1])<br />    <br />    #model output in binary format<br />    output_path = os.path.join('/opt/ml/processing/model', "model.joblib")<br />    dump(clf, output_path)</pre> | Data scientist |
| Create a Step Functions workflow that includes your SageMaker Processing job as one of the steps.  | Install and import the [AWS Step Functions Data Science SDK](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/readmelink.html) and upload the **training.py** file to Amazon S3. Then, use the [Amazon SageMaker Python SDK](https://github.com/aws/sagemaker-python-sdk) to define a processing step in Step Functions.Make sure that you’ve [created an IAM execution role for Step Functions](https://sagemaker-examples.readthedocs.io/en/latest/step-functions-data-science-sdk/step_functions_mlworkflow_processing/step_functions_mlworkflow_scikit_learn_data_processing_and_model_evaluation.html#Create-an-Execution-Role-for-Step-Functions) in your AWS account.<br />**Example environment set up and custom training script to upload to Amazon S3**<pre>!pip install stepfunctions<br /><br />import boto3<br />import stepfunctions<br />import sagemaker<br />import datetime<br /><br />from stepfunctions import steps<br />from stepfunctions.inputs import ExecutionInput<br />from stepfunctions.steps import (<br />    Chain<br />)<br />from stepfunctions.workflow import Workflow<br />from sagemaker.processing import ScriptProcessor, ProcessingInput, ProcessingOutput<br /><br />sagemaker_session = sagemaker.Session()<br />bucket = sagemaker_session.default_bucket() <br />role = sagemaker.get_execution_role()<br />prefix = 'byoc-training-model'<br /><br /># See prerequisites section to create this role<br />workflow_execution_role = f"arn:aws:iam::{account_id}:role/AmazonSageMaker-StepFunctionsWorkflowExecutionRole"<br /><br />execution_input = ExecutionInput(<br />    schema={<br />        "PreprocessingJobName": str})<br /><br /><br />input_code = sagemaker_session.upload_data(<br />    "training.py",<br />    bucket=bucket,<br />    key_prefix="preprocessing.py",<br />)</pre><br />**Example SageMaker processing step definition that uses a custom Amazon ECR image and Python script**Make sure that you use the `execution_input` parameter to specify the job name. The parameter’s value must be unique each time the job runs. Also, the **training.py** file’s code is passed as an `input` parameter to the `ProcessingStep`, which means that it will be copied inside the container. The destination for the `ProcessingInput` code is the same as the second argument inside the `container_entrypoint`.<pre>script_processor = ScriptProcessor(command=['python3'],<br />                image_uri=image_uri,<br />                role=role,<br />                instance_count=1,<br />                instance_type='ml.m5.xlarge')<br /><br /><br />processing_step = steps.ProcessingStep(<br />    "training-step",<br />    processor=script_processor,<br />    job_name=execution_input["PreprocessingJobName"],<br />    inputs=[<br />        ProcessingInput(<br />            source=input_code,<br />            destination="/opt/ml/processing/input/code",<br />            input_name="code",<br />        ),<br />    ],<br />    outputs=[<br />        ProcessingOutput(<br />            source='/opt/ml/processing/model', <br />            destination="s3://{}/{}".format(bucket, prefix), <br />            output_name='byoc-example')<br />    ],<br />    container_entrypoint=["python3", "/opt/ml/processing/input/code/training.py"],<br />)</pre><br />**Example Step Functions workflow that runs a SageMaker processing job**This example workflow includes the SageMaker processing job step only, not a complete Step Functions workflow. For a full example workflow, see [Example notebooks in SageMaker](https://aws-step-functions-data-science-sdk.readthedocs.io/en/stable/readmelink.html#example-notebooks-in-sagemaker) in the AWS Step Functions Data Science SDK documentation.<pre>workflow_graph = Chain([processing_step])<br /><br />workflow = Workflow(<br />    name="ProcessingWorkflow",<br />    definition=workflow_graph,<br />    role=workflow_execution_role<br />)<br /><br />workflow.create()<br /># Execute workflow<br />execution = workflow.execute(<br />    inputs={<br />        "PreprocessingJobName": str(datetime.datetime.now().strftime("%Y%m%d%H%M-%SS")),  # Each pre processing job (SageMaker processing job) requires a unique name,<br />    }<br />)<br />execution_output = execution.get_output(wait=True)</pre> | Data scientist |

## Related resources
<a name="create-a-custom-docker-container-image-for-sagemaker-and-use-it-for-model-training-in-aws-step-functions-resources"></a>
+ [Process data](https://docs.aws.amazon.com/sagemaker/latest/dg/processing-job.html) (*Amazon SageMaker Developer Guide*)
+ [Adapting your own training container](https://docs.aws.amazon.com/sagemaker/latest/dg/adapt-training-container.html) (*Amazon SageMaker Developer Guide*)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

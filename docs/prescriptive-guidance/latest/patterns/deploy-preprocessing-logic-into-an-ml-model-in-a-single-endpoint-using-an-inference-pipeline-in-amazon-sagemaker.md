---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker.html
---

# Deploy preprocessing logic into an ML model in a single endpoint using an inference pipeline in Amazon SageMaker
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker"></a>

*Mohan Gowda Purushothama, Gabriel Rodriguez Garcia, and Mateusz Zaremba, Amazon Web Services*

## Summary
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker-summary"></a>

This pattern explains how to deploy multiple pipeline model objects in a single endpoint by using an [inference pipeline](https://docs.aws.amazon.com/sagemaker/latest/dg/inference-pipelines.html) in Amazon SageMaker. The pipeline model object represents different machine learning (ML) workflow stages, such as preprocessing, model inference, and postprocessing. To illustrate the deployment of serially connected pipeline model objects, this pattern shows you how to deploy a preprocessing [Scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/sklearn.html) container and a regression model based on the [linear learner algorithm](https://docs.aws.amazon.com/sagemaker/latest/dg/linear-learner.html) built into SageMaker. The deployment is hosted behind a single endpoint in SageMaker.

**Note**
The deployment in this pattern uses the ml.m4.2xlarge instance type. We recommend using an instance type that aligns with your data size requirements and the complexity of your workflow. For more information, see [Amazon SageMaker Pricing](https://aws.amazon.com/sagemaker/pricing/). This pattern uses [prebuilt Docker images for Scikit-learn](https://docs.aws.amazon.com/sagemaker/latest/dg/pre-built-docker-containers-scikit-learn-spark.html), but you can use your own Docker containers and integrate them into your workflow.

## Prerequisites and limitations
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ [Python 3.9](https://www.python.org/downloads/release/python-390/)
+ [Amazon SageMaker Python SDK](https://sagemaker.readthedocs.io/en/stable/) and [Boto3 library](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
+ AWS Identity and Access Management (AWS IAM) [role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html) with basic SageMaker [permissions](https://docs.aws.amazon.com/sagemaker/latest/dg/api-permissions-reference.html) and Amazon Simple Storage Service (Amazon S3) [permissions](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-policy-language-overview.html)

**Product versions**
+ [Amazon SageMaker Python SDK 2.49.2](https://sagemaker.readthedocs.io/en/v2.49.2/)

## Architecture
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker-architecture"></a>

**Target technology stack**
+ Amazon Elastic Container Registry (Amazon ECR)
+ Amazon SageMaker
+ Amazon SageMaker Studio
+ Amazon Simple Storage Service (Amazon S3)
+ [Real-time inference](https://docs.aws.amazon.com/sagemaker/latest/dg/realtime-endpoints.html) endpoint for Amazon SageMaker

**Target architecture**

The following diagram shows the architecture for the deployment of an Amazon SageMaker pipeline model object.

![Architecture for deployment of SageMaker pipeline model object](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1105d51b-752f-46d7-962c-acef1fb3399f/images/12f06715-b1c2-4de0-b277-99ce87308152.png)

The diagram shows the following workflow:

1. A SageMaker notebook deploys a pipeline model.

1. An S3 bucket stores the model artifacts.

1. Amazon ECR gets the source container images from the S3 bucket.

## Tools
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker-tools"></a>

**AWS tools**
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon SageMaker](https://docs.aws.amazon.com/sagemaker/latest/dg/whatis.html) is a managed ML service that helps you build and train ML models and then deploy them into a production-ready hosted environment.
+ [Amazon SageMaker Studio](https://docs.aws.amazon.com/sagemaker/latest/dg/studio.html) is a web-based, integrated development environment (IDE) for ML that lets you build, train, debug, deploy, and monitor your ML models.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Code**

The code for this pattern is available in the GitHub [Inference Pipeline with Scikit-learn and Linear Learner](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-python-sdk/scikit_learn_inference_pipeline/Inference%20Pipeline%20with%20Scikit-learn%20and%20Linear%20Learner.ipynb) repository.

## Epics
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker-epics"></a>

### Prepare the dataset
<a name="prepare-the-dataset"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the dataset for your regression task. | [Open a notebook](https://docs.aws.amazon.com/sagemaker/latest/dg/notebooks-create-open.html#notebooks-open) in Amazon SageMaker Studio.<br />To import all necessary libraries and initialize your working environment, use the following example code in your notebook:<pre>import sagemaker<br />from sagemaker import get_execution_role<br /><br />sagemaker_session = sagemaker.Session()<br /><br /># Get a SageMaker-compatible role used by this Notebook Instance.<br />role = get_execution_role()<br /><br /># S3 prefix<br />bucket = sagemaker_session.default_bucket()<br />prefix = "Scikit-LinearLearner-pipeline-abalone-example"</pre><br />To download a sample dataset, add the following code to your notebook:<pre>! mkdir abalone_data<br />! aws s3 cp s3://sagemaker-sample-files/datasets/tabular/uci_abalone/abalone.csv ./abalone_data</pre>** **The example in this pattern uses the [Abalone Data Set](https://archive.ics.uci.edu/ml/datasets/abalone) from the UCI Machine Learning Repository. | Data scientist |
| Upload the dataset to an S3 bucket. | In the notebook where you prepared your dataset earlier, add the following code to upload your sample data to an S3 bucket:<pre>WORK_DIRECTORY = "abalone_data"<br /><br />train_input = sagemaker_session.upload_data(<br />    path="{}/{}".format(WORK_DIRECTORY, "abalone.csv"),<br />    bucket=bucket,<br />    key_prefix="{}/{}".format(prefix, "train"),<br />)</pre> | Data scientist |

### Create the data preprocessor using SKLearn
<a name="create-the-data-preprocessor-using-sklearn"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Prepare the preprocessor.py script. | 1. Copy the preprocessing logic from the Python file in the GitHub [sklearn\_abalone\_featurizer.py](https://github.com/aws/amazon-sagemaker-examples/blob/main/sagemaker-python-sdk/scikit_learn_inference_pipeline/sklearn_abalone_featurizer.py) repository, and then paste the code into a separate Python file called `sklearn_abalone_featurizer.py`. You can modify the code to fit your custom dataset and custom workflow.<br />2. Save the `sklearn_abalone_featurizer.py` file in the root directory of your project (that is, in the same location where you run your SageMaker notebook). | Data scientist |
| Create the SKLearn preprocessor object. | To create an SKLearn preprocessor object (called SKLearn Estimator) that you can incorporate into your final inference pipeline, run the following code in your SageMaker notebook:<pre>from sagemaker.sklearn.estimator import SKLearn<br /><br />FRAMEWORK_VERSION = "0.23-1"<br />script_path = "sklearn_abalone_featurizer.py"<br /><br />sklearn_preprocessor = SKLearn(<br />    entry_point=script_path,<br />    role=role,<br />    framework_version=FRAMEWORK_VERSION,<br />    instance_type="ml.c4.xlarge",<br />    sagemaker_session=sagemaker_session,<br />)<br />sklearn_preprocessor.fit({"train": train_input})</pre> | Data scientist |
| Test the preprocessor's inference. | To confirm that your preprocessor is defined correctly, launch a [batch transform job](https://docs.aws.amazon.com/sagemaker/latest/dg/batch-transform.html) by entering the following code in your SageMaker notebook:<pre># Define a SKLearn Transformer from the trained SKLearn Estimator<br />transformer = sklearn_preprocessor.transformer(<br />    instance_count=1, instance_type="ml.m5.xlarge", assemble_with="Line", accept="text/csv"<br />)<br /><br /><br /># Preprocess training input<br />transformer.transform(train_input, content_type="text/csv")<br />print("Waiting for transform job: " + transformer.latest_transform_job.job_name)<br />transformer.wait()<br />preprocessed_train = transformer.output_path</pre> |  |

### Create a machine learning model
<a name="create-a-machine-learning-model"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a model object. | To create a model object based on the linear learner algorithm, enter the following code in your SageMaker notebook:<pre>import boto3<br />from sagemaker.image_uris import retrieve<br /><br />ll_image = retrieve("linear-learner", boto3.Session().region_name)<br />s3_ll_output_key_prefix = "ll_training_output"<br />s3_ll_output_location = "s3://{}/{}/{}/{}".format(<br />    bucket, prefix, s3_ll_output_key_prefix, "ll_model"<br />)<br /><br />ll_estimator = sagemaker.estimator.Estimator(<br />    ll_image,<br />    role,<br />    instance_count=1,<br />    instance_type="ml.m4.2xlarge",<br />    volume_size=20,<br />    max_run=3600,<br />    input_mode="File",<br />    output_path=s3_ll_output_location,<br />    sagemaker_session=sagemaker_session,<br />)<br /><br />ll_estimator.set_hyperparameters(feature_dim=10, predictor_type="regressor", mini_batch_size=32)<br /><br />ll_train_data = sagemaker.inputs.TrainingInput(<br />    preprocessed_train,<br />    distribution="FullyReplicated",<br />    content_type="text/csv",<br />    s3_data_type="S3Prefix",<br />)<br /><br />data_channels = {"train": ll_train_data}<br />ll_estimator.fit(inputs=data_channels, logs=True)</pre><br />The preceding code retrieves the relevant Amazon ECR Docker image from the public Amazon ECR Registry for the model, creates an estimator object, and then uses that object to train the regression model. | Data scientist |

### Deploy the final pipeline
<a name="deploy-the-final-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the pipeline model. | To create a pipeline model object (that is, a preprocessor object) and deploy the object, enter the following code in your SageMaker notebook:<pre>from sagemaker.model import Model<br />from sagemaker.pipeline import PipelineModel<br />import boto3<br />from time import gmtime, strftime<br /><br />timestamp_prefix = strftime("%Y-%m-%d-%H-%M-%S", gmtime())<br /><br />scikit_learn_inferencee_model = sklearn_preprocessor.create_model()<br />linear_learner_model = ll_estimator.create_model()<br /><br />model_name = "inference-pipeline-" + timestamp_prefix<br />endpoint_name = "inference-pipeline-ep-" + timestamp_prefix<br />sm_model = PipelineModel(<br />    name=model_name, role=role, models= [scikit_learn_inferencee_model, linear_learner_model]<br />)<br /><br />sm_model.deploy(initial_instance_count=1, instance_type="ml.c4.xlarge", endpoint_name=endpoint_name)</pre>You can adjust the instance type used in the model object to meet your needs. | Data scientist |
| Test the inference. | To confirm the endpoint is working correctly, run the following sample inference code in your SageMaker notebook:<pre>from sagemaker.predictor import Predictor<br />from sagemaker.serializers import CSVSerializer<br /><br />payload = "M, 0.44, 0.365, 0.125, 0.516, 0.2155, 0.114, 0.155"<br />actual_rings = 10<br />predictor = Predictor(<br />    endpoint_name=endpoint_name, sagemaker_session=sagemaker_session, serializer=CSVSerializer()<br />)<br /><br />print(predictor.predict(payload))</pre> | Data scientist |

## Related resources
<a name="deploy-preprocessing-logic-into-an-ml-model-in-a-single-endpoint-using-an-inference-pipeline-in-amazon-sagemaker-resources"></a>
+ [Preprocess input data before making predictions using Amazon SageMaker inference pipelines and Scikit-learn](https://aws.amazon.com/blogs/machine-learning/preprocess-input-data-before-making-predictions-using-amazon-sagemaker-inference-pipelines-and-scikit-learn/) (AWS Machine Learning Blog)
+ [End to end Machine Learning with Amazon SageMaker](https://github.com/aws-samples/amazon-sagemaker-build-train-deploy) (GitHub)

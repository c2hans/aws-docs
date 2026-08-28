---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/streamline-machine-learning-workflows-by-using-amazon-sagemaker.html
---

# Streamline machine learning workflows from local development to scalable experiments by using SageMaker AI and Hydra
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker"></a>

*David Sauerwein, Marco Geiger, and Julian Ferdinand Grueber, Amazon Web Services*

## Summary
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-summary"></a>

This pattern provides a unified approach to configuring and running machine learning (ML) algorithms from local testing to production on Amazon SageMaker AI. ML algorithms are the focus of this pattern, but its approach extends to feature engineering, inference, and whole ML pipelines. This pattern demonstrates the transition from local script development to SageMaker AI training jobs through a sample use case.

A typical ML workflow is to develop and test solutions on a local machine, run large scale experiments (for example, with different parameters) in the cloud, and deploy the approved solution in the cloud. Then, the deployed solution must be monitored and maintained. Without a unified approach to this workflow, developers often need to refactor their code at each stage. If the solution depends on a large number of parameters that might change at any stage of this workflow, it can become increasingly difficult to remain organized and consistent.

This pattern addresses these challenges. First, it eliminates the need for code refactoring between environments by providing a unified workflow that remains consistent whether running on local machines, in containers, or on SageMaker AI. Second, it simplifies parameter management through Hydra's configuration system, where parameters are defined in separate configuration files that can be easily modified and combined, with automatic logging of each run's configuration. For more details about how this pattern addresses these challenges, see [Additional information](#streamline-machine-learning-workflows-by-using-amazon-sagemaker-additional).

## Prerequisites and limitations
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ An AWS Identity and Access Management (IAM) [user role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create_for-user.html) for deploying and starting the SageMaker AI training jobs
+ AWS Command Line Interface (AWS CLI) version 2.0 or later [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html)
+ [Poetry](https://python-poetry.org/) version 1.8 or later, but earlier than 2.0, installed
+ [Docker](https://www.docker.com/) installed
+ Python [version 3.10.x](https://www.python.org/downloads/release/python-31011/)

**Limitations**
+ The code currently only targets SageMaker AI training jobs. Extending it to processing jobs and whole SageMaker AI pipelines is straightforward.
+ For a fully productionized SageMaker AI setup, additional details need to be in place. Examples could be custom AWS Key Management Service (AWS KMS) keys for compute and storage, or networking configurations. You can also configure these additional options by using Hydra in a dedicated subfolder of the `config` folder.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-architecture"></a>

The following diagram depicts the architecture of the solution.

![Workflow to create and run SageMaker AI training or HPO jobs.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/1db57484-f85c-49a6-b870-471dade02b26/images/d80e7474-a975-4d92-8f66-2d34e33053fd.png)

The diagram shows the following workflow:

1. The data scientist can iterate over the algorithm at small scale in a local environment, adjust parameters, and test the training script rapidly without the need for Docker or SageMaker AI. (For more details, see the "Run locally for quick testing" task in [Epics](#streamline-machine-learning-workflows-by-using-amazon-sagemaker-epics).)

1. Once satisfied with the algorithm, the data scientist builds and pushes the Docker image to the Amazon Elastic Container Registry (Amazon ECR) repository named `hydra-sm-artifact`. (For more details, see "Run workflows on SageMaker AI" in [Epics](#streamline-machine-learning-workflows-by-using-amazon-sagemaker-epics).)

1. The data scientist initiates either SageMaker AI training jobs or hyperparameter optimization (HPO) jobs by using Python scripts. For regular training jobs, the adjusted configuration is written to the Amazon Simple Storage Service (Amazon S3) bucket named `hydra-sample-config`. For HPO jobs, the default configuration set located in the `config` folder is applied.

1. The SageMaker AI training job pulls the Docker image, reads the input data from the Amazon S3 bucket `hydra-sample-data`, and either fetches the configuration from the Amazon S3 bucket `hydra-sample-config` or uses the default configuration. After training, the job saves the output data to the Amazon S3 bucket `hydra-sample-data`.

**Automation and scale**
+ For automated training, retraining, or inference, you can integrate the AWS CLI code with services like [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html), [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html), or [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html).
+ Scaling can be achieved by changing configurations for instance sizes or by adding configurations for distributed training.

## Tools
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWS services through commands in your command-line shell. For this pattern, the AWS CLI is useful for both initial resource configuration and testing.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/?id=docs_gateway) is a managed machine learning (ML) service that helps you build and train ML models and then deploy them into a production-ready hosted environment. SageMaker AI Training is a fully managed ML service within SageMaker AI that enables the training of ML models at scale. The tool can handle the computational demands of training models efficiently, making use of built-in scalability and integration with other AWS services. SageMaker AI Training also supports custom algorithms and containers, making it flexible for a wide range of ML workflows.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers. It was used in this pattern to ensure consistent environments across various stages, from development to deployment, and to package dependencies and code reliably. Docker’s containerization allowed for easy scaling and version control across the workflow.
+ [Hydra](https://hydra.cc/) is a configuration management tool that provides flexibility for handling multiple configurations and dynamic resource management. It is instrumental in managing environment configurations, allowing seamless deployment across different environments. For more details about Hydra, see [Additional information](#streamline-machine-learning-workflows-by-using-amazon-sagemaker-additional).
+ [Python](https://www.python.org/) is a general-purpose computer programming language. Python was used to write the ML code and the deployment workflow.
+ [Poetry](https://python-poetry.org/) is a tool for dependency management and packaging in Python.

**Code repository**

The code for this pattern is available in the GitHub [configuring-sagemaker-training-jobs-with-hydra](https://github.com/aws-samples/configuring-sagemaker-training-jobs-with-hydra) repository.

## Best practices
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-best-practices"></a>
+ Choose an IAM role for deploying and starting the SageMaker AI training jobs that follows the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.
+ Use temporary credentials to access the IAM role in the terminal.

## Epics
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and activate the virtual environment. | To create and activate the virtual environment, run the following commands in the root of the repository:<pre>poetry install <br />poetry shell</pre> | General AWS |
| Deploy the infrastructure.  | To deploy the infrastructure using CloudFormation, run the following command:<pre>aws cloudformation deploy --template-file infra/hydra-sagemaker-setup.yaml --stack-name hydra-sagemaker-setup  --capabilities CAPABILITY_NAMED_IAM</pre> | General AWS, DevOps engineer |
| Download the sample data.  | To download the input data from [openml](https://www.openml.org/) to your local machine, run the following command:<pre>python scripts/download_data.py</pre> | General AWS |
| Run locally for quick testing. | To run the training code locally for testing, run the following command:<pre>python mypackage/train.py data.train_data_path=data/train.csv evaluation.base_dir_path=data</pre><br />The logs of all executions are stored by execution time in a folder called `outputs`. For more information, see the "Output" section in the [GitHub repository](https://github.com/aws-samples/configuring-sagemaker-training-jobs-with-hydra).<br />You can also perform multiple trainings in parallel, with different parameters, by using the `--multirun` functionality. For more details, see the [Hydra documentation](https://hydra.cc/docs/tutorials/basic/running_your_app/multi-run/). | Data scientist |

### Run workflows on SageMaker AI
<a name="run-workflows-on-sm"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set the environment variables. | To run your job on SageMaker AI, set the following environment variables, providing your AWS Region and your AWS account ID:<pre>export ECR_REPO_NAME=hydra-sm-artifact<br />export image_tag=latest<br />export AWS_REGION="<your_aws_region>" # for instance, us-east-1<br />export ACCOUNT_ID="<your_account_id>"<br />export BUCKET_NAME_DATA=hydra-sample-data-$ACCOUNT_ID<br />export BUCKET_NAME_CONFIG=hydra-sample-config-$ACCOUNT_ID<br />export AWS_DEFAULT_REGION=$AWS_REGION<br />export ROLE_ARN=arn:aws:iam::${ACCOUNT_ID}:role/hydra-sample-sagemaker<br />export INPUT_DATA_S3_PATH=s3://$BUCKET_NAME_DATA/hydra-on-sm/input/<br />export OUTPUT_DATA_S3_PATH=s3://$BUCKET_NAME_DATA/hydra-on-sm/output/</pre> | General AWS |
| Create and push Docker image. | To create the Docker image and push it to the Amazon ECR repository, run the following command:<pre>chmod +x scripts/create_and_push_image.sh<br />scripts/create_and_push_image.sh $ECR_REPO_NAME $image_tag $AWS_REGION $ACCOUNT_ID</pre><br />This task assumes that you have valid credentials in your environment. The Docker image is pushed to the Amazon ECR repository specified in the environment variable in the previous task and is used to activate the SageMaker AI container in which the training job will run. | ML engineer, General AWS |
| Copy input data to Amazon S3. | The SageMaker AI training job needs to pick up the input data. To copy the input data to the Amazon S3 bucket for data, run the following command: <pre>aws s3 cp data/train.csv "${INPUT_DATA_S3_PATH}train.csv" </pre> | Data engineer, General AWS |
| Submit SageMaker AI training jobs. | To simplify the execution of your scripts, specify default configuration parameters in the `default.yaml` file. In addition to ensuring consistency across runs, this approach also offers the flexibility to easily override default settings as needed. See the following example:<pre>python scripts/start_sagemaker_training_job.py sagemaker.role_arn=$ROLE_ARN sagemaker.config_s3_bucket=$BUCKET_NAME_CONFIG sagemaker.input_data_s3_path=$INPUT_DATA_S3_PATH sagemaker.output_data_s3_path=$OUTPUT_DATA_S3_PATH</pre> | General AWS, ML engineer, Data scientist |
| Run SageMaker AI hyperparameter tuning. | Running SageMaker AI hyperparameter tuning is similar to submitting a SageMaker AII training job. However, the execution script differs in some important ways as you can see in the [start\_sagemaker\_hpo\_job.py](https://github.com/aws-samples/configuring-sagemaker-training-jobs-with-hydra/blob/main/scripts/start_sagemaker_hpo_job.py) file. The hyperparameters to be tuned must be passed through the boto3 payload, not a channel to the training job.<br />To start the hyperparameter optimization (HPO) job, run the following commands:<pre>python scripts/start_sagemaker_hpo_job.py sagemaker.role_arn=$ROLE_ARN sagemaker.config_s3_bucket=$BUCKET_NAME_CONFIG sagemaker.input_data_s3_path=$INPUT_DATA_S3_PATH sagemaker.output_data_s3_path=$OUTPUT_DATA_S3_PATH</pre> | Data scientist |

## Troubleshooting
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Expired token | Export fresh AWS credentials. |
| Lack of IAM permissions | Make sure that you export the credentials of an IAM role that has all the required IAM permissions to deploy the CloudFormation template and to start the SageMaker AI training jobs. |

## Related resources
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-resources"></a>
+ [Train a model with Amazon SageMaker AI](https://docs.aws.amazon.com/sagemaker/latest/dg/how-it-works-training.html) (AWS documentation)
+ [What is Hyperparameter Tuning?](https://aws.amazon.com/what-is/hyperparameter-tuning/#:~:text=Hyperparameter%20tuning%20allows%20data%20scientists,the%20model%20as%20a%20hyperparameter.)

## Additional information
<a name="streamline-machine-learning-workflows-by-using-amazon-sagemaker-additional"></a>

This pattern addresses the following challenges:

**Consistency from local development to at-scale deployment** – With this pattern, developers can use the same workflow, regardless of whether they’re using local Python scripts, running local Docker containers, conducting large experiments on SageMaker AI, or deploying in production on SageMaker AI. This consistency is important for the following reasons:
+ **Faster iteration** – It allows for fast, local experimentation without the need for major adjustments when scaling up.
+ **No refactoring** – Transitioning to larger experiments on SageMaker AI is seamless, requiring no overhaul of the existing setup.
+ **Continuous improvement** – Developing new features and continuously improving the algorithm is straightforward because the code remains the same across environments.

**Configuration management** – This pattern makes use of [Hydra](https://hydra.cc/), a configuration management tool, to provide the following benefits:
+ Parameters are defined in configuration files, separate from the code.
+ Different parameter sets can be swapped or combined easily.
+ Experiment tracking is simplified because each run's configuration is logged automatically.
+ Cloud experiments can use the same configuration structure as local runs, ensuring consistency.

With Hydra, you can manage configuration effectively, enabling the following features:
+ **Divide configurations** – Break your project configurations into smaller, manageable pieces that can be independently modified. This approach makes it easier to handle complex projects.
+ **Adjust defaults easily** – Change your baseline configurations quickly, making it simpler to test new ideas.
+ **Align CLI inputs and config files** – Combine command line inputs with your configuration files smoothly. This approach reduces clutter and confusion, making your project more manageable over time.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

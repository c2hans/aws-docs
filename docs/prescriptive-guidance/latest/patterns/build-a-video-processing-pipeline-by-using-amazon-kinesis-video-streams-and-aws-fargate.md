---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate.html
---

# Build a video processing pipeline by using Amazon Kinesis Video Streams and AWS Fargate
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate"></a>

*Piotr Chotkowski and Pushparaju Thangavel, Amazon Web Services*

## Summary
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-summary"></a>

This pattern demonstrates how to use [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) and [AWS Fargate](https://aws.amazon.com/fargate) to extract frames from a video stream and store them as image files for further processing in [Amazon Simple Storage Service (Amazon S3](https://aws.amazon.com/s3/)).

The pattern provides a sample application in the form of a Java Maven project. This application defines the AWS infrastructure by using the [AWS Cloud Development Kit](https://aws.amazon.com/cdk/) (AWS CDK). Both the frame processing logic and the infrastructure definitions are written in the Java programming language. You can use this sample application as a basis for developing your own real-time video processing pipeline or to build the video preprocessing step of a machine learning pipeline.

## Prerequisites and limitations
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-prereqs"></a>

**Prerequisites **
+ An active AWS account
+ Java SE Development Kit (JDK) 11, installed
+ [Apache Maven](https://maven.apache.org/), installed
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/getting_started.html), installed
+ [AWS Command Line Interface (AWS CLI)](https://docs.aws.amazon.com/cli/latest/userguide/install-cliv2.html) version 2, installed
+ [Docker](https://docs.docker.com/get-docker/) (required for building Docker images to use in AWS Fargate task definitions), installed

**Limitations **

This pattern is intended as a proof of concept, or as a basis for further development. It should not be used in its current form in production deployments.

**Product versions**
+ This pattern was tested with the AWS CDK version 1.77.0 (see [AWS CDK versions](https://docs.aws.amazon.com/cdk/api/latest/versions.html))
+ JDK 11
+ AWS CLI version 2

## Architecture
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-architecture"></a>

**Target technology stack**
+ Amazon Kinesis Video Streams
+ AWS Fargate task
+ Amazon Simple Queue Service (Amazon SQS) queue
+ Amazon S3 bucket

**Target architecture**

![Architecture for using Kinesis Video Streams and Fargate to build a video processing pipeline.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/9d1442c2-f3ee-47fd-8cce-90d9206ce4d4/images/a60e585f-27be-4dd6-897b-c38adf1d283f.png)

The user creates a Kinesis video stream, uploads a video, and sends a JSON message that contains details about the input Kinesis video stream and the output S3 bucket to an SQS queue. AWS Fargate, which is running the main application in a container, pulls the message from the SQS queue and starts extracting frames. Each frame is saved in an image file and stored in the target S3 bucket.

**Automation and scale**

The sample application can scale both horizontally and vertically within a single AWS Region. Horizontal scaling can be achieved by increasing the number of deployed AWS Fargate tasks that read from the SQS queue. Vertical scaling can be achieved by increasing the number of frame-splitting and image-publishing threads in the application. These settings are passed as environment variables to the application in the definition of the [QueueProcessingFargateService](https://docs.aws.amazon.com/cdk/api/latest/docs/@aws-cdk_aws-ecs-patterns.QueueProcessingFargateService.html) resource in the AWS CDK. Due to the nature of AWS CDK stack deployment, you can deploy this application in multiple AWS Regions and accounts with no additional effort.

## Tools
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-tools"></a>

**Tools**
+ [AWS CDK](https://aws.amazon.com/cdk/) is a software development framework for defining your cloud infrastructure and resources by using programming languages such as TypeScript, JavaScript, Python, Java, and C\#/.Net.
+ [Amazon Kinesis Video Streams](https://aws.amazon.com/kinesis/video-streams/) is a fully managed AWS service that you can use to stream live video from devices to the AWS Cloud, or build applications for real-time video processing or batch-oriented video analytics.
+ [AWS Fargate](https://aws.amazon.com/fargate) is a serverless compute engine for containers. Fargate removes the need to provision and manage servers, and lets you focus on developing your applications.
+ [Amazon S3](https://aws.amazon.com/s3/) is an object storage service that offers scalability, data availability, security, and performance.
+ [Amazon SQS](https://aws.amazon.com/sqs/) is a fully managed message queuing service that enables you to decouple and scale microservices, distributed systems, and serverless applications.

**Code**
+ A .zip file of the sample application project (`frame-splitter-code.zip`) is attached.

## Epics
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-epics"></a>

### Deploy the infrastructure
<a name="deploy-the-infrastructure"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Start the Docker daemon. | Start the Docker daemon on your local system. The AWS CDK uses Docker to build the image that is used in the AWS Fargate task. You must run Docker before you proceed to the next step. | Developer, DevOps engineer |
| Build the project. | Download the `frame-splitter-code` sample application (attached) and extract its contents into a folder on your local machine. Before you can deploy the infrastructure, you have to build the [Java Maven](https://maven.apache.org/) project. At a command prompt, navigate to the root directory of the project, and build the project by running the command: <pre>mvn clean install</pre> | Developer, DevOps engineer |
| Bootstrap the AWS CDK. | (First-time AWS CDK users only) If this is the first time you’re using the AWS CDK, you might have to bootstrap the environment by running the AWS CLI command:<pre>cdk bootstrap --profile "$AWS_PROFILE_NAME" </pre><br />where `$AWS_PROFILE_NAME` holds the name of the AWS profile from your AWS credentials. Or, you can remove this parameter to use the default profile. For more information, see the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/latest/guide/bootstrapping.html). | Developer, DevOps engineer |
| Deploy the AWS CDK stack. | In this step, you create the required infrastructure resources (SQS queue, S3 bucket, AWS Fargate task definition) in your AWS account, build the Docker image that is required for the AWS Fargate task, and deploy the application. At a command prompt, navigate to the root directory of the project, and run the command:<pre>cdk deploy --profile "$AWS_PROFILE_NAME" --all </pre><br />where `$AWS_PROFILE_NAME` holds the name of the AWS profile from your AWS credentials. Or, you can remove this parameter to use the default profile. Confirm the deployment. Note the **QueueUrl **and **Bucket **values from the CDK deployment output; you will need these in later steps. The AWS CDK creates the assets, uploads them to your AWS account, and creates all infrastructure resources. You can observe the resource creation process in the [AWS CloudFormation console](https://console.aws.amazon.com/cloudformation/). For more information, see the [AWS CloudFormation documentation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) and the [AWS CDK documentation](https://docs.aws.amazon.com/cdk/latest/guide/hello_world.html#hello_world_tutorial_deploy). | Developer, DevOps engineer |
| Create a video stream. | In this step, you create a Kinesis video stream that will serve as an input stream for video processing. Make sure that you have the AWS CLI installed and configured. In the AWS CLI, run:<pre>aws kinesisvideo --profile "$AWS_PROFILE_NAME" create-stream --stream-name "$STREAM_NAME" --data-retention-in-hours "24" </pre><br />where `$AWS_PROFILE_NAME` holds the name of the AWS profile from your AWS credentials (or remove this parameter to use the default profile) and `$STREAM_NAME` is any valid stream name. <br />Alternatively, you can create a video stream by using the Kinesis console by following the steps in the [Kinesis Video Streams documentation](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/gs-createstream.html#gs-createstream-console). Note the AWS Resource Name (ARN) of the created stream; you will need it later. | Developer, DevOps engineer |

### Run an example
<a name="run-an-example"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the video to the stream. | In the project folder for the sample `frame-splitter-code` application, open the `ProcessingTaskTest.java` file in the `src/test/java/amazon/awscdk/examples/splitter` folder. Replace the `profileName`** **and `streamName`** **variables with the values you used in the previous steps. To upload the example video to the Kinesis video stream you created in the previous step, run:  <pre>amazon.awscdk.examples.splitter.ProcessingTaskTest#testExample test</pre><br />Alternatively, you can upload your video by using one of the methods described in the [Kinesis Video Streams documentation](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/producer-sdk.html). | Developer, DevOps engineer |
| Initiate video processing. | Now that you have uploaded a video to the Kinesis video stream, you can start processing it. To initiate the processing logic, you have to send a message with details to the SQS queue that the AWS CDK created during deployment. To send a message by using the AWS CLI, run:<pre>aws sqs --profile "$AWS_PROFILE_NAME" send-message --queue-url QUEUE_URL --message-body MESSAGE </pre><br />where `$AWS_PROFILE_NAME` holds the name of the AWS profile from your AWS credentials (remove this parameter to use the default profile), `QUEUE_URL` is the **QueueUrl **value from the AWS CDK output, and `MESSAGE` is a JSON string in the following format: <pre>{ "streamARN": "STREAM_ARN", "bucket": "BUCKET_NAME", "s3Directory": "test-output" }</pre><br />where `STREAM_ARN` is the ARN of of the video stream you created in an earlier step and `BUCKET_NAME` is the **Bucket** value from the AWS CDK output. <br />Sending this message initiates video processing. Alternatively, you can send a message by using the Amazon SQS console, as described in the [Amazon SQS documentation](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-using-send-messages.html). | Developer, DevOps engineer |
| View images of the video frames. | You can see the resulting images in the S3 output bucket `s3://BUCKET_NAME/test-output` where `BUCKET_NAME` is the **Bucket** value from the AWS CDK output. | Developer, DevOps engineer |

## Related resources
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-resources"></a>
+ [AWS CDK documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
+ [AWS CDK API reference](https://docs.aws.amazon.com/cdk/api/latest/docs/aws-construct-library.html)
+ [AWS CDK introductory workshop](https://cdkworkshop.com/)
+ [Amazon Kinesis Video Streams documentation](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/what-is-kinesis-video.html)
+ [Example: Identifying Objects in Video Streams Using SageMaker](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-sagemaker.html)
+ [Example: Parsing and Rendering Kinesis Video Streams Fragments](https://docs.aws.amazon.com/kinesisvideostreams/latest/dg/examples-renderer.html)
+ [Analyze live video at scale in real time using Amazon Kinesis Video Streams and Amazon SageMaker](https://aws.amazon.com/blogs/machine-learning/analyze-live-video-at-scale-in-real-time-using-amazon-kinesis-video-streams-and-amazon-sagemaker/) (AWS Machine Learning blog post)
+ [AWS Fargate Getting Started](https://aws.amazon.com/fargate/getting-started/)

## Additional information
<a name="build-a-video-processing-pipeline-by-using-amazon-kinesis-video-streams-and-aws-fargate-additional"></a>

**Choosing an IDE**

We recommend that you use your favorite Java IDE to build and explore this project.

**Cleaning up**

After you finish running this example, remove all deployed resources to avoid incurring additional AWS infrastructure costs.

To remove the infrastructure and the video stream, use these two commands in the AWS CLI:

```
cdk destroy --profile "$AWS_PROFILE_NAME" --all
```

```
aws kinesisvideo --profile "$AWS_PROFILE_NAME" delete-stream --stream-arn "$STREAM_ARN"
```

Alternatively, you can remove the resources manually by using the AWS CloudFormation console to remove the AWS CloudFormation stack, and the Kinesis console to remove the Kinesis video stream. Note that `cdk destroy` doesn’t remove the output S3 bucket or the images in Amazon Elastic Container Registry (Amazon ECR) repositories (`aws-cdk/assets`). You have to remove them manually.

## Attachments
<a name="attachments-9d1442c2-f3ee-47fd-8cce-90d9206ce4d4"></a>

To access additional content that is associated with this document, download and unzip the following file: [attachment.zip](samples/p-attach/9d1442c2-f3ee-47fd-8cce-90d9206ce4d4/attachments/attachment.zip)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

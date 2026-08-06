---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-lambda-functions-with-container-images.html
---

# Deploy Lambda functions with container images
<a name="deploy-lambda-functions-with-container-images"></a>

*Ram Kandaswamy, Amazon Web Services*

## Summary
<a name="deploy-lambda-functions-with-container-images-summary"></a>

AWS Lambda supports containers images as a deployment model. This pattern shows how to deploy Lambda functions through container images.

Lambda is a serverless, event-driven compute service that you can use to run code for virtually any type of application or backend service without provisioning or managing servers. With container image support for Lambda functions, you get the benefits of up to 10 GB of storage for your application artifact and the ability to use familiar container image development tools.

The example in this pattern uses Python as the underlying programming language, but you can use other languages, such as Java, Node.js, or Go. For the source, consider a Git-based system such as GitHub, GitLab, or Bitbucket, or use Amazon Simple Storage Service (Amazon S3).

## Prerequisites and limitations
<a name="deploy-lambda-functions-with-container-images-prereqs"></a>

**Prerequisites **
+ Amazon Elastic Container Registry (Amazon ECR) activated
+ Application code
+ Docker images with the runtime interface client and the latest version of Python
+ Working knowledge of Git

**Limitations **
+ Maximum image size supported is 10 GB.
+ Maximum runtime for a Lambda based container deployment is 15 minutes.

## Architecture
<a name="deploy-lambda-functions-with-container-images-architecture"></a>

**Target architecture **

![Four-step process to create the Lambda function.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e421cc58-d33e-493d-b0bb-c3ffe39c2eb9/images/7f36d3d8-d161-497a-b036-26d886a16c69.png)

1. You create a Git repository and commit the application code to the repository.

1. The AWS CodeBuild project is triggered by commit changes.

1. The CodeBuild project creates the Docker image and publishes the built image to Amazon ECR.

1. You create the Lambda function using the image in Amazon ECR.

**Automation and scale**

This pattern can be automated by using AWS CloudFormation, AWS Cloud Development Kit (AWS CDK), or API operations from an SDK. Lambda can automatically scale based on the number of requests, and you can tune it by using the concurrency parameters. For more information, see the [Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/lambda-concurrency.html).

## Tools
<a name="deploy-lambda-functions-with-container-images-tools"></a>

**AWS services**
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) AWS CloudFormationhelps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions. This pattern uses [AWS CloudFormation Application Composer](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/app-composer-for-cloudformation.html), which helps you visually view and edit CloudFormation templates.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories), [GitLab](https://docs.gitlab.com/ee/user/get_started/get_started_projects.html), and [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/tutorial-learn-bitbucket-with-git/) are some of the commonly used Git-based source control system to keep track of source code changes.

## Best practices
<a name="deploy-lambda-functions-with-container-images-best-practices"></a>
+ Make your function as efficient and small as possible to avoid loading unnecessary files.
+ Strive to have static layers higher up in your Docker file list, and place layers that change more often lower down. This improves caching, which improves performance.
+ The image owner is responsible for updating and patching the image. Add that update cadence to your operational processes. For more information, see the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/best-practices.html#function-code).

## Epics
<a name="deploy-lambda-functions-with-container-images-epics"></a>

### Create a project in CodeBuild
<a name="create-a-project-in-codebuild"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a Git repository. | Create a Git repository that will contain the application source code, the Dockerfile, and the `buildspec.yaml` file.  | Developer |
| Create a CodeBuild project. | To use a CodeBuild project to create the custom Lambda image, do the following: 1. Sign in to the AWS Management Console, and open the CodeBuild console at https://console.aws.amazon.com/codesuite/codebuild/. <br />2. Create a new project. For source, choose the Git repository that you created. For information about different kinds of Git repository integration, see the [Working with connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html) documentation.<br />3. Confirm that privileged mode is enabled. To build Docker images, this is necessary. Otherwise, the image will not build successfully.<br />4. Provide values for the project name and description.  | Developer |
| Edit the Dockerfile. | The Dockerfile should be located in the top-level directory where you're developing the application. The Python code should be in the `src` folder.<br />When you create the image, use the [official Lambda supported images](https://gallery.ecr.aws/lambda?page=1). Otherwise, a bootstrap error will occur, making the packing process more difficult.<br />For details, see the [Additional information](#deploy-lambda-functions-with-container-images-additional) section. | Developer |
| Create a repository in Amazon ECR. | Create a container repository in Amazon ECR. In the following example command, the name of the repository created is `cf-demo`:<pre>aws ecr create-repository --cf-demo </pre><br />The repository will be referenced in the `buildspec.yaml` file. | AWS administrator, Developer |
| Push the image to Amazon ECR. | You can use CodeBuild to perform the image-build process. CodeBuild needs permission to interact with Amazon ECR and to work with S3. As part of the process, the Docker image is built and pushed to the Amazon ECR registry. For details on the template and the code, see the [Additional information](#deploy-lambda-functions-with-container-images-additional) section. | Developer |
| Verify that the image is in the repository. | To verify that the image is in the repository, on the Amazon ECR console, choose **Repositories**. The image should be listed, with tags and with the results of a vulnerability scan report if that feature was turned on in the Amazon ECR settings.  For more information, see the [AWS documentation](https://docs.aws.amazon.com/cli/latest/reference/ecr/put-registry-scanning-configuration.html). | Developer |

### Create the Lambda function to run the image
<a name="create-the-lambda-function-to-run-the-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the Lambda function. | On the Lambda console, choose **Create function**, and then choose **Container image**. Enter the function name and the URI for the image that is in the Amazon ECR repository, and then choose **Create function**. For more information, see the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/API_CreateFunction.html). | App developer |
| Test the Lambda function. | To invoke and test the function, choose **Test**. For more information, see the [AWS Lambda documentation](https://docs.aws.amazon.com/lambda/latest/dg/testing-functions.html). | App developer |

## Troubleshooting
<a name="deploy-lambda-functions-with-container-images-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Build is not succeeding. | 1. Check if the privileged mode is turned on for the CodeBuild project.<br />2. Ensure that the Docker related commands have the necessary permissions. Trying adding `sudo` to the commands.<br />3. Verify that the IAM role associated with CodeBuild has a policy with appropriate actions to interact with Amazon ECR, Amazon S3, and CloudWatch logs. |

## Related resources
<a name="deploy-lambda-functions-with-container-images-resources"></a>
+ [Base images for Lambda](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-images.html)
+ [Docker sample for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-docker.html)
+ [Pass temporary credentials](https://aws.amazon.com/premiumsupport/knowledge-center/codebuild-temporary-credentials-docker/)

## Additional information
<a name="deploy-lambda-functions-with-container-images-additional"></a>

**Edit the Dockerfile**

The following code shows the commands that you edit in the Dockerfile:

```
FROM public.ecr.aws/lambda/python:3.xx

# Copy function code
COPY app.py ${LAMBDA_TASK_ROOT}
COPY requirements.txt  ${LAMBDA_TASK_ROOT}

# install dependencies
RUN pip3 install --user -r requirements.txt

# Set the CMD to your handler (could also be done as a parameter override outside of the Dockerfile)
CMD [ "app.lambda_handler" ]
```

In the `FROM` command, use appropriate value for the Python version that is supported by Lambda (for example, `3.12`). This will be the base image that is available in the public Amazon ECR image repository.

The `COPY app.py ${LAMBDA_TASK_ROOT}` command copies the code to the task root directory, which the Lambda function will use. This command uses the environment variable so we don’t have to worry about the actual path. The function to be run is passed as an argument to the `CMD [ "app.lambda_handler" ]` command.

The `COPY requirements.txt` command captures the dependencies necessary for the code.

The `RUN pip install --user -r requirements.txt` command installs the dependencies to the local user directory.

To build your image, run the following command.

```
docker build -t <image name> .
```

**Add the image in Amazon ECR**

In the following code, replace `aws_account_id` with the account number, and replace `us-east-1` if you are using a different Region. The `buildspec` file uses the CodeBuild build number to uniquely identify image versions as a tag value. You can change this to fit your requirements.

*The buildspec custom code*

```
phases:
  install:
    runtime-versions:
       python: 3.xx
  pre_build:
    commands:
      - python3 --version
      - pip3 install --upgrade pip
      - pip3 install --upgrade awscli
      - sudo docker info
  build:
    commands:
      - echo Build started on `date`
      - echo Building the Docker image...
      - ls
      - cd app
      - docker build -t cf-demo:$CODEBUILD_BUILD_NUMBER .
      - docker container ls
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker image...
      - aws ecr get-login-password --region us-east-1 | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.us-east-1.amazonaws.com
      - docker tag cf-demo:$CODEBUILD_BUILD_NUMBER aws_account_id.dkr.ecr.us-east-1.amazonaws.com/cf-demo:$CODEBUILD_BUILD_NUMBER
      - docker push aws_account_id.dkr.ecr.us-east-1.amazonaws.com/cf-demo:$CODEBUILD_BUILD_NUMBER
```

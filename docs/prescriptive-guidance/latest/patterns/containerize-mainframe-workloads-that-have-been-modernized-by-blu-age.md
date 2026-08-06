---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/containerize-mainframe-workloads-that-have-been-modernized-by-blu-age.html
---

# Containerize mainframe workloads that have been modernized by Blu Age
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age"></a>

*Richard Milner-Watts, Amazon Web Services*

## Summary
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-summary"></a>

This pattern provides a sample container environment for running mainframe workloads that have been modernized by using the [Blu Age](https://www.bluage.com/) tool. Blu Age converts legacy mainframe workloads into modern Java code. This pattern provides a wrapper around the Java application so you can run it by using container orchestration services such as [Amazon Elastic Container Service (Amazon ECS)](https://aws.amazon.com/ecs/) or [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/).

For more information about modernizing your workloads by using Blu Age and AWS services, see these AWS Prescriptive Guidance publications:
+ [Running modernized Blu Age mainframe workloads on serverless AWS infrastructure](https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/)
+ [Deploy an environment for containerized Blu Age applications by using Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-environment-for-containerized-blu-age-applications-by-using-terraform.html)

For assistance with using Blu Age to modernize your mainframe workloads, contact the Blu Age team by choosing **Contact our experts** on the [Blu Age website](https://www.bluage.com/). For assistance with migrating your modernized workloads to AWS, integrating them with AWS services, and moving them into production, contact your AWS account manager or fill out the [AWS Professional Services form](https://pages.awscloud.com/AWS-Professional-Services.html).

## Prerequisites and limitations
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-prereqs"></a>

**Prerequisites**
+ A modernized Java application that was created by Blu Age. For testing purposes, this pattern provides a sample Java application that you can use as a proof of concept.
+ A [Docker](https://aws.amazon.com/docker/) environment that you can use to build the container.

**Limitations**

Depending on the container orchestration platform that you use, the resources that can be made available to the container (such as CPU, RAM, and storage) might be limited. For example, if you’re using Amazon ECS with AWS Fargate, see the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) for limits and considerations.

## Architecture
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-architecture"></a>

**Source technology stack**
+ Blu Age
+ Java

**Target technology stack**
+ Docker

**Target architecture**

The following diagram shows the architecture of the Blu Age application within a Docker container.

![Blu Age application in Docker container](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/c1747094-357b-4222-b4eb-b1336d810f83/images/0554332d-eff5-49ca-9789-da39b5a10045.png)

1. The entry point for the container is the wrapper script. This bash script is responsible for preparing the runtime environment for the Blu Age application and processing outputs.

1. Environment variables within the container are used to configure variables in the wrapper script, such as the Amazon Simple Storage Service (Amazon S3) bucket names and database credentials. Environment variables are supplied by either AWS Secrets Manager or Parameter Store, a capability of AWS Systems Manager. If you’re using Amazon ECS as your container orchestration service, you can also hardcode the environment variables in the Amazon ECS task definition.

1. The wrapper script is responsible for pulling any input files from the S3 bucket into the container before you run the Blu Age application. The AWS Command Line Interface (AWS CLI) is installed within the container. This provides a mechanism for accessing objects that are stored in Amazon S3 through the gateway virtual private cloud (VPC) endpoint.

1. The Java Archive (JAR) file for the Blu Age application might need to communicate with other data sources, such as Amazon Aurora.

1. After completion, the wrapper script delivers the resulting output files into an S3 bucket for further processing (for example, by Amazon CloudWatch logging services). The pattern also supports delivering zipped log files to Amazon S3, if you’re using an alternative to standard CloudWatch logging.

## Tools
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-tools"></a>

**AWS services**
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a fast and scalable container management service that helps you run, stop, and manage containers on a cluster.

**Tools**
+ [Docker](https://aws.amazon.com/docker/) is a software platform for building, testing, and deploying applications. Docker packages software into standardized units called [containers](https://aws.amazon.com/containers/), which have everything the software needs to run, including libraries, system tools, code, and runtime. You can use Docker to deploy and scale applications into any environment.
+ [Bash](https://www.gnu.org/software/bash/manual/) is a command language interface (shell) for the GNU operating system.
+ [Java](https://www.java.com/) is the programming language and development environment used in this pattern.
+ [Blu Age](https://www.bluage.com/) is an AWS mainframe modernization tool that converts legacy mainframe workloads, including application code, dependencies, and infrastructure, into modern workloads for the cloud.

**Code repository**

The code for this pattern is available in the GitHub [Blu Age sample container repository](https://github.com/aws-samples/aws-blu-age-sample-container).

## Best practices
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-best-practices"></a>
+ Externalize the variables for altering your application’s behavior by using environment variables. These variables enable the container orchestration solution to alter the runtime environment without rebuilding the container. This pattern includes examples of environment variables that can be useful for Blu Age applications.
+ Validate any application dependencies before you run your Blu Age application. For example, verify that the database is available and credentials are valid. Write tests in the wrapper script to verify dependencies, and fail early if they are not met.
+ Use verbose logging within the wrapper script. Interacting directly with a running container can be challenging, depending on the orchestration platform and how long the job takes. Make sure that useful output is written to `STDOUT` to help diagnose any issues. For example, output might include the contents of the application’s working directory both before and after you run the application.

## Epics
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-epics"></a>

### Obtain a Blu Age application JAR file
<a name="obtain-a-blu-age-application-jar-file"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Option 1 - Work with Blu Age to obtain your application's JAR file. | The container in this pattern requires a Blu Age application. Alternatively, you can use the sample Java application that’s provided with this pattern for a prototype.<br />Work with the Blu Age team to obtain a JAR file for your application that can be baked into the container. If the JAR file isn’t available, see the next task to use the sample application instead. | Cloud architect |
| Option 2 - Build or use the supplied sample application JAR file. | This pattern provides a prebuilt sample JAR file. This file outputs the application’s environment variables to `STDOUT` before sleeping for 30 seconds and exiting.<br />This file is named `bluAgeSample.jar` and is located in the [docker folder](https://github.com/aws-samples/aws-blu-age-sample-container/tree/main/docker) of the GitHub repository.<br />If you want to alter the code and build your own version of the JAR file, use the source code located at [./java\_sample/src/sample\_java\_app.java](https://github.com/aws-samples/aws-blu-age-sample-container/tree/main/java_sample/src) in the GitHub repository. You can use the build script at [./java\_sample/build.sh](https://github.com/aws-samples/aws-blu-age-sample-container/tree/main/java_sample) to compile the Java source and build a new JAR fie. | App developer |

### Build the Blu Age container
<a name="build-the-blu-age-container"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the GitHub repository. | Clone the sample code repository by using the command:<pre>git clone https://github.com/aws-samples/aws-blu-age-sample-container</pre> | AWS DevOps |
| Use Docker to build the container. | Use Docker to build the container before you push it to a Docker registry such as Amazon ECR:1. From your chosen terminal, navigate to the `docker` folder within your local GitHub repository.<br />2. Use this command to build the container:<pre>docker build -t <tag> .</pre><br />where `<tag> `is the container name you want to use. | AWS DevOps |
| Test the Blu Age container. | (Optional) If necessary, test the container locally by using the command:<pre>docker run -it <tag> /bin/bash</pre> | AWS DevOps |
| Authenticate to your Docker repository. | If you plan to use Amazon  ECR, follow the instructions in the [Amazon ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html) to install and configure the AWS CLI and authenticate the Docker CLI to your default registry.<br />We recommend that you use the [get-login-password command](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/get-login-password.html) for authentication.  The [Amazon ECR console](https://console.aws.amazon.com/ecr/) provides a pre-populated version of this command if you use the **View push commands** button. For more information, see the [Amazon ECR documentation](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-console.html).<pre>aws ecr get-login-password --region <region> | docker login --username AWS --password-stdin <account>.dkr.ecr.<region>.amazonaws.com</pre><br />If you don’t plan to use Amazon ECR, follow the instructions provided for your container registry system. | AWS DevOps |
| Create a container repository. | Create a repository in Amazon ECR. For instructions, see the pattern [Deploy an environment for containerized Blu Age applications by using Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-environment-for-containerized-blu-age-applications-by-using-terraform.html).<br />If you’re using another container registry system, follow the instructions provided for that system. | AWS DevOps |
| Tag and push your container to the target repository. | If you're using Amazon ECR:1. Tag the local Docker image with the Amazon ECR registry and repository, so you can push it to your remote repository:<pre>docker tag <tag>:latest <account>.dkr.ecr.<region>.amazonaws.com/<repository>:<versionNumber></pre><br />2. Push the image to the remote repository:<pre>docker push <account>.dkr.ecr.<region>.amazonaws.com/<repository>:<versionNumber></pre><br />For more information, see [Pushing a Docker image](https://docs.aws.amazon.com/AmazonECR/latest/userguide/docker-push-ecr-image.html) in the *Amazon ECR User Guide*. | AWS DevOps |

## Related resources
<a name="containerize-mainframe-workloads-that-have-been-modernized-by-blu-age-resources"></a>

**AWS resources**
+ [AWS Blu Age sample container repository](https://github.com/aws-samples/aws-blu-age-sample-container)
+ [Running modernized Blu Age mainframe workloads on serverless AWS infrastructure](https://docs.aws.amazon.com/prescriptive-guidance/latest/run-bluage-modernized-mainframes/)
+ [Deploy an environment for containerized Blu Age applications by using Terraform](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-an-environment-for-containerized-blu-age-applications-by-using-terraform.html)
+ [Using Amazon ECR with the AWS CLI](https://docs.aws.amazon.com/AmazonECR/latest/userguide/getting-started-cli.html) (*Amazon ECR User Guide*)
+ [Private registry authentication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/registry_auth.html) (*Amazon ECR User Guide*)
+ [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html)
+ [Amazon EKS documentation](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

**Additional resources**
+ [Blu Age website](https://www.bluage.com/)
+ [Docker website](https://docker.com/)

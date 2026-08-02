---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html
---

# Deploy containerized applications on AWS IoT Greengrass V2 running as a Docker container
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container"></a>

*Salih Bakir, Giuseppe Di Bella, and Gustav Svalander, Amazon Web Services*

## Summary
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-summary"></a>

AWS IoT Greengrass Version 2, when deployed as a Docker container, doesn't natively support running Docker application containers. This pattern shows you how to create a custom container image based on the latest version of AWS IoT Greengrass V2 that enables Docker-in-Docker (DinD) functionality. With DinD, you can run containerized applications within the AWS IoT Greengrass V2 environment.

You can deploy this pattern as a stand-alone solution or integrate it with container orchestration platforms like Amazon ECS Anywhere. In either deployment model, you maintain full AWS IoT Greengrass V2 functionality including AWS IoT SiteWise Edge processing capabilities, while enabling scalable container-based deployments.

## Prerequisites and limitations
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ For general AWS IoT Greengrass Version 2 prerequisites, see [Prerequisites](https://docs.aws.amazon.com/greengrass/v2/developerguide/getting-started-prerequisites.html) in the AWS IoT Greengrass Version 2 documentation.
+ Docker Engine, installed and configured on Linux, macOS, or Windows.
+ Docker Compose (if you use the Docker Compose command line interface (CLI) to run Docker images).
+ A Linux operating system.
+ A hypervisor with a host server that supports virtualization.
+ System requirements:
  + 2 GB of RAM (minimum)
  + 5 GB of available disk space (minimum)
  + For AWS IoT SiteWise Edge, an x86\_64 quad-core CPU with 16 GB of RAM and 50 GB of available disk space. For more information about AWS IoT SiteWise data processing, see [Data processing pack requirements](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/configure-gateway-ggv2.html#w2aac17c19c13b7) in the AWS IoT SiteWise documentation.

**Product versions**
+ AWS IoT Greengrass Version 2 version 2.5.3 or later
+ Docker-in-Docker version 1.0.0 or later
+ Docker Compose version 1.22 or later
+ Docker Engine version 20.10.12 or later

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-architecture"></a>

**Target technology stack**
+ **Data sources** – IoT devices, sensors, or industrial equipment that generates data for processing
+ **AWS IoT Greengrass V2** – Running as a Docker container with D-in-D capabilities, deployed on edge infrastructures
+ **Containerized applications** – Custom applications running within the AWS IoT Greengrass V2 environment as nested Docker containers
+ **(Optional) Amazon ECS Anywhere** – Container orchestration that manages the AWS IoT Greengrass V2 container deployment
+ **Other AWS services** – AWS IoT Core, AWS IoT SiteWise, and other AWS services for data processing and management

**Target architecture **

The following diagram shows an example target deployment architecture that uses Amazon ECS Anywhere, which is a container management tool.

![Deployment architecture using Amazon ECS Anywhere.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2ecf5354-40e0-4fd9-9798-086719059784/images/5ed2652e-9604-4809-8962-b167e1991658.png)

The diagram shows the following workflow:

**1: Container image storage** – Amazon ECR stores the AWS IoT Greengrass container images and any custom application containers needed for edge processing.

**2 **and** 3: Container deployment** – Amazon ECS Anywhere deploys the AWS IoT Greengrass container image from Amazon ECR to the edge location, managing the container lifecycle and deployment process.

**4: Component deployment** – The deployed AWS IoT Greengrass core automatically deploys its relevant components based on its configuration. Components include AWS IoT SiteWise Edge and other necessary edge processing components within the containerized environment.

**5: Data ingestion** – After it’s fully configured, AWS IoT Greengrass begins ingesting telemetry and sensor data from various IoT data sources at the edge location.

**6: Data processing and cloud integration** – The containerized AWS IoT Greengrass core processes data locally using its deployed components (including AWS IoT SiteWise Edge for industrial data). Then, it sends processed data to AWS Cloud services for further analysis and storage.

## Tools
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-tools"></a>

**AWS services**
+ [Amazon ECS Anywhere](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/launch-type-external.html) helps you deploy, use, and manage Amazon ECS tasks and services on your own infrastructure.
+ [Amazon Elastic Compute Cloud (Amazon EC2)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) provides scalable computing capacity in the AWS Cloud. You can launch as many virtual servers as you need and quickly scale them up or down.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html) is an open source Internet of Things (IoT) edge runtime and cloud service that helps you build, deploy, and manage IoT applications on your devices.
+ [AWS IoT SiteWise](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/what-is-sitewise.html) helps you collect, model, analyze, and visualize data from industrial equipment at scale.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [Docker Compose](https://docs.docker.com/compose/) is a tool for defining and running multi-container applications.
+ [Docker Engine](https://docs.docker.com/engine/) is an open source containerization technology for building and containerizing applications.

**Code repository**

The code for this pattern is available in the GitHub [AWS IoT Greengrass v2 Docker-in-Docker](https://github.com/aws-samples/aws-iot-greengrass-docker-in-docker) repository.

## Epics
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-epics"></a>

### Build the AWS IoT Greengrass V2 Docker-in-Docker image
<a name="build-the-gg2-docker-in-docker-image"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone and navigate to the repository. | To clone the repository, use the following command: <br />`git clone https://github.com/aws-samples/aws-iot-greengrass-docker-in-docker.git`<br />To navigate to the `docker` directory, use the following command:<br />`cd aws-iot-greengrass-docker-in-docker/docker` | DevOps engineer, AWS DevOps |
| Build the Docker image. | To build the Docker image with the default (latest) version, run the following command:<br />`docker build -t x86_64/aws-iot-greengrass:latest .`<br />Or, to build the Docker image with a specific version, run the following command:<br />`docker build --build-arg GREENGRASS_RELEASE_VERSION=2.12.0 -t x86_64/aws-iot-greengrass:2.12.0 .`<br />To verify the build, run the following command:<br />`docker images \| grep aws-iot-greengrass`<br />  | AWS DevOps, DevOps engineer, App developer |
| (Optional) Push to Amazon ECR. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | App developer, AWS DevOps, DevOps engineer |

### Configure AWS credentials
<a name="configure-aws-credentials"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select authentication method. | Choose one of the following options:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | AWS administrator |
| Configure authentication method. | For the authentication method you selected, use the following configuration guidance:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | AWS administrator |

### Run with Docker Compose
<a name="run-with-docker-compose"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure `docker-compose.yml`. | Update the `docker-compose.yml` file with environment variables as follows:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | DevOps engineer |
| Start and verify container. | To start in the foreground, run the following command:<br />`docker-compose up --build`<br />Or, to start in the background, run the following command:<br />`docker-compose up --build -d`<br />To verify status, run the following command:<br />`docker-compose ps`<br />To monitor logs, run the following command:<br />`docker-compose logs -f` | DevOps engineer |

### Run with Docker CLI
<a name="run-with-docker-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run container with Docker CLI. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | DevOps engineer |
| Verify container. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | DevOps engineer |

### Manage containerized applications
<a name="manage-containerized-applications"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy applications. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | App developer |
| Access and test Docker-in-Docker. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | DevOps engineer |

### (Optional) Integrate with Amazon ECS Anywhere
<a name="optional-integrate-with-ecs-anywhere"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Amazon ECS cluster. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | AWS administrator |
| Deploy Amazon ECS task. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | AWS administrator |

### Stop and cleanup
<a name="stop-and-cleanup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop container. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) | DevOps engineer |

## Troubleshooting
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Container fails to start with permission errors. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)`--privileged` grants extended privileges to the container. |
| Provisioning fails with credential errors. | To verify credentials are configured correctly, use the following steps:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)<br />Make sure that IAM permissions include `iot:CreateThing`, `iot:CreatePolicy`, `iot:AttachPolicy`, `iam:CreateRole`, and `iam:AttachRolePolicy`. |
| Cannot connect to Docker daemon inside container. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) |
| Container runs out of disk space. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)Ensure minimum disk space: 5 GB for basic operations and 50 GB for AWS IoT SiteWise Edge |
| Build issues. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html) |
| Network connectivity issues. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)Verify that the firewall allows outbound HTTPS (443) and MQTT (8883) traffic. |
| Greengrass components fail to deploy. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)Check component-specific logs in the `/greengrass/v2/logs/` directory. |
| Container exits immediately after starting. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container.html)Verify all required environment variables are set correctly if `PROVISION=true`. Make sure that the `--init` flag is used when starting the container. |

## Related resources
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-resources"></a>

**AWS resources**
+ [Amazon Elastic Container Service](https://aws.amazon.com/ecs/)
+ [Configure edge data processing for AWS IoT SiteWise models and assets](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/edge-processing.html)
+ [What is AWS IoT Greengrass](https://docs.aws.amazon.com/greengrass/v2/developerguide/what-is-iot-greengrass.html)

**Other resources**
+ [Docker documentation](https://docs.docker.com/)

## Additional information
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-additional"></a>
+ For AWS IoT SiteWise Edge data processing, Docker must be available within the AWS IoT Greengrass environment.
+ To run a nested container, you must run the AWS IoT Greengrass container with administrator-level credentials.

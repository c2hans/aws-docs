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
| (Optional) Push to Amazon ECR. | 1. To create the repository, run the following command:<br />`aws ecr create-repository --repository-name aws-iot-greengrass-dind --region us-east-1`<br />2. To authenticate, run the following command:<br />`aws ecr get-login-password --region us-east-1 \| docker login --username AWS --password-stdin <ACCOUNT-ID>.dkr.ecr.us-east-1.amazonaws.com`<br />3. To tag and push, run the following commands:<br />`docker tag x86_64/aws-iot-greengrass:latest <ACCOUNT-ID>.dkr.ecr.us-east-1.amazonaws.com/aws-iot-greengrass-dind:latest`<br />`docker push <ACCOUNT_ID>.dkr.ecr.us-east-1.amazonaws.com/aws-iot-greengrass-dind:latest` | App developer, AWS DevOps, DevOps engineer |

### Configure AWS credentials
<a name="configure-aws-credentials"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Select authentication method. | Choose one of the following options:+ **Option 1 (Recommended)**: IAM roles – Use if running on Amazon EC2, Amazon ECS, or Amazon EKS with proper IAM roles. No additional configuration needed.<br />+ **Option 2**: Environment variables – For testing and development.<br />+ **Option 3**: Credentials file – Not recommended for production.<br />+ **Option 4**: Legacy `env.cfg` file. | AWS administrator |
| Configure authentication method. | For the authentication method you selected, use the following configuration guidance:+ **Option 2 (Environment variables)** – Prepare `AWS_ACCESS_KEY_ID`, `AWS_SECRET_ACCESS_KEY`, and optionally `AWS_SESSION_TOKEN`.<br />+ **Option 3 (Credentials file)** – Create credentials directory and file:(a) Run the following command:<br />`mkdir -p ~/greengrass-v2-credentials`(b) Create the following file at `~/greengrass-v2-credentials/credentials`:<br />`[default]`<br />`aws_access_key_id=YourAccessKey`<br />`aws_secret_access_key=YourSecretKey`(c) Secure the file as follows:<br />`chmod 600 ~/greengrass-v2-credentials/credentials`<br />+ **Option 4 (**`env.cfg`**)** – Create the `env.cfg` file in the `docker` directory as follows:<br />`GGC_ROOT_PATH=/greengrass/v2`<br />`AWS_REGION=us-east-1`<br />`PROVISION=true`<br />`THING_NAME=MyGreengrassCore`<br />`THING_GROUP_NAME=MyGreengrassCoreGroup`<br />`TES_ROLE_NAME=GreengrassV2TokenExchangeRole`<br />`TES_ROLE_ALIAS_NAME=GreengrassCoreTokenExchangeRoleAlias`<br />`COMPONENT_DEFAULT_USER=ggc_user:ggc_group` | AWS administrator |

### Run with Docker Compose
<a name="run-with-docker-compose"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure `docker-compose.yml`. | Update the `docker-compose.yml` file with environment variables as follows:+ Key variables: `PROVISION,` `AWS_REGION`, `THING_NAME`, `THING_GROUP_NAME`, `TES_ROLE_NAME`, `TES_ROLE_ALIAS_NAME`<br />+ For credentials through environment variables, uncomment the following:<br />`environment:`<br />` - AWS_ACCESS_KEY_ID=YourKey`<br />` - AWS_SECRET_ACCESS_KEY=YourSecret`+ For credentials file, uncomment the following:<br />`volumes:`<br />` - ~/greengrass-v2-credentials:/root/.aws/:ro`+ For log persistence, add the following:<br />`volumes:`<br />` - ./logs:/greengrass/v2/logs` | DevOps engineer |
| Start and verify container. | To start in the foreground, run the following command:<br />`docker-compose up --build`<br />Or, to start in the background, run the following command:<br />`docker-compose up --build -d`<br />To verify status, run the following command:<br />`docker-compose ps`<br />To monitor logs, run the following command:<br />`docker-compose logs -f` | DevOps engineer |

### Run with Docker CLI
<a name="run-with-docker-cli"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Run container with Docker CLI. | + To initiate a basic run without provisioning, run the following command:<br />`docker run --init --privileged -it --name aws-iot-greengrass x86_64/aws-iot-greengrass:latest`+ To initiate a run with environment variables, run the following command:<br />`docker run --init --privileged -it --name aws-iot-greengrass -e PROVISION=true -e AWS_REGION=us-east-1 -e AWS_ACCESS_KEY_ID=YourKey -e AWS_SECRET_ACCESS_KEY=YourSecret -e THING_NAME=MyGreengrassCore -e THING_GROUP_NAME=MyGreengrassCoreGroup -p 8883:8883 x86_64/aws-iot-greengrass:latest`+ To initiate a run with a credentials file, run the following command:<br />`docker run --init --privileged -it --name aws-iot-greengrass -v ~/greengrass-v2-credentials:/root/.aws:ro -e PROVISION=true -e AWS_REGION=us-east-1 -e THING_NAME=MyGreengrassCore -p 8883:8883 x86_64/aws-iot-greengrass:latest`+ To initiate a run with an `env.cfg` file, run the following command:<br />`docker run --init --privileged -it --name aws-iot-greengrass -v ~/greengrass-v2-credentials:/root/.aws:ro --env-file env.cfg -p 8883:8883 x86_64/aws-iot-greengrass:latest`+ To initiate a run with persistent logs, run the following command:<br />`docker run --init --privileged -it --name aws-iot-greengrass -v \$(pwd)/logs:/greengrass/v2/logs x86_64/aws-iot-greengrass:latest` | DevOps engineer |
| Verify container. | + To check the container’s status, run the following command:<br />`docker ps \| grep aws-iot-greengrass`+ To monitor logs, run the following command:<br />`docker logs -f aws-iot-greengrass` | DevOps engineer |

### Manage containerized applications
<a name="manage-containerized-applications"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy applications. | + To deploy the application container, run the following command:<br />`docker run -d --name my-app nginx:alpine`+ To verify deployment, run the following command:<br />`docker ps`+ To access logs, run the following command:<br />`cd /greengrass/v2/logs && cat greengrass.log` | App developer |
| Access and test Docker-in-Docker. | 1. To open a shell in the container, run the following command:<br />`docker exec -it aws-iot-greengrass sh`<br />2. To verify Docker, run the following commands:<br />`docker --version`<br />`docker ps`<br />3. To test Docker-in-Docker, run the following command:<br />`docker run --rm hello-world` | DevOps engineer |

### (Optional) Integrate with Amazon ECS Anywhere
<a name="optional-integrate-with-ecs-anywhere"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up Amazon ECS cluster. | + To create an Amazon ECS cluster, run the following command:<br />`aws ecs create-cluster --cluster-name greengrass-cluster --region us-east-1`+ To create SSM activation, run the following command:<br />`aws ssm create-activation --default-instance-name greengrass-edge --iam-role GreengrassECSAnywhereRole --registration-limit 10 --region us-east-1`+ To install SSM Agent on an edge device, run the following command:<br />`curl -o install.sh https://s3.amazonaws.com/aws-ssm-downloads/latest/linux_amd64/install.sh`<br />`chmod +x install.sh`<br />`./install.sh activation-code activation-id us-east-1` | AWS administrator |
| Deploy Amazon ECS task. | + Create `greengrass-task-definition.json` with task configuration including `containerDefinitions` with `privileged:true`, environment variables, and volume mounts for `/var/lib/docker` and `/greengrass/v2.Register` task. Run the following command:<br />`aws ecs register-task-definition --cli-input-json file://greengrass-task-definition.json`+ To create the service, run the following command:<br />`aws ecs create-service --cluster greengrass-cluster --service-name greengrass-service --task-definition greengrass-dind --desired-count 1 --launch-type EXTERNAL --region us-east-1`+ To verify deployment, run the following command:<br />`aws ecs describe-services --cluster greengrass-cluster --services greengrass-service --region us-east-1` | AWS administrator |

### Stop and cleanup
<a name="stop-and-cleanup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Stop container. | + To stop the container by using Docker Compose, run the following commands:<br />`docker-compose stop`<br />`docker-compose down`<br />`docker-compose down -v`+ To stop the container (removes volumes) by using Docker CLI, run the following commands:<br />`docker stop aws-iot-greengrass`<br />`docker rm aws-iot-greengrass`+ To stop the container by using force remove, run the following command:<br />`docker rm -f aws-iot-greengrass` | DevOps engineer |

## Troubleshooting
<a name="deploy-containerized-applications-on-aws-iot-greengrass-version-2-running-as-a-docker-container-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Container fails to start with permission errors. | 1. To make sure that the container runs with the `--privileged` flag required for Docker-in-Docker, run the following command:<br />`docker run --init --privileged -it --name aws-iot-greengrass x86_64/aws-iot-greengrass:latest`<br />2. In the `docker-compose.yml` file, set the following:<br />`privileged: true``--privileged` grants extended privileges to the container. |
| Provisioning fails with credential errors. | To verify credentials are configured correctly, use the following steps:1. Check IAM role:<br />`aws sts get-caller-identity`<br />2. Verify environment variables:<br />`docker exec -it aws-iot-greengrass sh -c 'echo \$AWS_ACCESS_KEY_ID'`<br />3. Check credentials file:<br />`docker exec -it aws-iot-greengrass sh -c 'cat /root/.aws/credentials'`<br />Make sure that IAM permissions include `iot:CreateThing`, `iot:CreatePolicy`, `iot:AttachPolicy`, `iam:CreateRole`, and `iam:AttachRolePolicy`. |
| Cannot connect to Docker daemon inside container. | 1. Check the Docker daemon status:<br />`docker exec -it aws-iot-greengrass sh -c 'ps aux \| grep dockerd'`<br />2. Verify that the Docker socket exists:<br />`docker exec -it aws-iot-greengrass sh -c 'ls -la /var/run/docker.sock'`<br />3. Manually start if needed:<br />`docker exec -it aws-iot-greengrass sh -c 'dockerd > /var/log/docker.log 2>&1 &'` |
| Container runs out of disk space. | 1. Check disk space:<br />`df -h`<br />2. Clean Docker resources:<br />`docker system prune -a --volumes`<br />3. Remove old Greengrass artifacts:<br />`docker exec -it aws-iot-greengrass sh -c 'rm -rf /greengrass/v2/work/*`'Ensure minimum disk space: 5 GB for basic operations and 50 GB for AWS IoT SiteWise Edge |
| Build issues. | 1. Make sure that you’re in the `docker` directory:<br />`cd docker && pwd`<br />2. Verify that `Dockerfile` exists:<br />`ls -la Dockerfile`<br />3. Check that Docker is installed and running:<br />`docker --version && docker ps` |
| Network connectivity issues. | 1. Test DNS resolution:<br />`docker exec -it aws-iot-greengrass sh -c 'nslookup google.com'`<br />2. Test AWS connectivity:<br />`docker exec -it aws-iot-greengrass sh -c 'curl https://iot.us-east-1.amazonaws.com'`Verify that the firewall allows outbound HTTPS (443) and MQTT (8883) traffic. |
| Greengrass components fail to deploy. | 1. Check Greengrass logs:<br />`docker exec -it aws-iot-greengrass sh -c 'cat /greengrass/v2/logs/greengrass.log'`<br />2. Verify TES role configuration:<br />`aws iot describe-role-alias --role-alias TES_ROLE_ALIAS_NAME`Check component-specific logs in the `/greengrass/v2/logs/` directory. |
| Container exits immediately after starting. | 1. Check container logs for errors:<br />`docker logs aws-iot-greengrass`<br />2. Run with interactive shell for debugging:<br />`docker run --init --privileged -it --entrypoint sh x86_64/aws-iot-greengrass:latest`Verify all required environment variables are set correctly if `PROVISION=true`. Make sure that the `--init` flag is used when starting the container. |

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

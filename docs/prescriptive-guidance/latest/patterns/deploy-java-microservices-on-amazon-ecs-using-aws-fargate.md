---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-java-microservices-on-amazon-ecs-using-aws-fargate.html
---

# Deploy Java microservices on Amazon ECS using AWS Fargate
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate"></a>

*Vijay Thompson and Sandeep Bondugula, Amazon Web Services*

## Summary
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate-summary"></a>

This pattern provides guidance for deploying containerized Java microservices on Amazon Elastic Container Service (Amazon ECS) by using AWS Fargate. The pattern doesn't use Amazon Elastic Container Registry (Amazon ECR) for container management; instead, Docker images are pulled in from a Docker hub.

## Prerequisites and limitations
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate-prereqs"></a>

**Prerequisites**
+ An existing Java microservices application on a Docker hub
+ A public Docker repository
+ An active AWS account
+ Familiarity with AWS services, including Amazon ECS and Fargate
+ Docker, Java, and Spring Boot framework
+ Amazon Relational Database Service (Amazon RDS) up and running (optional)
+ A virtual private cloud (VPC) if the application requires Amazon RDS (optional)

## Architecture
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate-architecture"></a>

**Source technology stack**
+ Java microservices (for example, implemented in Spring Boot) and deployed on Docker

**Source architecture**

![Source architecture for Java microservices deployed on Docker](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/65185957-2b8b-43a6-964c-95ce0a45ba17/images/0a946ca8-fe37-4ede-85cb-a80a1c36105d.png)

**Target technology stack**
+ An Amazon ECS cluster that hosts each microservice by using Fargate
+ A VPC network to host the Amazon ECS cluster and associated security groups
+ A cluster/task definition for each microservice that spins up containers by using Fargate

**Target architecture**

![Target architecture on Java microservices on Amazon ECS](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/65185957-2b8b-43a6-964c-95ce0a45ba17/images/b21349ea-21fc-4688-b76a-1bde479858aa.png)

## Tools
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate-tools"></a>

**Tools**
+ [Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) eliminates the need to install and operate your own container orchestration software, manage and scale a cluster of virtual machines, or schedule containers on those virtual machines.
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) helps you run containers without needing to manage servers or Amazon Elastic Compute Cloud (Amazon EC2) instances. It’s used in conjunction with Amazon Elastic Container Service (Amazon ECS).
+ [Docker](https://www.docker.com/) is a software platform that allows you to build, test, and deploy applications quickly. Docker packages software into standardized units called *containers *that have everything the software needs to run, including libraries, system tools, code, and runtime.

**Docker code**

The following Dockerfile specifies the Java Development Kit (JDK) version that is used, where the Java archive (JAR) file exists, the port number that is exposed, and the entry point for the application.

```
FROM openjdk:11
ADD target/Spring-docker.jar Spring-docker.jar
EXPOSE 8080
ENTRYPOINT ["java","-jar","Spring-docker.jar"]
```

## Epics
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate-epics"></a>

### Create new task definitions
<a name="create-new-task-definitions"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a task definition. | Running a Docker container in Amazon ECS requires a task definition. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/](https://console.aws.amazon.com/ecs/), choose **Task definitions**, and then create a new task definition. For more information, see the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html). | AWS systems administrator, App developer |
| Choose launch type. | Choose **Fargate** as the launch type. | AWS systems administrator, App developer |
| Configure the task. | Define a task name and configure the application with the appropriate amount of task memory and CPU. | AWS systems administrator, App developer |
| Define the container. | Specify the container name. For the image, enter the Docker site name, the repository name, and the tag name of the Docker image (`docker.io/sample-repo/sample-application:sample-tag-name`). Set memory limits for the application, and set port mappings (`8080, 80`)  for the allowed ports. | AWS systems administrator, App developer |
| Create the task. | When the task and container configurations are in place, create the task. For detailed instructions, see the links in the *Related resources* section. | AWS systems administrator, App developer |

### Configure the cluster
<a name="configure-the-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create and configure a cluster. | Choose **Networking only** as the cluster type, configure the name, and then create the cluster or use an existing cluster if available. For more information, see the [Amazon ECS documentation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html). | AWS systems administrator, App developer |

### Configure Task
<a name="configure-task"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a task. | Inside the cluster, choose **Run new task**. | AWS systems administrator, App developer |
| Choose launch type. | Choose **Fargate **as the launch type. | AWS systems administrator, App developer |
| Choose task definition, revision, and platform version. | Choose the task that you want to run, the revision of the task definition, and the platform version. | AWS systems administrator, App developer |
| Select the cluster. | Choose the cluster where you want to run the task from. | AWS systems administrator, App developer |
| Specify the number of tasks. | Configure the number of tasks that should run. If you're launching with two or more tasks, a load balancer is required to distribute the traffic among the tasks. | AWS systems administrator, App developer |
| Specify the task group. | (Optional) Specify a task group name to identify a set of related tasks as a task group. | AWS systems administrator, App developer |
| Configure the cluster VPC, subnets, and security groups. | Configure the cluster VPC and the subnets on which you want to deploy the application. Create or update security groups  (HTTP, HTTPS, and port 8080) to provide access to inbound and outbound connections. | AWS systems administrator, App developer |
| Configure public IP settings. | Enable or disable the public IP, depending on whether you want to use a public IP address for Fargate tasks. The default, recommended option is **Enabled**. | AWS systems administrator, App developer |
| Review settings and create the task | Review your settings, and then choose **Run Task**. | AWS systems administrator, App developer |

### Cut over
<a name="cut-over"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy the application URL. | When the task status has been updated to *Running*, select the task. In the Networking section, copy the public IP. | AWS systems administrator, App developer |
| Test your application. | In your browser, enter the public IP to test the application. | AWS systems administrator, App developer |

## Related resources
<a name="deploy-java-microservices-on-amazon-ecs-using-aws-fargate-resources"></a>
+ [Docker Basics for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/docker-basics.html) (Amazon ECS documentation)
+ [Amazon ECS on AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) (Amazon ECS documentation)
+ [Creating a Task Definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html) (Amazon ECS documentation)
+ [Creating a Cluster](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create_cluster.html) (Amazon ECS documentation)
+ [Configuring Basic Service Parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/basic-service-params.html) (Amazon ECS documentation)
+ [Configuring a Network](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-configure-network.html) (Amazon ECS documentation)
+ [Deploying Java Microservices on Amazon ECS](https://aws.amazon.com/blogs/compute/deploying-java-microservices-on-amazon-ec2-container-service/) (blog post)

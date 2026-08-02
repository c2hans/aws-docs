---
source_url: https://docs.aws.amazon.com/solutions/devops-on-amazon-redshift/index.html
---

# Guidance for DevOps on Amazon Redshift

## Overview

**Important:** This Guidance requires the use of [AWS CodeCommit](/codecommit/latest/userguide/welcome.html) , which is no longer available to new customers. Existing customers of AWS CodeCommit can continue using and deploying this Guidance as normal. This Guidance demonstrates best practices for running development and operations (DevOps) on Amazon Redshift using both open source software and AWS services. DevOps is a set of practices that combine software development and IT operations to provide continuous integration and continuous delivery (CI/CD). It can help customers establish an agile software development process, shorten the development lifecycle, and deliver high-quality software.

## How it works

### AWS Services

This architecture displays best practices for running development and operations (DevOps) on Amazon Redshift.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/devops-on-amazon-redshift.pdf)Step 1Add or modify Data Definition Language or Data Manipulation Language (DDL/DML) scripts in the configuration files. Commit changes into AWS CodeCommit.Step 2CodeCommit invokes a code build using configuration specified in the buildspec.yml file. The build is based on pre_build, build, and post_build commands.Step 3AWS CodeBuild builds the container image and pushes it to AWS CodeDeploy.Step 4CodeDeploy pushes the container image to the Amazon Elastic Container Registry (Amazon ECR) repository.Step 5Amazon Elastic Kubernetes Service (Amazon EKS) cluster extracts the latest image from Amazon ECR and deploys it as a new cluster. A task is defined to run application code like a service.Step 6Amazon EKS cluster picks up the container image, reads configuration in the Amazon Simple Storage Service (Amazon S3) bucket to determine the invoking step, connects with the Amazon Redshift cluster, and invokes the DDL/DML code.Step 7Code is deployed in the Amazon Redshift cluster environment, the task completes, and the deployment service waits for another change to the DDL/DML script.### Open source software

This architecture displays DevOps best practices to build and run open source software on Amazon Redshift.

[Download the architecture diagram](https://d1.awsstatic.com/solutions/guidance/architecture-diagrams/devops-on-amazon-redshift.pdf#page=2)Step 1Add or modify DDL/DML scripts in configuration files. Commit changes into GitHub for deployment.Step 2GitHub uses a webhook to start the build process on Jenkins. A declarative pipeline job in Jenkins is kicked to start the build process.Step 3Jenkins builds a Docker container image using the configuration specified in the Docker file. Once an image is built, the Jenkins job pushes the image to Docker Hub.Step 4Jenkins job pulls the latest Docker Hub image, and creates a new container, invoking the DDL/DML scripts specified in the configuration file.Step 5A Docker container with the latest image is invoked to deploy the changes in multiple environments. Logs and test results in the Docker container are saved to the mapped Amazon Elastic Compute Cloud (Amazon EC2) directory.Step 6The code performed in the Docker container checks each performed step from config files, and saves it in an Amazon S3 bucket. In the event of container restart, the last saved checkpoint is used.## Deploy with confidence

Everything you need to launch this Guidance in your account is right here.

- **Let's make it happen**: The sample code is a starting point. It is industry validated, prescriptive but not definitive, and a peek under the hood to help you begin.

[Open sample code on GitHub](https://github.com/aws-solutions-library-samples/guidance-for-devops-on-amazon-redshift)

## Well-Architected Pillars

The architecture diagram above is an example of a Solution created with Well-Architected best practices in mind. To be fully Well-Architected, you should follow as many Well-Architected best practices as possible.

### Operational Excellence

This Guidance ensures you are well-architected by helping you evaluate your workloads against other best practices. One way this is accomplished is by using configuration as code, which allows teams to manage config files from a centralized location. Another way to ensure continual improvement is through feedback loops, which are implemented within this Guidance through GitHub, where the feedback received is prioritized and implemented as different versions of this Guidance are released. [Read the Operational Excellence whitepaper](/wellarchitected/latest/operational-excellence-pillar/welcome.html)

### Security

For secure authentication and authorization, Amazon EC2 uses private keys for enhanced security. AWS Identity and Access Management (IAM) is used for AWS services with least privileged access granted, while non-root accounts are used to perform scripts and workloads in Amazon EC2 instances and containers. [Read the Security whitepaper](/wellarchitected/latest/security-pillar/welcome.html)

### Reliability

To ensure you have a reliable application-level architecture, this Guidance saves Jenkins container configurations in an Amazon EC2 directory. The external configuration makes Jenkins stateless, providing you with the ability to restart when needed. Compute used in this Guidance is also stateless, so in case of failures, the Guidance can be restarted without configuration changes. Logs and metrics are captured directly within the Amazon EC2 instance and Amazon CloudWatch sends notifications when thresholds are crossed or significant events occur. This Guidance also enables recovery from disaster events by performing the DDL and DML scripts that are saved configurations (these are YAML formatted templates that define an environment's version, tier, configuration option settings, and tags). When configuration or code changes are needed, this Guidance uses GitHub (an open source environment) and CodeCommit to deploy the changes. [Read the Reliability whitepaper](/wellarchitected/latest/reliability-pillar/welcome.html)

### Performance Efficiency

The services in this Guidance are built and meet the functional capabilities needed to deploy this Guidance's best practices. To experiment with this Guidance and optimize it based on your data, you can deploy this Guidance with an AWS CloudFormation template and experiment with: Creating different Amazon Redshift clusters and running SQL scripts, such as changing the INI files. Customizing the Docker build (inject any additional libraries and dependencies) by using Dockerfile, a text document that contains all the commands a user could call on the command line to assemble an image. Adding configuration for the Jenkins job build with a Jenkinsfile, a text file that contains the definition of a Jenkins Pipeline, and is checked into source control. Changing to build process details with buildspec.yml, a collection of build commands and related settings in YAML format. We recommend you deploy the Amazon EC2 instance in the same Region with the Amazon Redshift cluster to reduce connection latency while performing the SQL statement commands. [Read the Performance Efficiency whitepaper](/wellarchitected/latest/performance-efficiency-pillar/welcome.html)

### Cost Optimization

Except for Amazon EC2 instances, all services in this Guidance are serverless. If you use CloudFormation, it deploys to a virtual private cloud (VPC) that displays costs associated with the Guidance. Because this Guidance is deployed in a contained VPC, there are no data transfer charges. We do recommend you stop any instances when not in use to reduce costs. [Read the Cost Optimization whitepaper](/wellarchitected/latest/cost-optimization-pillar/welcome.html)

### Sustainability

Except for Amazon EC2, the serverless components in this Guidance help reduce your carbon footprint by scaling to continually match your workloads while ensuring that only the minimum resources are required. [Read the Sustainability whitepaper](/wellarchitected/latest/sustainability-pillar/sustainability-pillar.html)

[Read usage guidelines](/solutions/guidance-disclaimers/)

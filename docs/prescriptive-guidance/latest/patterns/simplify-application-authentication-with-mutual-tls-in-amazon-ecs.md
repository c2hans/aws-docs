---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/simplify-application-authentication-with-mutual-tls-in-amazon-ecs.html
---

# Simplify application authentication with mutual TLS in Amazon ECS by using Application Load Balancer
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs"></a>

*Olawale Olaleye and Shamanth Devagari, Amazon Web Services*

## Summary
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-summary"></a>

This pattern helps you to simplify your application authentication and offload security burdens with mutual TLS in Amazon Elastic Container Service (Amazon ECS) by using [Application Load Balancer (ALB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/mutual-authentication.html). With ALB, you can authenticate X.509 client certificates from AWS Private Certificate Authority. This powerful combination helps to achieve secure communication between your services, reducing the need for complex authentication mechanisms within your applications. In addition, the pattern uses Amazon Elastic Container Registry (Amazon ECR) to store container images.

The example in this pattern uses Docker images from a public gallery to create the sample workloads initially. Subsequently, new Docker images are built to be stored in Amazon ECR. For the source, consider a Git-based system such as GitHub, GitLab, or Bitbucket, or use Amazon Simple Storage Service Amazon S3 (Amazon S3). For building the Docker images, consider using AWS CodeBuild for the subsequent images.

## Prerequisites and limitations
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-prereqs"></a>

**Prerequisites**
+ An active AWS account with access to deploy AWS CloudFormation stacks. Make sure that you have AWS Identity and Access Management (IAM) [user or role permissions](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/control-access-with-iam.html) to deploy CloudFormation.
+ AWS Command Line Interface (AWS CLI) [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html). [Configure](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html) your AWS credentials on your local machine or in your environment by either using the AWS CLI or by setting the environment variables in the `~/.aws/credentials` file.
+ OpenSSL [installed](https://www.openssl.org/).
+ Docker [installed](https://www.docker.com/get-started/).
+ Familiarity with the AWS services described in [Tools](#simplify-application-authentication-with-mutual-tls-in-amazon-ecs-tools).
+ Knowledge of Docker and NGINX.

**Limitations**
+ Mutual TLS for Application Load Balancer only supports X.509v3 client certificates. X.509v1 client certificates are not supported.
+ The CloudFormation template that is provided in this pattern’s code repository doesn’t include provisioning a CodeBuild project as part of the stack.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

**Product versions**
+ Docker version 27.3.1 or later
+ AWS CLI version 2.14.5 or later

## Architecture
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-architecture"></a>

The following diagram shows the architecture components for this pattern.

![Workflow to authenticate with mutual TLS using Application Load Balancer.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a343fa4e-097f-416b-9c83-01a28eb57dc3/images/e1371297-b987-4487-9b13-8120933c921f.png)

 The diagram shows the following workflow:

1. Create a Git repository, and commit the application code to the repository.

1. Create a private certificate authority (CA) in AWS Private CA.

1. Create a CodeBuild project. The CodeBuildproject is triggered by commit changes and creates the Docker image and publishes the built image to Amazon ECR.

1. Copy the certificate chain and certificate body from the CA, and upload the certificate bundle to Amazon S3.

1. Create a trust store with the CA bundle that you uploaded to Amazon S3. Associate the trust store with the mutual TLS listeners on the Application Load Balancer (ALB).

1. Use the private CA to issue client certificates for the container workloads. Also create a private TLS certificate using AWS Private CA.

1. Import the private TLS certificate into AWS Certificate Manager (ACM), and use it with the ALB.

1. The container workload in `ServiceTwo` uses the issued client certificate to authenticate with the ALB when it communicates with the container workload in `ServiceOne`.

1. The container workload in `ServiceOne` uses the issued client certificate to authenticate with the ALB when it communicates with the container workload in `ServiceTwo`.

**Automation and scale**

This pattern can be fully automated by using CloudFormation, AWS Cloud Development Kit (AWS CDK) , or API operations from an SDK to provision the AWS resources.

You can use AWS CodePipeline to implement a continuous integration and continuous deployment (CI/CD) pipeline using CodeBuild to automate container image build process and deploying new releases to the Amazon ECS cluster services.

## Tools
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-tools"></a>

**AWS services **
+ [AWS Certificate Manager (ACM)](https://docs.aws.amazon.com/acm/latest/userguide/acm-overview.html) helps you create, store, and renew public and private SSL/TLS X.509 certificates and keys that protect your AWS websites and applications.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Container Service (Amazon ECS)](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/Welcome.html) is a highly scalable, fast container management service for running, stopping, and managing containers on a cluster. You can run your tasks and services on a serverless infrastructure that is managed by AWS Fargate. Alternatively, for more control over your infrastructure, you can run your tasks and services on a cluster of Amazon Elastic Compute Cloud (Amazon EC2) instances that you manage.
+ [Amazon ECS Exec](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-exec.html) allows you to directly interact with containers without needing to first interact with the host container operating system, open inbound ports, or manage SSH keys. You can use ECS Exec to run commands in, or get a shell to, a container running on an Amazon EC2 instance or on AWS Fargate.
+ [Elastic Load Balancing (ELB)](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) distributes incoming application or network traffic across multiple targets. For example, you can distribute traffic across Amazon EC2 instances, containers, and IP addresses, in one or more Availability Zones. ELB monitors the health of its registered targets, and routes traffic only to the healthy targets. ELB scales your load balancer as your incoming traffic changes over time. It can automatically scale to the majority of workloads.
+ [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/userguide/what-is-fargate.html) helps you run containers without needing to manage servers or Amazon EC2 instances. Fargate is compatible with both Amazon ECS and Amazon Elastic Kubernetes Service (Amazon EKS). You can run your Amazon ECS tasks and services with the Fargate launch type or a Fargate capacity provider. To do so, package your application in containers, specify the CPU and memory requirements, define networking and IAM policies, and launch the application. Each Fargate task has its own isolation boundary and doesn’t share the underlying kernel, CPU resources, memory resources, or elastic network interface with another task.
+ [AWS Private Certificate Authority](https://docs.aws.amazon.com/privateca/latest/userguide/PcaWelcome.html) enables creation of private certificate authority (CA) hierarchies, including root and subordinate CAs, without the investment and maintenance costs of operating an on-premises CA.

**Other tools**** **
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [GitHub](https://docs.github.com/en/repositories/creating-and-managing-repositories/quickstart-for-repositories), [GitLab](https://docs.gitlab.com/ee/user/get_started/get_started_projects.html), and [Bitbucket](https://support.atlassian.com/bitbucket-cloud/docs/tutorial-learn-bitbucket-with-git/) are some of the commonly used Git-based source control system to keep track of source code changes.
+ [NGINX Open Source](https://nginx.org/en/docs/?_ga=2.187509224.1322712425.1699399865-405102969.1699399865) is an open source load balancer, content cache, and web server. This pattern uses it as a web server.
+ [OpenSSL](https://www.openssl.org/) is an open source library that provides services that are used by the OpenSSL implementations of TLS and CMS.

**Code repository**

The code for this pattern is available in the GitHub [mTLS-with-Application-Load-Balancer-in-Amazon-ECS](https://github.com/aws-samples/mTLS-with-Application-Load-Balancer-in-Amazon-ECS) repository.

## Best practices
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-best-practices"></a>
+ Use Amazon ECS Exec to run commands or get a shell to a container running on Fargate. You can also use ECS Exec to help collect diagnostic information for debugging.
+ Use security groups and network access control lists (ACLs) to control inbound and outbound traffic between the services. Fargate tasks receive an IP address from the configured subnet in your virtual private cloud (VPC).

## Epics
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-epics"></a>

### Create the repository
<a name="create-the-repository"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Download the source code. | To download this pattern’s source code, fork or clone the GitHub [mTLS-with-Application-Load-Balancer-in-Amazon-ECS](https://github.com/aws-samples/mTLS-with-Application-Load-Balancer-in-Amazon-ECS) repository. | DevOps engineer |
| Create a Git repository. | To create a Git repository to contain the Dockerfile and the `buildspec.yaml` files, use the following steps:1. Create a folder in your virtual environment. Name it with your project name.<br />2. Open a terminal on your local machine, and navigate to this folder.<br />3. To clone the [mTLS-with-Application-Load-Balancer-in-Amazon-ECS](https://github.com/aws-samples/mTLS-with-Application-Load-Balancer-in-Amazon-ECS) repository to your project directory, enter the following command:<br />`git clone https://github.com/aws-samples/mTLS-with-Application-Load-Balancer-in-Amazon-ECS.git` | DevOps engineer |

### Create CA and generate certificates
<a name="create-ca-and-generate-certificates"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a private CA in AWS Private CA. | To create a private certificate authority (CA), run the following commands in your terminal. Replace the values in the example variables with your own values. <pre>export AWS_DEFAULT_REGION="us-west-2"<br />export SERVICES_DOMAIN="www.example.com"<br /><br />export ROOT_CA_ARN=`aws acm-pca create-certificate-authority \<br />    --certificate-authority-type ROOT \<br />    --certificate-authority-configuration \<br />    "KeyAlgorithm=RSA_2048,<br />    SigningAlgorithm=SHA256WITHRSA,<br />    Subject={<br />        Country=US,<br />        State=WA,<br />        Locality=Seattle,<br />        Organization=Build on AWS,<br />        OrganizationalUnit=mTLS Amazon ECS and ALB Example,<br />        CommonName=${SERVICES_DOMAIN}}" \<br />        --query CertificateAuthorityArn --output text`</pre><br />For more details, see [Create a private CA in AWS Private CA](https://docs.aws.amazon.com/privateca/latest/userguide/create-CA.html) in the AWS documentation. | DevOps engineer, AWS DevOps |
| Create and install your private CA certificate. | To create and install a certificate for your private root CA, run the following commands in your terminal:1. Generate a certificate signing request (CSR).<pre>ROOT_CA_CSR=`aws acm-pca get-certificate-authority-csr \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --query Csr --output text`</pre><br />2. Issue the root certificate.<pre>AWS_CLI_VERSION=$(aws --version 2>&1 | cut -d/ -f2 | cut -d. -f1)<br />[[ ${AWS_CLI_VERSION} -gt 1 ]] && ROOT_CA_CSR="$(echo ${ROOT_CA_CSR} | base64)"<br /><br />ROOT_CA_CERT_ARN=`aws acm-pca issue-certificate \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --template-arn arn:aws:acm-pca:::template/RootCACertificate/V1 \<br />    --signing-algorithm SHA256WITHRSA \<br />    --validity Value=10,Type=YEARS \<br />    --csr "${ROOT_CA_CSR}" \<br />    --query CertificateArn --output text`</pre><br />3. Retrieve the root certificate.<pre>ROOT_CA_CERT=`aws acm-pca get-certificate \<br />    --certificate-arn ${ROOT_CA_CERT_ARN} \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --query Certificate --output text`<br /><br /># store for later use<br />aws acm-pca get-certificate \<br />    --certificate-arn ${ROOT_CA_CERT_ARN} \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --query Certificate --output text > ca-cert.pem</pre><br />4. Import the root CA certificate to install it on the CA.<pre>[[ ${AWS_CLI_VERSION} -gt 1 ]] && ROOT_CA_CERT="$(echo ${ROOT_CA_CERT} | base64)"<br /><br />aws acm-pca import-certificate-authority-certificate \<br />    --certificate-authority-arn $ROOT_CA_ARN \<br />    --certificate "${ROOT_CA_CERT}"</pre><br />For more details, see [Installing the CA certificate](https://docs.aws.amazon.com/privateca/latest/userguide/PCACertInstall.html) in the AWS documentation. | AWS DevOps, DevOps engineer |
| Request a managed certificate. | To request a private certificate in AWS Certificate Manager to use with your private ALB, use the following command:<pre>export TLS_CERTIFICATE_ARN=`aws acm request-certificate \<br />    --domain-name "*.${DOMAIN_DOMAIN}" \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --query CertificateArn --output text`</pre> | DevOps engineer, AWS DevOps |
| Use the private CA to issue a client certificate. | + To create a certificate signing request (CSR) for the two services, use the following AWS CLI command:`openssl req -out client_csr1.pem -new -newkey rsa:2048 -nodes -keyout client_private-key1.pem`<br />`openssl req -out client_csr2.pem -new -newkey rsa:2048 -nodes -keyout client_private-key2.pem`<br />This command returns the CSR and the private key for the two services. + To issue a certificate for the services, run the following commands to use the private CA that you created:<pre>SERVICE_ONE_CERT_ARN=`aws acm-pca issue-certificate \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --csr fileb://client_csr1.pem \<br />    --signing-algorithm "SHA256WITHRSA" \<br />    --validity Value=5,Type="YEARS" --query CertificateArn --output text` <br /><br />echo "SERVICE_ONE_CERT_ARN: ${SERVICE_ONE_CERT_ARN}"<br /><br />aws acm-pca get-certificate \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --certificate-arn ${SERVICE_ONE_CERT_ARN} \<br />     | jq -r '.Certificate' > client_cert1.cert<br /><br />SERVICE_TWO_CERT_ARN=`aws acm-pca issue-certificate \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --csr fileb://client_csr2.pem \<br />    --signing-algorithm "SHA256WITHRSA" \<br />    --validity Value=5,Type="YEARS" --query CertificateArn --output text` <br /><br />echo "SERVICE_TWO_CERT_ARN: ${SERVICE_TWO_CERT_ARN}"<br /><br />aws acm-pca get-certificate \<br />    --certificate-authority-arn ${ROOT_CA_ARN} \<br />    --certificate-arn ${SERVICE_TWO_CERT_ARN} \<br />     | jq -r '.Certificate' > client_cert2.cert</pre><br />For more information, see [Issue private end-entity certificates](https://docs.aws.amazon.com/privateca/latest/userguide/PcaIssueCert.html) in the AWS documentation. | DevOps engineer, AWS DevOps |

### Provision AWS services
<a name="provision-aws-services"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Provision AWS services with the CloudFormation template. | To provision the virtual private cloud (VPC), Amazon ECS cluster, Amazon ECS services, Application Load Balancer, and Amazon Elastic Container Registry (Amazon ECR), use the CloudFormation template. | DevOps engineer |
| Get variables. | Verify that you have an Amazon ECS cluster with two services running. To retrieve the resource details and store them as variables, use the following commands:<pre><br />export LoadBalancerDNS=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`LoadBalancerDNS`].OutputValue')<br /><br />export ECRRepositoryUri=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`ECRRepositoryUri`].OutputValue')<br /><br />export ECRRepositoryServiceOneUri=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`ECRRepositoryServiceOneUri`].OutputValue')<br /><br />export ECRRepositoryServiceTwoUri=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`ECRRepositoryServiceTwoUri`].OutputValue')<br /><br />export ClusterName=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`ClusterName`].OutputValue')<br /><br />export BucketName=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`BucketName`].OutputValue')<br /><br />export Service1ListenerArn=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`Service1ListenerArn`].OutputValue')<br /><br />export Service2ListenerArn=$(aws cloudformation describe-stacks --stack-name ecs-mtls \<br />--output text \<br />--query 'Stacks[0].Outputs[?OutputKey==`Service2ListenerArn`].OutputValue')</pre> | DevOps engineer |
| Create a CodeBuild project. | To use a CodeBuild project to create the Docker images for your Amazon ECS services, do the following:1. Sign in to the AWS Management Console, and open the CodeBuild console at [https://console.aws.amazon.com/codesuite/codebuild/](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html).<br />2. Create a new project. For **Source**, choose the Git repository that you created. For information about different kinds of Git repository integration, see [Working with connections](https://docs.aws.amazon.com/dtconsole/latest/userguide/connections.html) in the AWS documentation.<br />3. Confirm that **Privileged **mode is enabled. To build Docker images, this mode is necessary. Otherwise, the image will not build successfully.<br />4. Use the custom `buildspec.yaml` file shared for each service.<br />5. Provide values for the project name and description.<br />For more details, see [Create a build project in AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/create-project.html) in the AWS documentation. | AWS DevOps, DevOps engineer |
| Build the Docker images. | You can use CodeBuild to perform the image build process. CodeBuild needs permissions to interact with Amazon ECR and to work with Amazon S3.<br />As part of the process, the Docker image is built and pushed to the Amazon ECR registry. For details about the template and the code, see [Additional information](#simplify-application-authentication-with-mutual-tls-in-amazon-ecs-additional).<br />(Optional) To build locally for test purposes, use the following command:<pre># login to ECR<br />aws ecr get-login-password | docker login --username AWS --password-stdin $ECRRepositoryUri<br /><br /># build image for service one<br />cd /service1<br />aws s3 cp s3://$BucketName/serviceone/ service1/ --recursive<br />docker build -t $ECRRepositoryServiceOneUri .<br />docker push $ECRRepositoryServiceOneUri<br /><br /># build image for service two<br />cd ../service2<br />aws s3 cp s3://$BucketName/servicetwo/ service2/ --recursive<br />docker build -t $ECRRepositoryServiceTwoUri .<br />docker push $ECRRepositoryServiceTwoUri</pre> | DevOps engineer |

### Enable mutual TLS
<a name="enable-mutual-tls"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Upload the CA certificate to Amazon S3. | To upload the CA certificate to the Amazon S3 bucket, use the following example command:<br />`aws s3 cp ca-cert.pem s3://$BucketName/acm-trust-store/ ` | AWS DevOps, DevOps engineer |
| Create the trust store. | To create the trust store, use the following example command:<pre>TrustStoreArn=`aws elbv2 create-trust-store --name acm-pca-trust-certs \<br />    --ca-certificates-bundle-s3-bucket $BucketName \<br />    --ca-certificates-bundle-s3-key acm-trust-store/ca-cert.pem --query 'TrustStores[].TrustStoreArn' --output text`</pre> | AWS DevOps, DevOps engineer |
| Upload client certificates. | To upload client certificates to Amazon S3 for Docker images, use the following example command:<pre># for service one<br />aws s3 cp client_cert1.cert s3://$BucketName/serviceone/<br />aws s3 cp client_private-key1.pem s3://$BucketName/serviceone/<br /><br /># for service two<br />aws s3 cp client_cert2.cert s3://$BucketName/servicetwo/<br />aws s3 cp client_private-key2.pem s3://$BucketName/servicetwo/</pre> | AWS DevOps, DevOps engineer |
| Modify the listener. | To enable mutual TLS on the ALB, modify the HTTPS listeners by using the following commands:<pre>aws elbv2 modify-listener \<br />    --listener-arn $Service1ListenerArn \<br />    --certificates CertificateArn=$TLS_CERTIFICATE_ARN_TWO \<br />    --ssl-policy ELBSecurityPolicy-2016-08 \<br />    --protocol HTTPS \<br />    --port 8080 \<br />    --mutual-authentication Mode=verify,TrustStoreArn=$TrustStoreArn,IgnoreClientCertificateExpiry=false<br /><br />aws elbv2 modify-listener \<br />    --listener-arn $Service2ListenerArn \<br />    --certificates CertificateArn=$TLS_CERTIFICATE_ARN_TWO \<br />    --ssl-policy ELBSecurityPolicy-2016-08 \<br />    --protocol HTTPS \<br />    --port 8090 \<br />    --mutual-authentication Mode=verify,TrustStoreArn=$TrustStoreArn,IgnoreClientCertificateExpiry=false<br /></pre><br />For more information, see [Configuring mutual TLS on an Application Load Balancer](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/configuring-mtls-with-elb.html) in the AWS documentation. | AWS DevOps, DevOps engineer |

### Update the services
<a name="update-the-services"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Update the Amazon ECS task definition. | To update the Amazon ECS task definition, modify the `image` parameter in the new revision.<br />To get the values for the respective services, update the task definitions with the new Docker images Uri that you built in the previous steps: `echo $ECRRepositoryServiceOneUri` or `echo $ECRRepositoryServiceTwoUri`<pre><br />    "containerDefinitions": [<br />        {<br />            "name": "nginx",<br />            "image": "public.ecr.aws/nginx/nginx:latest",   # <----- change to new Uri<br />            "cpu": 0,</pre><br />For more information, see [Updating an Amazon ECS task definition](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-task-definition-console-v2.html) using the console in the AWS documentation.  | AWS DevOps, DevOps engineer |
| Update the Amazon ECS service. | Update the service with the latest task definition. This task definition is the blueprint for the newly built Docker images, and it contains the client certificate that’s required for the mutual TLS authentication. <br /> To update the service, use the following procedure:1. Open the Amazon ECS console at [https://console.aws.amazon.com/ecs/v2](https://console.aws.amazon.com/ecs/v2).<br />2. On the **Clusters** page, choose the cluster.<br />3. On the cluster details page, in the **Services** section, select the checkbox next to the service, and then choose **Update**.<br />4. To have your service start a new deployment, select **Force new deployment**.<br />5. For **Task definition**, choose the task definition family and the latest revision.<br />6. Choose **Update**.<br />Repeat the steps for the other service. | AWS administrator, AWS DevOps, DevOps engineer |

### Access the application
<a name="access-the-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Copy the application URL. | Use the Amazon ECS console to view the task. When the task status has been updated to **Running**, select the task. In the **Task **section, copy the task ID. | AWS administrator, AWS DevOps |
| Test your application. | To test your application, use ECS Exec to access the tasks.1. For service one, use the following command:<pre>container="nginx"<br /><br />ECS_EXEC_TASK_ARN="<TASK ARN>"<br />aws ecs execute-command --cluster $ClusterName \<br />    --task $ECS_EXEC_TASK_ARN \<br />    --container $container \<br />    --interactive \<br />    --command "/bin/bash"</pre><br />2. In the service one task’s container, use the following command to enter the internal load balancer `url `and the listener port that points to service two. Then specify the path to the client certificate to test the application:<pre>curl -kvs https://<internal-alb-url>:8090 --key /usr/local/share/ca-certificates/client.key --cert /usr/local/share/ca-certificates/client.crt</pre><br />3. In the service two task’s container, use the following command to enter the internal load balancer `url` and the listener port that points to service one. Then specify the path to the client certificate to test the application:<pre>curl -kvs https://<internal-alb-url>:8080 --key /usr/local/share/ca-certificates/client.key --cert /usr/local/share/ca-certificates/client.crt</pre>The `-k` flag in the curl commands (as part of `-kvs`) disables SSL certificate validation. You can remove this flag when using an SSL certificate that matches your domain name, enabling proper certificate validation. | AWS administrator, AWS DevOps |

## Related resources
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-resources"></a>

**Amazon ECS documentation**
+ [Creating an Amazon ECS task definition using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-task-definition.html)
+ [Creating a container image for use on Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html)
+ [Amazon ECS clusters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/clusters.html)
+ [Amazon ECS for AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-container-image.html#create-container-image-next-steps)
+ [Amazon ECS networking best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/networking-best-practices.html)
+ [Amazon ECS service definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service_definition_parameters.html)

**Other AWS resources**
+ [How do I use AWS private CA to configure mTLS on the Application Load Balancer?](https://repost.aws/knowledge-center/elb-alb-configure-private-ca-mtls) (AWS re:Post)

## Additional information
<a name="simplify-application-authentication-with-mutual-tls-in-amazon-ecs-additional"></a>

**Editing the Dockerfile**** **

The following code shows the commands that you edit in the Dockerfile for service 1:

```
FROM public.ecr.aws/nginx/nginx:latest
WORKDIR /usr/share/nginx/html
RUN echo "Returning response from Service 1: Ok" > /usr/share/nginx/html/index.html
ADD client_cert1.cert client_private-key1.pem /usr/local/share/ca-certificates/
RUN chmod -R 400 /usr/local/share/ca-certificates/
```

The following code shows the commands that you edit in the Dockerfile for service 2:

```
FROM public.ecr.aws/nginx/nginx:latest
WORKDIR /usr/share/nginx/html
RUN echo "Returning response from Service 2: Ok" > /usr/share/nginx/html/index.html
ADD client_cert2.cert client_private-key2.pem /usr/local/share/ca-certificates/
RUN chmod -R 400 /usr/local/share/ca-certificates/
```

If you’re building the Docker images with CodeBuild, the `buildspec` file uses the CodeBuild build number to uniquely identify image versions as a tag value. You can change the `buildspec` file to fit your requirements, as shown in the following `buildspec `custom code:

```
version: 0.2

phases:
  pre_build:
    commands:
      - echo Logging in to Amazon ECR...
      - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $ECR_REPOSITORY_URI
      - COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
      - IMAGE_TAG=${COMMIT_HASH:=latest}
  build:
    commands:
        # change the S3 path depending on the service
      - aws s3 cp s3://$YOUR_S3_BUCKET_NAME/serviceone/ $CodeBuild_SRC_DIR/ --recursive
      - echo Build started on `date`
      - echo Building the Docker image...
      - docker build -t $ECR_REPOSITORY_URI:latest .
      - docker tag $ECR_REPOSITORY_URI:latest $ECR_REPOSITORY_URI:$IMAGE_TAG
  post_build:
    commands:
      - echo Build completed on `date`
      - echo Pushing the Docker images...
      - docker push $ECR_REPOSITORY_URI:latest
      - docker push $ECR_REPOSITORY_URI:$IMAGE_TAG
      - echo Writing image definitions file...
      # for ECS deployment reference
      - printf '[{"name":"%s","imageUri":"%s"}]' $CONTAINER_NAME $ECR_REPOSITORY_URI:$IMAGE_TAG > imagedefinitions.json

artifacts:
  files:
    - imagedefinitions.json
```

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/internal-developer-platform/examples.html
---

# Examples of golden paths for internal development platforms
<a name="examples"></a>

This section contains the following examples of golden paths:
+ [Serverless workloads](#example-serverless)
+ [Amazon Elastic Container Service (Amazon ECS)](#example-ecs)
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](#example-eks)

## Serverless workloads
<a name="example-serverless"></a>

### Development
<a name="development.48dd1f77-7ade-5610-8e33-db4b4a5a6e08"></a>
+ Use the [AWS Serverless Application Model (AWS SAM) CLI](https://docs.aws.amazon.com/serverless-application-model/latest/developerguide/serverless-test-and-debug.html) for local development and testing.
+ Use the [AWS Integrated Application Test Kit](https://github.com/awslabs/aws-iatk) for integration testing.
+ During load testing, use [Amazon CodeGuru Profiler](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html) to fine-tune your application.

### Application design and deployment
<a name="application-design-and-deployment.d10b2a6c-bd46-562b-a035-43f74201c377"></a>
+ Use the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) for infrastructure as code.
+ Automate infrastructure and application deployment by using [CDK Pipelines](https://docs.aws.amazon.com/cdk/v2/guide/cdk_pipeline.html).
+ For scaffolding resources, create [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) functions by using container images and store them in [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html).
+ Use [Lambda images](https://gallery.ecr.aws/lambda) over generic images.
+ For networking, it is recommended that you deploy Lambda functions in virtual private clouds (VPCs) that have [VPC Flow Logs](https://docs.aws.amazon.com/vpc/latest/userguide/flow-logs.html) enabled and that you use [interface VPC endpoints](https://docs.aws.amazon.com/vpc/latest/privatelink/create-interface-endpoint.html) to access private resources.
+ Use [Amazon API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/welcome.html) to route HTTP requests to Lambda functions.
+ Use [versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) to manage the deployment of your Lambda functions.
+ Use [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) for dynamic configurations with validators.
+ Use [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html) to retrieve secrets.
+ For canary testing, use [alias routing configuration](https://docs.aws.amazon.com/lambda/latest/dg/configuration-aliases.html#configuring-alias-routing) to send a portion of traffic to a second Lambda function version.
+ Use [automatic rollbacks](https://docs.aws.amazon.com/codedeploy/latest/userguide/deployments-rollback-and-redeploy.html#deployments-rollback-and-redeploy-automatic-rollbacks) in AWS CodeDeploy and configure [alarms](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.html) in Amazon CloudWatch to initiate the rollbacks.

### Operations
<a name="operations.e3649d0b-7b6c-555b-a589-458052d145fe"></a>
+ Enable [API Gateway access logs](https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-logging.html).
+ Log the API Gateway request ID, the extended request ID, and the Lambda request ID.
+ Use structured logs for Lambda functions, preferably in JSON format.
+ Emit logs to standard output (stdout) instead of calling the CloudWatch Logs API.
+ Use [AWS Lambda Powertools](https://github.com/aws-powertools/) to implement serverless best practices.
+ Set your log retention period according to your organization's requirements.
+ Enable [CloudWatch Lambda Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/Lambda-Insights.html) to collect, aggregate, and summarize diagnostic information, such as cold starts. This can help you isolate and quickly resolve issues with your Lambda functions.
+ In CloudWatch, use `Errors`, `Throttles`, `ProvisionedConcurrencySpilloverInvocations`, and `Duration` metrics to monitor your Lambda functions. For more information, see [Working with Lambda function metrics](https://docs.aws.amazon.com/lambda/latest/dg/monitoring-metrics.html#monitoring-metrics-types).
+ In CloudWatch, use 4xx error codes, 5xx error codes, and latency metrics to monitor your APIs.
+ Use [AWS X-Ray](https://docs.aws.amazon.com/xray/latest/devguide/aws-xray.html) to collect data about requests that your application serves. For applications that use distributed components and services, this helps you quickly identify issues and opportunities for optimization.

## Amazon Elastic Container Service (Amazon ECS)
<a name="example-ecs"></a>

### Development
<a name="development.6d7ac79d-5533-55d2-964d-315c6611674a"></a>
+ Follow [best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-considerations.html) for Amazon Elastic Container Service (Amazon ECS) container images.
+ Use [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) to store container images and for continuous security scanning.

### Application design and deployment
<a name="application-design-and-deployment.975018b2-c4a8-58aa-9dfd-c1f44f451ae3"></a>
+ Follow [best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/application_architecture.html#application_architecture_fargate) to architect your application on Amazon ECS.
+ Use the [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html) for infrastructure as code and CI/CD pipelines for both infrastructure and application deployment.
+ Use [Amazon ECS Service Connect](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/service-connect.html) to manage Amazon ECS configurations for service discovery, connectivity, and traffic monitoring.
+ Use [Amazon Elastic File System (Amazon EFS)](https://docs.aws.amazon.com/efs/latest/ug/whatisefs.html) for containerized applications that scale horizontally. Use [Amazon Elastic Block Store (Amazon EBS)](https://docs.aws.amazon.com/ebs/latest/userguide/what-is-ebs.html) if your application requires sub-millisecond latency and doesn't need a shared file system.

### Operations
<a name="operations.8c3c8cb6-5188-50b9-a299-a77e38159e33"></a>
+ Use [AWS Fargate](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/AWS_Fargate.html) because it provides a managed way to containerize your workload without having to manage servers or clusters of Amazon Elastic Compute Cloud (Amazon EC2) instances.
+ Use [blue/Green deployment](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-bluegreen.html) with AWS CodeDeploy.
+ Use [Amazon CloudWatch Container Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/deploy-container-insights-ECS.html) to collect, aggregate, and summarize metrics and logs from your containerized applications and microservices.
+ Enable the [FireLens for Amazon ECS](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/using_firelens.html) log driver and use the [AWS for Fluent Bit](https://github.com/aws/aws-for-fluent-bit) sidecar container to improve performance and redirect log streams to separate locations, such as Amazon Simple Storage Service (Amazon S3) or CloudWatch log groups.

### Additional resources
<a name="additional-resources.91e92eed-5d29-5aed-87e5-1eab8e13618f"></a>
+ [Amazon ECS blueprints](https://github.com/aws-ia/ecs-blueprints) (GitHub)

## Amazon Elastic Kubernetes Service (Amazon EKS)
<a name="example-eks"></a>

### Development
<a name="development.6d7ac79d-5533-55d2-964d-315c6611674a"></a>
+ Follow [best practices](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/container-considerations.html) for Amazon Elastic Container Service (Amazon ECS) container images.
+ Use [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) to store container images and for continuous security scanning.

### Application design and deployment
<a name="application-design-and-deployment.85bfdc38-5328-5007-8dc3-06cfce3de072"></a>
+ Use [Helm](https://helm.sh/docs/) to package your application templates.
+ Follow a GitOps approach by using [Argo CD](https://argo-cd.readthedocs.io/en/stable/) to deploy your application.
+ Use the [AWS Load Balancer Controller](https://docs.aws.amazon.com/eks/latest/userguide/aws-load-balancer-controller.html) to manage Elastic Load Balancing resources for your Kubernetes cluster.
+ Use [cert-manager](https://github.com/cert-manager/cert-manager) and [AWS Private Certificate Authority Issuer](https://github.com/cert-manager/aws-privateca-issuer/) to manage TLS certificates.
+ Use [Amazon Elastic Block Store (Amazon EBS) Container Storage Interface (CSI) driver](https://docs.aws.amazon.com/eks/latest/userguide/ebs-csi.html) or the [Amazon Elastic File System (Amazon EFS) CSI driver](https://docs.aws.amazon.com/eks/latest/userguide/efs-csi.html) for storage options.
+ Use [ExternalDNS](https://github.com/kubernetes-sigs/external-dns) to integrate Kubernetes services with Amazon Route 53.
+ Use [External Secrets Operator](https://github.com/external-secrets/external-secrets) to store secrets in AWS Secrets Manager or AWS Systems Manager Parameter Store.
+ Use [Crossplane](https://www.crossplane.io/) to manage AWS infrastructure from your Kubernetes cluster.

### Operations
<a name="operations.593817e8-989e-5d8b-9604-2d087e977edb"></a>
+ Use [Calico](https://www.tigera.io/project-calico/) for network policies and [Gatekeeper](https://github.com/open-policy-agent/gatekeeper) as a policy controller.
+ Use [Karpenter](https://github.com/aws/karpenter-provider-aws) for cluster autoscaling.
+ Use [Amazon Managed Service for Prometheus](https://docs.aws.amazon.com/prometheus/latest/userguide/what-is-Amazon-Managed-Service-Prometheus.html) and [Amazon Managed Grafana](https://docs.aws.amazon.com/grafana/latest/userguide/what-is-Amazon-Managed-Service-Grafana.html) for observability.
+ Use [Kubecost](https://www.kubecost.com/) to provide a real-time infrastructure cost visibility.

### Additional resources
<a name="additional-resources.0bcd4f06-c5a8-51e6-9340-413a4090a466"></a>
+ [Amazon EKS blueprints for Terraform](https://aws-ia.github.io/terraform-aws-eks-blueprints/)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

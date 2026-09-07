---
source_url: https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/cicd-on-aws.html
---

# CI/CD on AWS
<a name="cicd-on-aws"></a>

CI/CD can be pictured as a pipeline, where new code is submitted on one end, tested over a series of stages (source, build, test, staging, and production), and then published as production-ready code.

![A diagram depicting an example of the AWS code pipeline](https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g2.png)

*CICD pipeline overview*

Each stage of the CI/CD pipeline is structured as a logical unit in the delivery process. Each stage acts as a gate that vets a certain aspect of the code. As the code progresses through the pipeline, the assumption is that the quality of the code is higher in the later stages, because more aspects of it continue to be verified. Problems uncovered in an early stage stop the code from progressing through the pipeline. Results from the tests are immediately sent to the team, and all further builds and releases are stopped if software does not pass the stage.

AWS brings in a complete set of CI/CD developer tools to accelerate software development and release cycles. [AWS CodePipeline](https://aws.amazon.com/codepipeline/) automates the build, test, and deploy phases of the release process every time there is a code change, based on the defined release model. This enables the rapid and reliable delivery of features and updates.

Code pipelines can integrate with other services. These can be AWS Services, such as [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3), or third-party products, such as GitHub. AWS CodePipeline can address a variety of development and operation use cases including:
+ Compiling, building, and testing code with [AWS CodeBuild](https://aws.amazon.com/codebuild/)
+ Continuous delivery of container-based applications to the cloud
+ Pre-deployment validation of artifacts (such as descriptors and container images) required for network service or specific cloud-native network functions
+ Functional, integration, and performance tests for containerized network function/virtual network function (CNF/VNF), including baseline and regression testing
+ Reliability and disaster recovery (DR) testing.

![A diagram depicting AWS CICD pipeline components](https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g3.png)

*AWS CICD pipeline components*

AWS can set up CI/CD pipelines using the following AWS Developer Tools:
+ [AWS CodeCommit](https://aws.amazon.com/codecommit/)
+ [AWS CodeBuild](https://aws.amazon.com/codebuild/)
+ [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
+ [AWS CodeDeploy](https://aws.amazon.com/codedeploy/)
+ [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/)
+ [AWS CodeStar](https://aws.amazon.com/codestar/)

CI/CD pipeline creation can be automated using [AWS CDK](https://aws.amazon.com/cdk/) and [CloudFormation](https://aws.amazon.com/cloudformation/). In the NFV domain, this AWS native automation can be integrated into a Management and Orchestration (MANO) framework and the CSP’s service orchestration framework.

The CI/CD process includes the following steps:
+ Network setup – AWS CDK and CloudFormation initiate creation of the network prerequisites:
+ Networking stack (VPC, subnets, network address translation (NAT) gateway, route table, and internet gateway)
+ Infrastructure deployment – AWS CDK and CloudFormation initiate the creation of the following resource stacks:
+ Compute stack ([Amazon Elastic Kubernetes Service](https://aws.amazon.com/eks/) (Amazon EKS) cluster creation, EKS Worker nodes, [AWS Lambda](https://aws.amazon.com/lambda/))
+ Storage stack (Amazon S3 buckets, [Amazon Elastic Block Store ](https://aws.amazon.com/ebs)(Amazon EBS) volumes, and [ Amazon Elastic File System ](https://aws.amazon.com/efs/)(Amazon EFS)
+ Monitoring stack ([ CloudWatch ](https://aws.amazon.com/cloudwatch/), [ Amazon OpenSearch Service ](https://aws.amazon.com/opensearch-service/) (OpenSearch Service)
+ Security stack ([AWS Identity and Access Management](https://aws.amazon.com/iam/) (AWS IAM), [ Amazon Elastic Compute Cloud ](https://aws.amazon.com/ec2) (Amazon EC2) security groups, VPC [ network access control lists ](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-network-acls.html) (NACLs)
+ **Cloud Network Function (CNF) deployment **– In this stage, CNF is deployed onto EKS clusters using [ Kubectl ](https://kubernetes.io/docs/reference/kubectl/overview/) and Helm charts tools. This stage also deploys any specific applications or tools needed by the CNFs to work efficiently (such as [ Prometheus ](https://prometheus.io/) or [ Fluentd ](https://www.fluentd.org/)). CNFs can either be deployed via Lambda functions or with AWS CodeBuild.
+ Continuous updates and deployment – These are a sequence of steps that are carried out iteratively to deploy changes that are part of container/configuration changes resulting in upgrades. Similar to the CNF deployment case, continuous updates and deployment can be automated using AWS Services, with the trigger from [AWS CodeCommit](https://aws.amazon.com/codecommit/), [ Amazon Elastic Container Registry ](https://aws.amazon.com/ecr/) (Amazon ECR), or a third-party source system such as [ GitLab Webhooks ](https://docs.gitlab.com/ee/user/project/integrations/webhooks.html).

![A diagram depicting AWS CICD pipeline flow.](https://docs.aws.amazon.com/whitepapers/latest/cicd_for_5g_networks_on_aws/images/cicd_5g4.png)

*AWS CICD pipeline flow diagram*

The CI/CD pipeline is built using [AWS CodePipeline](https://aws.amazon.com/codepipeline/), and utilizes a continuous delivery service that models, visualizes, and automates the steps required to release software. By defining stages in a pipeline, you can retrieve code from a source code repository, build that source code into a releasable artifact, test the artifact, and deploy it to production. Only code that successfully passes through all these stages will be deployed. You can optionally add other requirements to your pipeline, such as manual approvals, to help ensure that only approved changes are deployed to production.

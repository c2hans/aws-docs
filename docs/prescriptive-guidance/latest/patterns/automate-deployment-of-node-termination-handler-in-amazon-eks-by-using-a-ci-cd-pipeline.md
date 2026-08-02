---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline.html
---

# Automate deployment of Node Termination Handler in Amazon EKS by using a CI/CD pipeline
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline"></a>

*Sandip Gangapadhyay, Sandeep Gawande, Viyoma Sachdeva, Pragtideep Singh, and John Vargas, Amazon Web Services*

## Summary
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-summary"></a>

**Notice**: AWS CodeCommit is no longer available to new customers. Existing customers of AWS CodeCommit can continue to use the service as normal. [Learn more](https://aws.amazon.com/blogs/devops/how-to-migrate-your-aws-codecommit-repository-to-another-git-provider/)

On the Amazon Web Services (AWS) Cloud, you can use [AWS Node Termination Handler](https://github.com/aws/aws-node-termination-handler), an open-source project, to handle Amazon Elastic Compute Cloud (Amazon EC2) instance shutdown within Kubernetes gracefully. AWS Node Termination Handler helps to ensure that the Kubernetes control plane responds appropriately to events that can cause your EC2 instance to become unavailable. Such events include the following:
+ [EC2 instance scheduled maintenance](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring-instances-status-check_sched.html)
+ [Amazon EC2 Spot Instance interruptions](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html)
+ [Auto Scaling group scale in](https://docs.aws.amazon.com/autoscaling/ec2/userguide/AutoScalingGroupLifecycle.html#as-lifecycle-scale-in)
+ [Auto Scaling group rebalancing](https://docs.aws.amazon.com/autoscaling/ec2/userguide/auto-scaling-benefits.html#AutoScalingBehavior.InstanceUsage) across Availability Zones
+ EC2 instance termination through the API or the AWS Management Console

If an event isn’t handled, your application code might not stop gracefully. It also might take longer to recover full availability, or it might accidentally schedule work to nodes that are going down. The `aws-node-termination-handler` (NTH) can operate in two different modes: Instance Metadata Service (IMDS) or Queue Processor. For more information about the two modes, see the [Readme file](https://github.com/aws/aws-node-termination-handler#readme).

This pattern uses AWS CodeCommit, and it automates the deployment of NTH by using Queue Processor through a continuous integration and continuous delivery (CI/CD) pipeline.

**Note**
If you're using [EKS managed node groups](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html), you don't need the `aws-node-termination-handler`.

## Prerequisites and limitations
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-prereqs"></a>

**Prerequisites **
+ An active AWS account.
+ A web browser that is supported for use with the AWS Management Console. See the [list of supported browsers](https://aws.amazon.com/premiumsupport/knowledge-center/browsers-management-console/).
+ AWS Cloud Development Kit (AWS CDK) [installed](https://docs.aws.amazon.com/cdk/v2/guide/getting_started.html#getting_started_install).
+ `kubectl`, the Kubernetes command line tool, [installed](https://kubernetes.io/docs/tasks/tools/).
+ `eksctl`, the AWS Command Line Interface (AWS CLI) for Amazon Elastic Kubernetes Service (Amazon EKS), [installed](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html).
+ A running EKS cluster with version 1.20 or later.
+ A self-managed node group attached to the EKS cluster. To create an Amazon EKS cluster with a self-managed node group, run the following command.

  ```
  eksctl create cluster --managed=false --region <region> --name <cluster_name>
  ```

  For more information on `eksctl`, see the [eksctl documentation](https://eksctl.io/usage/creating-and-managing-clusters/).
+ AWS Identity and Access Management (IAM) OpenID Connect (OIDC) provider for your cluster. For more information, see [Creating an IAM OIDC provider for your cluster](https://docs.aws.amazon.com/eks/latest/userguide/enable-iam-roles-for-service-accounts.html).

**Limitations **
+ You must use an AWS Region that supports the Amazon EKS service.

**Product versions**
+ Kubernetes version 1.20 or later
+ `eksctl` version 0.107.0 or later
+ AWS CDK version 2.27.0 or later

## Architecture
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-architecture"></a>

**Target technology stack  **
+ A virtual private cloud (VPC)
+ An EKS cluster
+ Amazon Simple Queue Service (Amazon SQS)
+ IAM
+ Kubernetes

**Target architecture**** **

The following diagram shows the high-level view of the end-to-end steps when the node termination is started.

![A VPC with an Auto Scaling group, an EKS cluster with Node Termination Handler, and an SQS queue.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/970dfb73-9526-4942-a974-e8eef6416596/images/9e0125ae-d55b-49dd-ae70-ccaedf03832a.png)

The workflow shown in the diagram consists of the following high-level steps:

1. The automatic scaling EC2 instance terminate event is sent to the SQS queue.

1. The NTH Pod monitors for new messages in the SQS queue.

1. The NTH Pod receives the new message and does the following:
   + Cordons the node so that new pod does not run on the node.
   + Drains the node, so that the existing pod is evacuated
   + Sends a lifecycle hook signal to the Auto Scaling group so that the node can be terminated.

**Automation and scale**
+ Code is managed and deployed by AWS CDK, backed by AWS CloudFormation nested stacks.
+ The [Amazon EKS control plane](https://docs.aws.amazon.com/eks/latest/userguide/disaster-recovery-resiliency.html) runs across multiple Availability Zones to ensure high availability.
+ For [automatic scaling](https://docs.aws.amazon.com/eks/latest/userguide/autoscaling.html), Amazon EKS supports the Kubernetes [Cluster Autoscaler](https://github.com/kubernetes/autoscaler/tree/master/cluster-autoscaler) and [Karpenter](https://karpenter.sh/).

## Tools
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-tools"></a>

**AWS services**
+ [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/latest/guide/home.html) is a software development framework that helps you define and provision AWS Cloud infrastructure in code.
+ [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) is a fully managed build service that helps you compile source code, run unit tests, and produce artifacts that are ready to deploy.
+ [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) is a version control service that helps you privately store and manage Git repositories, without needing to manage your own source control system.
+ [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) helps you quickly model and configure the different stages of a software release and automate the steps required to release software changes continuously.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) helps you maintain application availability and allows you to automatically add or remove Amazon EC2 instances according to conditions you define.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.

**Other tools**
+ [kubectl](https://kubernetes.io/docs/reference/kubectl/kubectl/) is a Kubernetes command line tool for running commands against Kubernetes clusters. You can use kubectl to deploy applications, inspect and manage cluster resources, and view logs.

**Code **

The code for this pattern is available in the [deploy-nth-to-eks](https://github.com/aws-samples/deploy-nth-to-eks) repo on GitHub.com. The code repo contains the following files and folders.
+ `nth folder` – The Helm chart, values files, and the scripts to scan and deploy the AWS CloudFormation template for Node Termination Handler.
+ `config/config.json` – The configuration parameter file for the application. This file contains all the parameters needed for CDK to be deployed.
+ `cdk` – AWS CDK source code.
+ `setup.sh` – The script used to deploy the AWS CDK application to create the required CI/CD pipeline and other required resources.
+ `uninstall.sh` – The script used to clean up the resources.

To use the example code, follow the instructions in the *Epics* section.

## Best practices
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-best-practices"></a>

For best practices when automating AWS Node Termination Handler, see the following:
+ [EKS Best Practices Guides](https://aws.github.io/aws-eks-best-practices/)
+ [Node Termination Handler - Configuration](https://github.com/aws/aws-node-termination-handler/tree/main/config/helm/aws-node-termination-handler)

## Epics
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-epics"></a>

### Set up your environment
<a name="set-up-your-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repo. | To clone the repo by using SSH (Secure Shell), run the following the command.<pre>git clone git@github.com:aws-samples/deploy-nth-to-eks.git</pre><br />To clone the repo by using HTTPS, run the following the command.<pre>git clone https://github.com/aws-samples/deploy-nth-to-eks.git</pre><br />Cloning the repo creates a folder named `deploy-nth-to-eks`.<br />Change to that directory.<pre>cd deploy-nth-to-eks</pre> | App developer, AWS DevOps, DevOps engineer |
| Set the kubeconfig file. | Set your AWS credentials in your terminal and confirm that you have rights to assume the cluster role. You can use the following example code.<pre>aws eks update-kubeconfig --name <Cluster_Name> --region <region>--role-arn <Role_ARN></pre> | AWS DevOps, DevOps engineer, App developer |

### Deploy the CI/CD pipeline
<a name="deploy-the-ci-cd-pipeline"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up the parameters. | In the `config/config.json` file, set up the following required parameters.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline.html) | App developer, AWS DevOps, DevOps engineer |
| Create the CI/CD pipeline to deploy NTH. | Run the setup.sh script.<pre>./setup.sh</pre><br />The script will deploy the AWS CDK application that will create the CodeCommit repo with example code, the pipeline, and CodeBuild projects based on the user input parameters in `config/config.json` file.<br />This script will ask for the password as it installs npm packages with the sudo command. | App developer, AWS DevOps, DevOps engineer |
| Review the CI/CD pipeline. | Open the AWS Management Console, and review the following resources created in the stack.[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline.html)<br />After the pipeline runs successfully, Helm release `aws-node-termination-handler` is installed in the EKS cluster. Also, a Pod named `aws-node-termination-handler` is running in the `kube-system` namespace in the cluster. | App developer, AWS DevOps, DevOps engineer |

### Test NTH deployment
<a name="test-nth-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Simulate an Auto Scaling group scale-in event. | To simulate an automatic scaling scale-in event, do the following:[See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline.html) |  |
| Review the logs. | During the scale-in event, the NTH Pod will cordon and drain the corresponding worker node (the EC2 instance that will be terminated as part of the scale-in event). To check the logs, use the code in the *Additional information* section. | App developer, AWS DevOps, DevOps engineer |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up all AWS resources. | To clean up the resources created by this pattern, run the following command.<pre>./uninstall.sh</pre><br />This will clean up all the resources created in this pattern by deleting the CloudFormation stack. | DevOps engineer |

## Troubleshooting
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The npm registry isn’t set correctly. | During the installation of this solution, the script installs npm install to download all the required packages. If, during the installation, you see a message that says "Cannot find module," the npm registry might not be set correctly. To see the current registry setting, run the following command.<pre>npm config get registry</pre><br />To set the registry with `https://registry.npmjs.org/`, run the following command.<pre>npm config set registry https://registry.npmjs.org</pre> |
| Delay SQS message delivery. | As part of your troubleshooting, if you want to delay the SQS message delivery to NTH Pod, you can adjust the SQS delivery delay parameter. For more information, see [Amazon SQS delay queues](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-delay-queues.html). |

## Related resources
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-resources"></a>
+ [AWS Node Termination Handler source code](https://github.com/aws/aws-node-termination-handler)
+ [EC2 workshop](https://ec2spotworkshops.com/using_ec2_spot_instances_with_eks/070_selfmanagednodegroupswithspot/deployhandler.html)
+ [AWS CodePipeline](https://aws.amazon.com/codepipeline/)
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://aws.amazon.com/eks/)
+ [AWS Cloud Development Kit](https://aws.amazon.com/cdk/)
+ [AWS CloudFormation](https://aws.amazon.com/cloudformation/)

## Additional information
<a name="automate-deployment-of-node-termination-handler-in-amazon-eks-by-using-a-ci-cd-pipeline-additional"></a>

1. Find the NTH Pod name.

```
kubectl get pods -n kube-system |grep aws-node-termination-handler
aws-node-termination-handler-65445555-kbqc7   1/1     Running   0          26m
kubectl get pods -n kube-system |grep aws-node-termination-handler
aws-node-termination-handler-65445555-kbqc7   1/1     Running   0          26m
```

2. Check the logs. An example log looks like the following. It shows that the node has been cordoned and drained before sending the Auto Scaling group lifecycle hook completion signal.

```
kubectl -n kube-system logs aws-node-termination-handler-65445555-kbqc7
022/07/17 20:20:43 INF Adding new event to the event store event={"AutoScalingGroupName":"eksctl-my-cluster-target-nodegroup-ng-10d99c89-NodeGroup-ZME36IGAP7O1","Description":"ASG Lifecycle Termination event received. Instance will be interrupted at 2022-07-17 20:20:42.702 +0000 UTC \n","EndTime":"0001-01-01T00:00:00Z","EventID":"asg-lifecycle-term-33383831316538382d353564362d343332362d613931352d383430666165636334333564","InProgress":false,"InstanceID":"i-0409f2a9d3085b80e","IsManaged":true,"Kind":"SQS_TERMINATE","NodeLabels":null,"NodeName":"ip-192-168-75-60.us-east-2.compute.internal","NodeProcessed":false,"Pods":null,"ProviderID":"aws:///us-east-2c/i-0409f2a9d3085b80e","StartTime":"2022-07-17T20:20:42.702Z","State":""}
2022/07/17 20:20:44 INF Requesting instance drain event-id=asg-lifecycle-term-33383831316538382d353564362d343332362d613931352d383430666165636334333564 instance-id=i-0409f2a9d3085b80e kind=SQS_TERMINATE node-name=ip-192-168-75-60.us-east-2.compute.internal provider-id=aws:///us-east-2c/i-0409f2a9d3085b80e
2022/07/17 20:20:44 INF Pods on node node_name=ip-192-168-75-60.us-east-2.compute.internal pod_names=["aws-node-qchsw","aws-node-termination-handler-65445555-kbqc7","kube-proxy-mz5x5"]
2022/07/17 20:20:44 INF Draining the node
2022/07/17 20:20:44 ??? WARNING: ignoring DaemonSet-managed Pods: kube-system/aws-node-qchsw, kube-system/kube-proxy-mz5x5
2022/07/17 20:20:44 INF Node successfully cordoned and drained node_name=ip-192-168-75-60.us-east-2.compute.internal reason="ASG Lifecycle Termination event received. Instance will be interrupted at 2022-07-17 20:20:42.702 +0000 UTC \n"
2022/07/17 20:20:44 INF Completed ASG Lifecycle Hook (NTH-K8S-TERM-HOOK) for instance i-0409f2a9d3085b80e
```

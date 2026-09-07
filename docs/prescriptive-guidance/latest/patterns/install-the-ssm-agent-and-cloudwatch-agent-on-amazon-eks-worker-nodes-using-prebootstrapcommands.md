---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands.html
---

# Install the SSM Agent and CloudWatch agent on Amazon EKS worker nodes using preBootstrapCommands
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands"></a>

*Akkamahadevi Hiremath, Amazon Web Services*

## Summary
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-summary"></a>

This pattern provides code samples and steps to install the AWS Systems Manager Agent (SSM Agent) and Amazon CloudWatch agent on Amazon Elastic Kubernetes Service (Amazon EKS) worker nodes in the Amazon Web Services (AWS) Cloud during Amazon EKS cluster creation. You can install the SSM Agent and CloudWatch agent by using the `preBootstrapCommands` property from the `eksctl` [config file schema](https://eksctl.io/usage/schema/) (Weaveworks documentation). Then, you can use the SSM Agent to connect to your worker nodes without using an Amazon Elastic Compute Cloud (Amazon EC2) key pair. Additionally, you can use the CloudWatch agent to monitor memory and disk utilization on your Amazon EKS worker nodes.

## Prerequisites and limitations
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-prereqs"></a>

**Prerequisites**
+ An active AWS account
+ The [eksctl command line utility](https://docs.aws.amazon.com/eks/latest/userguide/eksctl.html), installed and configured on macOS, Linux, or Windows
+ The [kubectl command line utility](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html), installed and configured on macOS, Linux, or Windows

**Limitations**
+ We recommend that you avoid adding long-running scripts to the `preBootstrapCommands`** **property, because this delays the node from joining the Amazon EKS cluster during scaling activities. We recommend that you create a [custom Amazon Machine Image (AMI)](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/using-features.customenv.html) instead.
+ This pattern applies to Amazon EC2 Linux instances only.

## Architecture
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-architecture"></a>

**Technology stack**
+ Amazon CloudWatch
+ Amazon Elastic Kubernetes Service (Amazon EKS)
+ AWS Systems Manager Parameter Store

**Target architecture**

The following diagram shows an example of a user connecting to Amazon EKS worker nodes using SSM Agent which was installed using the `preBootstrapCommands`.

![](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/b37a3cdb-204f-4014-8317-3600a793dac7/images/9a5760af-23bb-4616-97b0-b401a9d080cf.png)

The diagram shows the following workflow:

1. The user creates an Amazon EKS cluster by using the `eksctl` configuration file with the `preBootstrapCommands` property, which installs the SSM Agent and CloudWatch agent.

1. Any new instances that join the cluster later due to scaling activities get created with the pre-installed SSM Agent and CloudWatch agent.

1. The user connects to Amazon EC2 by using the SSM Agent and then monitors memory and disk utilization by using the CloudWatch agent.

## Tools
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-tools"></a>
+ [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html) helps you monitor the metrics of your AWS resources and the applications that you run on AWS in real time.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) provides secure, hierarchical storage for configuration data management and secrets management.
+ [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) helps you manage your EC2 instances, on-premises instances, and virtual machines through an interactive, one-click, browser-based shell or through the AWS Command Line Interface (AWS CLI).
+ [eksctl](https://eksctl.io/usage/schema/) is a command-line utility for creating and managing Kubernetes clusters on Amazon EKS.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl/) is a command-line utility for communicating with the cluster API server.

## Epics
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-epics"></a>

### Create an Amazon EKS cluster
<a name="create-an-amazon-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Store the CloudWatch agent configuration file. | Store the CloudWatch agent configuration file in the [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) in the AWS Region where you want to create your Amazon EKS cluster. To do this, [create a parameter](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html) in AWS Systems Manager Parameter Store and note the name of the parameter (for example, `AmazonCloudwatch-linux`).<br />For more information, see the *Example CloudWatch agent configuration file *code in the [Additional information](#install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-additional) section of this pattern. | DevOps engineer |
| Create the eksctl configuration file and cluster.  | 1. Create an `eksctl` configuration file that includes the CloudWatch agent and SSM Agent installation steps. For more information, see the *Example eksctl configuration file* code in the [Additional information](#install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-additional) section of this pattern.<br />2. Create a cluster by running the `eksctl create cluster -f cluster.yaml` command. | AWS DevOps |

### Verify that the SSM Agent and CloudWatch agent work
<a name="verify-that-the-ssm-agent-and-cloudwatch-agent-work"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the SSM Agent. | Use SSH to connect to your Amazon EKS cluster nodes by using any of the methods covered in [Start a session](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#start-ec2-console%20%20or%20https:%2F%2Fdocs.aws.amazon.com%2Fsystems-manager%2Flatest%2Fuserguide%2Fsession-manager-working-with-sessions-start.html%23sessions-start-cli) from the AWS Systems Manager documentation. | AWS DevOps |
| Test the CloudWatch agent. | Use the CloudWatch console to validate the CloudWatch agent:1. Sign in to the AWS Management Console and open the [CloudWatch console](https://console.aws.amazon.com/cloudwatch/).<br />2. On the navigation pane, expand **Metrics** and then choose **All metrics**.<br />3. In the search box on the **Browse** tab, enter and then choose **CWAgent metrics **to** **see the memory and disk metrics. | AWS DevOps |

## Related resources
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-resources"></a>
+ [Installing and running the CloudWatch agent on your servers](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-commandline-fleet.html) (Amazon CloudWatch documentation)
+ [Create a Systems Manager parameter (console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/parameter-create-console.html) (AWS Systems Manager documentation)
+ [Create the CloudWatch agent configuration file](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/create-cloudwatch-agent-configuration-file.html) (Amazon CloudWatch documentation)
+ [Starting a session (AWS CLI)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#sessions-start-cli) (AWS Systems Manager documentation)
+ [Starting a session (Amazon EC2 console)](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-working-with-sessions-start.html#start-ec2-console) (AWS Systems Manager documentation)

## Additional information
<a name="install-the-ssm-agent-and-cloudwatch-agent-on-amazon-eks-worker-nodes-using-prebootstrapcommands-additional"></a>

**Example CloudWatch agent configuration file**

In the following example, the CloudWatch agent is configured to monitor disk and memory utilization on Amazon Linux instances:

```
{
    "agent": {
        "metrics_collection_interval": 60,
        "run_as_user": "cwagent"
    },
    "metrics": {
        "append_dimensions": {
            "AutoScalingGroupName": "${aws:AutoScalingGroupName}",
            "ImageId": "${aws:ImageId}",
            "InstanceId": "${aws:InstanceId}",
            "InstanceType": "${aws:InstanceType}"
        },
        "metrics_collected": {
            "disk": {
                "measurement": [
                    "used_percent"
                ],
                "metrics_collection_interval": 60,
                "resources": [
                    "*"
                ]
            },
            "mem": {
                "measurement": [
                    "mem_used_percent"
                ],
                "metrics_collection_interval": 60
            }
        }
    }
}
```

**Example eksctl configuration file**

```
apiVersion: eksctl.io/v1alpha5
kind: ClusterConfig
metadata:
  name: test
  region: us-east-2
  version: "1.24"
managedNodeGroups:
  - name: test
    minSize: 2
    maxSize: 4
    desiredCapacity: 2
    volumeSize: 20
    instanceType: t3.medium
    preBootstrapCommands:
    - sudo yum install amazon-ssm-agent -y
    - sudo systemctl enable amazon-ssm-agent
    - sudo systemctl start amazon-ssm-agent
    - sudo yum install amazon-cloudwatch-agent -y
    - sudo /opt/aws/amazon-cloudwatch-agent/bin/amazon-cloudwatch-agent-ctl -a fetch-config -m ec2 -s -c ssm:AmazonCloudwatch-linux
    iam:
      attachPolicyARNs:
        - arn:aws:iam::aws:policy/AmazonEKSWorkerNodePolicy
        - arn:aws:iam::aws:policy/AmazonEKS_CNI_Policy
        - arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly
        - arn:aws:iam::aws:policy/CloudWatchAgentServerPolicy
        - arn:aws:iam::aws:policy/AmazonSSMManagedInstanceCore
```

**Additional code details**
+ In the last line of the `preBootstrapCommands` property, `AmazonCloudwatch-linux` is the name of the parameter created in AWS System Manager Parameter Store. You must include `AmazonCloudwatch-linux` in Parameter Store in the same AWS Region where you created the Amazon EKS cluster. You can also specify a file path, but we recommend using Systems Manager for easier automation and reusability.
+ If you use `preBootstrapCommands` in the `eksctl` configuration file, you see two launch templates in the AWS Management Console. The first launch template includes the commands specified in `preBootstrapCommands`. The second template includes the commands specified in `preBootstrapCommands` and default Amazon EKS user data. This data is required to get the nodes to join the cluster. The node group’s Auto Scaling group uses this user data to spin up new instances.
+ If you use the `iam` attribute in the `eksctl` configuration file, you must list the default Amazon EKS policies with any additional policies required in your attached AWS Identity and Access Management (IAM) policies. In the code snippet from the *Create the eksctl configuration file and cluster *step, `CloudWatchAgentServerPolicy` and `AmazonSSMMangedInstanceCore` are additional policies added to make sure that the CloudWatch agent and SSM Agent work as expected. The `AmazonEKSWorkerNodePolicy`, `AmazonEKS_CNI_Policy`, `AmazonEC2ContainerRegistryReadOnly` policies are mandatory policies required for the Amazon EKS cluster to function correctly.

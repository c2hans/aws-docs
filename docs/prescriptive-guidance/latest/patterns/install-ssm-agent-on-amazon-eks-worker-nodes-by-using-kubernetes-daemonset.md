---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset.html
---

# Install SSM Agent on Amazon EKS worker nodes by using Kubernetes DaemonSet
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset"></a>

*Mahendra Revanasiddappa, Amazon Web Services*

## Summary
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-summary"></a>

**Note, September 2021:** The latest Amazon EKS optimized AMIs install SSM Agent automatically. For more information, see the [release notes](https://github.com/awslabs/amazon-eks-ami/releases/tag/v20210621) for the June 2021 AMIs.

In Amazon Elastic Kubernetes Service (Amazon EKS), because of security guidelines, worker nodes don't have Secure Shell (SSH) key pairs attached to them. This pattern shows how you can use the Kubernetes DaemonSet resource type to install AWS Systems Manager Agent (SSM Agent) on all worker nodes, instead of installing it manually or replacing the Amazon Machine Image (AMI) for the nodes. DaemonSet uses a cron job on the worker node to schedule the installation of SSM Agent. You can also use this pattern to install other packages on worker nodes.

When you're troubleshooting issues in the cluster, installing SSM Agent on demand enables you to establish an SSH session with the worker node, to collect logs or to look into instance configuration, without SSH key pairs.

## Prerequisites and limitations
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-prereqs"></a>

**Prerequisites**
+ An existing Amazon EKS cluster with Amazon Elastic Compute Cloud (Amazon EC2) worker nodes.
+ Container instances should have the required permissions to communicate with the SSM service. The AWS Identity and Access Management (IAM) managed role **AmazonSSMManagedInstanceCore** provides the required permissions for SSM Agent to run on EC2 instances. For more information, see the [AWS Systems Manager documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-profile.html).

**Limitations**
+ This pattern isn't applicable to AWS Fargate, because DaemonSets aren't supported on the Fargate platform.
+ This pattern applies only to Linux-based worker nodes.
+ The DaemonSet pods run in privileged mode. If the Amazon EKS cluster has a webhook that blocks pods in privileged mode, the SSM Agent will not be installed.

## Architecture
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-architecture"></a>

The following diagram illustrates the architecture for this pattern.

![Using Kubernetes DaemonSet to install SSM Agent on Amazon EKS worker nodes.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/016d53f3-45c1-4913-b542-67124e1462b8/images/3a6dfd00-e54b-44d5-843a-4c26ce9826c9.png)

## Tools
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-tools"></a>

**Tools**
+ [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) is a command-line utility that is used to interact with an Amazon EKS cluster. This pattern uses `kubectl` to deploy a DaemonSet on the Amazon EKS cluster, which will install SSM Agent on all worker nodes.
+ [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) makes it easy for you to run Kubernetes on AWS without having to install, operate, and maintain your own Kubernetes control plane or nodes. Kubernetes is an open-source system for automating the deployment, scaling, and management of containerized applications.
+ [AWS Systems Manager Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html) lets you manage your EC2 instances, on-premises instances, and virtual machines (VMs) through an interactive, one-click, browser-based shell or through the AWS Command Line Interface (AWS CLI).

**Code**

Use the following code to create a DaemonSet configuration file that will install SSM Agent on the Amazon EKS cluster. Follow the instructions in the [Epics](#install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-epics) section.

```
cat << EOF > ssm_daemonset.yaml
apiVersion: apps/v1
kind: DaemonSet
metadata:
  labels:
    k8s-app: ssm-installer
  name: ssm-installer
  namespace: kube-system
spec:
  selector:
    matchLabels:
      k8s-app: ssm-installer
  template:
    metadata:
      labels:
        k8s-app: ssm-installer
    spec:
      containers:
      - name: sleeper
        image: busybox
        command: ['sh', '-c', 'echo I keep things running! && sleep 3600']
      initContainers:
      - image: amazonlinux
        imagePullPolicy: Always
        name: ssm
        command: ["/bin/bash"]
        args: ["-c","echo '* * * * * root yum install -y https://s3.amazonaws.com/ec2-downloads-windows/SSMAgent/latest/linux_amd64/amazon-ssm-agent.rpm & rm -rf /etc/cron.d/ssmstart' > /etc/cron.d/ssmstart"]
        securityContext:
          allowPrivilegeEscalation: true
        volumeMounts:
        - mountPath: /etc/cron.d
          name: cronfile
        terminationMessagePath: /dev/termination-log
        terminationMessagePolicy: File
      volumes:
      - name: cronfile
        hostPath:
          path: /etc/cron.d
          type: Directory
      dnsPolicy: ClusterFirst
      restartPolicy: Always
      schedulerName: default-scheduler
      terminationGracePeriodSeconds: 30
EOF
```

## Epics
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-epics"></a>

### Set up kubectl
<a name="set-up-kubectl"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Install and configure kubectl to access the EKS cluster. | If `kubectl` isn't already installed and configured to access the Amazon EKS cluster, see [Installing kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) in the Amazon EKS documentation. | DevOps |

### Deploy the DaemonSet
<a name="deploy-the-daemonset"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the DaemonSet configuration file. | Use the code in the [Code](#install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-tools) section earlier in this pattern to create a DaemonSet configuration file called `ssm_daemonset.yaml`, which will be deployed to the Amazon EKS cluster. <br />The pod launched by DaemonSet has a main container and an `init` container. The main container has a `sleep` command. The `init` container includes a `command` section that creates a cron job file to install SSM Agent at the path `/etc/cron.d/`. The cron job runs only once, and the file it creates is automatically deleted after the job is complete. <br />When the init container has finished, the main container waits for 60 minutes before exiting. After 60 minutes, a new pod is launched. This pod installs SSM Agent, if it’s missing, or updates SSM Agent to the latest version.<br />If required, you can modify the `sleep` command to restart the pod once a day or to run more often.  | DevOps |
| Deploy the DaemonSet on the Amazon EKS cluster. | To deploy the DaemonSet configuration file you created in the previous step on the Amazon EKS cluster, use the following command:<pre>kubectl apply -f ssm_daemonset.yaml </pre><br />This command creates a DaemonSet to run the pods on worker nodes to install SSM Agent. | DevOps |

## Related resources
<a name="install-ssm-agent-on-amazon-eks-worker-nodes-by-using-kubernetes-daemonset-resources"></a>
+ [Installing kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) (Amazon EKS documentation)
+ [Setting up Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager-getting-started.html) (AWS Systems Manager documentation)

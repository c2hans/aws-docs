---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/event-driven-auto-scaling-with-eks-pod-identity-and-keda.html
---

# Set up event-driven auto scaling in Amazon EKS by using Amazon EKS Pod Identity and KEDA
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda"></a>

*Dipen Desai, Abhay Diwan, Kamal Joshi, and Mahendra Revanasiddappa, Amazon Web Services*

## Summary
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-summary"></a>

Orchestration platforms, such as [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html), have streamlined the lifecycle management of container-based applications. This helps organizations focus on building, securing, operating, and maintaining container-based applications. As event-driven deployments become more common, organizations are more frequently scaling Kubernetes deployments based on various event sources. This method, combined with auto scaling, can result in significant cost savings by providing on-demand compute resources and efficient scaling that is tailored to application logic.

[KEDA](https://keda.sh/) is a Kubernetes-based event-driven autoscaler. KEDA helps you scale any container in Kubernetes based on the number of events that need to be processed. It is lightweight and integrates with any Kubernetes cluster. It also works with standard Kubernetes components, such as [Horizontal Pod Autoscaling (HPA)](https://kubernetes.io/docs/tasks/run-application/horizontal-pod-autoscale/). KEDA also offers [TriggerAuthentication](https://keda.sh/docs/2.14/concepts/authentication/#re-use-credentials-and-delegate-auth-with-triggerauthentication), which is a feature that helps you delegate authentication. It allows you to describe authentication parameters that are separate from the ScaledObject and the deployment containers.

AWS provides AWS Identity and Access Management (IAM) roles that support diverse Kubernetes deployment options, including Amazon EKS, Amazon EKS Anywhere, Red Hat OpenShift Service on AWS (ROSA), and self-managed Kubernetes clusters on Amazon Elastic Compute Cloud (Amazon EC2). These roles use IAM constructs, such as OpenID Connect (OIDC) identity providers and IAM trust policies, to operate across different environments without relying directly on Amazon EKS services or APIs. For more information, see [IAM roles for service accounts](https://docs.aws.amazon.com/eks/latest/userguide/iam-roles-for-service-accounts.html) in the Amazon EKS documentation.

[Amazon EKS Pod Identity](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) simplifies the process for Kubernetes service accounts to assume IAM roles without requiring OIDC providers. It provides the ability to manage credentials for your applications. Instead of creating and distributing your AWS credentials to the containers or using the Amazon EC2 instance’s role, you associate an IAM role with a Kubernetes service account and configure your Pods to use the service account. This helps you use an IAM role across multiple clusters and simplifies policy management by enabling the reuse of permission policies across IAM roles.

By implementing KEDA with Amazon EKS Pod Identity, businesses can achieve efficient event-driven auto scaling and simplified credential management. Applications scale based on demand, which optimizes resource utilization and reduces costs.

This pattern helps you integrate Amazon EKS Pod Identity with KEDA. It showcases how you can use the `keda-operator` service account and delegate authentication with `TriggerAuthentication`. It also describes how to set up a trust relationship between an IAM role for the KEDA operator and an IAM role for the application. This trust relationship allows KEDA to monitor messages in the event queues and adjust scaling for the destination Kubernetes objects.

## Prerequisites and limitations
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-prereqs"></a>

**Prerequisites**
+ AWS Command Line Interface (AWS CLI) version 2.13.17 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ Python version 3.11.5 or later, [installed](https://www.python.org/downloads/)
+ AWS SDK for Python (Boto3) version 1.34.135 or later, [installed](https://boto3.amazonaws.com/v1/documentation/api/latest/guide/quickstart.html)
+ Helm version 3.12.3 or later, [installed](https://helm.sh/docs/intro/install/)
+ kubectl version 1.25.1 or later, [installed](https://kubernetes.io/docs/tasks/tools/)
+ Docker Engine version 26.1.1 or later, [installed](https://docs.docker.com/engine/install/)
+ An Amazon EKS cluster version 1.24 or later, [created](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)
+ Prerequisites for creating the Amazon EKS Pod Identity agent, [met](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html#pod-id-agent-add-on-create)

**Limitations**
+ It is required that you establish a trust relationship between the `keda-operator` role and the `keda-identity` role. Instructions are provided in the [Epics](#event-driven-auto-scaling-with-eks-pod-identity-and-keda-epics) section of this pattern.

## Architecture
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-architecture"></a>

In this pattern, you create the following AWS resources:
+ **Amazon Elastic Container Registry (Amazon ECR) repository** – In this pattern, this repo is named `keda-pod-identity-registry`. This private repo is used to store Docker images of the sample application.
+ **Amazon Simple Queue Service (Amazon SQS) queue** – In this pattern, this queue is named `event-messages-queue`. The queue acts as a message buffer that collects and stores incoming messages. KEDA monitors the queue metrics, such as message count or queue length, and it automatically scales the application based on these metrics.
+ **IAM role for the application** – In this pattern, this role is named `keda-identity`. The `keda-operator` role assumes this role. This role allows access to the Amazon SQS queue.
+ **IAM role for the KEDA operator** – In this pattern, this role is named `keda-operator`. The KEDA operator uses this role to make the required AWS API calls. This role has permissions to assume the `keda-identity` role. Because of the trust relationship between the `keda-operator` and the `keda-identity` roles, the `keda-operator` role has Amazon SQS permissions.

Through the `TriggerAuthentication` and `ScaledObject` Kubernetes custom resources, the operator uses the `keda-identity` role to connect with an Amazon SQS queue. Based on the queue size, KEDA automatically scales the application deployment. It adds 1 pod for every 5 unread messages in the queue. In the default configuration, if there are no unread messages in the Amazon SQS queue, the application scales down to 0 pods. The KEDA operator monitors the queue at an interval that you specify.

The following image shows how you use Amazon EKS Pod Identity to provide the `keda-operator` role with secure access to the Amazon SQS queue.

![Using KEDA and Amazon EKS Pod Identity to automatically scale a Kubernetes-based application.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/56f7506d-e8d3-43e5-bec6-42267fedd0ae/images/05bdbd09-9eb8-4c0b-8c0d-efe38aecb683.png)

The diagram shows the following workflow:

1. You install the Amazon EKS Pod Identity agent in the Amazon EKS cluster.

1. You deploy KEDA operator in the KEDA namespace in the Amazon EKS cluster.

1. You create the `keda-operator` and `keda-identity` IAM roles in the target AWS account.

1. You establish a trust relationship between the IAM roles.

1. You deploy the application in the `security` namespace.

1. The KEDA operator polls messages in an Amazon SQS queue.

1. KEDA initiates HPA, which automatically scales the application based on the queue size.

## Tools
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-tools"></a>

**AWS services**
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [Amazon Simple Queue Service (Amazon SQS)](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.html) provides a secure, durable, and available hosted queue that helps you integrate and decouple distributed software systems and components.

**Other tools**
+ [KEDA](https://keda.sh/) is a Kubernetes-based event-driven autoscaler.

**Code repository**

The code for this pattern is available in the GitHub [Event-driven auto scaling using EKS Pod Identity and KEDA](https://github.com/aws-samples/event-driven-autoscaling-using-podidentity-and-keda/tree/main) repository.

## Best practices
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-best-practices"></a>

We recommend that you adhere to the following best practices:
+ [Amazon EKS best practices](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html)
+ [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html)
+ [Amazon SQS best practices](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-best-practices.html)

## Epics
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-epics"></a>

### Create AWS resources
<a name="create-aws-resources"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create the IAM role for the KEDA operator. | 1. Sign in to the AWS Management Console, and then open the [IAM console](https://console.aws.amazon.com/iam/).<br />2. In the navigation pane, choose **Roles**.<br />3. Choose **Create role**.<br />4. Choose the **Custom trust policy** role type.<br />5. In the **Custom trust policy** section, enter the following custom trust policy for this role:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "Service": "pods.eks.amazonaws.com"<br />            },<br />            "Action": [<br />                "sts:AssumeRole",<br />                "sts:TagSession"<br />            ]<br />        }<br />    ]<br />}</pre><br />6. On the **Add permissions** page, choose **Next**. You do not add any policies to this role.<br />7. For **Role name**, enter `keda-operator`.<br />8. Choose **Create role**. | AWS administrator |
| Create the IAM role for the sample application. | 1. In the IAM console, in the navigation pane, choose **Roles**.<br />2. Choose **Create role**.<br />3. Choose the **Custom trust policy** role type.<br />4. In the **Custom trust policy** section, enter the following custom trust policy for this role. Replace `<account number>` with your target account number:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "Service": "pods.eks.amazonaws.com",<br />                "AWS": "arn:aws:iam::<account number>:role/keda-operator"<br />            },<br />            "Action": [<br />                "sts:AssumeRole",<br />                "sts:TagSession"<br />            ]<br />        }<br />    ]<br />}</pre><br />5. On the **Add permissions** page, add the following AWS managed polices to the role:`AmazonSQSReadOnlyAccess``AWSLambdaSQSQueueExecutionRole`<br />6. Choose **Next**.<br />7. For **Role name**, enter `keda-identity`.<br />8. Choose **Create role**. | AWS administrator |
| Create an Amazon SQS queue. | 1. Open the [Amazon SQS console](https://console.aws.amazon.com/sqs/).<br />2. Choose **Create queue**.<br />3. For **Type**, choose **Standard**.<br />4. On Create queue page, for **Name**, enter `event-messages-queue`.<br />5. Choose **Create queue**. You do not change any of the default settings for this queue. | General AWS |
| Create an Amazon ECR repository. | 1. Open the [Amazon ECR console](https://console.aws.amazon.com/ecr/repositories).<br />2. Choose **Create repository**.<br />3. For **Repository name**, enter `keda-pod-identity-registry`.<br />4. Choose **Create repository**. You do not change any of the default settings for this repository. | General AWS |

### Set up the Amazon EKS cluster
<a name="set-up-the-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the Amazon EKS Pod Identity agent. | For the target Amazon EKS cluster, set up the Amazon EKS Pod Identity agent. Follow the instructions in [Set up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html#pod-id-agent-add-on-create) in the Amazon EKS documentation. | AWS DevOps |
| Deploy KEDA. | 1. Enter the following commands to deploy KEDA on the target Amazon EKS cluster:<pre># Add Helm Repo for Keda<br />helm repo add kedacore https://kedacore.github.io/charts<br /># Update Helm repo<br />helm repo update<br /># Install Keda<br />helm install keda kedacore/keda --namespace keda --create-namespace</pre><br />For more information, see [Deploying with Helm](https://keda.sh/docs/2.14/deploy/#helm) in the KEDA documentation.<br />2. After successful deployment, in the output, validate that three deployments are created for the KEDA operator. The following is a sample output:<pre>NAME                              READY   UP-TO-DATE   AVAILABLE   AGE<br />keda-admission-webhooks           1/1     1            1           89s<br />keda-operator                     1/1     1            1           89s<br />keda-operator-metrics-apiserver   1/1     1            1           89s</pre> | DevOps engineer |
| Assign the IAM role to the Kubernetes service account. | Follow the instructions in [Assign an IAM role to a Kubernetes service account](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-association.html) in the Amazon EKS documentation. Use the following values:+ For **IAM role**, enter `keda-operator`.<br />+ For **Kubernetes namespace**, enter `keda`.<br />+ For **Kubernetes service account**, enter `keda-operator`. | AWS DevOps |
| Create a namespace. | Enter the following command to create a `security` namespace in the target Amazon EKS cluster:<pre>kubectl create ns security</pre> | DevOps engineer |

### Deploy the sample application
<a name="deploy-the-sample-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the application files. | Enter the following command to clone the [Event-driven auto scaling using EKS Pod Identity and KEDA repository](https://github.com/aws-samples/event-driven-autoscaling-using-podidentity-and-keda/tree/main) from GitHub:<pre>git clone https://github.com/aws-samples/event-driven-autoscaling-using-podidentity-and-keda.git</pre> | DevOps engineer |
| Build the Docker image. | 1. Enter the following command to navigate into the cloned repository:<pre>cd event-driven-autoscaling-using-podidentity-and-keda</pre><br />2. Enter the following command to build the Docker image for the sample application:<pre>docker build -t keda-pod-identity-registry .</pre> | DevOps engineer |
| Push the Docker image to Amazon ECR. | 1. In the terminal where you built the Docker image, enter the following command to log in to Amazon ECR. Replace `<AWS_REGION>` and `<AWS_ACCOUNT_ID>` with values from your AWS environment:<pre>aws ecr get-login-password \<br />   --region <AWS_REGION> | docker login \<br />   --username AWS \<br />   --password-stdin <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com</pre><br />2. Enter the following command to tag the image. Replace `<AWS_REGION>` and `<AWS_ACCOUNT_ID>` with values from your AWS environment:<br />`docker tag keda-pod-identity-registry:latest <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/keda-pod-identity-registry:latest`<br />3. Enter the following command to push the image to Amazon ECR. Replace `<AWS_REGION>` and `<AWS_ACCOUNT_ID>` with values from your AWS environment:<br />`docker push <AWS_ACCOUNT_ID>.dkr.ecr.<AWS_REGION>.amazonaws.com/keda-pod-identity-registry:latest`You can find push commands by navigating to the Amazon ECR repository page and then choosing **View push commands**. | DevOps engineer |
| Deploy the sample application. | 1. In the cloned repository, open the **deploy.yaml** file.<br />2. Replace `<AWS_ACCOUNT_ID>` and `<AWS_REGION>` with values from your environment.<br />3. Save and close the **deploy.yaml** file.<br />4. Enter the following command to deploy the sample application on the target Amazon EKS cluster:<pre>kubectl apply -f deploy.yaml</pre><br />This command creates a deployment and service account in the cluster. | DevOps engineer |
| Assign the IAM role to the application service account. | Do one of the following to associate the `keda-identity` IAM role with the service account for the sample application:+ Follow the instructions in [Assign an IAM role to a Kubernetes service account](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-association.html) in the Amazon EKS documentation. Use the following values:For **IAM role**, enter `keda-identity`.For **Kubernetes namespace**, enter `security`.For **Kubernetes service account**, enter `my-sqs-read-msgs`.<br />+ Enter the following AWS CLI command. Replace `<cluster-name>` with the name of the target Amazon EKS cluster, and replace `<role-ARN>` with the Amazon Resource Name (ARN) of the `keda-identity` role:<pre>aws eks create-pod-identity-association \<br />   --cluster-name <cluster-name> \<br />   --role-arn <role-ARN> \<br />   --namespace security \<br />   --service-account my-sqs-read-msgs</pre> | DevOps engineer |
| Deploy `ScaledObject` and `TriggerAuthentication`. | 1. In the cloned repository, open the **keda.yaml** file.<br />2. Replace `{{AWS_ACCOUNT_ID}}` with the ID of your target AWS account.<br />3. Replace `{{AWS_REGION}}` with your target AWS Region.<br />4. (Optional) In lines 21–24, update the parameters for the `ScaledObject` scaling policy. See the following for more information about these parameters:[pollingInterval](https://keda.sh/docs/2.16/reference/scaledobject-spec/#pollinginterval)[cooldownPeriod](https://keda.sh/docs/2.16/reference/scaledobject-spec/#cooldownperiod)[idleReplicaCount](https://keda.sh/docs/2.16/reference/scaledobject-spec/#idlereplicacount)[minReplicaCount](https://keda.sh/docs/2.16/reference/scaledobject-spec/#minreplicacount)<br />5. Save and close the **keda.yaml** file.<br />6. Enter the following command to deploy the `ScaledObject` and `TriggerAuthentication` resources:<pre>kubectl -n security apply -f keda.yaml</pre> | DevOps engineer |

### Test auto scaling
<a name="test-auto-scaling"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Send messages to the Amazon SQS queue. | 1. Enter the following command to navigate into the cloned repository:<pre>cd event-driven-autoscaling-using-podidentity-and-keda</pre><br />2. Enter the following command to send test messages to the Amazon SQS queue:<pre>python sqs_send_msg.py</pre><br />The **sqs\_send\_msg.py** script acts as an application that generates messages for testing auto scaling.If you're running Python 3, enter `python3 sqs_send_msg.py`. | DevOps engineer |
| Monitor the application pods. | 1. In different terminal, enter the following command to monitor the pods:<pre>kubectl -n security get po </pre><br />2. For every 5 unread messages in the Amazon SQS queue, KEDA adds one pod. In the output of the previous command, confirm that new pods are being added. The following is a sample output:<pre>kubectl -n security get po<br />NAME                      READY   STATUS    RESTARTS   AGE<br />q-read-797f4c7589-2bj76   1/1     Running   0          2s<br />q-read-797f4c7589-4zxph   1/1     Running   0          49s<br />q-read-797f4c7589-cg9dt   1/1     Running   0          18s<br />q-read-797f4c7589-slc69   1/1     Running   0          33s</pre><br />3. When you are finished testing, in the original terminal, enter CTRL \+ C (Windows) or CMD \+ C (macOS). This stops the **python sqs\_send\_msg.py** script. | DevOps engineer |

## Troubleshooting
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| The KEDA operator cannot scale the application. | Enter the following command to check the logs of the `keda-operator` IAM role:<pre>kubectl logs -n keda -l app=keda-operator -c keda-operator</pre><br /> <br />If there is an `HTTP 403` response code, then the application and the KEDA scaler do not have sufficient permissions to access the Amazon SQS queue. Complete the following steps:1. Check the IAM policies and statements for the `keda-identity` role to confirm that that queue read access is granted.<br />2. Validate the trust relationship between the IAM roles. The following is an example:<pre>{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Effect": "Allow",<br />            "Principal": {<br />                "Service": "pods.eks.amazonaws.com"<br />            },<br />            "Action": [<br />                "sts:AssumeRole",<br />                "sts:TagSession"<br />            ]<br />        }<br />    ]<br />}</pre><br />If there is an `Assume-Role` error, then an [Amazon EKS node IAM role](https://docs.aws.amazon.com/eks/latest/userguide/create-node-role.html) is unable to assume the IAM role that is defined for `TriggerAuthentication`. Complete the following steps:1. Enter the following command to delete the `keda-operator` pod and create a new one:<pre>kubectl delete pod keda-operator-<alphenumeric-value> --namespace keda</pre><br />2. Enter the following command to check the identity that the pod assumes:<pre>kubectl describe pod <keda-operator-pod-name> --namespace keda</pre><br />3. When the pod successfully restarts, confirm that the following two variables are added to the pod description:`AWS_CONTAINER_CREDENTIALS_FULL_URI``AWS_CONTAINER_AUTHORIZATION_TOKEN_FILE` |

## Related resources
<a name="event-driven-auto-scaling-with-eks-pod-identity-and-keda-resources"></a>
+ [Set up the Amazon EKS Pod Identity Agent](https://docs.aws.amazon.com/eks/latest/userguide/pod-id-agent-setup.html) (Amazon EKS documentation)
+ [Deploying KEDA](https://keda.sh/docs/2.14/deploy/) (KEDA documentation)
+ [ScaledObject specification](https://keda.sh/docs/2.16/reference/scaledobject-spec/) (KEDA documentation)
+ [Authentication with TriggerAuthentication](https://keda.sh/docs/2.14/concepts/authentication/) (KEDA documentation)

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters.html
---

# Deploy workloads from Azure DevOps pipelines to private Amazon EKS clusters
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters"></a>

*Mahendra Revanasiddappa, Amazon Web Services*

## Summary
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-summary"></a>

This pattern demonstrates how to implement continuous integration and continuous delivery (CI/CD) from Azure DevOps pipelines to private Amazon Elastic Kubernetes Service (Amazon EKS) clusters. It addresses a critical challenge faced by organizations that are enhancing their security posture by transitioning to private API server endpoints for their Amazon EKS clusters.

A public endpoint exposes the Kubernetes API server directly to the internet, creating a larger attack surface that malicious actors could potentially target. By switching to a private endpoint, access to the cluster's control plane is restricted to within the customer's virtual private cloud (VPC).

Although transitioning an Amazon EKS cluster to a private API endpoint significantly enhances security, it introduces connectivity challenges for external CI/CD platforms like Azure DevOps. The private endpoint is only accessible from within the cluster's VPC or peered networks. Therefore, standard Microsoft-hosted Azure DevOps agents, operating outside the AWS private network, can’t reach the Kubernetes API server directly. This breaks typical deployment workflows that rely on tools like kubectl or Helm running on these agents because they fail to establish a connection to the cluster.

To overcome this problem, this pattern showcases an efficient approach by using self-hosted Azure DevOps agents within private Amazon EKS clusters. This solution offers superior cost optimization, operational efficiency, and scalability while preserving security requirements. This approach particularly benefits enterprises seeking to streamline their multi-cloud DevOps processes without compromising on performance or security.

## Prerequisites and limitations
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ AWS Command Line Interface (AWS CLI) version 2.13.17 or later, [installed.](https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html)
+ kubectl version 1.25.1 or later, [installed.](https://kubernetes.io/docs/tasks/tools/)
+ A private Amazon EKS cluster version 1.24 or later [created](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html), with permissions to create namespaces, secrets, and deployments[.](https://docs.aws.amazon.com/eks/latest/userguide/create-cluster.html)
+ Worker nodes in an Amazon EKS cluster with outbound connectivity to the internet so that the Azure DevOps agent running on them can connect to Azure DevOps agent pool.
+ GitHub account [created](https://github.com/signup).
+ An Azure DevOps project with access to configure service connections, which are authenticated connections between Azure Pipelines and external or remote services, [created](https://learn.microsoft.com/en-us/azure/devops/user-guide/sign-up-invite-teammates?view=azure-devops&tabs=microsoft-account).
+ The AWS Toolkit for Azure DevOps version 1.15 or later installed for the Azure DevOps project described in the previous point. For installation instructions, see [AWS Toolkit for Azure DevOps](https://marketplace.visualstudio.com/items?itemName=AmazonWebServices.aws-vsts-tools) in Visual Studio Marketplace.

**Limitations**
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS Services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-architecture"></a>

This pattern creates the following:
+ **Amazon ECR repository** - The Amazon Elastic Container Registry (Amazon ECR) repository stores the Docker image with the Azure DevOps agent and the sample app that is deployed.
+ **Azure DevOps agent pool** - An Azure DevOps self-hosted agent pool registers the agent running on the private Amazon EKS cluster.
+ **IAM role** - An AWS Identity and Access Management (IAM) role for the Azure service connection to provide required access to the agent that’s running on a private Amazon EKS cluster.
+ **Azure DevOps service connection** - A service connection in an Azure DevOps account to use the IAM role that provides the required access for the pipeline jobs to access AWS services.

The following diagram shows the architecture of deploying a self-hosted Azure DevOps agent on a private Amazon EKS cluster and deploying a sample application on the same cluster.

![Deployment of self-hosted Azure DevOps agent and sample application on private Amazon EKS cluster.](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/a965834f-a1e2-4679-bd8c-15eed4f57b55/images/ee22bd3e-311c-46e0-8024-9b7e7752080a.png)

The diagram shows the following workflow:

1. Deploy a self-hosted Azure DevOps agent as a deployment inside an Amazon EKS cluster.

1. An Azure DevOps agent connects to the agent pool on an Azure DevOps account using a personal access token (PAT) for authentication.

1. Azure Pipelines configures a pipeline to deploy by using code from a GitHub repository.

1. The pipeline runs on the agent from the agent pool that was configured in the pipeline configuration. The Azure DevOps agent gets the job information of the pipeline by constantly polling to the Azure DevOps account.

1. The Azure DevOps agent builds a Docker image as part of the pipeline job and pushes the image to the Amazon ECR repository.

1. The Azure DevOps agent deploys the sample application on a private Amazon EKS cluster in a namespace called `webapp`.

## Tools
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-tools"></a>

**Tools**
+ [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) is a managed container image registry service that’s secure, scalable, and reliable.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.

**Other tools**
+ [Docker](https://www.docker.com/) is a set of platform as a service (PaaS) products that use virtualization at the operating-system level to deliver software in containers.
+ [kubectl](https://kubernetes.io/docs/tasks/tools/) is a command-line interface that helps you run commands against Kubernetes clusters.

**Code repository**
+ The code for this pattern is available in the GitHub [deploy-kubernetes-resources-to-amazon-eks-using-azure-devops](https://github.com/aws-samples/deploy-kubernetes-resources-to-amazon-eks-using-azure-devops) repository.

## Best practices
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-best-practices"></a>
+ For Amazon EKS, see the [Amazon EKS Best Practices Guide](https://docs.aws.amazon.com/eks/latest/best-practices/introduction.html).
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-epics"></a>

### Create a service connection
<a name="create-a-service-connection"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Find the Azure DevOps organization GUID. | Sign in to your Azure DevOps account, and then use the following URL to find the organization GUID: `https://dev.azure.com/{DevOps_Org_ID}/_apis/projectCollections?api-version=6.0` In the URL, replace `{DevOps_org_ID}` with your Azure DevOps organization ID. | AWS DevOps |
| Configure an IdP in the AWS account. | To configure an Identity provider (IdP) in the AWS account for an Azure service connection, use the following steps:1. Sign in to the AWS Management Console, and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).<br />2. In the left pane, choose **Identity providers**.<br />3. Choose **Add Provider**.<br />4. Choose **OpenID Connect** as the **Provider type**.<br />5. For **Provider URL**, enter the Azure DevOps issuer URL. Each tenant of Azure DevOps has a unique `OrganizationGUID` that typically uses the following format: `https://vstoken.dev.azure.com/{OrganizationGUID}` Replace `{OrganizationGUID}` with your Azure DevOps organization ID.<br />6. For **Audience**, enter **api://AzureADTokenExchange**. This is a fixed value for Azure DevOps.<br />7. Choose **Add Provider**.<br />8. Take note of the ARN of the newly created provider for your use in the next task.<br />For more details, see [How to federate into AWS from Azure DevOps using OpenID Connect](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-federate-into-aws-from-azure-devops-using-openid-connect/). | AWS DevOps |
| Create an IAM policy in the AWS account. | To create an IAM policy to provide the required permissions to the IAM role used by the Azure DevOps pipeline, use the following steps:1. In the IAM console, in the left pane, choose **Policies**.<br />2. Choose **Create Policy**.<br />3. For **Specify Permissions**, in **Policy editor**, select **JSON**. Replace the default JSON policy with the following JSON:<pre><br />{<br />    "Version": "2012-10-17",		 	 	 <br />    "Statement": [<br />        {<br />            "Sid": "Statement1",<br />            "Effect": "Allow",<br />            "Action": [<br />                "ecr:*",<br />                "eks:DescribeCluster",<br />                "eks:ListClusters"<br />            ],<br />            "Resource": "*"<br />        }<br />    ]<br />}</pre><br />4. Choose **Next.**<br />5. For **Policy name**, enter a name for the IAM policy. This pattern uses the name **ADO-policy**.<br />6. Choose **Create policy**. | AWS DevOps |
| Create an IAM role in the AWS account. | To configure an IAM role in the AWS account for the Azure service connection, use the following steps:1. In the IAM console, in the left pane, choose **Roles**.<br />2. Choose **Create role**.<br />3. For **Trusted entity type**, select **Web Identity**.<br />4. Select the correct IdP from the dropdown list. The IdP name starts with `vstoken.dev.azure.com/{OrganizationGUID}`.<br />5. In the **Audience **dropdown list, select **api://AzureADTokenExchange**.<br />6. To limit this role to only one service connection, add a condition. Under **Condition**, select **Add condition**, and for **Key**, select **vstoken.dev.azure.com/{OrganizationGUID}:sub**. In **Condition**, select **StringEquals**. For **Value**, use the following format: `sc://{OrganizationName}/{ProjectName}/{ServiceConnectionName}`. For `ServiceConnectionName`, use **aws-sc.** You will create this service connection in the next task.<br />7. Choose **Next**.<br />8. For **Add permissions**, select **ADO-policy**, which is the policy that you created in a previous task.<br />9. Choose **Next**, and for **Role name**, enter **ado-role**. For **Select Trusted Entities**, use the following trust policy:<pre>{<br />  "Version": "2012-10-17",		 	 	 <br />  "Statement": [<br />    {<br />      "Effect": "Allow",<br />      "Principal": {<br />        "Federated": "arn:aws:iam::{account_id}:oidc-provider/vstoken.dev.azure.com/{OrganizationGUID}"<br />      },<br />      "Action": "sts:AssumeRoleWithWebIdentity",<br />      "Condition": {<br />        "StringEquals": {<br />          "vstoken.dev.azure.com/{OrganizationGUID}:aud": "api://AzureADTokenExchange",<br />          "vstoken.dev.azure.com/{OrganizationGUID}:sub": "sc://{OrganizationName}/{ProjectName}/{ServiceConnectionName}"<br />        }<br />      }<br />    }<br />  ]<br />}</pre><br />In the policy, provide your information for the following placeholders:+ `{account_id}` - AWS account ID<br />+ `{OrganizationGUID}` - Azure DevOps Organization GUID<br />+ `{OrganizationName}` - Azure DevOps Organization name<br />+ `{ProjectName}` - Azure DevOps project name<br />+ `{ServiceConnectionName}` - Azure DevOps service connection name. Use **aws-sc.** You will create this service connection in the next task. | AWS DevOps |
| Create a service connection in the Azure DevOps account. | To configure an Azure service connection, use the following steps:1. In your Azure DevOps project, select **Project settings**, **Service connections**.<br />2. Choose **New service connection**, select the type of service connection as `aws`, and then select **Next**.<br />3. For **Role to Assume**, enter the arn for the IAM role **ado-role.** You created **ado-role **in the previous task *Create an IAM role in the AWS account*.<br />4. Select the **Use OIDC** checkbox.<br />5. For **Service connection name**, enter **aws-sc** in task properties.<br />6. Choose **Save**.<br />For more details, see [Create a service connection](https://learn.microsoft.com/en-us/azure/devops/pipelines/library/service-endpoints?view=azure-devops#create-a-service-connection) in the Microsoft documentation. | AWS DevOps |
| Add IAM role to Amazon EKS configuration file. | The IAM role must have the necessary permissions to perform the required operations on the Amazon EKS cluster. Because it’s a pipeline role, the IAM role must be able to manage almost all types of resources on the cluster. Therefore, the `system:masters` group permission is appropriate for this role.<br />To add the required configuration to the `aws-auth ConfigMap` within Kubernetes, use the following code:<pre>- groups:<br />  - system:masters<br />  rolearn: arn:aws:iam::{account_id}:role/ADO-role<br />  username: ADO-role</pre><br />Replace `{account_id}` with your AWS account ID.<br />For more information, see [How Amazon EKS works with IAM](https://docs.aws.amazon.com/eks/latest/userguide/security-iam-service-with-iam.html#security-iam-service-with-iam-roles) in the Amazon EKS documentation. | AWS DevOps |

### Create an agent pool
<a name="create-an-agent-pool"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a self-hosted agent pool. | To configure a self-hosted agent pool in the Azure DevOps account, use the following steps:1. Sign in to your Azure DevOps account organization.<br />2. Choose **Azure DevOps Organization**.<br />3. Choose your Azure DevOps project.<br />4. Choose **Project settings**.<br />5. Choose **Agent pools**.<br />6. Choose **Add pool**.<br />7. Select **Self-hosted**.<br />8. For **Name**, enter **eks-agent**.<br />9. Select the **Grant access permission to all pipelines** checkbox.<br />10. Choose **Create**.<br />For more details, see [Create and manage agent pools](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/pools-queues?view=azure-devops&tabs=yaml%2Cbrowser) in the Microsoft documentation. |  |

### Build Azure DevOps agent image and push to Amazon ECR
<a name="build-azure-devops-agent-image-and-push-to-ecr"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create an Amazon ECR repository. | The Docker images that are used to deploy the Azure DevOps agent and sample application (`webapp`) on the private Amazon EKS cluster must be stored in an Amazon ECR repository. To create an Amazon ECR repository, use the following steps:1. Open the Amazon ECR console at [https://console.aws.amazon.com/ecr/repositories](https://console.aws.amazon.com/ecr/repositories).<br />2. From the navigation bar, choose the **AWS Region** to create your repository in.<br />3. On the **Repositories** page, choose **Private repositories**, and then choose **Create repository**.<br />4. For **Repository name**, enter **webapp**. For the sample application in this pattern to work, the Amazon ECR repository name must use **webapp**. If you use a different name for the repository, see [Troubleshooting](#deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-troubleshooting). <br />For more details, see [Creating an Amazon ECR private repository to store images](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-create.html) in the Amazon ECR documentation. | AWS DevOps |
| Create a Dockerfile to build the Azure DevOps agent. | Create a Dockerfile to build the Docker image that has the Azure DevOps agent installed. Store the following content in a file named `Dockerfile`:<pre><br />FROM ubuntu:22.04 <br />ENV TARGETARCH="linux-x64"<br />RUN apt update && apt upgrade -y && apt install -y curl git jq libicu70 unzip wget<br /><br />RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"<br />RUN unzip awscliv2.zip<br />RUN ./aws/install<br />RUN rm -rf aws awscliv2.zip<br /><br />RUN curl -sSL https://get.docker.com/ | sh<br /><br />RUN curl -sL https://aka.ms/InstallAzureCLIDeb | bash<br />RUN mkdir -p azp <br />WORKDIR /azp/<br /><br />COPY ./start.sh ./ <br />RUN chmod +x ./start.sh<br /><br />RUN useradd -m -d /home/agent agent <br />RUN chown -R agent:agent /azp /home/agent<br />RUN groupadd -f docker <br />RUN usermod -aG docker agent<br />USER agent<br /><br />ENTRYPOINT [ "./start.sh" ]</pre> | AWS DevOps |
| Create script for the Azure DevOps agent. | To create the `start.sh` script, use the following steps:1. Go to the procedure [Create and build the Dockerfile](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/docker?view=azure-devops#create-and-build-the-dockerfile-1) in the Microsoft documentation, and scroll to **step 5. Save the following content to **`~/azp-agent-in-docker/start.sh`**, making sure to use Unix-style (LF) line endings**.<br />2. Copy the script’s content, and save it in a file named `start.sh` in the same directory as the Dockerfile. | AWS DevOps |
| Build a Docker image with the Azure DevOps agent.  | To create a Docker image to install the Azure DevOps agent, use the Dockerfile that you created earlier to build the image. In the same directory where the Dockerfile is stored, run the following commands:<pre>aws ecr get-login-password --region region | docker login --username AWS --password-stdin aws_account_id.dkr.ecr.region.amazonaws.com<br /><br />docker build --platform linux/amd64 -t ado-agent:latest .<br /><br />docker tag ado-agent:latest aws_account_id.dkr.ecr.region.amazonaws.com/webapp:latest<br /><br />docker push aws_account_id.dkr.ecr.region.amazonaws.com/webapp:latest</pre><br />Replace `aws_account_id` and `region` with your AWS account ID and AWS Region. | AWS DevOps |

### Deploy the Azure DevOps agent to a private Amazon EKS cluster
<a name="deploy-the-azure-devops-agent-to-a-private-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Generate an Azure personal access token. | The agent running on the private Amazon EKS cluster requires a personal access token (PAT) so that it can authenticate with the Azure DevOps account. To generate a PAT, use the following steps:1. Sign in with the user account you plan to use in your Azure DevOps organization (`https://dev.azure.com/{Your_Organization}`).1. From your home page, open your user settings, and then select **Personal access tokens**.<br />2. Choose **New Token.**<br />3. Enter the **Name **for the token.<br />4. Choose **Show all scopes.**<br />5. For **Agent Pools**, select the **Read & manage** checkbox.<br />6. Choose **Create.**<br />7. To create a secret on the private Amazon EKS cluster, use the following configuration:<pre>apiVersion: v1<br />kind: Secret<br />metadata:<br />  name: azdevops-pat<br />  namespace: default<br />type: Opaque<br />stringData:<br />  AZP_TOKEN: <PAT Token></pre>1. Store the configuration in a file named `ado-secret.yaml`. Replace `<PAT Token>` with the personal access token that you just created. To create the secret, run the following command:<pre>kubectl create -f ado-secret.yaml</pre><br />For more details, see [Register an agent using a personal access token (PAT)](https://learn.microsoft.com/en-us/azure/devops/pipelines/agents/personal-access-token-agent-registration?view=azure-devops) in the Microsoft documentation. | AWS DevOps |
| Use the Kubernetes manifest file for agent deployment. | To deploy the Azure DevOps agent on the private Amazon EKS cluster, copy the following manifest file and store the file as `agent-deployment.yaml`: <pre>apiVersion: apps/v1<br />kind: Deployment<br />metadata:<br />  name: azure-pipelines-agent-eks<br />  labels:<br />    app: azure-pipelines-agent<br />spec:<br />  replicas: 1<br />  selector:<br />    matchLabels:<br />      app: azure-pipelines-agent<br />  template:<br />    metadata:<br />      labels:<br />        app: azure-pipelines-agent<br />    spec:<br />      containers:<br />      - name: docker<br />        image: docker:dind<br />        securityContext: <br />          privileged: true<br />        volumeMounts:<br />        - name: shared-workspace<br />          mountPath: /workspace<br />        - name: dind-storage<br />          mountPath: /var/lib/docker<br />        env:<br />        - name: DOCKER_TLS_CERTDIR<br />          value: ""<br />      - name: azure-pipelines-agent<br />        image: aws_account_id.dkr.ecr.region.amazonaws.com/webapp:latest<br />        env:<br />        - name: AZP_URL<br />          value: "<Azure account URL>"<br />        - name: AZP_POOL<br />          value: "eks-agent"<br />        - name: AZP_TOKEN<br />          valueFrom:<br />            secretKeyRef:<br />              name: azdevops-pat<br />              key: AZP_TOKEN<br />        - name: AZP_AGENT_NAME<br />          valueFrom:<br />            fieldRef:<br />              fieldPath: metadata.name<br />        - name: DOCKER_HOST<br />          value: tcp://localhost:2375<br />        volumeMounts:<br />        - mountPath: /workspace<br />          name: shared-workspace<br />      volumes:<br />      - name: dind-storage<br />        emptyDir: {}<br />      - name: shared-workspace<br />        emptyDir: {}</pre><br />Replace `aws_account_id` and `<Azure account URL>` with your AWS account ID and Azure DevOps account URL. | AWS DevOps |
| Deploy the agent on the private Amazon EKS cluster. | To deploy the Azure Devops agent on the private Amazon EKS cluster, use the following command:<pre>kubectl create -f agent-deployment.tf</pre> | AWS DevOps |
| Verify the agent is running. | To verify that the Azure DevOps agent is running, use the following command:<pre>kubectl get deploy azure-pipelines-agent-eks<br /></pre><br />The expected output should be similar to the following:<pre><br />NAME                        READY   UP-TO-DATE   AVAILABLE   AGE<br />azure-pipelines-agent-eks   1/1     1            1           58s</pre><br />Make sure that the `READY `column shows `1/1`. | AWS DevOps |
| Verify the agent is registered with the Azure DevOps agent pool. | To verify that the agent is deployed on the private Amazon EKS cluster and is registered with the agent pool `eks-agent`, use the following steps:1. Sign in to your Azure DevOps organization (`https://dev.azure.com/{Your_Organization}`).<br />2. Choose **Project settings**.<br />3. Choose **Agent pools**. <br />4. Select the **eks-agent** pool, and then check the **Agents **tab.<br />You should see one agent listed with a **Status** of **Online**, and the name of the agent should start with **azure-pipelines-agent-eks-\***. | AWS DevOps |

### Deploy sample application
<a name="deploy-sample-application"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Fork the sample application repository to your GitHub account.  | Fork the following AWS Samples repository to your GitHub account:<br />[https://github.com/aws-samples/deploy-kubernetes-resources-to-amazon-eks-using-azure-devops](https://github.com/aws-samples/deploy-kubernetes-resources-to-amazon-eks-using-azure-devops) | AWS DevOps |
| Create a pipeline. | To create a pipeline in your Azure DevOps account, use the following steps:1. Sign in with the user account you plan to use in your Azure DevOps organization (`https://dev.azure.com/{Your_Organization}`).<br />2. Navigate to your project and pipelines console.<br />3. Choose **New Pipeline.**<br />4. For **Where is your code**, choose **GitHub.**<br />5. Provide the credentials required for the pipeline to connect to your GitHub account<br />6. Select the repository **deploy-kubernetes-resources-to-amazon-eks-using-azure-devops**.<br />7. For **Configure your pipeline, **select **Existing Azure Pipelines YAML file**.<br />8. For **Select an existing YAML file, **select **main** for **Branch **and **azure\_pipelines.yaml** for** path**. <br />9. Choose **Continue**.<br />10. For **Review your pipeline YAML**, replace the input parameter values for `awsRegion` and `awsEKSClusterName` with your information:<pre>pool:<br />  name: eks-agent<br />#pool: self-hosted # If you are running self-hosted Azure DevOps Agents<br /><br />stages:<br /># Refering the pipeline template, input parameter that are not specified will be added with defaults<br />- template: ./pipeline_templates/main_template.yaml<br />  parameters:<br />    serviceConnectionName: aws-sc<br />    awsRegion: <your region><br />    awsEKSClusterName: <name of your EKS cluster><br />    projectName: webapp<br /></pre>1. Choose **RUN**. | AWS DevOps |
| Verify that the sample application deployed. | After the pipeline completes, verify the successful deployment of the sample application by checking both the Amazon ECR repository and the Amazon EKS cluster.<br />To verify artifacts in the Amazon ECR repository, use the following steps:1. Navigate to the `webapp` Amazon ECR repository.<br />2. Confirm the presence of the following new artifacts:+ Docker image – `<date>.<build_number>-image`<br />+ Helm chart – `<date>.<build_number>-helm`<br />For example, `20250501.1-image` and `20250501.1-helm`.<br />To verify deployment on the private Amazon EKS cluster in the namespace `webapp`, use the following command:<pre>kubectl get deploy -n webapp </pre><br />The expected output is as follows:<pre><br />NAME     READY   UP-TO-DATE   AVAILABLE<br />webapp   1/1     1            1           </pre><br />Note: If this is your first pipeline run, you might need to authorize the service connection and agent pool. Look for permission requests in the Azure DevOps pipeline interface, and approve them to proceed. | AWS DevOps |

## Troubleshooting
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| Pipeline fails when Amazon ECR repository name doesn’t match `webapp` | The sample application expects the Amazon ECR repository name to match the `projectName: webapp` parameter in `azure_pipeline.yml`.<br />To resolve this issue, rename your Amazon ECR repository to `webapp`, or update the following:+ Rename the `webapp` directory in your forked GitHub repository to match your Amazon ECR repository name.<br />+ Update the `projectName` parameter in `azure_pipeline.yml` to match your Amazon ECR repository name. |
| Error: Kubernetes cluster unreachable: the server has asked for the client to provide credentials | If you encounter this error in the "Pull and Deploy Helm Chart" step in your Azure pipeline, the root cause typically stems from an incorrect IAM role configuration in your Amazon EKS cluster's `aws-auth ConfigMap`.<br />To resolve this issue, check the following:+ Verify your `aws-auth ConfigMap` configuration.<br />+ Check your Amazon EKS cluster's authentication settings: Open the Amazon EKS console, **Cluster details**, **Access configuration**. Make sure that **Authentication mode** is set to **EKS API and ConfigMap** (not just **EKS API**). |

## Related resources
<a name="deploy-workloads-from-azure-devops-pipelines-to-private-amazon-eks-clusters-resources"></a>

**AWS Blogs**
+ [How to federate into AWS from Azure DevOps using OpenID Connect](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-federate-into-aws-from-azure-devops-using-openid-connect/)

**AWS services documentation**
+ [Amazon ECR](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html)
+ [Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)

**Microsoft documentation**
+ [What is Azure DevOps?](https://learn.microsoft.com/en-us/azure/devops/user-guide/what-is-azure-devops?view=azure-devops)
+ [What is Azure Pipelines?](https://learn.microsoft.com/en-us/azure/devops/pipelines/get-started/what-is-azure-pipelines?view=azure-devops)

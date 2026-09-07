---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks.html
---

# Use Amazon Bedrock agents to automate creation of access entry controls in Amazon EKS through text-based prompts
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks"></a>

*Keshav Ganesh and Sudhanshu Saurav, Amazon Web Services*

## Summary
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-summary"></a>

Organizations face challenges in managing access controls and resource provisioning when multiple teams need to work with a shared Amazon Elastic Kubernetes Service (Amazon EKS) cluster. A managed Kubernetes service such as Amazon EKS has simplified cluster operations. However, the administrative overhead of managing team access and resource permissions remains complex and time-consuming.

This pattern shows how Amazon Bedrock agents can help you automate Amazon EKS cluster access management. This automation allows development teams to focus on their core application development rather than dealing with access control setup and management. You can customize an Amazon Bedrock agent to perform actions for a wide variety of tasks through simple natural language prompts.

By using AWS Lambda functions as action groups, an Amazon Bedrock agent can handle tasks such as creating user access entries and managing access policies. In addition, an Amazon Bedrock agent can configure pod identity associations that allow access to AWS Identity and Access Management (IAM) resources for the pods running in the cluster. Using this solution, organizations can streamline their Amazon EKS cluster administration with simple text-based prompts, reduce manual overhead, and improve overall development efficiency.

## Prerequisites and limitations
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-prereqs"></a>

**Prerequisites**
+ An active AWS account.
+ Established IAM [roles and permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/security_iam_id-based-policy-examples.html) for the deployment process. This includes permissions to access Amazon Bedrock foundation models (FM), create Lambda functions, and any other required resources across the target AWS accounts.
+ [Access enabled](https://docs.aws.amazon.com/bedrock/latest/userguide/model-access.html) in the active AWS account to these Amazon Bedrock FMs: Amazon Titan Text Embeddings V2 and Anthropic Claude 3 Haiku.
+ AWS Command Line Interface (AWS CLI) version 2.9.11 or later, [installed](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-getting-started.html) and [configured](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-configure.html).
+ eksctl 0.194.0 or later, [installed](https://eksctl.io/installation/).

**Limitations**
+ Training and documentation might be required to help ensure smooth adoption and effective use of these techniques. Using Amazon Bedrock, Amazon EKS, Lambda, Amazon OpenSearch Service, and [OpenAPI](https://www.openapis.org/what-is-openapi) involve a significant learning curve for developers and DevOps teams.
+ Some AWS services aren’t available in all AWS Regions. For Region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/). For specific endpoints, see [Service endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/aws-service-information.html), and choose the link for the service.

## Architecture
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-architecture"></a>

The following diagram shows the workflow and architecture components for this pattern.

![Workflow and components to create access controls in Amazon EKS with Amazon Bedrock agents.](https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/2c52b1ba-bbad-4a46-ab1e-10e69a0a66e7/images/c7981a86-f734-4c07-a2f7-63ad38b66ab6.png)

This solution performs the following steps:

1. The user interacts with the Amazon Bedrock agent by submitting a prompt or query that serves as input for the agent to process and take action.

1. Based on the prompt, the Amazon Bedrock agent checks the OpenAPI schema to identify the correct API to target. If the Amazon Bedrock agent finds the correct API call, the request goes to the action group that is associated with the Lambda function that implements these actions.

1. If a relevant API isn’t found, the Amazon Bedrock agent queries the OpenSearch collection. The OpenSearch collection uses indexed knowledge base content that is sourced from the Amazon S3 bucket that contains the *Amazon EKS User Guide*.

1. The OpenSearch collection returns relevant contextual information to the Amazon Bedrock agent.

1. For actionable requests (those that match an API operation), the Amazon Bedrock agent executes within a virtual private cloud (VPC) and triggers the Lambda function.

1. The Lambda function performs an action that’s based on the user’s input inside the Amazon EKS cluster.

1. The Amazon S3 bucket for the Lambda code stores the artifact that has the code and logic written for the Lambda function.

## Tools
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-tools"></a>

**AWS services**
+ [Amazon Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/what-is-bedrock.html) is a fully managed service that makes high-performing foundation models (FMs) from leading AI startups and Amazon available for your use through a unified API.
+ [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) helps you set up AWS resources, provision them quickly and consistently, and manage them throughout their lifecycle across AWS accounts and AWS Regions.
+ [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/getting-started.html) helps you run Kubernetes on AWS without needing to install or maintain your own Kubernetes control plane or nodes.
+ [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWS resources by controlling who is authenticated and authorized to use them.
+ [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) is a compute service that helps you run code without needing to provision or manage servers. It runs your code only when needed and scales automatically, so you pay only for the compute time that you use.
+ [Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/what-is.html) is a managed service that helps you deploy, operate, and scale OpenSearch clusters in the AWS Cloud. Its collections feature helps you to organize your data and build comprehensive knowledge bases that AI assistants such as Amazon Bedrock agents can use.
+ [Amazon Simple Storage Service (Amazon S3)](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data.

**Other tools**
+ [eksctl](https://docs.aws.amazon.com/eks/latest/userguide/getting-started-eksctl.html) is a command-line utility for creating and managing Kubernetes clusters on Amazon EKS.

**Code repository**

The code for this pattern is available in the GitHub [eks-access-controls-bedrock-agent](https://github.com/aws-samples/eks-access-controls-bedrock-agent.git) repository.

## Best practices
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-best-practices"></a>
+ Maintain the highest possible security when implementing this pattern. Make sure that the Amazon EKS cluster is private, has limited access permissions, and all the resources are inside a virtual private cloud (VPC). For additional information, see [Best practices for security](https://docs.aws.amazon.com/eks/latest/best-practices/security.html) in the Amazon EKS documentation.
+ Use AWS KMS [customer managed keys](https://docs.aws.amazon.com/kms/latest/developerguide/concepts.html) wherever possible, and grant limited access permissions to them.
+ Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see [Grant least privilege](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#grant-least-priv) and [Security best practices](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) in the IAM documentation.

## Epics
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-epics"></a>

### Set up the environment
<a name="set-up-the-environment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clone the repository. | To clone this pattern’s repository, run the following command in your local workstation:<pre>git clone https://github.com/aws-samples/eks-access-controls-bedrock-agent.git</pre> | AWS DevOps |
| Get the AWS account ID. | To get the AWS account ID, use the following steps:1. Open a shell in the root folder of the cloned repo, `eks-access-controls-bedrock-agent`.<br />2. To get your AWS account ID, navigate to the cloned directory and run the following command:<pre>AWS_ACCOUNT=$(aws sts get-caller-identity --query "Account" --output text)</pre><br />This command stores your AWS account ID in the `AWS_ACCOUNT` variable. | AWS DevOps |
| Create the S3 bucket for Lambda code. | To implement this solution, you must create three Amazon S3 buckets that serve different purposes, as shown in the [architecture](#using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-architecture) diagram. The S3 buckets are for Lambda code, a knowledge base, and OpenAPI schema.<br />To create the Lambda code bucket, use the following steps:1. To create an S3 bucket for Lambda code, run the following command:<pre>aws s3 mb s3://bedrock-agent-lambda-artifacts-${AWS_ACCOUNT} --region us-east-1</pre><br />2. To install the Lambda code dependency, run the following command:<pre>cd eks-lambda<br />npm install<br />tsc<br />cd .. && cd opensearch-lambda<br />npm install<br />tsc<br />cd ..</pre><br />3. To package the code and upload it to the S3 bucket for Lambda, run the following command:<pre>aws cloudformation package \<br /> --template-file eks-access-controls.yaml \<br /> --s3-bucket bedrock-agent-lambda-artifacts-${AWS_ACCOUNT} \<br /> --output-template-file eks-access-controls-template.yaml \<br /> --region us-east-1</pre><br />The package command creates a new CloudFormation template (`eks-access-controls-template.yaml`) that contains:+ References to the Lambda function code stored in your S3 bucket.<br />+ Definitions for all required AWS infrastructure including VPC, subnets, Amazon Bedrock agent, and OpenSearch collection. You can use this template to deploy the complete solution by using CloudFormation. | AWS DevOps |
| Create the S3 bucket for the knowledge base. | To create the Amazon S3 bucket for the knowledge base, use the following steps:1. To create the Amazon S3 bucket for the knowledge base, run the following command:<pre>aws s3 mb s3://eks-knowledge-base-${AWS_ACCOUNT} --region us-east-1</pre><br />2. To download the *Amazon EKS User Guide* and store it in a directory, run the following commands:<pre>mkdir dataSource <br />cd dataSource <br />curl https://docs.aws.amazon.com/pdfs/eks/latest/userguide/eks-ug.pdf -o eks-user-guide.pdf</pre><br />3. To upload the user guide to the S3 bucket that you created in step 1, run the following command:<pre>aws s3 cp eks-user-guide.pdf s3://eks-knowledge-base-${AWS_ACCOUNT} \<br />--region us-east-1 \</pre><br />4. To return to the root directory, run the following command:<pre>cd ..</pre> | AWS DevOps |
| Create the S3 bucket for the OpenAPI schema. | To create the Amazon S3 bucket for the OpenAPI schema, use the following steps:1. To create the S3 bucket, run the following command: <pre>aws s3 mb s3://eks-openapi-schema-${AWS_ACCOUNT} --region us-east-1</pre><br />2. To upload the OpenAPI schema to the S3 bucket, run the following command:<pre>aws s3 cp openapi-schema.yaml s3://eks-openapi-schema-${AWS_ACCOUNT} --region us-east-1</pre> | AWS DevOps |

### Deploy the CloudFormation stack
<a name="deploy-the-cfnshort-stack"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Deploy the CloudFormation stack.  | To deploy the CloudFormation stack, use the CloudFormation template file `eks-access-controls-template.yaml` that you created earlier. For more detailed instructions, see [Create a stack from the CloudFormation console](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.html) in the CloudFormation documentation.Provisioning the OpenSearch index with the CloudFormation template takes about 10 minutes.<br />After the stack is created, make a note of the `VPC_ID` and `PRIVATE_SUBNET ID`s. | AWS DevOps |
| Create the Amazon EKS cluster.  | To create the Amazon EKS cluster inside the VPC, use the following steps:1. Create a copy of the `eks-config.yaml` configuration file, and name the copy as `eks-deploy.yaml`.<br />2. Open `eks-deploy.yaml` in a text editor. Then, replace the following placeholder values with values from the deployed stack: `VPC_ID`, `PRIVATE_SUBNET1`, and `PRIVATE_SUBNET2`<br />3. To create the cluster by using the eksctl utility, run the following command:<pre>eksctl create cluster -f eks-deploy.yaml</pre>This cluster creation process can take up to 15-20 minutes to complete.<br />4. To verify that the cluster was created successfully, run the following commands:<pre>aws eks describe-cluster --name  --query "cluster.status"<br />aws eks update-kubeconfig --name  --region <br />kubectl get nodes </pre><br />The expected results are as follows:+ The cluster status is `ACTIVE`.<br />+ The command `kubectl get nodes` shows that all nodes are in `Ready` state. | AWS DevOps |

### Connect the Lambda function and the Amazon EKS cluster
<a name="connect-the-lam-function-and-the-eks-cluster"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Create a connection between the Amazon EKS cluster and the Lambda function. | To set up network and IAM permissions to allow the Lambda function to communicate with the Amazon EKS cluster, use the following steps:1. To identify the IAM role that’s attached to the Lambda function, open the AWS Management Console and locate the Lambda function named `bedrock-agent-eks-access-control`. Make a note of the Amazon Resource Name (ARN) of the IAM role.<br />2. To create an access entry in the Amazon EKS cluster for the Lambda function’s IAM role, run the following command:<pre>aws eks create-access-entry --cluster-name eks-testing-cluster --principal-arn <principal-Role-ARN></pre><br />3. To assign `AmazonEKSClusterAdminPolicy` permissions to this role, run the following command:<pre>aws eks associate-access-policy --cluster-name eks-testing-cluster --principal-arn <principal-Role-ARN> --policy-arn arn:aws:eks::aws:cluster-access-policy/AmazonEKSClusterAdminPolicy --access-scope type=cluster </pre><br />For more information, see [Associate access policies with access entries](https://docs.aws.amazon.com/eks/latest/userguide/access-policies.html) and [AmazonEKSClusterAdminPolicy](https://docs.aws.amazon.com/eks/latest/userguide/access-policy-permissions.html#access-policy-permissions-amazoneksclusteradminpolicy) in the Amazon EKS documentation.<br />4. Locate the Amazon EKS cluster’s security group. Add an inbound rule to allow incoming network traffic from the Lambda function to the Amazon EKS cluster.<br />Use the following values for the inbound rule:**Type** – HTTPS**Port range** – 443**Source** – Lambda security group<br />For more information, see [Configure security group rules](https://docs.aws.amazon.com/vpc/latest/userguide/working-with-security-group-rules.html) in the Amazon VPC documentation. | AWS DevOps |

### Test the solution
<a name="test-the-solution"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Test the Amazon Bedrock agent. | Before testing the Amazon Bedrock agent, make sure that you do the following:+ Test with non-production roles first.<br />+ Document any changes made to cluster access.<br />+ Have a plan to revert changes if needed.<br />To access the Amazon Bedrock agent, use the following steps:1. Sign in to the AWS Management Console using an [IAM role with Amazon Bedrock permissions](https://docs.aws.amazon.com/bedrock/latest/userguide/getting-started.html), and open the Amazon Bedrock console at [https://console.aws.amazon.com/bedrock/](https://console.aws.amazon.com/bedrock/).<br />2. Select **Agents** from the left navigation pane. Then, choose your configured agent in the **Agents** section.<br />3. To test the agent, try the following sample prompts in which you replace `Principal-ARN-OF-ROLE` with an actual IAM role ARN:+ To create an access entry for any IAM role that you wanted to provide access to the EKS cluster, use the following prompt: `Create an access entry in cluster eks-testing-new for a role whose principal arn is <Principal-ARN-OF-ROLE> with access policy as AmazonEKSAdminPolicy`<br />*Expected result*:The agent should confirm the access entry creation.To verify, check using the AWS Management Console or use the Amazon EKS API and run the following command: `aws eks list-access-entries --cluster-name ekscluster`<br />+ To describe the access entry that you created, use the following prompt: `Describe an access entry in cluster eks-testing-new whose principal arn is <Principal-ARN-OF-ROLE>`<br />*Expected result*:The agent should return details about the access entry.The details should match what you configured earlier for the access entry.<br />+ To delete the access entry that you created, use the following prompt: `Delete the access entry in cluster eks-testing-new whose principal arn is <Principal-ARN-OF-ROLE>`<br />*Expected result*:The agent should confirm the deletion of the access entry.To verify, check using the AWS Management Console or use the Amazon EKS API and run the following command: `aws eks list-access-entries --cluster-name ekscluster`<br />You can also ask the agent to perform actions for EKS Pod Identity associations. For more details, see [Learn how EKS Pod Identity grants pods access to AWS services](https://docs.aws.amazon.com/eks/latest/userguide/pod-identities.html) in the Amazon EKS documentation. | AWS DevOps |

### Clean up
<a name="clean-up"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | To clean up the resources that this pattern created, use the following procedure. Wait for each deletion step to complete before proceeding to the next step.This procedure will permanently delete all resources created by these stacks. Make sure that you've backed up any important data before proceeding.1. To delete the Amazon EKS cluster, run the following command:<pre>eksctl delete cluster -f eks-deploy.yaml</pre>This operation can take 15-20 minutes to complete.<br />2. To delete the Amazon S3 buckets, run the following commands:To empty the Lambda bucket:<pre>aws s3 rm s3://bedrock-agent-lambda-artifacts-${AWS_ACCOUNT} --recursive</pre>To empty the knowledge base bucket:<pre>aws s3 rm s3://eks-knowledge-base-${AWS_ACCOUNT} –recursive</pre>To empty the OpenAPI schema bucket:<pre>aws s3 rm s3://bedrock-agent-openapi-schema-${AWS_ACCOUNT} –recursive</pre>To delete the empty buckets:<pre>aws s3 rb s3://bedrock-agent-lambda-artifacts-${AWS_ACCOUNT}<br />aws s3 rb s3://eks-knowledge-base-${AWS_ACCOUNT}<br />aws s3 rb s3://bedrock-agent-openapi-schema-${AWS_ACCOUNT}</pre><br />3. To delete the CloudFormation stack, run the following command:<pre>aws cloudformation delete-stack \ --stack-name</pre><br />4. To verify deletion of the Amazon EKS cluster, run the following command:<pre>eksctl get clusters</pre><br />5. To verify deletion of the Amazon S3 buckets, run the following commands:To verify deletion of the Lambda bucket:<pre>aws s3 ls | grep "bedrock-agent-lambda-artifacts"</pre>To verify deletion of the knowledge base bucket:<pre>aws s3 ls | grep "eks-knowledge-base"</pre>To verify deletion of the OpenAPI schema bucket:<pre>aws s3 ls | grep "bedrock-agent-openapi-schema"</pre><br />6. To verify stack deletion, run the following command:<pre>aws cloudformation list-stacks \--query 'StackSummaries[?StackName==``]'</pre><br />If the stack fails to delete, see [Troubleshooting](#using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-troubleshooting). | AWS DevOps |

## Troubleshooting
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| A non-zero error code is returned during environment setup. | Verify that you’re using the correct folder when running any command to deploy this solution. For more information, see the [FIRST\_DEPLOY.md](https://github.com/aws-samples/eks-access-controls-bedrock-agent/blob/main/FIRST_DEPLOY.md) file in this pattern’s repository. |
| The Lambda function isn’t able to do the task. | Make sure that connectivity is set up correctly from the Lambda function to the Amazon EKS cluster. |
| The agent prompts don’t recognize the APIs. | Redeploy the solution. For more information, see the [RE\_DEPLOY.md](https://github.com/aws-samples/eks-access-controls-bedrock-agent/blob/main/RE_DEPLOY.md) file in this pattern’s repository. |
| The stack fails to delete. | An initial attempt to delete the stack might fail. This failure can occur because of dependency issues with the custom resource that was created for the OpenSearch collection which does the indexing for the knowledge base. To delete the stack, retry the delete operation by retaining the custom resource. |

## Related resources
<a name="using-amazon-bedrock-agents-to-automate-creation-of-access-entry-controls-in-amazon-eks-resources"></a>

**AWS Blog **
+ [A deep dive into simplified Amazon EKS access management controls](https://aws.amazon.com/blogs/containers/a-deep-dive-into-simplified-amazon-eks-access-management-controls/)

**Amazon Bedrock documentation**
+ [Automate tasks in your application using AI agents](https://docs.aws.amazon.com/bedrock/latest/userguide/agents.html)
+ [How Amazon Bedrock Agents works](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-how.html)
+ [Test and troubleshoot agent behavior](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-test.html)
+ [Use action groups to define actions for your agent to perform](https://docs.aws.amazon.com/bedrock/latest/userguide/agents-action-create.html)

**Amazon EKS documentation**
+ [Learn how access control works in Amazon EKS](https://docs.aws.amazon.com/eks/latest/userguide/cluster-auth.html)

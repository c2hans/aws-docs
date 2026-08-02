---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-eks-auto-mode-using-github-actions.html
---

# Enable Amazon EKS Auto Mode across EKS clusters by using GitHub Actions
<a name="enable-eks-auto-mode-using-github-actions"></a>

*Urbija Goswami and Anugrah Lakra, Amazon Web Services*

## Summary
<a name="enable-eks-auto-mode-using-github-actions-summary"></a>

Amazon Elastic Kubernetes Service clusters traditionally require manual management of compute resources through node groups. This creates operational overhead for:
+ Capacity planning and scaling decisions
+ Node provisioning and lifecycle management
+ Cost optimization across different workload types
+ Infrastructure maintenance and updates

Amazon EKS [Auto Mode](https://docs.aws.amazon.com/eks/latest/userguide/automode.html) automates compute resource management by dynamically provisioning and scaling nodes based on workload demands, eliminating the need for manual node group management.

However, many organizations struggle to consistently enable and manage Amazon EKS Auto Mode across their existing and new clusters. Common challenges include:
+ Complex migration processes from existing node groups
+ Risk of service disruption during transition
+ Need for careful capacity planning and testing
+ Requirement for specific [Amazon IAM](https://aws.amazon.com/iam/?trk=6a436c72-0178-4620-97ad-0220ccc59fd0&sc_channel=ps&ef_id=CjwKCAjw7vzOBhBxEiwAc7WNr57daOn9724PwXVGy7aBxG_uuEHktjCWJbcY1q1BrZBaApyi1sAb_BoCQj0QAvD_BwE:G:s&s_kwcid=AL!4422!3!795924581177!e!!g!!amazon%20iam!23523526050!193629723318&gad_campaignid=23523526050&gbraid=0AAAAADjHtp_aCwsziIR-n3ST_xwoCqAuc&gclid=CjwKCAjw7vzOBhBxEiwAc7WNr57daOn9724PwXVGy7aBxG_uuEHktjCWJbcY1q1BrZBaApyi1sAb_BoCQj0QAvD_BwE) permissions and configurations
+ Coordination across multiple teams and environments

This pattern implements a [GitHub Actions](https://docs.github.com/en/actions) workflow that enables EKS Auto Mode on EKS clusters in a specific AWS Region. Before enabling Auto Mode, the workflow creates timestamped backups of the cluster state (cluster configuration, node groups, Helm releases, and custom resources) and uploads them to an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

After enabling Auto Mode, the workflow drains and deletes old node groups, updates cluster role permissions, and cleans up previous scaling components such as Karpenter and Cluster Autoscaler. The workflow can be integrated with existing continuous integration and continuous delivery/deployment (CI/CD) pipelines.

## Prerequisites and limitations
<a name="enable-eks-auto-mode-using-github-actions-prereqs"></a>

**Prerequisites**

**1. Required **
+ A [GitHub account](https://github.com/) and your own GitHub repository to run the workflow
+ An active [AWS account](https://aws.amazon.com/account/) with administrative permissions

**2. Local tools installation**
+ [Terraform](https://developer.hashicorp.com/terraform/install) version 1.13.0 or later
+ [GitHub CLI](https://cli.github.com/) (gh), configured with appropriate credentials
+ [kubectl](https://docs.aws.amazon.com/eks/latest/userguide/install-kubectl.html) and [eksctl](https://docs.aws.amazon.com/eks/latest/eksctl/installation.html), configured for cluster management

**3. EKS Cluster Requirements**
+ Kubernetes version 1.29 or later
+ Endpoint access configuration:
  + Either it is set to public and private endpoints
  + Or Private endpoint with NAT Gateway in private subnets
+ [EKS API](https://docs.aws.amazon.com/eks/latest/userguide/grant-k8s-access.html) and [ConfigMap](https://docs.aws.amazon.com/eks/latest/userguide/auth-configmap.html) cluster access enabled (required to allow EKS to dynamically manage Auto Mode nodes and update the aws-auth ConfigMap for proper cluster authentication during migration)
+ Active [node groups or managed node pools](https://docs.aws.amazon.com/eks/latest/userguide/managed-node-groups.html)

**4. IAM OIDC Configuration Requirements**
+ IAM role and identity provider for GitHub that includes:
  + Trust policy for GitHub OIDC
  + Permissions for:
    + EKS Cluster management
    + S3 bucket access
    + IAMrole management
    + EC2 network management
+ See the [iam.tf](https://github.com/aws-samples/sample-enable-eks-auto-mode-using-github-actions/blob/main/iam.tf) code for simple setup using Terraform. The IAM role (`GitHubActionsEKSRole`) will be created when the Terraform code is applied.

**Limitations **
+ Only supports EKS clusters with Kubernetes version 1.29 and above
+ Only supports Karpenter version 1.1.0 and above
+ Region-specific implementation. Some AWS services aren't available in all AWS Regions. For region availability, see [AWS services by Region](https://aws.amazon.com/about-aws/global-infrastructure/regional-product-services/)
+ Requires cluster endpoint accessibility
+ Limited to AWS-managed node groups

## Architecture
<a name="enable-eks-auto-mode-using-github-actions-architecture"></a>

**Target technology stack **
+ [https://docs.github.com/en/actions](https://docs.github.com/en/actions)
+ [AWS IAM](https://docs.aws.amazon.com/singlesignon/latest/userguide/what-is.html)
+ [Amazon EKS](https://aws.amazon.com/eks/)
+ [Amazon S3](https://aws.amazon.com/s3/)

**Target architecture **

![](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/images/pattern-img/e1fa4e49-96a5-42ae-9886-766298664db4/images/a2c46a84-3bf5-4f1e-8216-ab29b4ba894e.png)

1. The GitHub Actions Workflow is triggered from the GitHub Repository by the user.

1. The GitHub Actions Workflow assumes an IAM role using OIDC to make the necessary changes in the AWSaccount. It also checks for the presence of the EKS Auto Node role in the account and if not present, the role is created and the necessary policies are attached.

1. A backup of the current state of the EKS cluster needing Auto Mode enabled is uploaded to an S3 bucket.

1. The cluster role of the cluster needing Auto Mode enabled is retrieved and additional permissions (AmazonEKSComputePolicy, AmazonEKSBlockStoragePolicy, AmazonEKSLoadBalancingPolicy, AmazonEKSNetworkingPolicy, AmazonEKSClusterPolicy) are added to it if not present for EKS Auto Mode. Additionally, as a pre-migration step, subnets of the clusters are updated with tags for EKS Auto Mode enablement.

1. The workflow enables the EKS Auto Mode in the EKS cluster.

1. Old node groups are identified and deleted. This is skipped if the user hasn’t given the permissions to the IAM role described in the optional setup steps below.

1. Scaling components (Karpenter and Cluster Autoscaler) are also removed if present previously.

 The GitHub Actions workflow consists of three main jobs:

1. `check-clusters`: Identifies clusters without Auto Mode enabled and updates IAM policies and subnet tags.

1. `backup-and-check`: Backs up cluster state before migration.

1. `gradual-migration` : Enables Auto Mode while gradually draining existing node groups and cleaning up old scaling components. It also does a final verification of clusters’ states after migration.

**Note**
If you need node configuration backups or plan to delete nodes/node groups during migration to EKS Auto Mode, then you can add the IAM role created using the terraform code to aws-auth ConfigMap. Without it, you can still view node group configurations.

## Tools
<a name="enable-eks-auto-mode-using-github-actions-tools"></a>

**AWS services**
+ [https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html): [AWS CLI](https://docs.aws.amazon.com/cli/latest/userguide/cli-chap-welcome.html) is an open source tool that helps you interact with AWSservices through commands in your command-line shell. In our solution, we make use of the command-line interface for AWSservices to execute EKS cluster configuration updates, IAM role updates and query cluster status throughout the automation process.
+ **Amazon EKS**: [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) helps you run Kubernetes on AWSwithout needing to install or maintain your own Kubernetes control plane or nodes. In this pattern, Amazon EKS is the target service where Auto Mode is enabled to automate compute provisioning and node scaling across clusters in a specific Region.
+ **IAM**: [IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) helps you securely manage access to your AWSresources by controlling who is authenticated and authorized to use them. In our solution, we use it to manage permissions for GitHub Actions to modify EKS cluster configurations via OIDC federation. The solution also modifies the cluster role permissions and adds a job to create EKS Node Role so that EKS Auto Mode can schedule the pending pods in new nodes that it spins up as a part of the node pools.
+ **Amazon S3: **[Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) is a cloud-based object storage service that helps you store, protect, and retrieve any amount of data. In our solution, we use an S3 bucket to store the timestamped backups of the clusters before EKS Auto Mode is enabled in them, which would help in disaster recovery.

**Other tools:**
+ **GitHub Actions**: [GitHub Actions](https://docs.github.com/en/actions) is a CI/CD platform that is used in our solution to automate the EKS Auto Mode enablement workflow. It also provides secure authentication via OIDC and manages pipeline execution across multiple clusters.
+ **HashiCorp Terraform**: [Terraform](https://developer.hashicorp.com/terraform/docs) is an infrastructure as code (IaC) tool that helps you use code to provision and manage cloud infrastructure and resources. Our solution uses Terraform to provision IAM roles and policies and to add OIDC provider configuration for secure GitHub Actions integration.

**Code repository**

The code for this pattern is available in the GitHub [EKS Auto Mode Enablement via GitHub Actions](https://github.com/aws-samples/sample-enable-eks-auto-mode-using-github-actions/tree/main) repository.

## Best practices
<a name="enable-eks-auto-mode-using-github-actions-best-practices"></a>
+ **Security**:
  + Follow the principle of least privilege and grant the minimum permissions required to perform a task. For more information, see G[rant least privilege and Security best practices in the IAM documentation.](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#grant-least-privilege.) See the [iam.tf](https://github.com/aws-samples/sample-enable-eks-auto-mode-using-github-actions/blob/main/iam.tf) file in the repository for the minimum required configuration.
  + Scope the IAM role trust policy to your specific GitHub repository and branch to prevent unauthorized workflow runs from assuming the role.
  + Enable EKS control plane logging (API server, audit, authenticator) before starting the migration so you can diagnose scheduling or authentication issues after Auto Mode is enabled.
  + Add `--sse AES256 to all aws s3 cp` commands in the [backup script](https://github.com/aws-samples/sample-enable-eks-auto-mode-using-github-actions/blob/main/scripts/backup-cluster-state.sh) to enforce server-side encryption on cluster state backups.
+ **Reliability**:
  + Test the workflow against a non-production cluster first. Verify that workloads reschedule correctly on Auto Mode nodes before migrating production clusters.
  + Verify that S3 backups completed successfully and contain valid cluster config, node group, Helm release, and custom resource data before proceeding with Auto Mode enablement.
  + After enabling Auto Mode, monitor pod scheduling events and node provisioning latency using [Amazon CloudWatch Container Insights ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/ContainerInsights.html)to detect issues early.
+ **Performance**:
  + Review Auto Mode node pool scaling patterns periodically and adjust workload resource requests and limits to avoid over-provisioning or scheduling delays.
+ **Cost**:
  + Tag EKS clusters and associated resources (IAM roles, S3 backup buckets, subnets) with environment and ownership metadata to support cost tracking and operational visibility. For more information, see [tagging AWS resources documentation](https://docs.aws.amazon.com/general/latest/gr/aws_tagging.html.). You can edit the workflow file to add custom tags during the migration process.
  + Set up AWS Cost Explorer alerts to monitor changes in compute costs after enabling Auto Mode, since Auto Mode may change instance types and scaling behavior. For more information, see Analyzing your costs with [AWS Cost Explorer documentation](https://docs.aws.amazon.com/cost-management/latest/userguide/ce-what-is.html.).
+ **Operations**:
  + Keep the workflow file and Terraform configurations in version control and document any environment-specific overrides such as region, role ARN, or S3 bucket name.

## Epics
<a name="enable-eks-auto-mode-using-github-actions-epics"></a>

### Tool SetUp
<a name="tool-setup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Configure the GitHub repository. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-eks-auto-mode-using-github-actions.html) | AWS DevOps, Cloud architect |

### (Optional) Set up an IAM role
<a name="optional-set-up-an-iam-role"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Set up IAM for backup and node group deletion | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-eks-auto-mode-using-github-actions.html)<pre>eksctl create iamidentitymapping \ --cluster $CLUSTER_NAME\ --region us-east-1 \ --arn arn:aws:iam::$ACCOUNT_ID:role/GitHubActionsEKSRole \ --group system:masters \ --username github-actions</pre>Replace the **$CLUSTER\_NAME** and **$ACCOUNT\_ID** with the appropriate values. [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-eks-auto-mode-using-github-actions.html)<pre>CLUSTERS=$(aws eks list-clusters --region $AWS_REGION --query 'clusters[]' --output text)<br /><br />CLUSTERS_NEEDING_AUTO_MODE=""<br /><br />for cluster in $CLUSTERS; do<br />    <br />    <br />    AUTO_MODE=$(aws eks describe-cluster --name $cluster --region $AWS_REGION --query 'cluster.computeConfig.enabled' --output text 2>/dev/null || echo "false")<br />    <br />    if [ "$AUTO_MODE" != "True" ]; then<br />       <br />        CLUSTERS_NEEDING_AUTO_MODE="$CLUSTERS_NEEDING_AUTO_MODE $cluster"<br />        <br />        echo " Adding role access to cluster..."<br />        eksctl create iamidentitymapping \<br />          --cluster $cluster \<br />          --region $AWS_REGION \<br />          --arn $ROLE_ARN \<br />          --group system:masters\<br />          --username github-actions || echo "  ⚠️  Role mapping may already exist"<br />        <br />        echo "  ✅ Role access configured for $cluster"<br />done</pre><br />Replace the **$AWS\_REGION** and **$ROLE\_ARN** with the specific region and the arn of the IAM role created above respectively.  | AWS DevOps, Cloud architect |

### Execute and validate
<a name="execute-and-validate"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Trigger the GitHub Actions workflow. | The workflow is triggered automatically when any changes are pushed to the feature, main, or dev branches. To manually trigger via GitHub UI: 1. Go to the repository on GitHub 2. Click on the "Actions" tab 3. Select the workflow (auto-mode-pipeline) 4. Click "Run workflow" button 5. Choose the branch and click "Run workflow"<br />The workflow handles [verification ](https://github.com/aws-samples/sample-enable-eks-auto-mode-using-github-actions/blob/22b546b05630c63e5637928ad8a4f5947ad8fb33/.github/workflows/enable-eks-auto-mode.yml#L283)after migration by querying each migrated cluster's compute configuration using the AWSCLI to confirm that EKS Auto Mode has been successfully enabled and displays the current compute settings in a table format. | AWS DevOps, Cloud architect |

### Configure multi-environment deployment
<a name="configure-multi-environment-deployment"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Implementation of multi-environment deployment. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-eks-auto-mode-using-github-actions.html) |  |

### Cleanup
<a name="cleanup"></a>

| Task | Description | Skills required |
| --- | --- | --- |
| Clean up resources. | [See the AWS documentation website for more details](http://docs.aws.amazon.com/prescriptive-guidance/latest/patterns/enable-eks-auto-mode-using-github-actions.html) | General AWS, Cloud architect |

## Troubleshooting
<a name="enable-eks-auto-mode-using-github-actions-troubleshooting"></a>

| Issue | Solution |
| --- | --- |
| **Authentication Issues**<br /><br /> | • Verify GitHub OIDC provider is configured correctly in AWS IAM <br />• Check that the IAM role ARN in git secrets matches the actual role created with terraform (`GitHubActionsEKSRole`)<br />• Ensure GitHub repository has necessary secrets configured- AWS\_REGION and AWS\_ROLE\_ARN.<br />• Validate AWS Region settings match your cluster locations |
| **Permission Problems**<br /><br /> | • Test IAM role permissions locally: `bash aws sts assume-role --role-arn <role-arn> --role-session-name test-session aws eks list-clusters`<br />• Ensure the role has `eks:UpdateClusterConfig` and `eks:DescribeCluster` permissions |
| **Cluster Compatibility**<br /><br /> | • Confirm EKS clusters are running Kubernetes 1.29 or above: `bash aws eks describe-cluster --name <cluster-name> --query 'cluster.version'`<br />• Verify clusters are in ACTIVE state before enabling Auto Mode |
| **Workflow Failures**<br /> | • Check GitHub Actions logs for specific error messages<br /> • Verify the workflow file syntax in .github/workflows/auto-mode-pipeline.yml<br /> • Ensure environment variables are properly set in the workflow |

## Related resources
<a name="enable-eks-auto-mode-using-github-actions-resources"></a>
+ [EKS Auto Mode official documentation to get started](https://docs.aws.amazon.com/eks/latest/userguide/automode.html)
+ [Update Cluster config CLI documentation](https://docs.aws.amazon.com/cli/latest/reference/eks/update-cluster-config.html)
+ [GitHub secrets for GitHub actions](https://docs.github.com/en/actions/how-tos/write-workflows/choose-what-workflows-do/use-secrets)
+ [GitHub Actions documentation](https://docs.github.com/en/actions)
+ [OIDC federation documentation](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_providers_oidc.html)

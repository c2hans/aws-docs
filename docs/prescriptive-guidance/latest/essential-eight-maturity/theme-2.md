---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/essential-eight-maturity/theme-2.html
---

# Theme 2: Manage immutable infrastructure through secure pipelines
<a name="theme-2"></a>

**Essential Eight strategies covered**: Application control, patch applications, patch operating systems

For immutable infrastructure, you must secure deployment pipelines for system changes. AWS Distinguished Engineer, Colm MacCárthaigh, explained this principle in the [Zero-Privilege Operations: Running Services Without Access to Data](https://www.youtube.com/watch?v=kNbNWxVQP4w) (YouTube video) presentation at the 2022 AWS re:Invent conference.

By restricting direct access to configure AWS resources, you can require that all resources are deployed or changed through approved, secured, and automated pipelines. Usually, you create [AWS Identity and Access Management (IAM)](https://docs.aws.amazon.com/IAM/latest/UserGuide/introduction.html) policies that allow users to access only the account that hosts the deployment pipeline. You also configure IAM policies that allow [break-glass access](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/break-glass-access.html) for a limited number of users. To prevent manual changes, you can use security groups to block SSH and Windows remote desktop protocol (RDP) access to servers. [Session Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/session-manager.html), a capability of AWS Systems Manager, can provide access to instances without the need to open inbound ports or maintain bastion hosts.

Amazon Machine Images (AMIs) and container images must be built securely and repeatably. For Amazon EC2 instances, you can use [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) to build AMIs that have built-in security features, such as instance discovery, application control, and logging. For more information about application control, see [Implementing Application Control](https://www.cyber.gov.au/resources-business-and-government/maintaining-devices-and-systems/system-hardening-and-administration/system-hardening/implementing-application-control) on the ACSC website. You can also use Image Builder to build container images, and you can use [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) to share those images across accounts. A central security team can approve the automated process to build these AMIs and container images so that any resulting AMI or container image is approved for use by the application teams.

Applications must be defined in infrastructure as code (IaC), by using services such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) or [AWS Cloud Development Kit (AWS CDK)](https://docs.aws.amazon.com/cdk/v2/guide/home.html). Code analysis tools, such as AWS CloudFormation Guard, cfn-nag, or cdk-nag, can automatically test code against security best practices in your approved pipeline.

As with [Theme 1: Use managed services](theme-1.md), Amazon Inspector can report vulnerabilities across your AWS accounts. Centralised cloud and security teams can use this information to verify that the application team is meeting security and compliance requirements.

To monitor and report on compliance, perform ongoing reviews of IAM resources and logs. Use AWS Config rules to make sure that only approved AMIs are used, and make sure that Amazon Inspector is configured to scan Amazon ECR resources for vulnerabilities.

## Related best practices in the AWS Well-Architected Framework
<a name="theme-2-best-practices"></a>
+ [OPS05-BP04 Use build and deployment management systems](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/ops_dev_integ_build_mgmt_sys.html)
+ [REL08-BP04 Deploy using immutable infrastructure](https://docs.aws.amazon.com/wellarchitected/latest/framework/rel_tracking_change_management_immutable_infrastructure.html)
+ [SEC06-BP03 Reduce manual management and interactive access](https://docs.aws.amazon.com/wellarchitected/latest/framework/sec_protect_compute_reduce_manual_management.html)

## Implementing this theme
<a name="theme-2-implementation"></a>

### Implement AMI and container build pipelines
<a name="implement-ami-and-container-build-pipelines.e86fc4e4-a105-57bc-94a6-0b6762e102db"></a>
+ [Use EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html) and build the following into your AMIs:
  + [AWS Systems Manager Agent (SSM Agent)](https://docs.aws.amazon.com/systems-manager/latest/userguide/sysman-manual-agent-install.html), which is used for instance discovery and management
  + Security tools for application control, such as [Security Enhanced Linux (SELinux)](https://github.com/SELinuxProject) (GitHub), [File Access Policy Daemon (fapolicyd)](https://github.com/linux-application-whitelisting/fapolicyd/blob/main/README.md) (GitHub), or [OpenSCAP](https://www.open-scap.org/)
  + [Amazon CloudWatch Agent](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/install-CloudWatch-Agent-on-EC2-Instance.html), which is used for logging
+ For all EC2 instances, include the `CloudWatchAgentServerPolicy` and `AmazonSSMManagedInstanceCore` policies in the [instance profile or IAM role](https://docs.aws.amazon.com/systems-manager/latest/userguide/setup-instance-permissions.html) that Systems Manager uses to access your instance
+ [Share AMIs with the entire organization](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.html)
+ [Share EC2 Image Builder resources](https://docs.aws.amazon.com/imagebuilder/latest/userguide/manage-shared-resources.html)
+ [Make sure that application teams are referencing the latest AMIs](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/walkthrough-custom-resources-lambda-lookup-amiids.html)
+ [Use your AMI pipeline for patch management](https://docs.aws.amazon.com/imagebuilder/latest/userguide/security-patch-management.html)
+ Implement container build pipelines:
  + [Create a container image pipeline using the EC2 Image Builder console wizard](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-container-pipeline.html)
  + [Build a continuous delivery pipeline for your container images by using Amazon ECR as a source](https://aws.amazon.com/blogs/devops/build-a-continuous-delivery-pipeline-for-your-container-images-with-amazon-ecr-as-source/) (AWS blog post)
+ [Share ECR container images across your organization through multi-account and multi-Region architectures](https://aws.amazon.com/blogs/containers/amazon-ecr-in-multi-account-and-multi-region-architectures/)

### Implement secure application build pipelines
<a name="implement-secure-application-build-pipelines.e79544b4-80aa-5112-888c-079bcfa427e3"></a>
+ Implement build pipelines for IaC, such as by using [EC2 Image Builder and AWS CodePipeline](https://aws.amazon.com/blogs/mt/create-immutable-servers-using-ec2-image-builder-aws-codepipeline/) (AWS blog post)
+ Use code analysis tools, such as [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html), [cfn-nag](https://github.com/stelligent/cfn_nag) (GitHub), or [cdk-nag](https://github.com/cdklabs/cdk-nag) (GitHub), in CI/CD pipelines to help detect violations of best practices, such as:
  + IAM policies that are too permissive, such as those that use wildcards
  + Security group rules that are too permissive, such as those that use wildcards or allow SSH access
  + Access logs that are not enabled
  + Encryption that is not enabled
  + Password literals
+ [Implement scanning tools in pipelines](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/) (AWS blog post)
+ [Use AWS Identity and Access Management Access Analyzer in pipelines](https://aws.amazon.com/blogs/security/validate-iam-policies-in-cloudformation-templates-using-iam-access-analyzer/) (AWS blog post) to validate IAM policies that are defined in CloudFormation templates
+ Configure [IAM policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#:~:text=IAM%20policies%20define%20permissions%20for,CLI%2C%20or%20the%20AWS%20API.) and [service control policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_scps.html) for least-privilege access to use the pipeline or make any modifications to it

### Implement vulnerability scanning
<a name="implement-vulnerability-scanning.67d4fdce-e27d-5a22-9724-d3f4087ac7a6"></a>
+ [Enable Amazon Inspector in all accounts in your organization](https://docs.aws.amazon.com/inspector/latest/user/designating-admin.html)
+ Use Amazon Inspector to scan AMIs in your AMI build pipeline:
  + [Manage the lifecycle of AMIs in EC2 Image Builder](https://github.com/aws-samples/ec2-imagebuilder-ami-lifecycle) (GitHub)
+ [Configure enhanced scanning for Amazon ECR repositories by using Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-ecr.html#configure-ecr)
+ [Build a vulnerability management program to triage and remediate security findings](https://docs.aws.amazon.com/prescriptive-guidance/latest/vulnerability-management/)

## Monitoring this theme
<a name="theme-2-monitoring"></a>

### Monitor IAM and logs on an ongoing basis
<a name="monitor-9999999999999999iam--and-logs-on-an-ongoing-basis.34de15f8-9aeb-5b53-a11a-decc2e0a4d69"></a>
+ Periodically review your IAM policies to make sure that:
  + Only deployment pipelines have direct access to resources
  + Only approved services have direct access to data
  + Users don't have direct access to resources or data
+ Monitor AWS CloudTrail logs to confirm that users are modifying resources through pipelines and aren't directly modifying resources or accessing data
+ Periodically review IAM Access Analyzer findings
+ Set up an alert to notify you if the root user credentials for an AWS account are used

### Implement the following AWS Config rules
<a name="implement-the-following-9999999999999999cc--rules.517b57e1-5abe-5850-82b3-55e6dbddc139"></a>
+ `APPROVED_AMIS_BY_ID`
+ `APPROVED_AMIS_BY_TAG`
+ `ECR_PRIVATE_IMAGE_SCANNING_ENABLED`

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

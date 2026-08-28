---
source_url: https://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/multiple-domains-and-shared-spaces.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Multiple domains and shared spaces
<a name="multiple-domains-and-shared-spaces"></a>

[Amazon SageMaker AI](https://aws.amazon.com/sagemaker/) now supports the creation of multiple SageMaker AI domains in a single AWS Region for each account. Each domain can have its own domain settings, such as authentication mode, and networking settings, such as VPC and subnets. A user profile cannot be shared across domains. If a human user is part of multiple teams separated by domains, create a user profile for the user in each domain. Refer to the [Multiple Domains Overview](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-multiple.html) to learn about backfilling tags for existing domains.

Each domain set up in IAM authentication mode can make use of shared space for near real-time collaboration between users. With a shared space, users get access to a shared Amazon EFS directory, and a shared [JupyterServer](https://jupyter-server.readthedocs.io/en/latest/) app for the user interface, and can co-edit in near real-time. Automatic tagging of resources created by shared spaces allows the administrators to track costs on a project level. The shared JupyterServer UI also filters resources such as experiments and model registry entries so that only items relevant to the shared ML endeavor will be shown. The following diagram provides an overview of private apps and shared spaces within each domain.

![A diagram depicting an overview of private apps and shared spaces within a single domain.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/private-apps-shared-spaces.png)

## Set up shared spaces in your domain
<a name="set-up-shared-spaces-in-your-domain"></a>

Shared spaces are typically created for a particular ML endeavor or project where members of a single domain require near real-time access to the same underlying file storage and IDE. The user can access, read, edit, and share their notebooks in near real-time, which gives them the quickest path to start iterating with their peers.

To create a shared space, you must first designate a space default execution role which will govern the permissions for any user that utilizes the space. At the time of this writing, all users within a domain will have access to all shared spaces in their domain. Refer to [Create a shared space](https://docs.aws.amazon.com/sagemaker/latest/dg/domain-space-create.html) for the latest documentation on adding shared spaces to an existing domain.

## Set up your domain for IAM federation
<a name="set-up-your-domain-for-iam-federation"></a>

Before setting up AWS Identity and Access Management (IAM) federation for your SageMaker AI Studio domain, you need to set up an IAM federation user role (such as a platform administrator) in your IdP, as discussed in the * [Identity management](identity-management.md)* section.

For detailed instructions for setting up SageMaker AI Studio with the IAM option, refer to [Onboard to Amazon SageMaker Domain Using IAM Identity Center](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-iam.html).

## Set up your domain for single sign-on (SSO) federation
<a name="set-up-your-domain-for-sso-federation"></a>

To use single sign-on (SSO) federation, you need to enable AWS IAM Identity Center in your [AWS Organizations](https://aws.amazon.com/organizations/) management account in the same Region where you need to run SageMaker AI Studio. The domain setup steps are similar to IAM federation steps, except you select **AWS IAM Identity Center** **(IdC)** in the **Authentication** section.

For detailed instructions, refer to [Onboard to Amazon SageMaker Domain Using IAM Identity Center](https://docs.aws.amazon.com/sagemaker/latest/dg/onboard-sso-users.html).

## SageMaker AI Studio user profile
<a name="sagemaker-studio-user-profile"></a>

A *user profile* represents a single user within a domain, and is the main way to reference a "person" for the purposes of sharing, reporting, and other user-oriented features. This entity is created when a user onboards toSageMaker AI Studio. If an administrator invites a person by email or imports them from IdC, a user profile is automatically created. A user profile is the primary holder of settings for an individual user, and has a reference to the user's private [Amazon Elastic File System](https://aws.amazon.com/efs) (Amazon EFS) home directory. We recommend creating a user profile for each physical user of the SageMaker AI Studio application. Each user has their own dedicated directory on Amazon EFS, and user profiles cannot be shared across domains in the same account.

Each user profile sharing the SageMaker AI Studio domain gets dedicated compute resource(s) (such as SageMaker AI [Amazon Elastic Compute Cloud](https://aws.amazon.com/ec2/) (Amazon EC2) instance(s)) to run notebooks. The compute instances allocated to user one are completely isolated from those allocated to user two. Similarly, the compute resources allocated to users in one AWS account are completely separate from those allocated to users in another account. Each user can run up to four applications (*apps*) within isolated Docker containers, or images on the same instance type.

## Jupyter Server app
<a name="jupyter-server-app"></a>

When you launch an [Amazon SageMaker AI Studio notebook](https://aws.amazon.com/sagemaker/notebooks/) for a user by accessing the pre-signed URL or by logging in using AWS IAM IdC, the [Jupyter Server](https://jupyter-server.readthedocs.io/en/latest/) app is launched in the SageMaker AI service-managed VPC instance. Each user gets their own dedicated Jupyter Server app in a private app. By default, the Jupyter Server app for SageMaker AI Studio notebooks is run on a dedicated `ml.t3.medium` instance (reserved as a *system* instance type). The compute for this instance is not billed to the customer.

## The Jupyter Kernel Gateway app
<a name="jupyter-kernel-gateway-app"></a>

The [Kernel Gateway app](https://jupyter-kernel-gateway.readthedocs.io/en/latest/) can be created through the API or the SageMaker AI Studio interface, and it runs on the chosen instance type. This app can be run using one of the built-in SageMaker AI Studio images that are preconfigured with popular data science, and deep learning packages such as [TensorFlow](https://www.tensorflow.org/), [Apache MXNet](https://mxnet.apache.org/versions/1.9.1/), and [PyTorch](https://pytorch.org/).

Users can start and run multiple Jupyter notebook kernels, terminal sessions, and interactive consoles within the same SageMaker Studio image/Kernel Gateway app. Users can also run up to four Kernel Gateway apps or images on the same physical instance—each isolated by its container/image.

To create additional apps, you need to use a different instance type. A user profile can have only one instance running, of any instance type. For example, a user can run both a simple notebook using the SageMaker AI Studio built-in data science image, and another notebook using the built-in TensorFlow image, on the same instance. Users are billed for the time the instance is running. To avoid costs when the user is not actively running SageMaker AI Studio, the user needs to shut down the instance. For more information, refer to [Shut down and update Studio Apps](https://docs.aws.amazon.com/sagemaker/latest/dg/studio-tasks-update-apps.html).

Every time you shut down and reopen a Kernel Gateway app from the SageMaker AI Studio interface, that app is started on a new instance. This means that the package’s installation is not persisted through restarts of the same app. Similarly, if a user changes the instance type on a notebook, their installed packages and session variables are lost. However, you can use features such as *bring your own image* and *lifecycle scripts* to bring the user’s own packages to SageMaker AI Studio and persist them through instance switches and new instance launches.

## Amazon Elastic File System volume
<a name="amazon-efs-volume"></a>

When a domain is created, a single [Amazon Elastic File System](https://aws.amazon.com/efs/) (Amazon EFS) [volume](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/efs-volumes.html) is created for use by all the users within the domain. Each user profile receives a private home directory within the Amazon EFS volume for storing the user’s notebooks, GitHub repositories, and data files. Each space within a domain receives a private directory within the Amazon EFS volume that can be accessed by multiple user profiles. Access to the folders is segregated by user, through filesystem permissions. SageMaker AI Studio creates a global unique user ID for each user profile or space, and applies it as a Portable Operating System Interface (POSIX) user/group ID for the user’s home directory on EFS, which prevents other users/spaces from accessing its data.

### Backup and recovery
<a name="backup-and-recovery"></a>

An existing EFS volume cannot be attached to a new SageMaker AI domain. In a production setting, make sure the Amazon EFS volume is backed up (to another EFS volume, or to [Amazon Simple Storage Service](https://aws.amazon.com/s3/) (Amazon S3)). If an EFS volume is accidentally deleted, the administrator has to tear down and recreate the SageMaker AI Studio domain. The process is as follows:

Back up the list of user profiles, spaces and the associated EFS user IDs (UIDs) through the `[ListUserProfiles](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListUserProfiles.html)`, `[DescribeUserProfile](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeUserProfile.html)`, `[List Spaces](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_ListSpaces.html)`, and `[DescribeSpace](https://docs.aws.amazon.com/sagemaker/latest/APIReference/API_DescribeSpace.html)` API calls.

1. Create a new SageMaker AI Studio domain.

1. Create the user profiles and spaces.

1. For each user profile, copy over the files from the backup on EFS/Amazon S3.

1. Optionally, delete all apps and user profiles, on the old SageMaker AI Studio domain.

For detailed instructions refer to appendix section *[SageMaker AI Studio domain backup and recovery](appendix.md#sagemaker-studio-domain-backup-and-recovery)*.

**Note**
This can also be achieved through `LifecycleConfigurations` to back up data to and from S3 every time a user starts their app.

## Amazon EBS volume
<a name="amazon-ebs-volume"></a>

An [Amazon Elastic Block Store](https://aws.amazon.com/ebs/) (Amazon EBS) [storage volume](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-volumes.html) is also attached to each SageMaker AI Studio Notebook instance. It’s used as the root volume of the container or image running on the instance. While Amazon EFS storage is persistent, the Amazon EBS volume attached to container is temporary. The data stored locally on Amazon EBS volume won’t be persisted if customer deletes the app.

## Securing access to the pre-signed URL
<a name="securing-access-to-the-pre-signed-url"></a>

 When a SageMaker AI Studio user opens the notebook link, SageMaker AI Studio validates the federated user’s IAM policy to authorize access, and generates and resolves the pre-signed URL for the user. Because the SageMaker AI console runs on an internet domain, this generated, pre-signed URL is visible in the browser session. This presents an undesired threat vector for data theft and gaining access to customer data when proper access controls are not enforced.

 Studio supports a few methods for enforcing access controls against pre-signed URL data theft:
+  Client IP validation using the IAM policy condition `aws:sourceIp`
+  Client VPC validation using the IAM condition `aws:sourceVpc`
+  Client VPC endpoint validation using the IAM policy condition `aws:sourceVpce`

 When you access SageMaker AI Studio notebooks from the SageMaker AI console, the only available option is to use client IP validation with the IAM policy condition `aws:sourceIp`. However, you can use browser traffic routing products such as [Zscaler](https://www.zscaler.com/) to ensure scale and compliance for your workforce internet access. These traffic routing products generate their own source IP, whose IP range is not controlled by the enterprise customer. This makes it impossible for these enterprise customers to use the `aws:sourceIp` condition.

 To use client VPC endpoint validation using the IAM policy condition `aws:sourceVpce`, the creation of a pre-signed URL needs to originate in the same customer VPC where SageMaker AI Studio is deployed, and resolution of the pre-signed URL needs to happen via a SageMaker AI Studio VPC endpoint on the customer VPC. This resolution of the pre-signed URL during access time for corporate network users can be accomplished using DNS forwarding rules (both in Zscaler and corporate DNS), and then into the customer VPC endpoint using an [Amazon Route 53](https://aws.amazon.com/route53/) inbound resolver as shown in the following architecture:

![A diagram that shows accessing Studio pre-signed URL with VPC endpoint over corporate network.](http://docs.aws.amazon.com/whitepapers/latest/sagemaker-studio-admin-best-practices/images/pre-signed-url.png)

 For step-by-step guidance setting up the preceding architecture, refer to [Secure Amazon SageMaker AI Studio presigned URLs Part 1: Foundational infrastructure](https://aws.amazon.com/blogs/machine-learning/secure-amazon-sagemaker-studio-presigned-urls-part-1-foundational-infrastructure/).

## SageMaker AI domain quotas and limits
<a name="sagemaker-domain-quotas-and-limits"></a>
+  SageMaker AI Studio domain SSO federation is supported in only the Region, across member accounts of the AWS organization where AWS Identity Center is provisioned.
+  Shared spaces are not currently supported with domains set up with AWS Identity Center.
+  VPC and subnet configuration cannot be changed after creating the domain. You can, however, create a new domain with a different VPC and subnet configuration.
+  Domain access cannot be switched between IAM and SSO modes after creating the domain. You can create a new domain with a different authentication mode.
+  There is a limit of four kernel gateway apps per instance type launched for every user.
+  Each user can launch only one instance of each instance type.
+  There are limits on the resources consumed within a domain, such as number of instances launched by instance types, and number of user profiles that can be created. Refer to the [service quota page](https://docs.aws.amazon.com/general/latest/gr/sagemaker.html#limits_sagemaker) for a complete list of service limits.
+  Customers can submit an enterprise support case with business justification to raise the default resource limits such as number of domains or user profiles, subjected to account-level guardrails.
+ Be sure to check the [Service Quotas console](https://console.aws.amazon.com/servicequotas/) for the most current quotas or limits on the number of concurrent apps allowed per account. Domains and user profile limits are dependent on the concurrent apps limit. For example, an account can have a single domain with 1,000 user profiles, or 20 domains with 50 user profiles each.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/nhs-cloud-security-guidance-using-aws/principle-9-secure-user-management.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Principle 9: Secure user management
<a name="principle-9-secure-user-management"></a>

****
 Your provider should make the tools available for you to securely manage your use of their service. Management interfaces and procedures are a vital part of the security barrier, preventing unauthorised access and alteration of your resources, applications, and data.

## Section 9.1: Authentication of [admin] users to management interfaces and support channels
<a name="section-9.1-authentication-of-admin-users-to-management-interfaces-and-support-channels"></a>

****
 In order to maintain a secure service, [admin] users need to be properly authenticated before being allowed to perform management activities, report faults or request changes to the service.
 The Service User should ensure that a list of authorised individuals from your organisation who can use those mechanisms is maintained and regularly reviewed.

 To manage the AWS resources deployed, administrators need to authenticate to AWS with appropriate credentials and permissions.

 The constructs available in AWS providing context for authentication and authorisation are, in descending order of granularity:
+  The AWS Organization (the administrative and security hierarchy for one or more AWS Accounts), which offers Service Control Policies to set the maximum permissions envelope for AWS Accounts (see the [AWS Organizations](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_introduction.html) documentation for more information);
+  The AWS account;
+  The VPC within the AWS account; and
+  Individual resources within the AWS account (separated by the dimensions of network – such as subnets – or metadata, using tags).

 The Guidance makes only passing reference to authorisation, but it is imperative that this be considered in addition to authentication as part of the overall security strategy, to ensure that the appropriate privileges are assigned to the right individuals, groups, and systems accessing them.

 Access to the API that manages and controls each service is governed by IAM. IAM provides customers with the granular controls and features necessary for them to have confidence that authenticated and authorised users can access specified services and interfaces with the appropriate degree of privilege. It enables customers to create multiple users and manage the permissions for each of these users within their AWS Accounts.

 A *user *is an identity (within an AWS account) with unique security credentials that can be used to access AWS Services. To simplify administration, users can be included in Groups for those with the same access requirements. Users can also take on Roles, reflecting a temporary change to their access privileges for specific tasks (see below for more detail about this capability).

 These identities and associated permissions are the means for customers to authenticate and authorise individuals in their organisation to perform administrative and other tasks in customer AWS environments. IAM therefore eliminates the need to share passwords or access keys, and makes it easy to enable or disable a user’s access as appropriate.

 Access privileges are assigned through IAM policies, which express the precise permissions that the policy permits (or denies). These policies are then assignable to Users, Groups and Roles (as well as other kinds of AWS entities). There are several different types of policies, applicable in different contexts. Details are provided in [Policy types](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies.html#access_policy-types), but the most important types are introduced here:
+  Identity-based policies are those associated with Users, Groups, and Roles.
+  Resource-based policies are assigned to AWS resources (such as S3 buckets).
+  Permissions boundaries express the outer limits of permissions that any given user or role could *potentially* have, to guard against overly-permissive policies being inadvertently applied to these entities. Note that this does not set permissions limits on Resource-based policies.

 **API access delegation** — AWS supports two very important and powerful use cases with IAM *roles* in combination with users: cross-account API access, and delegating API access within an account. These enable better control and simplify access management, by helping customers avoid having to share long-term security credentials for cross-account access or more privileged access within an account.

 When a user assumes an IAM role, a set of temporary security credentials is assigned to that user, with the permissions associated with the role. It is these temporary credentials that are then used instead of the user’s long-term credentials in calls to AWS service APIs. Users interact with the service with the permissions granted to the IAM role assumed, rather than those assigned to their IAM identity (or Groups it may be a member of). This reduces the potential attack surface area by minimising the number of user credentials created and managed, and the number of passwords users have to remember. For details, see [IAM roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles.html).

 Another important IAM capability to use is Policy Conditions — source IP address, timestamp, tags, and so on, apply to all services, and others are service-specific, such as attributes in a DynamoDB table, AWS resource Names, and so on.

 The [Security best practices in IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html) page of the IAM documentation provides detailed advice for this and other aspects of that service.

 For authorization, tag-based access-control provides a powerful and flexible means of controlling permissions in the AWS environment; see the [*AWS Tagging Strategies*](https://d0.awsstatic.com/aws-answers/AWS_Tagging_Strategies.pdf) whitepaper and the [Controlling access to and for users and roles using tags](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_iam-tags.html) section of the IAM documentation for additional guidance.

 For certain services (such as S3), the API also covers some or all aspects of its function, as well as its configuration and management; hence there are service-specific access control mechanisms. The following list covers just a small subset of those available (as new services are released regularly), so customers should refer to the documentation specific to each of the services under consideration:
+  **Amazon EC2** — In addition to the IAM permissions and roles assignable to EC2 instances, inbound remote terminal connections to them using Secure Sockets Shell (SSH) may be authenticated using SSH key pairs for EC2. For details, see [Amazon EC2 key pairs and Linux instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-key-pairs.html).

   The access control capabilities of operating systems available for EC2 are extensive, but fall outside the scope of this whitepaper, so customers are encouraged to consult the available third-party documentation for these to manage access at that level.

   The recommended approach from AWS, however, is to employ the AWS Systems Manager service to reduce or eliminate altogether any manual human access to EC2 instances. Features in this service include (but are not restricted to):
  +  **Run Command and Automation**, which enables management operations to be undertaken on instances without the need for inbound terminal access
  +  **Inventory**, which collects data about instances and software installed on them; Distributor, which deploys applications and other software to them
  +  **Patch Manager**, a feature to deliver operating system and application software patches, and report on patching status
  +  **State Manager**, to enable consistent instance configuration

   For more details, see the [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) documentation.
+  **Amazon EBS** — Volumes attached to EC2 instances are secured using the mechanisms available in the operating system those instances are running; this is outside of this whitepaper’s scope.

   Detached volumes are secured using IAM, as described previously.
+  **Amazon S3** — Access control relies on a combination of Resource Policies (which in turn use IAM – see previous sections for details) and Bucket Policies to achieve this. For details, see [Identity and access management in Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-access-control.html).
+  **Amazon RDS** — For the majority of RDBMS engines available in this service, access to the data stored in RDS is secured through the mechanisms specific to those engines. As an application-level consideration, this falls outside of the scope of this whitepaper. See the engine-specific documentation to achieve this.

   At the time of writing, the exceptions to this are RDS MySQL and RDS PostgreSQL, for which customers can choose to manage authentication using IAM. See [IAM database authentication for MySQL and PostgreSQL](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/UsingWithRDS.IAMDBAuth.html) for details.
+  **Amazon DynamoDB** — Control of access to data stored in this service uses IAM. For details, see [Overview of Managing Access Permissions to Your Amazon DynamoDB Resources](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/access-control-overview.html).
+  **Amazon EMR** — There being several components to this service, access to each of these is controlled in a way appropriate to that component. Inbound remote terminal connections are made to cluster instances using Secure Sockets Shell (SSH), and authentication can use either Kerberos or SSH key pairs for EC2, as described in [Use an Amazon EC2 key pair for SSH credentials](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-access-ssh.html). Access to the EMR File System (EMRFS) is controlled using IAM Roles, as described in [Configure IAM roles for EMRFS requests to Amazon S3](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-emrfs-iam-roles.html).
+  **AWS Internet of Things (IoT) Core** — Access to the service itself and its associated device shadows is controlled using IAM. The devices themselves may authenticate to the IoT broker using IAM credentials, X.509 certificates, Amazon Cognito identities, or custom tokens.
+  **Machine learning (ML) services** — This category of services (including Amazon SageMaker AI, Amazon Comprehend Medical, Amazon Forecast, Amazon Lex, Amazon Polly, Amazon Rekognition, Amazon Textract, Amazon Translate, Amazon Transcribe, and so on) generally has access controlled using IAM, as previously described.

   **End user computing services** — These include Amazon WorkSpaces and Amazon AppStream 2.0 (complementary client application delivery services), Amazon WorkDocs and Amazon WorkSpaces Web (a service enabling secure remote access to non-internet-facing corporate resources, whether in the cloud or on premises). The first three of these are also secured using IAM, as described in [Identity and access management for WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-access-control.html), [Identity and Access Management for Amazon AppStream 2.0](https://docs.aws.amazon.com/appstream2/latest/developerguide/controlling-access.html), and [Prerequisites for Amazon WorkDocs](https://docs.aws.amazon.com/workdocs/latest/adminguide/prereqs.html#iam_policies).

   Access to Amazon WorkSpaces Web is managed by identity federation with a third-party Identity Provider such as Active Directory Federation Services, Ping One Federation Services, or Okta, as described in [Set up your SAML 2.0 identity provider](https://docs.aws.amazon.com/workspaces-web/latest/adminguide/setup-saml.html). For Amazon AppStream 2.0, see [Single Sign-on Access (SAML 2.0)](https://docs.aws.amazon.com/appstream2/latest/developerguide/external-identity-providers.html).

   It is also possible to control access to Amazon AppStream 2.0 via User Pools. For details, see [AppStream 2.0 User Pools](https://docs.aws.amazon.com/appstream2/latest/developerguide/user-pool.html).

****
 The Service User should use 2FA to obtain access to the system.

 **Applicable risk classes:** III-V

 If using IAM as the identity provider for AWS administrative access, additional factors (such as hardware or software tokens) may be registered against each identity in IAM.

****
 The Service User should configure logging of access attempts.

 The AWS CloudTrail service, described in detail in Principle 13: Audit information for users, monitors sign-in attempts to the AWS Management Console and access attempts to the AWS APIs. Customers may set up CloudTrail logs to fulfil this requirement.

## Section 9.2: Separation and access control within management interfaces
<a name="section-9.2-separation-and-access-control-within-management-interfaces"></a>

****
 Many cloud services are managed via web applications or APIs. These interfaces are a key part of the service’s security. If [admin] users are not adequately separated within management interfaces, one [admin] user may be able to affect the service, or modify the data of another.
 The Service User should ensure that authorised individuals from your organisation who can use those mechanisms are managed by the ‘principle of least privilege’, typically using a RBAC mechanism.

 IAM enables customers to implement security best practices, such as the principle of least privilege, by granting unique credentials to each user accessing resources in customers’ AWS accounts and restricting their permissions to only those AWS services and resources required for them to perform their jobs. AWS IAM is secure by default; new users have no access to AWS until permissions are explicitly granted.

 IAM enables customers to minimise the use of AWS account credentials. After users have been created, all interactions with AWS Services and resources should occur using user security credentials.

 An important complementary means of implementing the principle of least privilege is through the AWS Systems Manager Service. This provides a set of management tools that reduces further the need to access AWS resources (such as EC2 instances) directly, and enables actions performed in the course of that access to be logged in companion AWS services such as CloudTrail and CloudWatch Logs for audit purposes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

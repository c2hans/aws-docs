---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/security.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Security
<a name="security"></a>

 When you migrate your .NET applications to containers, many of the same security concerns as non-containerized environments need to be addressed. This section walks through the primary security components of running containerized applications in AWS. It covers how to use Windows authentication for user and application authentication, and how to control access of the containerized applications to other AWS services using IAM.

**Topics**
+ [Windows authentication](windows-authentication.md)
+ [Join the ECS instance (host) to the domain](join-the-ecs-instance-host-to-the-domain.md)
+ [Configure a group Managed Service Account in the Active Directory domain](configure-a-group-managed-service-account-in-the-active-directory-domain.md)
+ [Change your Dockerfile to support Windows authentication](change-your-dockerfile-to-support-windows-authentication.md)
+ [Create the CredentialSpec file](create-the-credentialspec-file.md)
+ [Configure ECS Task Definition with CredentialSpec](configure-ecs-task-definition-with-credentialspec.md)
+ [Using a load balancer with Windows Authentication](using-a-load-balancer-with-windows-authentication.md)
+ [Authenticating with AWS services](authenticating-with-aws-services.md)
+ [AWS SDK for .NET credential loading](aws-sdk-for-.net-credential-loading.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

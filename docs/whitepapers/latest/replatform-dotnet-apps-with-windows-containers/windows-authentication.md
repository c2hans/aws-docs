---
source_url: https://docs.aws.amazon.com/whitepapers/latest/replatform-dotnet-apps-with-windows-containers/windows-authentication.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Windows authentication
<a name="windows-authentication"></a>

 Many .NET applications use Windows (or integrated) authentication to enable users to sign in using their Active Directory domain credentials. Applications can also utilize Active Directory service accounts to connect to network resources such as SQL Server databases. If an application running on an EC2 instance (application server) needs access to a SQL Server database running on another EC2 instance (database server), both EC2 instances need to either join the same domain or join different domains with a trust relationship between them. Windows containers cannot be joined by domain, but they can be configured to use Active Directory identities.

 To enable an application running inside a container to authenticate against a domain:

1.  Join the ECS instance (host) to the domain.

1.  Configure a group Managed Service Account (gMSA) in the domain.

1.  Change your Dockerfile to support windows authentication.

1.  Create the `CredentialSpec` file.

1.  Configure the ECS Task Definition with `CredentialSpec`.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

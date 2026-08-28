---
source_url: https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/other-considerations.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Other considerations
<a name="other-considerations"></a>

 **FSMO Roles**. You can follow the same recommendation you would follow for your on-premises deployment to determine FSMO roles on DCs. See also [best practices from](https://support.microsoft.com/en-us/help/223346/fsmo-placement-and-optimization-on-active-directory-domain-controllers) [Microsoft.](https://support.microsoft.com/en-us/help/223346/fsmo-placement-and-optimization-on-active-directory-domain-controllers) In the case of AWS Managed Microsoft AD, all domain controllers and FSMO roles assignments are managed by AWS and do not require you to manage or change them.

 **Global Catalog**. Unless you have slow connections or an extremely large Active Directory database, we recommend adding global catalog role to all of your domain controllers in multi-domain forests (except the domain controller with the Infrastructure Master role).

 If you are [hosting Microsoft Exchange in AWS Cloud](https://aws.amazon.com/blogs/modernizing-with-aws/how-to-run-microsoft-exchange-server-on-aws-using-amazon-ec2/), at least one global catalog server is required in a site with Exchange servers. For more information about global catalog, see [Microsoft documentation.](https://technet.microsoft.com/pt-pt/library/how-global-catalog-servers-work(v%3Dws.10).aspx) Since there is only one domain in the forest for AWS Managed Microsoft AD, all domain controllers are configured as global catalog and will have full information about all objects.

 **Read Only Domain Controllers (RODC)**. It’s possible to deploy RODC on AWS if you are running Active Directory on EC2 instances and require it, and there are no special considerations for doing so. AWS Managed Microsoft AD does not support RODCs. All of the domain controllers that are deployed as a part of AWS Managed Microsoft AD are writable domain controllers.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

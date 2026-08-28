---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/set-up-access-mgmt-ad-trust.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Establish an Active Directory Trust
<a name="set-up-access-mgmt-ad-trust"></a>

To set up a trust, AMS requires your domain controller **Local Policies -> Security Options -> Network Access: Named Pipes that can be accessed anonymously**, have the **Netlogon** and **lsarpc** pipes listed. These pipes are listed by default, but are sometimes removed for security concerns. Once the trust is established, they can be removed from the list again.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

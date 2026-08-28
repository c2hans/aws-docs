---
source_url: https://docs.aws.amazon.com/managedservices/latest/onboardingguide/setup-net-federate-console.html
---

End of support notice: On June 30, 2027, AWS will end support for AMS Advanced. After June 30, 2027, you will no longer be able to access the AMS Advanced console or AMS Advanced resources. For more information, see [AMS Advanced end of support](https://docs.aws.amazon.com/managedservices/latest/userguide/SunsetPlan.html).

# Configuring federation to the AMS console (MALZ)
<a name="setup-net-federate-console"></a>

The IAM roles and SAML identity provider (Trusted Entity) detailed in the following table have been provisioned as part of the AMS infrastructure. These roles allow you to audit and view the AMS core accounts.

| Role | Permissions |
| --- | --- |
| AWSManagedServicesReadOnlyRole | Allows you to view the AMS infrastructure in the core accounts. |
| AWSManagedServicesCaseRole | Allows you to view the resources in your new application account and file AMS incidents and service requests. |
| AWSManagedServicesChangeManagementRole | Allows you to view the AMS infrastructure in the core accounts, file AWS Support tickets, and request some RFCs. |

For the full list of the roles available under different accounts see [IAM user role in AMS](defaults-user-role.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Managed Services. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query managedservices` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/transitioning-to-multiple-aws-accounts/doc-history.html
---

# Document history
<a name="doc-history"></a>

The following table describes significant changes to this guide.

|
|
| Change | Description | Date |
| --- |--- |--- |
| Resource control policies | We added information about resource control policies to the [Set up an organization](set-up-organization.md) section. | November 20, 2024 |
| Centralized egress best practices | We updated the [best practices](centralized-egress.md#best-practices-egress) for securing egress traffic. | May 6, 2024 |
| Organization best practices | We updated the [best practices](set-up-organization.md#organization-best-practices) for creating an organization in AWS Organizations. | December 4, 2023 |
| Billing considerations | We added the [Billing considerations](billing-considerations.md) section. | September 20, 2023 |
| Resource migration, application connectivity, and Amazon VPC Lattice | We added the [Resource migration](resource-migration.md) and [Connecting applications](network-connectivity.md#connecting-applications) sections. We also added information about a new AWS service, Amazon Virtual Private Cloud (Amazon VPC) Lattice. | April 27, 2023 |
| Account history and ABAC | We revised the [Create a landing zone](create-landing-zone.md) section to add information about how to make sure your new AWS accounts have usage history so that you can add them to to your AWS Control Tower landing zone. We also revised the [Add initial users](add-initial-users.md) section to add information about how you can use attribute-based access control (ABAC) to pass the authentication method from an external SAML-based IdP to AWS IAM Identity Center. | January 6, 2023 |
| Egress traffic networking | We revised the [Centralized egress](centralized-egress.md) section to add information about using Amazon Route 53 Resolver DNS Firewall to to limit egress traffic to specific domain names. | October 13, 2022 |
| Security of egress traffic | We added [Best practices for securing egress traffic](centralized-egress.md#best-practices-egress). | October 6, 2022 |
| Permissions boundaries | We improved the definition of a [permissions boundary](creating-a-permissions-boundary.md), and in the *Resources* section, we added a new link for more information about this topic. | September 22, 2022 |
| Initial publication | — | September 6, 2022 |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

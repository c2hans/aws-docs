---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/reserved-instances-types.html
---

# Types of Reserved Instances (offering classes)
<a name="reserved-instances-types"></a>

The offering class of a Reserved Instance is either Standard or Convertible. A Standard Reserved Instance provides a more significant discount than a Convertible Reserved Instance, but you can't exchange a Standard Reserved Instance. You can exchange Convertible Reserved Instances. You can modify Standard and Convertible Reserved Instances.

The configuration of a Reserved Instance comprises a single instance type, platform, scope, and tenancy over a term. If your computing needs change, you might be able to modify or exchange your Reserved Instance.

## Differences between Standard and Convertible Reserved Instances
<a name="offering-class-differences"></a>

The following are the differences between Standard and Convertible Reserved Instances.

|  | Standard Reserved Instance | Convertible Reserved Instance |
| --- | --- | --- |
| Modify Reserved Instances | Some attributes can be modified. For more information, see [Modify Reserved Instances](ri-modifying.md). | Some attributes can be modified. For more information, see [Modify Reserved Instances](ri-modifying.md). |
| Exchange Reserved Instances | Can't be exchanged. | Can be exchanged during the term for another Convertible Reserved Instance with new attributes, including instance family, instance type, platform, scope, or tenancy. For more information, see [Exchange Convertible Reserved Instances](ri-convertible-exchange.md). |
| Sell in the Reserved Instance Marketplace | Can be sold in the Reserved Instance Marketplace. | Can't be sold in the Reserved Instance Marketplace. |
| Buy in the Reserved Instance Marketplace | Can be bought in the Reserved Instance Marketplace. | Can't be bought in the Reserved Instance Marketplace. |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

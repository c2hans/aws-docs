---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/application-portfolio-assessment-guide/iterating-prioritization-criteria.html
---

# Iterating the prioritization criteria
<a name="iterating-prioritization-criteria"></a>

Before you create migration wave plans, we recommend that you iterate the application prioritization criteria to pivot from pilot application selection to long-term wave planning.

In earlier sections, we introduced a default prioritization criteria that would prioritize simple cloud-ready applications (see [Prioritizing applications](prioritization-and-migration-strategy.md#prioritizing-applications)). This was because in early stages we recommend starting with noncritical applications to refine migration processes and incorporate lessons learned. However, at this stage, and to create long-term plans, the order in which applications are migrated should be aligned to business drivers. Applying the new criteria will generate a new ranking of applications that will be a key input for wave planning.

Review the available data points from the application portfolio, and select the attributes that will determine application prioritization based on business drivers.

First, validate your business drivers (see [Business drivers and technical guiding principles](business-drivers-technical-guiding-principles.md)). Next, based on your business drivers, select the attributes that will help to prioritize applications for migration.

The following table shows example prioritization criteria aligned to business drivers for innovation.

|
|
| Attribute or data point | Possible values | Score (0-99) | Importance or relevance multiplying factor |
| --- |--- |--- |--- |
| Operating system | AIX | 80 | High (1x) |
| Solaris | 80 |
| HP-UX | 80 |
| Mainframe | 70 |
| Windows | 50 |
| Linux | 20 |
| Business criticality | High | 60 | High (1x) |
| Medium | 40 |
| Low | 20 |
| Architecture | Tightly coupled | 60 | High (1x) |
| Loosely coupled | 20 |
| Operating model | Traditional - no CI/CD | 60 | Medium-high (0.8x) |
| Basic CI/CD | 40 |
| Full DevOps | 20 |
| Number of compute instances | 1-3 | 60 | Medium-high (0.8x) |
| 4-10 | 40 |
| 11 or more | 20 |
| Migration strategy | Refactor (re-architect) | 70 | Medium (0.6x) |
| Replatform | 40 |
| Repurchase | 30 |
| Rehost | 10 |

The following table shows example prioritization criteria aligned to business drivers for quick cost reduction.

|
|
| Attribute or data point | Possible values | Score (0-99) | Importance or relevance multiplying factor |
| --- |--- |--- |--- |
| Database product | Oracle | 70 | High (1x) |
| Microsoft SQL | 70 |
| Others | 20 |
| Operating system | Windows | 70 | High (1x) |
| Linux | 70 |
| Others | 20 |
| CPU utilization (average) | More than 36% | 60 | High (1x) |
| Less than 36% | 40 |
| Number of compute instances | 11 or more | 60 | Medium-high (0.8x) |
| 4-10 | 40 |
| 1-3 | 20 |
| Migration strategy | Retire | 80 | Medium (0.6x) |
| Rehost | 70 |
| Replatform | 50 |
| Refactor (re-architect) | 10 |

Test the prioritization criteria and iterate until you generally agree with the output. It takes at least three or four iterations to obtain a baseline version.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

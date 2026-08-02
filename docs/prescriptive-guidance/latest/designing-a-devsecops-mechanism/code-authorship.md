---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/designing-a-devsecops-mechanism/code-authorship.html
---

# Code authorship
<a name="code-authorship"></a>

Who will write code within the organization? The division of responsibilities between application team developers and central infrastructure developers plays a crucial role in shaping organizational efficiency and innovation. Although application team developers can have varying levels of autonomy and expertise, central infrastructure developers often serve as a resource for specialized skills and standardized practices. Understanding the strengths and challenges of each approach is essential for organizations seeking to optimize their development strategies.

## Application team developers
<a name="application-team-developers"></a>

Will the application teams write most or all of the code? For some applications, they might have a strong development skillset and want to be empowered. For other teams, they might rely on a development team external to their team and expect a significant amount of consultation or to fully handoff all development. How you empower or block developers can affect the following issues:
+ Speed to market for new and refactored solutions
  + Is your company and the solutions that they rely on cutting-edge technology or well-know standards?
+ Competitive nature of the business or team
  + Does your company success rely heavily on being early to market?
+ Developer satisfaction
  + What type of employee will be satisfied using the solution you build?
+ Employee attrition
  + The more difficult a solution is to learn and use, the more likely developers will go elsewhere.
+ Company culture
  + Will the solution that you deliver align with how your company is accustomed to operating?

## Central infrastructure developers
<a name="central-infrastructure-developers"></a>

Some organizations or teams depend on an existing central infrastructure or a mainframe team for application infrastructure development. This is useful for consolidating the infrastructure skill sets required into a single team, easing the process of development and troubleshooting.

The challenges that can arrive with this approach are time commitments and requirement changes. When application teams are dependent on a central team, requirement accuracy must be higher and requirement gathering must follow a clearer and organized mechanism.

Consider the following points:
+ How will your organization or team prevent requirement drift?
+ What standards and communication tools are in place to facilitate this process?
+ How does your organization or team standardize service level agreements (SLAs) for requirement changes?

Having a central development team can also be beneficial when using a central repository, as discussed in [Shared repositories and contributions](shared-repositories.md).

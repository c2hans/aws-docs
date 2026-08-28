---
source_url: https://docs.aws.amazon.com/whitepapers/latest/aws-security-incident-response-guide/types-of-simulations.html
---

# Types of simulations
<a name="types-of-simulations"></a>

 There are three main types of simulations:
+  **Tabletop exercises** – The tabletop approach to simulations is strictly a discussion-based session involving the various incident response stakeholders to practice roles and responsibilities and use established communication tools and playbooks. Exercise facilitation can typically be accomplished in a full day in a virtual venue, physical venue, or a combination. Because of its discussion-based nature, the tabletop exercise focuses on processes, people, and collaboration. Technology is an integral part of the discussion; however, the actual use of incident response tools or scripts is generally not a part of the tabletop exercise.
+  **Purple Team exercises** – Purple Team exercises increase the level of collaboration between the incident responders (*Blue Team*) and simulated threat actors (*Red Team*). The Blue Team is generally comprised of members of the Security Operations Center (SOC), but can also include other stakeholders that would be involved during an actual cyber event. The Red Team is generally comprised of a penetration testing team or key stakeholders that are trained in offensive security. The Red Team works collaboratively with the exercise facilitators when designing a scenario so that the scenario is accurate and feasible. During Purple Team exercises, the primary focus is on the detection mechanisms, the tools, and the standard operating procedures (SOPs) supporting the incident response efforts.
+ ** Red Team exercises** – During a Red Team exercise, the offense (*Red Team*) conducts a simulation to achieve a certain objective or set of objectives from a pre-determined scope. The defenders (*Blue Team*) will not necessarily have knowledge of the scope and duration of the exercise, which provides a more realistic assessment of how they would respond to an actual incident. Because Red Team exercises can be invasive tests, you should be cautious and implement controls to verify that the exercise does not cause actual harm to your environment.

**Note**
AWS requires customers to review the policy for penetration testing available on the [ Penetration Testing website](https://aws.amazon.com/security/penetration-testing/) before they conduct Purple Team or Red Team exercises.

 Table 1 summarizes a few key differences in these types of simulations. It’s important to note that the definitions are generally considered loose definitions and can be customized to fit the needs of your organization.

* Table 1 – Types of simulations*

|   |  Tabletop exercise  |  Purple Team exercise  |  Red Team exercise  |
| --- | --- | --- | --- |
|  Summary  |  Paper-driven exercises that focus on one specific security incident scenario. These can be either high-level or technical, and are driven by a series of paper injects.  |  A more realistic offering compared to tabletop exercises. During Purple Team exercises, facilitators work collaboratively with the participants to increase exercise engagement and offer training where necessary.  |  Generally a more advanced simulation offering. There is usually a high level of covertness, where the participants might not know all of the details of the exercise.  |
|  Resources required  |  Limited technical resources required  |  Various stakeholders required and high level of technical resources needed  |  Various stakeholders required and high level of technical resources needed  |
|  Complexity  |  Low  |  Medium  |  High  |

 Consider facilitating cyber simulations at a regular interval. Each exercise type can provide unique benefits to the participants and the organization as a whole, so you might choose to start with less complex simulation types (such as tabletop exercises) and progress to more complex simulation types (Red Team exercises). You should select a simulation type based on your security maturity, resources, and your desired outcomes. Some customers might not choose to perform Red Team exercises due to complexity and cost.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

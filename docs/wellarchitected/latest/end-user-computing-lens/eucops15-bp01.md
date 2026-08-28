---
source_url: https://docs.aws.amazon.com/wellarchitected/latest/end-user-computing-lens/eucops15-bp01.html
---

# EUCOPS15-BP01 Update your solution design documentation over time, and use version control to track changes
<a name="eucops15-bp01"></a>

 Keep key architectural designs, operations handbooks, and support guides up to date, maintaining a library of reference material that can be used by new personnel, partners, or other support teams.

 **Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance-17"></a>

 For both Amazon WorkSpaces and WorkSpaces Applications, each service should have been deployed based upon a design that resulted from the collected input of key technology and business stakeholders. Evolving the solution design should be managed in a similarly inclusive fashion. Agree and sign off on all changes to the initial design through a project board before updating the solution. This approach verifies that invested parties have validated the key metrics required to deliver the new service and that the updated solution meets the requirements of both technical and business stakeholders.

 Design documentation should be maintained as continually updated documents that represent the state of the AWS EUC service deployments over time. It should capture the rationale for each design decision in addition to the technical and architectural solutions deployed to achieve each requirement. Maintain iterative versions of the design as changes are made so that you can see a historical view of the deployment.

 A design document is an essential piece of knowledge collateral which is invaluable for training purposes, onboarding new technical team members, reviewing and implementing changes to the infrastructure, and when working with partners to integrate new technologies or handover support to new teams.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Well-Architected. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wellarchitected` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

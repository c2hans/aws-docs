---
source_url: https://docs.aws.amazon.com/wellarchitected/2023-04-10/framework/sec_appsec_train_for_application_security.html
---

This is an earlier version of the AWS Well-Architected Framework. For the latest version, see [AWS Well-Architected Framework](https://docs.aws.amazon.com/wellarchitected/latest/framework/welcome.html).

# SEC11-BP01 Train for application security
<a name="sec_appsec_train_for_application_security"></a>

 Provide training to the builders in your organization on common practices for the secure development and operation of applications. Adopting security focused development practices helps reduce the likelihood of issues that are only detected at the security review stage.

**Desired outcome:** Software should be designed and built with security in mind. When the builders in an organization are trained on secure development practices that start with a threat model, it improves the overall quality and security of the software produced. This approach can reduce the time to ship software or features because less rework is needed after the security review stage.

 For the purposes of this best practice, *secure development* refers to the software that is being written and the tools or systems that support the software development lifecycle (SDLC).

**Common anti-patterns:**
+  Waiting until a security review, and then considering the security properties of a system.
+  Leaving all security decisions to the security team.
+  Failing to communicate how the decisions taken in the SDLC relate to the overall security expectations or policies of the organization.
+  Engaging in the security review process too late.

**Benefits of establishing this best practice:**
+  Better knowledge of the organizational requirements for security early in the development cycle.
+  Being able to identify and remediate potential security issues faster, resulting in a quicker delivery of features.
+  Improved quality of software and systems.

**Level of risk exposed if this best practice is not established:** Medium

## Implementation guidance
<a name="implementation-guidance"></a>

 Provide training to the builders in your organization. Starting off with a course on [threat modeling](https://catalog.workshops.aws/threatmodel/en-US) is a good foundation for helping train for security. Ideally, builders should be able to self-serve access to information relevant to their workloads. This access helps them make informed decisions about the security properties of the systems they build without needing to ask another team. The process for engaging the security team for reviews should be clearly defined and simple to follow. The steps in the review process should be included in the security training. Where known implementation patterns or templates are available, they should be simple to find and link to the overall security requirements. Consider using [AWS CloudFormation,](https://aws.amazon.com/cloudformation/) [AWS Cloud Development Kit (AWS CDK) Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html), [Service Catalog](https://aws.amazon.com/servicecatalog/), or other templating tools to reduce the need for custom configuration.

### Implementation steps
<a name="implementation-steps"></a>
+  Start builders with a course on [threat modeling](https://catalog.workshops.aws/threatmodel/en-US) to build a good foundation, and help train them on how to think about security.
+  Provide access to [AWS Training and Certification](https://www.aws.training/LearningLibrary?query=&filters=Language%3A1%20Domain%3A27&from=0&size=15&sort=_score&trk=el_a134p000007C9OtAAK&trkCampaign=GLBL-FY21-TRAINCERT-800-Security&sc_channel=el&sc_campaign=GLBL-FY21-TRAINCERT-800-Security-Blog&sc_outcome=Training_and_Certification&sc_geo=mult), industry, or AWS Partner training.
+  Provide training on your organization's security review process, which clarifies the division of responsibilities between the security team, workload teams, and other stakeholders.
+  Publish self-service guidance on how to meet your security requirements, including code examples and templates, if available.
+  Regularly obtain feedback from builder teams on their experience with the security review process and training, and use that feedback to improve.
+  Use game days or bug bash campaigns to help reduce the number of issues, and increase the skills of your builders.

## Resources
<a name="resources"></a>

 **Related best practices:**
+  [SEC11-BP08 Build a program that embeds security ownership in workload teams](sec_appsec_build_program_that_embeds_security_ownership_in_teams.md)

 **Related documents:**
+  [AWS Training and Certification](https://www.aws.training/LearningLibrary?query=&filters=Language%3A1%20Domain%3A27&from=0&size=15&sort=_score&trk=el_a134p000007C9OtAAK&trkCampaign=GLBL-FY21-TRAINCERT-800-Security&sc_channel=el&sc_campaign=GLBL-FY21-TRAINCERT-800-Security-Blog&sc_outcome=Training_and_Certification&sc_geo=mult)
+  [How to think about cloud security governance](https://aws.amazon.com/blogs/security/how-to-think-about-cloud-security-governance/)
+  [How to approach threat modeling](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/)
+  [Accelerating training – The AWS Skills Guild](https://docs.aws.amazon.com/whitepapers/latest/public-sector-cloud-transformation/accelerating-training-the-aws-skills-guild.html)

 **Related videos:**
+  [Proactive security: Considerations and approaches](https://www.youtube.com/watch?v=CBrUE6Qwfag)

 **Related examples:**
+  [Workshop on threat modeling](https://catalog.workshops.aws/threatmodel)
+  [Industry awareness for developers](https://owasp.org/www-project-top-ten/)

 **Related services:**
+  [AWS CloudFormation](https://aws.amazon.com/cloudformation/)
+  [AWS Cloud Development Kit (AWS CDK) (AWS CDK) Constructs](https://docs.aws.amazon.com/cdk/v2/guide/constructs.html)
+  [Service Catalog](https://aws.amazon.com/servicecatalog/)
+  [AWS BugBust](https://docs.aws.amazon.com/codeguru/latest/bugbust-ug/what-is-aws-bugbust.html)

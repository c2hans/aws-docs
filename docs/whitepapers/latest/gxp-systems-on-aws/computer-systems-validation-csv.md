---
source_url: https://docs.aws.amazon.com/whitepapers/latest/gxp-systems-on-aws/computer-systems-validation-csv.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Computer Systems Validation (CSV)
<a name="computer-systems-validation-csv"></a>

 You must still perform computer systems validation activities even if an application is running in the cloud. In fact, the overarching qualification strategy we have laid out in this paper has ensured that this CSV process can fundamentally be the same as before and hasn’t become more difficult for the application development teams through the introduction of cloud technologies.

 However, with the solid foundation provided by AWS and the regulated landing zone we can shift the focus to improving a traditional CSV process.

 You typically have a Standard Operating Procedure (SOP) describing your Software Development Lifecycle (SDLC) which is often based on GAMP 5: A Risk-Based Approach to Compliant GxP Computerized Systems. Many SOPs we have seen involve a lot of manual work and approvals which slow down the process. The more automation that can be introduced, the quicker the process, and the lower the chances of human error.

 The automation of IT processes is nothing new and customers have been implementing automated toolchains for years for on-premises development. The move to cloud provides all those same capabilities but also introduces some additional opportunities, especially in the virtualized infrastructure areas.

 In this section we will focus primarily on those additional capabilities now available through the cloud.

## Automating Installation Qualification (IQ)
<a name="automating-installation-qualification-iq"></a>

 It’s important to note that even though we are qualifying the underlying building blocks, the application teams still need to validate their application including performing the installation qualification (IQ) as part of their normal CSV activities in order to demonstrate their application specific combination of infrastructure building blocks was deployed and is functioning as expected. However, they can focus on testing the interaction between building blocks rather than the functionality of each building block itself.

 As mentioned, the automation of the development toolchain is nothing new to any high performing engineering team. The use of CI/CD and automated testing tools has been around for a long time. What hasn’t been possible before is the fully automated deployment of infrastructure and execution of the Installation Qualification (IQ) step.

 The use of Infrastructure as Code opens up the possibility to automate the IQ step as described in this [blog post](https://aws.amazon.com/blogs/industries/approving-aws-services-for-gxp-workloads/). The controlled infrastructure template acts as the pre-approved specification which can be compared against the stacks deployed by AWS CloudFormation. Summary reports and test evidence can be created or, if a deviation is found, the stack can be rolled back to the last known good state.

 Assuming the IQ step completes successfully, the automation can continue to the automation of Operational Qualification (OQ) and Performance Qualification (PQ).

## Maintaining an Application’s Qualified State
<a name="maintaining-an-applications-qualified-state"></a>

 Of course, once an application has been deployed, it needs to be maintained under a state of control. However, a lot of the heavy lifting for things like change management, configuration management, security management, backup and restore have been built into the regulated landing zone for the benefit of all application teams.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

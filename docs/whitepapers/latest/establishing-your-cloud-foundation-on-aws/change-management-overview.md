---
source_url: https://docs.aws.amazon.com/whitepapers/latest/establishing-your-cloud-foundation-on-aws/change-management-overview.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Overview
<a name="change-management-overview"></a>

The purpose of change management is to control the lifecycles of all changes, allowing changes to be made with minimal interruption to IT services. Changes to an environment introduces risk. Authorized changes should be prioritized, planned, tested, implemented, documented, and reviewed to mitigate any risks before deployment.

The Change Management capability ensures that changes are understood, recorded, evaluated prior to, during, and after implementation. It also complements the process and safety controls of your continuous integration (CI) practices and Continuous Delivery/Deployment (CD) methodology. The Change Management capability is*** NOT*** intended for changes made as part of an automated release process, such as a CI/CD pipeline, unless there is an exception or approval required for major or broad changes.

[ITIL](https://docs.aws.amazon.com/whitepapers/latest/change-management-in-the-cloud/what-is-itil.html) defines change management as “the process responsible for controlling the Lifecycle of all Changes. The primary objective of change management is to enable beneficial changes to be made, with minimum disruption to IT Services.” Every change should deliver business value and the change management processes should be geared towards enabling that delivery. ITIL states a number of benefits for effective change management, including “reducing failed changes and therefore service disruption, defects and re-work” and “delivering change promptly to meet business timescales". (ITIL Service Transition, AXELOS, 2011, page 44)

The key concepts of change management remain the same in the cloud as on-premises. Change delivers business value and it should be delivered efficiently. Agile methodologies and the automation capabilities of the cloud go hand in hand with the core principles of change management as they are also designed to deliver business value quickly and efficiently. There are some key areas, such as the management of infrastructure with software defined solutions, that may require existing change processes to be modified to adapt to new methods of delivering change.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

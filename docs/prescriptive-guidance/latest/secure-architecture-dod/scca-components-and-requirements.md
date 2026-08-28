---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/secure-architecture-dod/scca-components-and-requirements.html
---

# SCCA components and requirements
<a name="scca-components-and-requirements"></a>

The Defense Information Systems Agency (DISA) Secure Cloud Computing Architecture (SCCA), adopted by the US Department of Defense (DoD), is intended to be a scalable, cost-effective approach for securing cloud-based applications under a common security architecture. It provides a standard approach for securing IL4 and IL5 data in cloud environments. As described in the [DISA SCCA fact sheet](https://www.disa.mil/~/media/files/disa/fact-sheets/secure-cloud-computing.pdf), the overarching components of the SCCA include:
+ **Cloud Access Point (CAP)** –** **Provides access to the cloud, and protects DoD networks from the cloud. Streamlined protections focused on protecting the network boundary.
+ **Virtual Data Center Security Stack (VDSS)** – Virtual network enclave security to protect applications and data in commercial cloud offerings.
+ **Virtual Data Center Managed Services (VDMS)** – Application host security for privileged user access in commercial environments.
+ **Trusted Cloud Credential Manager (TCCM)** – Cloud credential manager to enforce role-based access control (RBAC) and least-privileged access.

The following image shows these components of the SCCA.

![Components of the DISA SCCA.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-architecture-dod/images/guide-img/9ef8ed3c-685a-4e51-9cc4-4701568d9bae/images/d2627f2b-2e08-4a33-bc5d-e855d77f764a.png)

This section discusses each component in detail and the corresponding components in the LZA that can help you adhere to the Defense Information Systems Agency (DISA) standard. The following image shows the LZA multi-account structure that builds the components of the SCCA within the AWS Cloud. This LZA multi-account structure is a foundation that helps you achieve an architecture that is fully compliant with DISA SCCA requirements. For an example of an architecture that helps you fully meet compliance requirements, see the [SCCA on AWS GovCloud architecture diagram](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/dod-scca-multiaccount-ra.pdf).

![Architecture diagram of the multi-account structure deployed by using the Landing Zone Accelerator on AWS.](http://docs.aws.amazon.com/prescriptive-guidance/latest/secure-architecture-dod/images/guide-img/9ef8ed3c-685a-4e51-9cc4-4701568d9bae/images/f8b055db-9460-4575-8c13-4d2f38c43302.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/whitepapers/latest/logical-separation/drivers-for-physical-separation-requirements.html
---

 This whitepaper is for historical reference only. Some content might be outdated and some links might not be available.

# Drivers for Physical Separation Requirements
<a name="drivers-for-physical-separation-requirements"></a>

 Requirements for physically dedicated environments are primarily driven by concerns around third-party or unauthorized access to systems, applications, or data. There is a general misunderstanding that physically separated environments will provide better protection against unintended information or system disclosure, tampering, and unauthorized access compared to logically separated multi-tenant cloud environments. However, when examining the most common attack vectors for unauthorized access — such as remote exploitation, human error, and insider threat — a physically separated environment does not reduce the risk profile. In fact, for any system that is accessible over a network or the Internet, physical separation — such as placing them in a locked cage or a separate data center facility — does not inherently provide added security or control over the most important forms of access.

 Additionally, smaller physically separated environments do not have parity with generally available cloud environments; hence any physical separation requirement can limit or delay a customer’s ability to leverage innovative investments (including security feature innovations) made on behalf of all customers using AWS services. Disadvantages may include higher cost structure, extensive compliance timelines, and limited redundancy options and features compared with the geo-diversity of commercial data center regions.

 AWS addresses the concerns driving physical separation requirements through the logical security capabilities we provide customers and the security controls we have in place to help protect customer data. The strength of that isolation combined with the automation and flexibility that it provides is on par with or better than the security controls seen in traditional, physically separated environments.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Whitepapers. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query whitepapers` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

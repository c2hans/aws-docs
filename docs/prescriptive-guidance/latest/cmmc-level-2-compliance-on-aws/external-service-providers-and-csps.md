---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/cmmc-level-2-compliance-on-aws/external-service-providers-and-csps.html
---

# External service providers and CSPs
<a name="external-service-providers-and-csps"></a>

If your organization uses ESPs in your CUI environment, you must understand how they affect your CMMC assessment scope. An ESP is any external company that provides services to your organization. A CSP is an ESP that provides its own cloud services. A managed service provider (MSP) that provides technical support but does not host its own cloud platform is an ESP, not a CSP.

## FedRAMP requirements for CSPs
<a name="fed-ramp-requirements-for-csps"></a>

Per DFARS 252.204-7012, contractors using external cloud services to process, store, or transmit CUI must use a CSP that meets security requirements equivalent to the FedRAMP Moderate baseline.

|
|
| CSP environment | FedRAMP status | CMMC eligibility |
| --- |--- |--- |
| AWS GovCloud (US) | FedRAMP High authorized | Exceeds the Moderate requirement |
| AWS US East/West (Commercial) | FedRAMP Moderate authorized | Meets the requirement when properly configured |

If a CSP is not FedRAMP Authorized, it must demonstrate FedRAMP Moderate equivalency per DoD policy, including a Body of Evidence validated by a Third-Party Assessment Organization (3PAO) and approved by DIBCAC.

## Customer responsibility matrix requirements
<a name="customer-responsibility-matrix-requirements"></a>

Per 32 CFR Part 170, a CRM is required for every ESP. The CRM must:
+ Describe the responsibilities of your organization and the service provider
+ Be documented in or referenced by your SSP
+ Be up-to-date and address all in-scope CMMC requirements performed wholly, partially, or jointly by the provider
+ Be available for the Assessment Team to evaluate using examine, interview, and test methods

ESP respondents must demonstrate sufficient knowledge and credible ownership of CRM requirements during C3PAO interviews. This CRM requirement applies to all ESPs, not just CSPs.

## ESP assessment rules
<a name="esp-assessment-rules"></a>

The assessment treatment of an ESP depends on whether it is a CSP and whether it handles CUI:

|
|
| ESP type | CUI involvement | Assessment treatment |
| --- |--- |--- |
| CSP that processes/stores/transmits CUI | Yes | Must meet FedRAMP requirements. FedRAMP authorization is accepted as evidence; services are not directly assessed by C3PAO. CRM required. |
| CSP that does not handle CUI | No | Not required to meet FedRAMP. Services are still in your assessment scope. |
| Non-CSP ESP that handles CUI | Yes | Treated as an extension of your environment. ESP services are assessed within your CMMC scope against all applicable requirements. |
| Non-CSP ESP that does not handle CUI | No | Does not require its own CMMC assessment. Services are in your assessment scope. |
| Staff augmentation ESP | Varies | If you provide all processes, technology, and facilities, the ESP does not need a separate CMMC assessment. |

Your on-premises infrastructure connecting to any CSP or ESP is within the CMMC Assessment Scope and will be assessed regardless of the provider's own compliance status.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

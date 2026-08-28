---
source_url: https://docs.aws.amazon.com/connecthealth/latest/userguide/patient-engagement-overview.html
---

# Patient engagement agents
<a name="patient-engagement-overview"></a>

Amazon Connect Health provides two AI agents for patient engagement: the Patient verification agent and the Appointment management agent. These agents handle routine patient interactions through voice calls via Amazon Connect. They integrate with the Epic EHR in real time through FHIR R4 APIs and support intelligent escalation to human agents with full context preservation.

**Topics**
+ [Communication channels](#communication-channels)
+ [Configuring and testing patient engagement agents](configuring-testing-pe-agents.md)
+ [Patient verification agent](patient-verification-agent.md)
+ [Appointment management agent](appointment-management-agent.md)
+ [Patient profile](patient-profile.md)
+ [Agent customization](agent-customization.md)
+ [Sample contact flow](contact-flow-setup.md)
+ [Insurance verification integration](insurance-verification.md)
+ [Epic EHR integration](epic-ehr-integration.md)

## Communication channels
<a name="communication-channels"></a>

Amazon Connect Health patient engagement agents currently support the voice channel only through Amazon Connect. Web chat, SMS, and other digital channels are not supported in the current release.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

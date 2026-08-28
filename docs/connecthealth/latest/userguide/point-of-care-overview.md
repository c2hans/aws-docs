---
source_url: https://docs.aws.amazon.com/connecthealth/latest/userguide/point-of-care-overview.html
---

# Point of care agents
<a name="point-of-care-overview"></a>

Amazon Connect Health point of care features are AI-powered capabilities that streamline administrative workflows in outpatient clinical settings. Point of care agentic capabilities combine speech recognition, generative AI, and reasoning to reduce documentation burden for clinicians and back-office staff.

Point of care features operate within a domain that you provision in your AWS account. Each feature accepts inputs — such as a real-time audio stream of a patient-clinician conversation, patient context from the EHR, and a clinical note template — and produces structured outputs for provider review including clinical documentation, evidence mappings, and after-visit summaries.

At launch, point of care capabilities include patient insights and ambient documentation.

**Topics**
+ [Key concepts](#poc-key-concepts)
+ [Regional availability](#poc-regional-availability)
+ [Patient insights](patient-insights.md)
+ [Ambient documentation](ambient-documentation.md)

## Key concepts
<a name="poc-key-concepts"></a>

| Concept | Description |
| --- | --- |
| Domain | An isolated environment within your AWS account where you provision point of care agents. |
| Subscription | A configuration resource that associates a provider or session with an agent. Required for ambient documentation. |
| Template | A structured definition of the clinical note format. Used by ambient documentation to generate documentation. |
| Vended artifacts | The output files written to your Amazon S3 bucket, such as pre-visit summaries, transcripts, and clinical notes. |

## Regional availability
<a name="poc-regional-availability"></a>

Point of care agents are available in the following AWS Regions:
+ US East (N. Virginia) - `us-east-1`
+ US West (Oregon) - `us-west-2`

**Note**
Patient insights is available as a preview in both supported Regions. Ambient documentation is generally available in both supported Regions.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Health. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connecthealth` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

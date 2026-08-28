---
source_url: https://docs.aws.amazon.com/healthlake/latest/devguide/reference-healthlake-preloaded-data-types.html
---

# Synthea preloaded data types for HealthLake
<a name="reference-healthlake-preloaded-data-types"></a>

HealthLake supports only SYNTHEA as a preloaded data type. [Synthea](https://synthetichealth.github.io/synthea/) is a synthetic patient generator that models `Patient` medical history. It’s hosted in an open-source Git repository that allows HealthLake to generate a FHIR R4-compliant resource `Bundle` so that users can test models without using actual patient data.

The following resource types are available in preloaded HealthLake data stores. For more information about preloading HealthLake data stores with Synthea data, see [Creating a HealthLake data store](managing-data-stores-create.md).

**Note**
To view a full list of HealthLake-supported FHIR R4 resources, see [FHIR R4 supported resource types for HealthLake](reference-fhir-resource-types.md).

**Synthea FHIR resource types supported by HealthLake**

|  |  |
| --- |--- |
| AllergyIntolerance | Location |
| CarePlan | MedicationAdministration |
| CareTeam | MedicationRequest |
| Claim | Observation |
| Condition | Organization |
| Device | Patient |
| DiagnosticReport | Practitioner |
| Encounter | PractitionerRole |
| ExplanationofBenefit | Procedure |
| ImagingStudy | Provenance |
| Immunization |   |

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS HealthLake. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query healthlake` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

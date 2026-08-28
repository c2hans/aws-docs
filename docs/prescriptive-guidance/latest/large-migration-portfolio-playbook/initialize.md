---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/large-migration-portfolio-playbook/initialize.html
---

# Stage 1: Initializing a large migration
<a name="initialize"></a>

In the initialize stage, you define the runbooks that you use to complete a detailed portfolio assessment and wave plan in the implementation stage. If another team member is responsible for defining the runbooks in your large migration project, skip to [Stage 2: Implementing a large migration](implement.md), where you will use the runbooks to migrate waves of applications and servers. By documenting the decisions made in this stage, you create actionable runbooks. For example, making decisions about the following questions leads to standard procedures that you document in your portfolio runbooks:
+ What migration metadata is required, and how do you collect it?
+ How do you prioritize applications and perform deep dives?
+ How do you plan waves?

In stage 1, you spend a lot of time defining the rules and building the runbooks because the activities in the runbook are repeated many times in stage 2 to support the migration.

Stage 1 consists of the following tasks and steps:
+ [Task 1: Performing the initial discovery and validating the migration strategy](discovery.md)
  + [Step 1: Validate the discovery data](discovery.md#discovery-1)
  + [Step 2: Identify the business and technical drivers](discovery.md#discovery-2)
  + [Step 3: Validate the migration strategies](discovery.md#discovery-3)
  + [Step 4: Validate the migration patterns](discovery.md#discovery-4)
+ [Task 2: Defining processes for identifying, collecting, and storing metadata](metadata.md)
  + [Step 1: Define the required metadata](metadata.md#metadata-1)
  + [Step 2: Build the metadata storage and collection processes](metadata.md#metadata-2)
  + [Step 3: Document metadata requirements and collection processes in a runbook](metadata.md#metadata-3)
+ [Task 3: Defining the application prioritization process](prioritization.md)
  + [Step 1: Define the application prioritization process](prioritization.md#prioritization-1)
  + [Step 2: Define the application prioritization rules](prioritization.md#prioritization-2)
  + [Step 3: Finalize the application prioritization process](prioritization.md#prioritization-3)
+ [Task 4: Defining the application deep dive process](deep-dive.md)
  + [Step 1: Define the application workshop process](deep-dive.md#deep-dive-1)
  + [Step 2: Define the application mapping process](deep-dive.md#deep-dive-2)
  + [Step 3: (Optional) Define the application target state](deep-dive.md#deep-dive-3)
  + [Step 4: Finalize the application deep dive process](deep-dive.md#deep-dive-4)
+ [Task 5: Defining the wave planning process](wave-planning.md)
  + [Step 1: Define the move group process](wave-planning.md#wave-planning-1)
  + [Step 2: Define the wave planning selection criteria](wave-planning.md#wave-planning-2)
  + [Step 3: Finalize the wave planning process](wave-planning.md#wave-planning-3)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Prescriptive Guidance. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query prescriptive-guidance` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

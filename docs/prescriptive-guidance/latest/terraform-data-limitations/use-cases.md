---
source_url: https://docs.aws.amazon.com/prescriptive-guidance/latest/terraform-data-limitations/use-cases.html
---

# Use case examples
<a name="use-cases"></a>

This guide covers two sample use cases for working around Terraform limitations on AWS:
+ Using Terraform to manage revisions in AWS Batch job definitions
+ Using Terraform to address challenges when you deploy Amazon Bedrock agents

## Managing revisions in AWS Batch job definitions
<a name="batch-job-definitions"></a>

This example assumes that you're deploying batch jobs by using the AWS Batch service and using Terraform as an IaC tool.

### Challenge
<a name="challenge.da88afa7-9696-5142-894a-8b210795036f"></a>

AWS Batch creates a new revision of a job definition with each update, which leads to an accumulation of revisions over time. This can complicate resource management and create confusion about which revisions are current, especially in enterprise environments where job definitions are frequently updated and downstream resources require accurate references to the latest versions.

### Solution
<a name="solution.93324d15-d5b2-5967-a570-f5af85aba72a"></a>

The following Terraform code uses several key components to address AWS Batch revision management.

```
resource "terraform_data" "batch_job_definition_cleanup" {
  triggers_replace = {
    always_run = timestamp()
  }

  provisioner "local-exec" {
    command = "..."  # AWS CLI commands to list and de-register older revisions
  }
}
```

In this code:
+ `terraform_data` is combined with a `local-exec` provisioner to run AWS Command Line Interface (AWS CLI) commands during Terraform operations.
+ Timestamp triggers ensure that every `terraform apply` command runs the cleanup script.
+ AWS CLI integration queries AWS Batch for all active job definition revisions and deregisters older revisions.
+ You can add a custom retention configuration to the command section to specify how many recent revisions to preserve.

### Benefits
<a name="benefits.b38ffab7-d8f1-5062-a178-c058cd771b2b"></a>
+ **Simplified management**: Prevents accumulation of outdated revisions to job definitions.
+ **Clear references**: Maintains accurate pointers to current versions of job definitions.
+ **Resource optimization**: Reduces clutter in the AWS Batch environment.
+ **Automation**: Integrates cleanly with existing Terraform workflows.

This approach demonstrates how Terraform's extensibility features can overcome provider limitations while maintaining IaC best practices. You can use this solution as a template for similar scenarios where dynamic resource discovery and management are needed.

## Deploying Amazon Bedrock agents
<a name="bedrock-agents"></a>

This example assumes that you're deploying an Amazon Bedrock agent to automate your DevOps tasks and using Terraform as an IaC tool.

### Challenge
<a name="challenge.24f7f422-f3f5-5ff6-b6e5-84f58f2f42cb"></a>

Deploying Amazon Bedrock agents requires a robust, automated workflow that introduces the following technical challenges:
+ Complete agent preparation
+ Verified readiness state
+ Zero manual intervention
+ Consistent infrastructure deployment

### Solution
<a name="solution.5dbba94a-0b51-57d4-a708-c8729cd09e0c"></a>

The following Terraform code uses several key components to address Amazon Bedrock agent preparation.

```
resource "terraform_data" "prepare_agent" {
  triggers_replace = {
    agent_state = sha256(jsonencode(aws_bedrockagent_agent.example))
  }

  provisioner "local-exec" {
    command = "aws bedrock-agent prepare-agent --agent-id ${aws_bedrockagent_agent.example.agent_id}"
  }
}

resource "time_sleep" "prepare_agent_sleep" {
  create_duration = "5s"

  lifecycle {
    replace_triggered_by = [terraform_data.prepare_agent]
  }
}
```

In this code:
+ `terraform_data` is combined with a `local-exec` provisioner to run AWS CLI commands during Terraform operations. The `terraform_data` named `prepare_agent` uses an AWS CLI command in the provisioner `local-exec` to prepare the agent. This ensures that no manual interventions will be required in the console or AWS CLI command.
+ Agent triggers ensure that resource creation starts only after the completion of the `aws_bedrockagent_agent` resource.
+ `time_sleep` implements a delay to ensure seamless operations.

This simplistic deployment strategy for Amazon Bedrock agents establishes an initialization process that sleeps for 5 seconds while the agent is getting to the prepared state.

You can enhance this solution by introducing a wait (for example, 10 seconds) until the condition is met after agent creation. You can extend this solution further by implementing comprehensive status verification mechanisms that aim for complete agent readiness. For example, you can implement status checking to prevent premature alias generation and mitigate potential API failures. An adaptive retry mechanism with clearly defined maximum wait times and detailed error tracking will help you troubleshoot failures. Critical considerations include maintaining a consistent deployment process, supporting automated infrastructure setup, and providing transparent progress monitoring.

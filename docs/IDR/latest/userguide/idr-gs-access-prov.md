---
source_url: https://docs.aws.amazon.com/IDR/latest/userguide/idr-gs-access-prov.html
---

# Provision access for alarm ingestion to Incident Detection and Response
<a name="idr-gs-access-prov"></a>

**Note**
If you didn't create the service-linked role (SLR) during the IDR CLI onboarding, follow the steps below to manually provision access.

To allow AWS Incident Detection and Response to ingest alarms from your account, create the `AWSServiceRoleForHealth_EventProcessor` SLR. AWS assumes the SLR to create a Managed EventBridge rule in your account. The managed EventBridge rule sends notifications from your account to AWS Incident Detection and Response. For information about this SLR, including the associated AWS managed policy, see [Using service-linked roles for AWS Health](https://docs.aws.amazon.com/health/latest/ug/using-service-linked-roles.html) in the *AWS Health User Guide*.

You can create this service-linked role in your account by following the instructions in [Create service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *AWS Identity and Access Management User Guide*. Or, you can use the following AWS Command Line Interface (AWS CLI) command:

```
aws iam create-service-linked-role --aws-service-name event-processor.health.amazonaws.com
```

**Key outputs**
+ Successful creation of the service-linked role in your account.

**Note**
The service-linked role - AWSServiceRoleForHealth\_EventProcessor needs to be created in each account you will use to send alarms to AWS Incident Detection and Response.

**Related information**

For more information, see the following topics:
+ [Using service-linked roles for AWS Health](https://docs.aws.amazon.com/health/latest/ug/using-service-linked-roles.html)
+ [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role)
+ [AWS managed policy: AWSHealth\_EventProcessorServiceRolePolicy](https://docs.aws.amazon.com/health/latest/ug/security-iam-awsmanpol.html#security-iam-awsmanpol-Health_EventProcessorServiceRolePolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Incident Detection Response. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query IDR` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

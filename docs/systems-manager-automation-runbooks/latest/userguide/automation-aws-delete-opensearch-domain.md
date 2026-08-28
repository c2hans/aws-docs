---
source_url: https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-delete-opensearch-domain.html
---

# `AWSConfigRemediation-DeleteOpenSearchDomain`
<a name="automation-aws-delete-opensearch-domain"></a>

 **Description**

 The `AWSConfigRemediation-DeleteOpenSearchDomain` runbook deletes the given Amazon OpenSearch Service domain using the [DeleteDomain](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/configuration-api.html#configuration-api-actions-deletedomain) API.

 [Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSConfigRemediation-DeleteOpenSearchDomain)

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**
+ DomainName

  Type: String

  Allowed values: (\\d{12}/)?[a-z]{1}[a-z0-9-]{2,28}

  Description: (Required) The name of the Amazon OpenSearch Service domain that you want to delete.
+ AutomationAssumeRole

  Type: String

  Description: (Required) The Amazon Resource Name (ARN) of the AWS Identity and Access Management (IAM) role that allows Systems Manager Automation to perform the actions on your behalf.

**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to use the runbook successfully.
+  `ssm:StartAutomationExecution`
+  `ssm:GetAutomationExecution`
+  `es:DeleteDomain`
+  `es:DescribeDomain`

 **Document Steps**
+  `aws:executeScript` - Accepts the Amazon OpenSearch Service domain name as input, deletes it, and verifies the deletion.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager Automation Runbook Reference. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query systems-manager-automation-runbooks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appintegrations-application-approved-origins-check.html
---

# appintegrations-application-approved-origins-check
<a name="appintegrations-application-approved-origins-check"></a>

Checks that Amazon AppIntegrations applications do not contain approved origins. The rule is NON\_COMPLIANT if configuration.ApplicationSourceConfig.ExternalUrlConfig.ApprovedOrigins is not an empty list.

**Identifier:** APPINTEGRATIONS\_APPLICATION\_APPROVED\_ORIGINS\_CHECK

**Resource Types:** AWS::AppIntegrations::Application

**Trigger type:** Configuration changes

**AWS Region:** Only available in Africa (Cape Town), Europe (Frankfurt), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

allowedApprovedOrigins (Optional)Type: CSV
Comma-separated list of approved origins that are allowed to access the application. If provided, the rule is NON\_COMPLIANT if configuration.ApplicationSourceConfig.ExternalUrlConfig.ApprovedOrigins contains origins not specified in this parameter.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d119c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

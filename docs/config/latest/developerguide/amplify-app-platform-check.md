---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/amplify-app-platform-check.html
---

# amplify-app-platform-check
<a name="amplify-app-platform-check"></a>

Checks if AWS Amplify apps are configured with the specified platform. The rule is NON\_COMPLIANT if configuration.Platform is a value not specified in the required rule parameter.

**Identifier:** AMPLIFY\_APP\_PLATFORM\_CHECK

**Resource Types:** AWS::Amplify::App

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), Asia Pacific (Hyderabad), Asia Pacific (Malaysia), Asia Pacific (Melbourne), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), Europe (Spain), China (Ningxia), Europe (Zurich) Region

**Parameters:**

approvedPlatformType: String
The approved platform for the rule to check. The rule is NON\_COMPLIANT if configuration.Platform is a value not specified in this parameter. Valid values include: 'WEB', 'WEB\_DYNAMIC', and 'WEB\_COMPUTE'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7c39c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

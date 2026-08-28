---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/appflow-flow-trigger-type-check.html
---

# appflow-flow-trigger-type-check
<a name="appflow-flow-trigger-type-check"></a>

Checks if an Amazon AppFlow flow runs using the specified trigger type. The rule is NON\_COMPLAINT if the flow does not run using the flow type specified in the required rule parameter.

**Identifier:** APPFLOW\_FLOW\_TRIGGER\_TYPE\_CHECK

**Resource Types:** AWS::AppFlow::Flow

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), Europe (Paris), US East (Ohio), Africa (Cape Town), Europe (Ireland), Europe (Frankfurt), South America (Sao Paulo), US East (N. Virginia), Asia Pacific (Seoul), Europe (London), Asia Pacific (Tokyo), US West (Oregon), US West (N. California), Asia Pacific (Singapore), Asia Pacific (Sydney), Canada (Central) Region

**Parameters:**

triggerTypeType: CSV
Comma-separated list of trigger types for the rule to check. Valid values include: 'Scheduled', 'Event', and 'OnDemand'.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d117c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

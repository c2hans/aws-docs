---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/healthlake-fhirdatastore-tagged.html
---

# healthlake-fhirdatastore-tagged
<a name="healthlake-fhirdatastore-tagged"></a>

Checks if Amazon HealthLake FHIRDatastores have tags. Optionally, required tag keys can be specified. The rule is NON\_COMPLIANT if there are no tags or if the specified tag keys are not present. The rule does not consider tags starting with `aws:`.

**Identifier:** HEALTHLAKE\_FHIRDATASTORE\_TAGGED

**Resource Types:** AWS::HealthLake::FHIRDatastore

**Trigger type:** Configuration changes

**AWS Region:** Only available in Asia Pacific (Mumbai), US East (Ohio), US East (N. Virginia), US West (Oregon) Region

**Parameters:**

requiredKeyTags (Optional)Type: CSV
Comma-separated list of tag keys for the rule to check. If provided, the rule is NON\_COMPLIANT if the evaluated resource does not contain these keys. Tag keys are case-sensitive. Tag keys starting with 'aws:' are not allowed.

## AWS CloudFormation template
<a name="w2aac20c16c17b7d913c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

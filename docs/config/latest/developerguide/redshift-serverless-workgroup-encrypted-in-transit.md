---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-serverless-workgroup-encrypted-in-transit.html
---

# redshift-serverless-workgroup-encrypted-in-transit
<a name="redshift-serverless-workgroup-encrypted-in-transit"></a>

Checks if AWS Redshift Serverless workgroups have the require\_ssl config parameter set to true. The rule is NON\_COMPLIANT if require\_ssl is set to false.

**Identifier:** REDSHIFT\_SERVERLESS\_WORKGROUP\_ENCRYPTED\_IN\_TRANSIT

**Resource Types:** AWS::RedshiftServerless::Workgroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1325c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

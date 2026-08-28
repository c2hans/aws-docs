---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/redshift-serverless-workgroup-routes-within-vpc.html
---

# redshift-serverless-workgroup-routes-within-vpc
<a name="redshift-serverless-workgroup-routes-within-vpc"></a>

Checks if Amazon Redshift Serverless workgroups route the network traffic through a VPC. The rule is NON\_COMPLIANT if workgroups have 'Turn on Enhanced VPC routing' disabled.

**Identifier:** REDSHIFT\_SERVERLESS\_WORKGROUP\_ROUTES\_WITHIN\_VPC

**Resource Types:** AWS::RedshiftServerless::Workgroup

**Trigger type:** Periodic

**AWS Region:** All supported AWS regions except Middle East (Bahrain), Asia Pacific (Jakarta), Africa (Cape Town), Middle East (UAE), South America (Sao Paulo), Asia Pacific (Hong Kong), Asia Pacific (Hyderabad), Asia Pacific (Osaka), Asia Pacific (Melbourne), Europe (Milan), AWS GovCloud (US-East), AWS GovCloud (US-West), Israel (Tel Aviv), Canada West (Calgary) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7e1329c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

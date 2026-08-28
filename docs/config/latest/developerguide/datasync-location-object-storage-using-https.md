---
source_url: https://docs.aws.amazon.com/config/latest/developerguide/datasync-location-object-storage-using-https.html
---

# datasync-location-object-storage-using-https
<a name="datasync-location-object-storage-using-https"></a>

Checks if AWS DataSync location object storage servers use the HTTPS protocol to communicate. The rule is NON\_COMPLIANT if configuration.ServerProtocol is not 'HTTPS'.

**Identifier:** DATASYNC\_LOCATION\_OBJECT\_STORAGE\_USING\_HTTPS

**Resource Types:** AWS::DataSync::LocationObjectStorage

**Trigger type:** Configuration changes

**AWS Region:** All supported AWS regions except Asia Pacific (New Zealand), China (Beijing), Asia Pacific (Thailand), Asia Pacific (Malaysia), AWS GovCloud (US-East), AWS GovCloud (US-West), Mexico (Central), Israel (Tel Aviv), Asia Pacific (Taipei), Canada West (Calgary), China (Ningxia) Region

**Parameters:**

None

## AWS CloudFormation template
<a name="w2aac20c16c17b7d439c19"></a>

To create AWS Config managed rules with AWS CloudFormation templates, see [Creating AWS Config Managed Rules With AWS CloudFormation Templates](aws-config-managed-rules-cloudformation-templates.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

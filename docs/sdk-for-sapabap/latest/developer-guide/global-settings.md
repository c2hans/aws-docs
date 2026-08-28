---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/global-settings.html
---

# Global settings
<a name="global-settings"></a>

Use `/n/AWS1/IMG` IMG transacation for AWS SDK for SAP ABAP, and Custom Business Configuration application for AWS SDK for SAP ABAP - BTP edition to configure the global settings. This topic uses IMG and Custom Business Configuration interchangeably.

This section covers the following topics.

**Topics**
+ [Technical settings](#technical-settings)
+ [Configure scenarios](#configure-scenarios)

## Technical settings
<a name="technical-settings"></a>

The Global settings of `/AWS1/IMG` transaction affect the behavior of the entire SDK. These settings are generally configured by a Basis administrator. You can set these values to the following recommended settings.
+ Select **New Entries**.
  + **S3 regionalization**: Access us-east-1 buckets by using [s3.amazonaws.com](http://s3.amazonaws.com).
  + **STS regionalization**: Access STS by using global endpoint.
  + **Disable EC2 metadata**: Keep this field blank. This field is read-only in the BTP edition, and is set to 'Yes' by default.
  + **Metadata Endpt Mode**: Use IPv4 metadata endpoint. This field is read-only in the BTP edition, and is auto-updated.
  + **Metadata Endpt URL**: Keep this field blank. This field is read-only in the BTP edition.
+ Select **Save**.

## Configure scenarios
<a name="configure-scenarios"></a>

Scenarios enable AWS SDK to more efficiently switch settings during a multi-Region disaster testing or disaster recovery testing scenario. You may not need this feature, and instead need only to configure the following DEFAULT scenario.
+ Select **New Entries**.
  + Scenario ID:`DEFAULT`
  + Scenario Description: Default Scenario
+ Select **Save**.

If you have a multi-Region disaster recovery setup or other unique cases that require a quick change of settings, then you can configure multiple scenarios.
+  `DEFAULT` - Standard operation.
+  `DR` - Special configuration if a disaster requires moving the entire system to another Region.
+  `DR_TEST` - Special configuration for simulating a disaster, for example, in a temporary clone of production.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

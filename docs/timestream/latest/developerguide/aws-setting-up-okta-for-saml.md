---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/aws-setting-up-okta-for-saml.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# Setting up Okta for SAML
<a name="aws-setting-up-okta-for-saml"></a>

1. Choose the **Sign On** tab. Choose the **View**.

1. Choose the **Setup Instructions** button in the **Settings** section.

**Finding the Okta metadata document**

1. To find the document, go to:

   ```
   https://<domain>-admin.okta.com/admin/apps/active
   ```
**Note**
 <domain> is your unique domain name for your Okta account.

1. Choose the **AWS Account Federation** application

1. Choose the **Sign On** tab

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

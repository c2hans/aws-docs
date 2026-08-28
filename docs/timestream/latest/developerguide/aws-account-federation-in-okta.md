---
source_url: https://docs.aws.amazon.com/timestream/latest/developerguide/aws-account-federation-in-okta.html
---

For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](https://docs.aws.amazon.com/timestream/latest/developerguide/timestream-for-influxdb.html).

# AWS account federation in Okta
<a name="aws-account-federation-in-okta"></a>

The Timestream for LiveAnalytics JDBC driver supports AWS Account Federation in Okta. To set up AWS Account Federation in Okta, complete the following steps:

1. Sign in to the Okta Admin dashboard using the following URL:

   ```
   https://<company-domain-name>-admin.okta.com/admin/apps/active
   ```
**Note**
 Replace **<company-domain-name>** with your domain name.

1. Upon successful sign-in, choose** Add Application** and search for **AWS Account Federation**.

1. Choose **Add**

1. Change the Login URL to the appropriate URL.

1. Choose **Next**

1. Choose **SAML 2.0** As the **Sign-On** method

1. Choose **Identity Provider metadata** to open the metadata XML file. Save the file locally.

1. Leave all other configuration options blank.

1. Choose **Done**

Now that you have completed AWS Account Federation in Okta, you may proceed to [Setting up Okta for SAML](aws-setting-up-okta-for-saml.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Timestream. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query timestream` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

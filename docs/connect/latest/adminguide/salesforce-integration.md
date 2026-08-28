---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/salesforce-integration.html
---

# Embed the Connect Customer Contact Control Panel (CCP) into Salesforce
<a name="salesforce-integration"></a>

The core functionality of the Connect Customer CTI Adapter provides a WebRTC browser-based Contact Control Panel (CCP) within Salesforce. The Connect Customer CTI integration consists of two components:
+ [A managed Salesforce package](https://appexchange.salesforce.com/appxListingDetail?listingId=a0N3A00000EJH4yUAH)
+ [An AWS Serverless application deployed to your AWS environment](https://serverlessrepo.aws.amazon.com/applications/arn:aws:serverlessrepo:us-west-2:821825267871:applications~AmazonConnectSalesforceLambda)

 For a detailed walk-through and setup of the full CTI Adapter capabilities for Salesforce Lightning, see the [Connect Customer CTI Adapter for Salesforce Lightning installation guide](https://amazon-connect.github.io/amazon-connect-salesforce-cti/docs/lightning/notices/).

 For the CTI Adapter for Salesforce Classic, see the [Connect Customer CTI Adapter for Salesforce Classic installation guide](https://amazon-connect.github.io/amazon-connect-salesforce-cti/docs/classic/notices/).

We recommend that you initially install the package into your Salesforce sandbox. After the package is installed, you can configure your Salesforce Call Center configuration within Salesforce.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/glue/latest/dg/connecting-to-data-salesforce.html
---

# Connecting to Salesforce
<a name="connecting-to-data-salesforce"></a>

Salesforce provides customer relationship management (CRM) software that help you with sales, customer service, e-commerce, and more. If you're a Salesforce user, you can connect AWS Glue to your Salesforce account. Then, you can use Salesforce as a data source or destination in your ETL Jobs. Run these jobs to transfer data between Salesforce and AWS services or other supported applications.

**Topics**
+ [AWS Glue support for Salesforce](salesforce-support.md)
+ [Policies containing the API operations for creating and using connections](salesforce-configuring-iam-permissions.md)
+ [Configuring Salesforce](salesforce-configuring.md)
+ [Apply System Admin profile](#salesforce-configuring-apply-system-admin-profile)
+ [Configuring Salesforce connections](salesforce-configuring-connections.md)
+ [Reading from Salesforce](salesforce-reading-from-entities.md)
+ [Writing to Salesforce](salesforce-writing-to.md)
+ [Salesforce connection options](salesforce-connection-options.md)
+ [Limitations for the Salesforce connector](salesforce-connector-limitations.md)
+ [Set up the Authorization Code flow for Salesforce](salesforce-setup-authorization-code-flow.md)
+ [Set up the JWT bearer OAuth flow for Salesforce](salesforce-setup-jwt-bearer-oauth.md)

## Apply System Admin profile
<a name="salesforce-configuring-apply-system-admin-profile"></a>

 In Salesforce, follow the steps to apply the System Admin profile:

1.  In Salesforce, navigate to **Settings > Connected Apps > Connected Apps OAuth Usage**.

1.  In the list of connected apps, find AWS Glue and choose **Install**. If needed, choose **Unblock**.

1.  Navigate to **Settings > Manage Connected Apps then choose AWS Glue**. Under OAuth Policies, choose **Admin approved users are pre-authorized** and select the **System Admin** profile. This action restricts access to AWS Glue only to users with the System Admin profile.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Glue. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query glue` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

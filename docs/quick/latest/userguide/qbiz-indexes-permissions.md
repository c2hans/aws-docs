---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/qbiz-indexes-permissions.html
---

# Setting up permissions
<a name="qbiz-indexes-permissions"></a>

To use Amazon Q Business indexes in Amazon Quick, you need to set up the appropriate permissions based on your implementation method:

## Initial Setup
<a name="initial-setup"></a>

1. Sign in to the Amazon Quick console as an administrator.

1. Navigate to the **Admin** section.

1. Select **AWS Resources**.

1. Choose **Amazon Q Business** from the list of available data sources.

1. Choose **Select Applications**.

## Application Setup
<a name="application-setup"></a>

You can either connect to an existing Amazon Q Business application or create a new one:

1. Choose one of the following options:
   + **Connect to existing Amazon Q Business application** - Select an existing application from your account.
   + **Create new Amazon Q Business application** - Create a new application. The new application will use the same authentication used by your Amazon Quick instance setup.

1. For new applications, the system automatically configures authentication based on your Amazon Quick instance setup.

1. Wait for application creation to complete.

1. You will be redirected to the Amazon Q Business application to configure indexes and data sources.

## Access Management by Implementation
<a name="access-management"></a>

**IDC Implementation**
+ Access is managed through AWS Identity Center.
+ Access to the Amazon Q Business application is managed through the Amazon Q Business console.

**Non-IDC Implementation**
+ All Amazon Quick users automatically gain access to connected Amazon Q Business indexes.
+ No additional access management required in Amazon Q Business.

Once permissions are set up, you can use your Amazon Q Business index as a knowledge base in Amazon Quick, and Admin users can create knowledge bases from Amazon Q Business indexes.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

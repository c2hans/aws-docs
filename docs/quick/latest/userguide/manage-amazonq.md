---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/manage-amazonq.html
---

# Manage Amazon Q permissions
<a name="manage-amazonq"></a>

Amazon Q is an AI-powered capability in Amazon Quick that enhances your data analysis experience. Quick admins can manage Amazon Q permissions in the Quick administration console. These permissions control how Amazon Q interacts with your data and users.

**Topics**
+ [Manage personalization permissions](#q-manage-personalization-permissions)
+ [Manage dashboard and visual indexing for search](#q-manage-dashboard-visual-indexing-for-search)
+ [Manage Dashboard Q&A](#q-manage-dashboard-qa)

## Manage personalization permissions
<a name="q-manage-personalization-permissions"></a>

Amazon Q can use user metadata to provide more context-aware responses. This feature allows for a more personalized experience when interacting with Amazon Q.

**To manage personalization permissions:**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Choose the user icon at the top right, and then choose **Manage Quick**.

1. Under the **Account** section, choose **Amazon Q**.

1. Locate the **Manage personalization permissions** section.

1. Use the toggle switch next to **Personalized responses** to enable or disable this feature.

When enabled, Amazon Q can read user metadata to tailor its responses to individual users. This may include considering the user's role, location, or prior documents when providing information or suggestions.

## Manage dashboard and visual indexing for search
<a name="q-manage-dashboard-visual-indexing-for-search"></a>

Amazon Q can index information from dashboards to make them easily searchable across applications. This feature enhances the discoverability of your dashboards and their contents.

**To manage dashboard and visual indexing:**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Choose the user icon at the top right, and then choose **Manage Amazon Quick**.

1. Under the **Account** section, choose **Amazon Q**.

1. Locate the **Manage dashboard and visual indexing for search** section.

1. Use the toggle switch next to **Dashboard & visual indexing** to enable or disable this feature.

When enabled, Amazon Q can read dashboard metadata and visual information such as keywords, data fields, and refresh times to quickly respond to queries.

## Manage Dashboard Q&A
<a name="q-manage-dashboard-qa"></a>

The Dashboard Q&A feature allows Amazon Q to answer questions about your data without requiring the use of Quick Topics. This provides a more flexible and intuitive way for users to interact with their dashboards.

**To manage Dashboard Q&A:**

1. Open the [Quick console](https://quicksight.aws.amazon.com/).

1. Choose the user icon at the top right, and then choose **Manage Amazon Quick**.

1. Under the **Account** section, choose **Amazon Q**.

1. Locate the **Manage Dashboard Q&A** section.

1. Use the toggle switch next to **Dashboard Q&A** to enable or disable this feature.

When enabled, Amazon Q can read dashboard metadata and visual information such as keywords, data fields, and refresh times to quickly respond to queries. This will eliminate the need for predefined Quick Topics.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

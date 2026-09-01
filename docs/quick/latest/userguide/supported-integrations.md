---
source_url: https://docs.aws.amazon.com/quick/latest/userguide/supported-integrations.html
---

# Supported integrations
<a name="supported-integrations"></a>

Amazon Quick supports integrations with various third-party applications and services. Each integration supports different combinations of actions and knowledge base creation capabilities. The following table shows the supported integrations and their capabilities.

**Supported Integration Capabilities**

| Integration | Actions | Knowledge Base |
| --- | --- | --- |
| Adobe Marketing Agent | ✓ | — |
| Airtable | ✓ | — |
| Amazon S3 | ✓ | ✓ |
| Asana | ✓ | — |
| Atlassian Confluence Cloud | ✓ | ✓ |
| Atlassian Jira Cloud | ✓ | — |
| AWS Agent Registry | ✓ | — |
| BambooHR | ✓ | — |
| Box | ✓ | — |
| Canva | ✓ | — |
| Cisco Webex Meetings | ✓ | — |
| Cisco Webex Video Messaging | ✓ | — |
| Dropbox | ✓ | — |
| Dun & Bradstreet | ✓ | — |
| Figma | ✓ | — |
| GitHub | ✓ | — |
| Gmail | ✓ | — |
| Google Analytics | ✓ | — |
| Google Calendar | ✓ | — |
| Google Chat | ✓ | — |
| Google Docs | ✓ | — |
| Google Drive | ✓ | ✓ |
| Google Meet | ✓ | — |
| Google Sheets | ✓ | — |
| Google Slides | ✓ | — |
| HG Insights | ✓ | — |
| HubSpot | ✓ | — |
| HuggingFace | ✓ | — |
| Intercom | ✓ | — |
| Linear | ✓ | — |
| Microsoft OneDrive | ✓ | ✓ |
| Microsoft OneNote | ✓ | — |
| Microsoft Outlook | ✓ | — |
| Microsoft SharePoint Online | ✓ | ✓ |
| Microsoft Teams | ✓ | — |
| Model Context Protocol (MCP) | ✓ | — |
| Monday.com | ✓ | — |
| Moodys GenAI Ready Data | ✓ | — |
| New Relic | ✓ | — |
| Notion | ✓ | — |
| OpenAPI Specification | ✓ | — |
| PagerDuty | ✓ | — |
| QuickBooks | ✓ | — |
| REST API | ✓ | — |
| Salesforce | ✓ | — |
| SAP Bill of Materials | ✓ | — |
| SAP Business Partner | ✓ | — |
| SAP Material Stock | ✓ | — |
| SAP Physical Inventory Docs | ✓ | — |
| SAP Product Master | ✓ | — |
| ServiceNow | ✓ | — |
| Shopify | ✓ | — |
| Slack | ✓ | — |
| Smartsheet | ✓ | — |
| Snowflake Cortex Agent | ✓ | — |
| Visier Agent | ✓ | — |
| Web Crawler | — | ✓ |
| WhatsApp | ✓ | — |
| Zapier | ✓ | — |
| Zendesk Suite | ✓ | — |
| Zoom | ✓ | — |
| ZoomInfo | ✓ | — |

**Note**
Not all applications support all integration types. The available options depend on the capabilities of each specific application and your user role.

## Integration capability definitions
<a name="integration-capability-definitions"></a>

**Actions**
Call APIs and perform actions in external applications directly from Amazon Quick. You can share action connectors with other users and use them in automated workflows.

**Knowledge base**
Create searchable repositories of information from external sources. Knowledge bases are children of data access integrations. Add them to spaces or use them directly in chat agents.

## Authentication method definitions
<a name="authentication-method-definitions"></a>

**User auth**
Custom user-based OAuth authentication requiring base URL, client ID, client secret, token URL, auth URL, and redirect URL.

**Service auth**
Service-to-service authentication using either API key (with base URL and email) or service-to-service OAuth (with base URL, client ID, client secret, and token URL).

**Managed OAuth 2.0**
Managed OAuth 2.0 authentication flow with provider-specific sign-in interface.

**AWS credentials**
AWS-specific authentication using AWS access keys and permissions.

**Basic auth**
Username and password authentication.

**Form/SAML auth**
Form-based or SAML authentication with configurable field selectors.

**JSON schema**
Schema-based authentication for OpenAPI specifications.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quick` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

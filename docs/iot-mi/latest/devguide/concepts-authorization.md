---
source_url: https://docs.aws.amazon.com/iot-mi/latest/devguide/concepts-authorization.html
---

# Authorization
<a name="concepts-authorization"></a>

C2C connectors can support OAuth 2.0 authorization, General Authorization, or both. The authorization type determines how your connector authenticates with the third-party platform and manages access to end user devices.

**OAuth 2.0 Authorization**
OAuth 2.0 provides user-level authorization through account linking. Each end user authenticates with the third-party platform and grants permission for the connector to access their devices. This ensures that device access is scoped to individual user accounts with explicit user consent.

**General Authorization**
General Authorization uses credentials such as API keys or tokens stored in AWS Secrets Manager. A single set of credentials can control devices across multiple end users. This approach is useful when the third-party platform doesn't support OAuth 2.0 or when you need to manage devices at scale without individual user authorization flows.

**Note**
Your connector can implement both authorization types in parallel, providing compatibility with diverse authorization frameworks.

**Topics**
+ [OAuth 2.0 requirements for account linking](concepts-account-linking.md)
+ [General/Custom Authorization requirements for connector developers](concepts-general-authorization-dev.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Managed integrations. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-mi` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

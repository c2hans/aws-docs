---
source_url: https://docs.aws.amazon.com/location/latest/developerguide/auth-concept-overview.html
---

# Authentication overview
<a name="auth-concept-overview"></a>

Amazon Location Service supports three authentication methods, each designed for different use cases. They differ in the APIs they can access, complexity, flexibility, and intended audience.

**API keys**
A plain text token that grants read-only access to Maps, Places, and Routes APIs without requiring user authentication. API keys are the simplest way to enable anonymous access in client-side applications such as web pages and mobile apps.

**Amazon Cognito**
An AWS identity service that provides temporary, scoped credentials for both authenticated and unauthenticated users. Amazon Cognito supports all Amazon Location Service APIs and enables richer authorization policies, including access to Geofences and Trackers.

**AWS Identity and Access Management (IAM)**
The AWS access management service for server-side applications, internal tools, and administrative operations. IAM provides full control over permissions using policies, roles, and temporary credentials via AWS STS.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

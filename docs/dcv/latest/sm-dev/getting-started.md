---
source_url: https://docs.aws.amazon.com/dcv/latest/sm-dev/getting-started.html
---

# Getting started with Session Manager API
<a name="getting-started"></a>

The Amazon DCV Session Manager API provides an automated interface for managing remote desktop sessions. Through this API, developers can create, list, start, stop, and otherwise control DCV sessions programmatically. This allows for the integration of Amazon DCV functionality into custom applications and workflows. By leveraging this API, organizations can streamline the management of remote visualization workloads, automating many common tasks.

Before you can start making calls to the Amazon DCV API, you'll need to obtain an access token that authenticates your application and authorizes it to access the necessary resources. The Amazon DCV API uses OAuth 2.0 for authentication, so you'll need to register your application and retrieve the necessary credentials. Once you have your access token, you can start sending requests to the Amazon DCV API endpoints to begin processing data.

**Topics**
+ [Step 1: Generate your API client](client-sdk.md)
+ [Step 2: Register your client API](credentials.md)
+ [Step 3: Get an access token and make an API request](request.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DCV. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query dcv` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

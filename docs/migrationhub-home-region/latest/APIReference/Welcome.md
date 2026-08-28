---
source_url: https://docs.aws.amazon.com/migrationhub-home-region/latest/APIReference/Welcome.html
---

# Welcome
<a name="Welcome"></a>

The AWS Migration Hub home region APIs are available specifically for working with your Migration Hub home region. You can use these APIs to determine a home region, as well as to create and work with controls that describe the home region.
+ You must make API calls for write actions (create, notify, associate, disassociate, import, or put) while in your home region, or a `HomeRegionNotSetException` error is returned.
+ API calls for read actions (list, describe, stop, and delete) are permitted outside of your home region.
+ If you call a write API outside the home region, an `InvalidInputException` is returned.
+ You can call `GetHomeRegion` action to obtain the account's Migration Hub home region.

For specific API usage, see the sections that follow in this AWS Migration Hub Home Region API reference.

This document was last published on August 28, 2026.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Migration Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query migrationhub-home-region` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

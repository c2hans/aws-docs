---
source_url: https://docs.aws.amazon.com/connect/latest/adminguide/enable-qr-search.html
---

# Enable Connect Customer quick responses in a custom Contact Control Panel (CCP)
<a name="enable-qr-search"></a>

To enable your agents to use quick responses for an embedded or custom CCP, you use the [ Connect Customer Streams library](https://github.com/amazon-connect/amazon-connect-streams) on GitHub to call the [SearchQuickResponse](https://docs.aws.amazon.com/amazon-q-connect/latest/APIReference/API_SearchQuickResponses.html) API and return a list of quick response search results to CCP. For more information, see [Connect Customer Streams Documentation](https://github.com/amazon-connect/amazon-connect-streams/blob/master/Documentation.md#quick-responses-apis) on Github.

**Note**
To prevent search API misuse, we implemented default values for the following request parameters:
`debounceTime` – 250ms between subsequent `SearchQuickResponse` API calls
`maxSearchResults` – 25
Search priority order:
`shortcut key`
`name`
`content`
`description`

For information about the agent's experience using quick responses, see [Search for quick responses to customers](search-qr-ccp.md).

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

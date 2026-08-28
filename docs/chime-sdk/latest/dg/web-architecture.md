---
source_url: https://docs.aws.amazon.com/chime-sdk/latest/dg/web-architecture.html
---

# Understanding web application architecture for the Amazon Chime SDK
<a name="web-architecture"></a>

You can serve your web application from a content delivery network, and load it when the user navigates to a URL in a browser. You can also wrap it in a platform-native Electron application that the user installs on their machine.

To join a new or existing meeting, the web application makes REST requests to the server application. Typically, the requests carry an authorization token or a cookie that your application uses for other API requests. You can also design your web client to send a region hint to the server, which the latter can use when providing the MediaRegion parameter to [chime:CreateMeeting](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_CreateMeeting.html). Your web application can determine the closest media services region by making an HTTP GET request to the [ https://nearest-media-region.l.chime.aws ](https://nearest-media-region.l.chime.aws/) endpoint.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Chime SDK. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query chime-sdk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

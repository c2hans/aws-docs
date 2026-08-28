---
source_url: https://docs.aws.amazon.com/gameliftstreams/latest/developerguide/sdk.html
---

# Amazon GameLift Streams backend service and web client
<a name="sdk"></a>

 Amazon GameLift Streams enables you to stream applications through a web browser. With the Amazon GameLift Streams Web SDK, you can set up a backend streaming service. Then, end users connect to a stream through a web client. They can play your game or interact with your application all through the cloud.

 The Amazon GameLift Streams Web SDK includes a sample backend server and a sample web client, which you can use to get started on creating a backend service. You can also use these samples to test how Amazon GameLift Streams streams, without additional development. To get started, refer to [Setting up a web server and client with Amazon GameLift Streams](setting-up-web-sdk.md).

 If you want to share a stream without building your own web client, you can use a stream URL instead. A stream URL opens your stream in a supported web browser for anyone you share it with, so you do not need the Amazon GameLift Streams Web SDK or a backend service to let end users stream. For more information, see [Share stream sessions with stream URLs](stream-urls.md).

**Topics**
+ [Amazon GameLift Streams compatible devices and browsers](compatible-devices-browsers.md)
+ [Required ports](required-ports.md)
+ [Setting up a web server and client with Amazon GameLift Streams](setting-up-web-sdk.md)
+ [Customize stream appearance](sdk-stream-appearance.md)
+ [Locale preference](sdk-locale-support.md)
+ [AWS credentials for your application](sdk-session-credentials.md)
+ [Mouse movement handling](sdk-mouse-movement.md)
+ [Data channel communication between an application and web client](data-channels.md)
+ [Amazon GameLift Streams Web SDK release notes](web-sdk-release-notes.md)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon GameLift Streams. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query gameliftstreams` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

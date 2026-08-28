---
source_url: https://docs.aws.amazon.com/appstudio/latest/userguide/cross-region-data-transfer.html
---

# Cross-Region data transfer in AWS App Studio
<a name="cross-region-data-transfer"></a>

AWS App Studio transfers data across AWS Regions to enable certain generative AI features in the service. This topic contains information about the features enabled by cross-Region data transfers, the type of data that moves across Regions, and how to opt out.

The following features are enabled by cross-Region data transfer, and will not be accessible in your instance if you opt out:

1. Creating an app with AI, used to kickstart app building by describing your app with natural language and creating resources for you.

1. The AI chat in the application studio, used to ask questions about app building, publishing, and sharing.

The following data is transferred across Regions:

1. The prompts or user input from the features described previously.

To opt out of cross-Region data transfer, and the features enabled by it, use the following procedure to fill out the opt-out request form from the console:

1. Open the App Studio console at [https://console.aws.amazon.com/appstudio/](https://console.aws.amazon.com/appstudio/).

1. Choose **Opt out of data transfer**.

1. Enter your AWS account ID, and provide your email address.

1. Choose **Submit**.

1. Once submitted, your request to opt out of cross-Region data transfer will be processed, which can take up to 60 days.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS App Studio. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appstudio` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/userguide/assistant-console-login.html
---

# Configure the AWS IoT SiteWise Assistant
<a name="assistant-console-login"></a>

**Note**
The SiteWise Monitor feature is no longer available to new customers. Existing customers can continue to use the service as normal. For more information, see [SiteWise Monitor availability change](https://docs.aws.amazon.com/iot-sitewise/latest/appguide/iotsitewise-monitor-availability-change.html).

**AWS IoT SiteWise Assistant configuration**

1. Sign in to the [AWS IoT SiteWise console](https://console.aws.amazon.com/iotsitewise/home).
**Note**
 Grant permissions to enable integration with AWS IoT TwinMaker service. This is required for the AWS IoT SiteWise Assistant, and the dashboard to execute SQL queries in AWS IoT SiteWise resources. See [Integrate AWS IoT SiteWise and AWS IoT TwinMaker](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/integrate-tm.html#it-enable).

![Integration with AWS IoT TwinMaker popup](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-enable-twinmaker-in-assistant.png)

1.  Choose **Assistant** from the left navigation panel.
![The Assistant is enabled by default.](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/ai-assistant-console.png)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT SiteWise. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-sitewise` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

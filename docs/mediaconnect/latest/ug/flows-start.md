---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/flows-start.html
---

# Starting a flow
<a name="flows-start"></a>

After you create a flow, you must start the flow. You can also stop and restart a flow at any time.

**To start a flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that you want to start.

   The details page for that flow appears.

1. Choose **Start**.

**To start a flow (AWS CLI)**
+ In the AWS CLI, use the `start-flow` command:

  ```
  aws mediaconnect start-flow --flow-arn {{arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame}} --profile {{PMprofile}}
  ```

  The following example shows the return value:

  ```
  {
    "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
    "Status": "STARTING"
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

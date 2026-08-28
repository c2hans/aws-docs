---
source_url: https://docs.aws.amazon.com/mediaconnect/latest/ug/outputs-view-list.html
---

# Viewing the list of outputs for a MediaConnect flow
<a name="outputs-view-list"></a>

You can view a list of a flow's outputs, along with the setup that is associated with each output. This list includes outputs that you added, as well as outputs that AWS Elemental MediaConnect added when subscribers create flows based on entitlements that you granted.

**To view a list of outputs on an existing flow (console)**

1. Open the MediaConnect console at [https://console.aws.amazon.com/mediaconnect/](https://console.aws.amazon.com/mediaconnect/).

1. On the **Flows** page, choose the name of the flow that you want to view.

   The details page for that flow appears.

1. Choose the **Outputs** tab.

   A list of outputs for that flow appears.

**To view a list of outputs on an existing flow (AWS CLI)**
+ In the AWS CLI, use the `describe-flow` command:

  ```
  aws mediaconnect describe-flow --flow-arn "{{arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame}}" --region {{us-east-1}} --profile {{PMprofile}}
  ```

  The return value shows the details of the entire flow, including all the outputs. The following example shows the return value:

  ```
  {
    "Flow": {
      "AvailabilityZone": "us-east-1d",
      "Entitlements": [],
      "FlowArn": "arn:aws:mediaconnect:us-east-1:111122223333:flow:1-23aBC45dEF67hiJ8-12AbC34DE5fG:BasketballGame",
      "Name": "BasketballGame",
      "Outputs": [
        {
          "Address": "192.0.2.12",
          "Description": "RTP-FEC Output",
          "Name": "NYCOutput",
          "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-3aBC45dEF67hiJ89-c34de5fG678h:NYCOutput",
          "Port": 5020,
          "Protocol": "rtp-fec"
        },
        {
          "Address": "198.51.100.8",
          "Description": "RTP Output",
          "Name": "DCOutput",
          "OutputArn": "arn:aws:mediaconnect:us-east-1:111122223333:output:2-987655dEF67hiJ89-c34de5fG678h:DCOutput",
          "Port": 5110,
          "Protocol": "rtp"
        }
      ],
      "Source": {
        "IngestIp": "195.51.100.21",
        "IngestPort": 5010,
        "Name": "BasketballGameSource",
        "Protocol": "rtp-fec",
        "SourceArn": "arn:aws:mediaconnect:us-east-1:111122223333:source:3-4aBC56dEF78hiJ90-4de5fG6Hi78Jk:BasketballGameSource",
        "AllowlistCidr": "10.24.34.0/23"
      },
      "Status": "STANDBY"
    }
  }
  ```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elemental MediaConnect. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mediaconnect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

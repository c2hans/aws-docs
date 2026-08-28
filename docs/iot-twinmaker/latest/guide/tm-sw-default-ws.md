---
source_url: https://docs.aws.amazon.com/iot-twinmaker/latest/guide/tm-sw-default-ws.html
---

# Using the IoTSiteWiseDefaultWorkspace
<a name="tm-sw-default-ws"></a>

When you opt in to the [AWS IoT SiteWiseAWS IoT TwinMaker integration](https://docs.aws.amazon.com/iot-sitewise/latest/userguide/integrate-tm.html), a default workspace named `IoTSiteWiseDefaultWorkspace` is created and automatically synced with AWS IoT SiteWise.

You can also use the AWS IoT TwinMaker `CreateWorkspace` API to create a workspace named `IoTSiteWiseDefaultWorkspace`.

## Prerequisites
<a name="tm-sw-default-ws-prereqs"></a>

Before creating `IoTSiteWiseDefaultWorkspace`, make sure you have done the following:
+ Create an AWS IoT TwinMaker service-linked role. See [Using service-linked roles for AWS IoT TwinMaker](using-service-linked-roles.md) for more information.
+ Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/).

  Review the role or user and verify that it has permission to `iotsitewise:EnableSiteWiseIntegration`.

  If needed, add permission to the role or user:

------
#### [ JSON ]

****

  ```
  {
      "Version":"2012-10-17",
      "Statement": [
          {
              "Effect": "Allow",
              "Action": "iotsitewise:EnableSiteWiseIntegration",
              "Resource": "*"
          }
      ]
  }
  ```

------

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT TwinMaker. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot-twinmaker` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

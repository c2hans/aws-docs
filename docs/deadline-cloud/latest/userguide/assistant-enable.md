---
source_url: https://docs.aws.amazon.com/deadline-cloud/latest/userguide/assistant-enable.html
---

# Enabling the Deadline Cloud assistant
<a name="assistant-enable"></a>

Only Deadline Cloud administrators can enable or disable the assistant. The assistant is disabled by default.

## Prerequisites
<a name="assistant-prerequisites"></a>

To use the assistant, your monitor must have the following:
+ An administrator who enables the assistant through the Deadline Cloud console
+ The IAM policy attached to the monitor user role

## Enabling the assistant
<a name="assistant-enable-procedure"></a>

Use the following procedure to enable the assistant for all monitor users.

**To enable the assistant**

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home).

1. In the navigation pane, choose **Monitors**, and then choose your monitor.

1. Choose **Edit** to open the monitor settings.

1. Select the **Enable Deadline Cloud assistant** checkbox.

1. Choose **Save**.

When you enable the assistant, Deadline Cloud:
+ Creates a IAM policy on the monitor user role that grants `bedrock:InvokeModelWithResponseStream` permission scoped to your Region's cross-region inference profile.
+ Persists the enabled state through the monitor settings API.

## Disabling the assistant
<a name="assistant-disable-procedure"></a>

Use the following procedure to disable the assistant.

**To disable the assistant**

1. Open the [Deadline Cloud console](https://console.aws.amazon.com/deadlinecloud/home).

1. In the navigation pane, choose **Monitors**, and then choose your monitor.

1. Choose **Edit** to open the monitor settings.

1. Clear the **Enable Deadline Cloud assistant** checkbox.

1. Choose **Save**.

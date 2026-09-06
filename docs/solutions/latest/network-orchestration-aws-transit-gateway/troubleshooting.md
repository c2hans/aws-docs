---
source_url: https://docs.aws.amazon.com/solutions/latest/network-orchestration-aws-transit-gateway/troubleshooting.html
---

# Troubleshooting
<a name="troubleshooting"></a>

This solution logs errors, warnings, informational messages, and debugging messages for the solution’s Lambda functions. To choose the type of messages to log:

1. Find the applicable function in the [AWS Lambda console](https://console.aws.amazon.com/lambda/).

1. Change the **LOG\_LEVEL** environment variable to the applicable type of message.

| Level | Description |
| --- | --- |
| ERROR | Logs include information about anything that causes an operation to fail. |
| WARNING | Logs include information about anything that can potentially cause inconsistencies in the function but not necessarily cause the operation to fail. Logs also include ERROR messages. |
| INFO | Logs include high-level information about how the function is operating. Logs also include ERROR and WARNING messages. |
| DEBUG | Logs include information that might be helpful when debugging a problem with the function. Logs also include ERROR, WARNING, and INFO messages. |

If these instructions don’t address your issue, [Contact AWS Support](#contact-aws-support) provides instructions for opening an AWS Support case for this solution.

## Problem: Amazon EventBridge event bus permissions error
<a name="problem-amazon-eventbridge-event-bus-permissions-error"></a>

During spoke stack deployment, if you receive a **CREATE\_FAILED** message for the `0` or the `1`, verify that the Amazon EventBridge event bus in the hub account allows the spoke account to send events to the primary account.

## Resolution
<a name="resolution"></a>

Update the hub stack with the spoke account ID. For instructions on entering the applicable spoke account ID for **Principal**, see [Managing event bus permissions](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus-permissions-manage.html).

## Problem: AlreadyExists error
<a name="problem-alreadyexists-error"></a>

During hub or spoke stack deployment, you receive an `0` error code. The following is an example.

```
Service role name AWSServiceRoleForVPCTransitGateway has been taken in this account, please try a different suffix. (Service: Iam, Status Code: 400, Request ID: <request-id>) (RequestToken: <request-token>, HandlerErrorCode: AlreadyExists)
```

## Resolution
<a name="resolution"></a>

If you’re deploying a new stack, review the instructions in [Step 2](#step-2-launch-the-service-linked-role-hub-stack-optional) of **Deploy the solution.**

If youu’re updating an existing stack, review the instructions in [Update the hub stack(s)](#update-the-hub-stack) and [Update the spoke stack(s).](#update-the-spoke-stacks)

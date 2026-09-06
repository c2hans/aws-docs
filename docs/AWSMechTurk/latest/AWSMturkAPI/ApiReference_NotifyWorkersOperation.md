---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_NotifyWorkersOperation.html
---

# NotifyWorkers
<a name="ApiReference_NotifyWorkersOperation"></a>

## Description
<a name="ApiReference_NotifyWorkersOperation-description"></a>

The `NotifyWorkers` operation sends an email to one or more Workers that you specify with the Worker ID. You can specify up to 100 Worker IDs to send the same message with a single call to the NotifyWorkers operation. The NotifyWorkers operation will send a notification email to a Worker only if you have previously approved or rejected work from the Worker.

## Request Syntax
<a name="ApiReference_NotifyWorkersOperation-request-syntax"></a>

```
{
  "Subject": {{String}},

  "MessageText": {{String}},

  "WorkerIds": {{Array of Strings}}
 }
```

## Request Parameters
<a name="ApiReference_NotifyWorkersOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` Subject `  | The subject line of the email message to send. Can include up to 200 characters.<br />Type: String | Yes |
|  ` MessageText `  | The text of the email message to send. Can include up to 4,096 characters.<br />Type: String | Yes |
|  ` WorkerIds `  | An array of WorkerIds to notify. You can notify upto 100 Workers at a time.<br />Type: Array of Strings | Yes |

## Response Elements
<a name="ApiReference_NotifyWorkersOperation-response-elements"></a>

 A successful request for the `NotifyWorkers` operation returns with no errors and an empty body.

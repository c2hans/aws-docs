---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_CreateWorkerBlockOperation.html
---

# CreateWorkerBlock
<a name="ApiReference_CreateWorkerBlockOperation"></a>

## Description
<a name="ApiReference_CreateWorkerBlockOperation-description"></a>

The `CreateWorkerBlock` operation allows you to prevent a Worker from working on your HITs. For example, you can block a Worker who is producing poor quality work. You can block up to 100,000 Workers.

## Request Syntax
<a name="ApiReference_CreateWorkerBlockOperation-request-syntax"></a>

```
{
  "WorkerId": {{String}},

  "Reason": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_CreateWorkerBlockOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` WorkerId `  | The ID of the Worker to block<br />Type: String | Yes |
|  ` Reason `  | A message that explains the reason for blocking the Worker. The Worker does not see this message.<br />Type: String | No |

## Response Elements
<a name="ApiReference_CreateWorkerBlockOperation-response-elements"></a>

 A successful request for the `CreateWorkerBlock` operation returns with no errors and an empty body.

---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DeleteWorkerBlockOperation.html
---

# DeleteWorkerBlock
<a name="ApiReference_DeleteWorkerBlockOperation"></a>

## Description
<a name="ApiReference_DeleteWorkerBlockOperation-description"></a>

The `DeleteWorkerBlock` operation allows you to reinstate a blocked Worker to work on your HITs. This operation reverses the effects of the CreateWorkerBlock operation. You need the Worker ID to use this operation. If the Worker ID is missing or invalid, this operation fails and returns the message “WorkerId is invalid.” If the specified Worker is not blocked, this operation returns successfully.

## Request Syntax
<a name="ApiReference_DeleteWorkerBlockOperation-request-syntax"></a>

```
{
  "WorkerId": {{String}},

  "Reason": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_DeleteWorkerBlockOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` WorkerId `  | The ID of the Worker to unblock<br />Type: String | Yes |
|  ` Reason `  | A message that explains the reason for unblocking the Worker. The Worker does not see this message.<br />Type: String | No |

## Response Elements
<a name="ApiReference_DeleteWorkerBlockOperation-response-elements"></a>

 A successful request for the `DeleteWorkerBlock` operation returns with no errors and an empty body.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

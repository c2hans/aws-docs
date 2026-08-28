---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_RejectQualificationRequestOperation.html
---

# RejectQualificationRequest
<a name="ApiReference_RejectQualificationRequestOperation"></a>

## Description
<a name="ApiReference_RejectQualificationRequestOperation-description"></a>

 The `RejectQualificationRequest` operation rejects a user's request for a Qualification.

 You can provide a text message explaining why the request was rejected. The Worker who made the request can see this message.

## Request Syntax
<a name="ApiReference_RejectQualificationRequestOperation-request-syntax"></a>

```
{
  "QualificationRequestId": {{String}},

  "Reason": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_RejectQualificationRequestOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` QualificationRequestId `  | The ID of the Qualification request, as returned by the [ListQualificationRequests](ApiReference_ListQualificationRequestsOperation.md) operation.<br />Type: String | Yes |
|  ` Reason `  | A text message explaining why the request was rejected, to be shown to the Worker who made the request.<br />Type: String | No |

## Response Elements
<a name="ApiReference_RejectQualificationRequestOperation-response-elements"></a>

 A successful request for the `RejectQualificationRequest` operation returns with no errors and an empty body.

## Example
<a name="ApiReference_RejectQualificationRequestOperation-examples"></a>

The following example shows how to use the `RejectQualificationRequest` operation:

### Sample Request
<a name="ApiReference_RejectQualificationRequestOperation-examples-sample-request"></a>

The following example rejects a specified Qualification request.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
  QualificationRequestId:"789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE"
}
```

### Sample Response
<a name="ApiReference_RejectQualificationRequestOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

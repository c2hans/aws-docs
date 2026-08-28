---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkerBlocksOperation.html
---

# ListWorkerBlocks
<a name="ApiReference_ListWorkerBlocksOperation"></a>

## Description
<a name="ApiReference_ListWorkerBlocksOperation-description"></a>

The `ListWorkersBlocks` operation retrieves a list of Workers who are blocked from working on your HITs.

## Request Syntax
<a name="ApiReference_ListWorkerBlocksOperation-request-syntax"></a>

```
{
  "NextToken": {{String}},

  "MaxResults": {{Integer}}
 }
```

## Request Parameters
<a name="ApiReference_ListWorkerBlocksOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListWorkerBlocksOperation-response-elements"></a>

A successful request returns a paginated list of Workers that have been blocked along with the reason for the block.

## Example
<a name="ApiReference_ListWorkerBlocksOperation-examples"></a>

The following example shows how to use the `ListWorkerBlocks` operation:

### Sample Request
<a name="ApiReference_ListWorkerBlocksOperation-examples-sample-request"></a>

The following example lists all Worker blocks.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
}
```

### Sample Response
<a name="ApiReference_ListWorkerBlocksOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  WorkerBlocks:[{WorkerId, Reason}],
  NumResults:3
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

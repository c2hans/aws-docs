---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsOperation.html
---

# ListHITs
<a name="ApiReference_ListHITsOperation"></a>

## Description
<a name="ApiReference_ListHITsOperation-description"></a>

The `ListHITs` operation returns all of a Requester's HITs. The operation returns HITs of any status, except for HITs that have been deleted of with the `DeleteHIT` operation or that have been auto-deleted.

 Having high volumes of active HITs may lead to latency or timeouts when calling `ListHITs`. To remedy this, call the [`DeleteHIT`](ApiReference_DeleteHITOperation.md) operation on HITs you no longer need access to.

## Request Syntax
<a name="ApiReference_ListHITsOperation-request-syntax"></a>

```
{
  "NextToken": {{String}},

  "MaxResults": {{Integer}}
 }
```

## Request Parameters
<a name="ApiReference_ListHITsOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListHITsOperation-response-elements"></a>

A successful request returns a paginated list of [HIT](ApiReference_HITDataStructureArticle.md) data structures.

## Example
<a name="ApiReference_ListHITsOperation-examples"></a>

The following example shows how to use the `ListHITs` operation:

### Sample Request
<a name="ApiReference_ListHITsOperation-examples-sample-request"></a>

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
}
```

### Sample Response
<a name="ApiReference_ListHITsOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  NextToken:{{PaginationToken}},
  NumResults:10,
  HITs:[HIT]
}
```

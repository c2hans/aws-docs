---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationRequestsOperation.html
---

# ListQualificationRequests
<a name="ApiReference_ListQualificationRequestsOperation"></a>

## Description
<a name="ApiReference_ListQualificationRequestsOperation-description"></a>

The `ListQualificationRequests` operation retrieves requests for Qualifications of a particular Qualification type. The owner of the Qualification type calls this operation to poll for pending requests, and accepts them using the AcceptQualification operation.

## Request Syntax
<a name="ApiReference_ListQualificationRequestsOperation-request-syntax"></a>

```
{
  "QualificationTypeId": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_ListQualificationRequestsOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` QualificationTypeId `  | The ID of the QualificationType.<br />Type: String | No |

## Response Elements
<a name="ApiReference_ListQualificationRequestsOperation-response-elements"></a>

A successful request returns a paginated list of QualificationRequests.

## Example
<a name="ApiReference_ListQualificationRequestsOperation-examples"></a>

The following example shows how to use the `ListQualificationRequests` operation:

### Sample Request
<a name="ApiReference_ListQualificationRequestsOperation-examples-sample-request"></a>

The following example lists requests for a Qualification type.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
  QualificationTypeId:"AZ34EXAMPLE"
}
```

### Sample Response
<a name="ApiReference_ListQualificationRequestsOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  QualificationRequests:[{{QualificationRequest }}],
  NumResults:10,
  NextToken:{{PaginationToken}}
}
```

---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListBonusPaymentsOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# ListBonusPayments
<a name="ApiReference_ListBonusPaymentsOperation"></a>

## Description
<a name="ApiReference_ListBonusPaymentsOperation-description"></a>

The `ListBonusPayments` operation retrieves the amounts of bonuses you have paid to Workers for a given HIT or assignment.

## Request Syntax
<a name="ApiReference_ListBonusPaymentsOperation-request-syntax"></a>

```
{
  "HITId": {{String}},

  "AssignmentId": {{String}},

  "NextToken": {{String}},

  "MaxResults": {{Integer}}
 }
```

## Request Parameters
<a name="ApiReference_ListBonusPaymentsOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The ID of the HIT associated with the bonus payments to retrieve. If not specified, all bonus payments for all assignments for the given HIT are returned. Either the HITId parameter or the AssignmentId parameter must be specified<br />Type: String | Conditional |
|  ` AssignmentId `  | The ID of the assignment associated with the bonus payments to retrieve. If specified, only bonus payments for the given assignment are returned. Either the HITId parameter or the AssignmentId parameter must be specified<br />Type: String | Conditional |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListBonusPaymentsOperation-response-elements"></a>

A successful request returns a paginated list of Bonuses with the following fields: WorkerId, BonusAmount, AssignmentId, Reason and GrantTime

## Example
<a name="ApiReference_ListBonusPaymentsOperation-examples"></a>

The following example shows how to use the `ListBonusPayments` operation:

### Sample Request
<a name="ApiReference_ListBonusPaymentsOperation-examples-sample-request"></a>

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
}
```

### Sample Response
<a name="ApiReference_ListBonusPaymentsOperation-examples-sample-response"></a>

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
  BonusPayments:[Bonus]
}
```

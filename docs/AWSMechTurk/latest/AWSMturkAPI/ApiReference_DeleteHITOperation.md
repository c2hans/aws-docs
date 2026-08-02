---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DeleteHITOperation.html
---

# DeleteHIT
<a name="ApiReference_DeleteHITOperation"></a>

## Description
<a name="ApiReference_DeleteHITOperation-description"></a>

 The `DeleteHIT` operation disposes of a HIT that is no longer needed. Only the Requester who created the HIT can delete it.

You can only dispose of HITs that are in the Reviewable state, with all of their submitted assignments already either approved or rejected. If you call the DeleteHIT operation on a HIT that is not in the Reviewable state (for example, that has not expired, or still has active assignments), or on a HIT that is Reviewable but without all of its submitted assignments already approved or rejected, the service returns an error.

**Note**
HITs are automatically disposed of after 120 days.
After you dispose of a HIT, you can no longer approve the HIT's rejected assignments.
Disposed of HITs are not returned in results for the SearchHITs operation.
Disposing of HITs can improve the performance of operations such as ListReviewableHITs and ListHITs.

## Request Syntax
<a name="ApiReference_DeleteHITOperation-request-syntax"></a>

```
{
  "HITId": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_DeleteHITOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The ID of the HIT.<br />Type: String | Yes |

## Response Elements
<a name="ApiReference_DeleteHITOperation-response-elements"></a>

 A successful request for the `DeleteHIT` operation returns with no errors and an empty body.

## Example
<a name="ApiReference_DeleteHITOperation-examples"></a>

The following example shows how to use the `DeleteHIT` operation:

### Sample Request
<a name="ApiReference_DeleteHITOperation-examples-sample-request"></a>

The following example deletes a HIT with the specified HIT ID.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
  HITId:"789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE"
}
```

### Sample Response
<a name="ApiReference_DeleteHITOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

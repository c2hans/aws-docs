---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListHITsForQualificationTypeOperation.html
---

# ListHITsForQualificationType
<a name="ApiReference_ListHITsForQualificationTypeOperation"></a>

## Description
<a name="ApiReference_ListHITsForQualificationTypeOperation-description"></a>

The `ListHITsForQualificationType` operation returns the HITs that use the given [`QualififcationType`](ApiReference_QualificationTypeDataStructureArticle.md) for a [`QualificationRequirement`](ApiReference_QualificationRequirementDataStructureArticle.md). The operation returns HITs of any status, except for HITs that have been deleted with the DeleteHIT operation or that have been auto-deleted.

 Having high volumes of active HITs may lead to latency or timeouts when calling `ListHITsForQualificationType`. To remedy this, call the [`DeleteHIT`](ApiReference_DeleteHITOperation.md) operation on HITs you no longer need access to.

## Request Syntax
<a name="ApiReference_ListHITsForQualificationTypeOperation-request-syntax"></a>

```
{
  "QualificationTypeId": {{String}},

  "NextToken": {{String}},

  "MaxResults": {{Integer}}
 }
```

## Request Parameters
<a name="ApiReference_ListHITsForQualificationTypeOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` QualificationTypeId `  | The ID of the Qualification type to use when querying HITs.<br />Type: String | No |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListHITsForQualificationTypeOperation-response-elements"></a>

A successful request returns a paginated list of [HIT](ApiReference_HITDataStructureArticle.md) data structures.

## Example
<a name="ApiReference_ListHITsForQualificationTypeOperation-examples"></a>

The following example shows how to use the `ListHITsForQualificationType` operation:

### Sample Request
<a name="ApiReference_ListHITsForQualificationTypeOperation-examples-sample-request"></a>

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
}
```

### Sample Response
<a name="ApiReference_ListHITsForQualificationTypeOperation-examples-sample-response"></a>

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

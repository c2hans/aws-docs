---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListWorkersWithQualificationTypeOperation.html
---

# ListWorkersWithQualificationType
<a name="ApiReference_ListWorkersWithQualificationTypeOperation"></a>

## Description
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-description"></a>

The `ListWorkersWithQualificationType` operation returns all of the Workers with a given Qualification type.

## Request Syntax
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-request-syntax"></a>

```
{
  "QualificationTypeId": {{String}},

  "Status": {{String}},

  "NextToken": {{String}},

  "MaxResults": {{Integer}},
 }
```

## Request Parameters
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` QualificationTypeId `  | The ID of the QualificationType.<br />Type: String | No |
|  ` Status `  | The status of the Qualifications to return. Granted \| Revoked<br />Type: String | No |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-response-elements"></a>

A successful request returns a paginated list of Qualifications that have been granted to Workers.

## Example
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-examples"></a>

The following example shows how to use the `ListWorkersWithQualificationType` operation:

### Sample Request
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-examples-sample-request"></a>

The following example performs a simple text query for Qualification types.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
  QualificationTypeId:"ZSPJXD4F1SFZP7YNJWR0"
}
```

### Sample Response
<a name="ApiReference_ListWorkersWithQualificationTypeOperation-examples-sample-response"></a>

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
  Qualifications:[{{Qualification}}]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

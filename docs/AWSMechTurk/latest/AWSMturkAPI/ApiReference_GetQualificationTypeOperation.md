---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationTypeOperation.html
---

# GetQualificationType
<a name="ApiReference_GetQualificationTypeOperation"></a>

## Description
<a name="ApiReference_GetQualificationTypeOperation-description"></a>

The `GetQualificationType`operation retrieves information about a Qualification type using its ID.

## Request Syntax
<a name="ApiReference_GetQualificationTypeOperation-request-syntax"></a>

```
{
  "QualificationTypeId": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_GetQualificationTypeOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` QualificationTypeId `  | The ID of the QualificationType.<br />Type: String | Yes |

## Response Elements
<a name="ApiReference_GetQualificationTypeOperation-response-elements"></a>

A successful request returns a [QualificationType](ApiReference_QualificationTypeDataStructureArticle.md) data structure.

## Example
<a name="ApiReference_GetQualificationTypeOperation-examples"></a>

The following example shows how to use the `GetQualificationType` operation:

### Sample Request
<a name="ApiReference_GetQualificationTypeOperation-examples-sample-request"></a>

The following example gets information about a Qualification type.

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
<a name="ApiReference_GetQualificationTypeOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
{
  QualificationTypeId:"789RVWYBAZW00EXAMPLE951RVWYBAZW00EXAMPLE",
  Name:"EnglishWritingAbility",
  Description:"The ability to write and edit in text in English",
  QualificationTypeStatus:"Active"
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

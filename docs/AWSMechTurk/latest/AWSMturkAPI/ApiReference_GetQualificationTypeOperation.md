---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

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

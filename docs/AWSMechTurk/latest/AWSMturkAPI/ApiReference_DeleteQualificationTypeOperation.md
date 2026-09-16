---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_DeleteQualificationTypeOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# DeleteQualificationType
<a name="ApiReference_DeleteQualificationTypeOperation"></a>

## Description
<a name="ApiReference_DeleteQualificationTypeOperation-description"></a>

 The `DeleteQualificationType` disposes a Qualification type and disposes any HIT types that are associated with the Qualification type.

This operation does not revoke Qualifications already assigned to Workers because the Qualifications might be needed for active HITs. If there are any pending requests for the Qualification type, Amazon Mechanical Turk rejects those requests. After you delete a Qualification type, you can no longer use it to create HITs or HIT types.

**Note**
DeleteQualificationType must wait for all the HITs that use the deleted Qualification type to be deleted before completing. It may take up to 48 hours before DeleteQualificationType completes and the unique name of the Qualification type is available for reuse with CreateQualificationType.

## Request Syntax
<a name="ApiReference_DeleteQualificationTypeOperation-request-syntax"></a>

```
{
  "QualificationTypeId": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_DeleteQualificationTypeOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` QualificationTypeId `  | The ID of the QualificationType to dispose.<br />Type: String | Yes |

## Response Elements
<a name="ApiReference_DeleteQualificationTypeOperation-response-elements"></a>

 A successful request for the `DeleteQualificationType` operation returns with no errors and an empty body.

## Example
<a name="ApiReference_DeleteQualificationTypeOperation-examples"></a>

The following example shows how to use the `DeleteQualificationType` operation:

### Sample Request
<a name="ApiReference_DeleteQualificationTypeOperation-examples-sample-request"></a>

The following example deletes a Qualification type and any HIT types that are associated with the Qualification type.

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
<a name="ApiReference_DeleteQualificationTypeOperation-examples-sample-response"></a>

The following is an example response:

```
HTTP/1.1 200 OK
x-amzn-RequestId: <RequestId>
Content-Type: application/x-amz-json-1.1
Content-Length: <PayloadSizeBytes>
Date: <Date>
```

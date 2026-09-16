---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetFileUploadURLOperation.html
---

**Amazon Mechanical Turk will permanently close on September 30, 2026.** For Workers and Requesters currently using the service, visit our [Amazon Mechanical Turk help page](https://www.mturk.com/help) to learn how you can prepare for this closure.

# GetFileUploadURL
<a name="ApiReference_GetFileUploadURLOperation"></a>

## Description
<a name="ApiReference_GetFileUploadURLOperation-description"></a>

**Important**
Beginning Tuesday, December 12th 2017 the Answer Specification structure will **no longer support the `FileUploadAnswer` element** to be used for the [QuestionForm](ApiReference_QuestionFormDataStructureArticle.md) data structure. Instead, we recommend that Requesters who want to create HITs asking Workers to upload files use [Amazon S3](http://aws.amazon.com/s3).

The `GetFileUploadURL` operation generates and returns a temporary URL. You use the temporary URL to retrieve a file uploaded by a Worker as an answer to a FileUploadAnswer question for a HIT. The temporary URL is generated the instant the GetFileUploadURL operation is called, and is valid for 60 seconds. You can get a temporary file upload URL any time until the HIT is disposed. After the HIT is disposed, any uploaded files are deleted, and cannot be retrieved.

## Request Syntax
<a name="ApiReference_GetFileUploadURLOperation-request-syntax"></a>

```
{
  "AssignmentId": {{String}},

  "QuestionIdentifier": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_GetFileUploadURLOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` AssignmentId `  | The ID of the assignment that contains the question with a FileUploadAnswer.<br />Type: String | Yes |
|  ` QuestionIdentifier `  | The identifier of the question with a FileUploadAnswer, as specified in the QuestionForm of the HIT.<br />Type: String | Yes |

## Response Elements
<a name="ApiReference_GetFileUploadURLOperation-response-elements"></a>

A successful request returns an FileUploadURL string containing the temporary URL.

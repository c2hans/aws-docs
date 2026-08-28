---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_ListQualificationTypesOperation.html
---

# ListQualificationTypes
<a name="ApiReference_ListQualificationTypesOperation"></a>

## Description
<a name="ApiReference_ListQualificationTypesOperation-description"></a>

The `ListQualificationTypes` operation searches for Qualification types using the specified search query, and returns a list of Qualification types.

## Request Syntax
<a name="ApiReference_ListQualificationTypesOperation-request-syntax"></a>

```
{
  "Query": {{String}},

  "MustBeRequestable": {{Boolean}},

  "MustBeOwnedByCaller": {{Boolean}},

  "NextToken": {{String}},

  "MaxResults": {{Integer}},
 }
```

## Request Parameters
<a name="ApiReference_ListQualificationTypesOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` Query `  | A search term<br />Type: String | No |
|  ` MustBeRequestable `  | Specifies that only Qualification types that a user can request through the Amazon Mechanical Turk web site, such as by taking a Qualification test, are returned as results of the search. Some Qualification types, such as those assigned automatically by the system, cannot be requested directly by users. If false, all Qualification types, including those managed by the system, are considered for the search.<br />Type: Boolean | Yes |
|  ` MustBeOwnedByCaller `  | Specifies that only Qualification types that the Requester created are returned. If false, the operation returns all Qualification types.<br />Type: Boolean<br />Default: False | No |
|  ` NextToken `  | Pagination token<br />Type: String | No |
|  ` MaxResults `  | <br />Type: Integer | No |

## Response Elements
<a name="ApiReference_ListQualificationTypesOperation-response-elements"></a>

A successful request returns a paginated list of Qualification Types.

## Example
<a name="ApiReference_ListQualificationTypesOperation-examples"></a>

The following example shows how to use the `ListQualificationTypes` operation:

### Sample Request
<a name="ApiReference_ListQualificationTypesOperation-examples-sample-request"></a>

The following example performs a simple text query for Qualification types.

```
POST / HTTP/1.1
Host: mturk-requester.us-east-1.amazonaws.com
Content-Length: <PayloadSizeBytes>
X-Amz-Date: <Date>
{
  Query:"LanguageSkill"
}
```

### Sample Response
<a name="ApiReference_ListQualificationTypesOperation-examples-sample-response"></a>

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
  QualificationType:[{{QualificationType}}]
}
```

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

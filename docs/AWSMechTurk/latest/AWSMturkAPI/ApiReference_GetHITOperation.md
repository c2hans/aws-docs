---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_GetHITOperation.html
---

# GetHIT
<a name="ApiReference_GetHITOperation"></a>

## Description
<a name="ApiReference_GetHITOperation-description"></a>

The `GetHIT` operation retrieves the details of the specified HIT.

## Request Syntax
<a name="ApiReference_GetHITOperation-request-syntax"></a>

```
{
  "HITId": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_GetHITOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The ID of the HIT.<br />Type: String | Yes |

## Response Elements
<a name="ApiReference_GetHITOperation-response-elements"></a>

A successful request returns a [HIT](ApiReference_HITDataStructureArticle.md) data structure.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Mechanical Turk. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSMechTurk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

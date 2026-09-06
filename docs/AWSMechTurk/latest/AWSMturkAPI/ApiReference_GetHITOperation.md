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

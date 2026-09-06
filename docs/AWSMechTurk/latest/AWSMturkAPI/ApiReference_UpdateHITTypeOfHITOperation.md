---
source_url: https://docs.aws.amazon.com/AWSMechTurk/latest/AWSMturkAPI/ApiReference_UpdateHITTypeOfHITOperation.html
---

# UpdateHITTypeOfHIT
<a name="ApiReference_UpdateHITTypeOfHITOperation"></a>

## Description
<a name="ApiReference_UpdateHITTypeOfHITOperation-description"></a>

The `UpdateHITTypeOfHIT` operation allows you to change the HITType properties of a HIT. This operation disassociates the HIT from its old HITType properties and associates it with the new HITType properties. The HIT takes on the properties of the new HITType in place of the old ones.

## Request Syntax
<a name="ApiReference_UpdateHITTypeOfHITOperation-request-syntax"></a>

```
{
  "HITId": {{String}},

  "HITTypeId": {{String}}
 }
```

## Request Parameters
<a name="ApiReference_UpdateHITTypeOfHITOperation-request-parameters"></a>

 The request accepts the following data in JSON format:

| Name | Description | Required |
| --- | --- | --- |
|  ` HITId `  | The HIT to update.<br />Type: String | Yes |
|  ` HITTypeId `  | The ID of the new HIT type.<br />Type: String | Yes |

## Response Elements
<a name="ApiReference_UpdateHITTypeOfHITOperation-response-elements"></a>

 A successful request for the `UpdateHITTypeOfHIT` operation returns with no errors and an empty body.

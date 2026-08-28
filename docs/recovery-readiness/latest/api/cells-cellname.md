---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/cells-cellname.html
---

# GetCell, UpdateCell, DeleteCell
<a name="cells-cellname"></a>

## URI
<a name="cells-cellname-url"></a>

`/cells/{{cellName}}`

## HTTP methods
<a name="cells-cellname-http-methods"></a>

### GET
<a name="cells-cellnameget"></a>

**Operation ID:** `GetCell`

Gets information about a cell including cell name, cell Amazon Resource Name (ARN), ARNs of nested cells for this cell, and a list of those cell ARNs with their associated recovery group ARNs.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{cellName}} | String | True | The name of the cell. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CellOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### PUT
<a name="cells-cellnameput"></a>

**Operation ID:** `UpdateCell`

Updates a cell to replace the list of nested cells with a new list of nested cells.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{cellName}} | String | True | The name of the cell. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CellOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### DELETE
<a name="cells-cellnamedelete"></a>

**Operation ID:** `DeleteCell`

Delete a cell. When successful, the response code is 204, with no response body.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{cellName}} | String | True | The name of the cell. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 204 | None | 204 response - Successful deletion |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="cells-cellnameoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{cellName}} | String | True | The name of the cell. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="cells-cellname-schemas"></a>

### Request bodies
<a name="cells-cellname-request-examples"></a>

#### PUT schema
<a name="cells-cellname-request-body-put-example"></a>

```
{
  "cells": [
    "string"
  ]
}
```

### Response bodies
<a name="cells-cellname-response-examples"></a>

#### CellOutput schema
<a name="cells-cellname-response-body-celloutput-example"></a>

```
{
  "cells": [
    "string"
  ],
  "parentReadinessScopes": [
    "string"
  ],
  "cellName": "string",
  "cellArn": "string",
  "tags": {
  }
}
```

## Properties
<a name="cells-cellname-properties"></a>

### CellOutput
<a name="cells-cellname-model-celloutput"></a>

Information about a cell.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cellArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the cell. |
| cellName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | The name of the cell. |
| cells | Array of type string | True | A list of cell ARNs. |
| parentReadinessScopes | Array of type string | True | The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element. |
| tags | [Tags](#cells-cellname-model-tags) | False | Tags on the resources. |

### CellUpdateParameters
<a name="cells-cellname-model-cellupdateparameters"></a>

Parameters used to update a cell.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type string | True | A list of cell Amazon Resource Names (ARNs), which completely replaces the previous list. |

### Tags
<a name="cells-cellname-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="cells-cellname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetCell
<a name="GetCell-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetCell)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetCell)

### UpdateCell
<a name="UpdateCell-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/UpdateCell)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/UpdateCell)

### DeleteCell
<a name="DeleteCell-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/DeleteCell)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/DeleteCell)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-readiness` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

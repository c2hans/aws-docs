---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/cells.html
---

# ListCells, CreateCell
<a name="cells"></a>

## URI
<a name="cells-url"></a>

`/cells`

## HTTP methods
<a name="cells-http-methods"></a>

### GET
<a name="cellsget"></a>

**Operation ID:** `ListCells`

Lists the cells for an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListCellsResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### POST
<a name="cellspost"></a>

**Operation ID:** `CreateCell`

Creates a cell in an account.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CellOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 409 | None | 409 response - Conflict exception. You might be using a predefined variable. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="cellsoptions"></a>

Enables CORS by returning correct headers.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="cells-schemas"></a>

### Request bodies
<a name="cells-request-examples"></a>

#### POST schema
<a name="cells-request-body-post-example"></a>

```
{
  "cells": [
    "string"
  ],
  "cellName": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="cells-response-examples"></a>

#### ListCellsResult schema
<a name="cells-response-body-listcellsresult-example"></a>

```
{
  "cells": [
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
  ],
  "nextToken": "string"
}
```

#### CellOutput schema
<a name="cells-response-body-celloutput-example"></a>

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
<a name="cells-properties"></a>

### CellCreateParameters
<a name="cells-model-cellcreateparameters"></a>

Parameters used to create a cell.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cellName | string | True | The name of the cell to create. |
| cells | Array of type string | False | A list of cell Amazon Resource Names (ARNs) contained within this cell, for use in nested cells. For example, Availability Zones within specific AWS Regions. |
| tags | [Tags](#cells-model-tags) | False |  |

### CellOutput
<a name="cells-model-celloutput"></a>

Information about a cell.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cellArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the cell. |
| cellName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | The name of the cell. |
| cells | Array of type string | True | A list of cell ARNs. |
| parentReadinessScopes | Array of type string | True | The readiness scope for the cell, which can be a cell Amazon Resource Name (ARN) or a recovery group ARN. This is a list but currently can have only one element. |
| tags | [Tags](#cells-model-tags) | False | Tags on the resources. |

### ListCellsResult
<a name="cells-model-listcellsresult"></a>

The result of a successful `ListCells` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type [CellOutput](#cells-model-celloutput) | False | A list of cells. |
| nextToken | string | False | The token that identifies which batch of results you want to see. |

### Tags
<a name="cells-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="cells-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListCells
<a name="ListCells-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/ListCells)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListCells)

### CreateCell
<a name="CreateCell-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for Python (Boto3)](/goto/boto3/aws-meridian-beta-2019-12-02/CreateCell)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/CreateCell)

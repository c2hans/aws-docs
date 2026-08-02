---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups-recoverygroupname.html
---

# GetRecoveryGroup, UpdateRecoveryGroup, DeleteRecoveryGroup
<a name="recoverygroups-recoverygroupname"></a>

## URI
<a name="recoverygroups-recoverygroupname-url"></a>

`/recoverygroups/{{recoveryGroupName}}`

## HTTP methods
<a name="recoverygroups-recoverygroupname-http-methods"></a>

### GET
<a name="recoverygroups-recoverygroupnameget"></a>

**Operation ID:** `GetRecoveryGroup`

Gets details about a recovery group, including a list of the cells that are included in it.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RecoveryGroupOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### PUT
<a name="recoverygroups-recoverygroupnameput"></a>

**Operation ID:** `UpdateRecoveryGroup`

Updates a recovery group.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RecoveryGroupOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 404 | None | 404 response - Malformed query string. The query string contains a syntax error or resource not found. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### DELETE
<a name="recoverygroups-recoverygroupnamedelete"></a>

**Operation ID:** `DeleteRecoveryGroup`

Deletes a recovery group.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

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
<a name="recoverygroups-recoverygroupnameoptions"></a>

Enable CORS by returning correct headers

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{recoveryGroupName}} | String | True | The name of a recovery group. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="recoverygroups-recoverygroupname-schemas"></a>

### Request bodies
<a name="recoverygroups-recoverygroupname-request-examples"></a>

#### PUT schema
<a name="recoverygroups-recoverygroupname-request-body-put-example"></a>

```
{
  "cells": [
    "string"
  ]
}
```

### Response bodies
<a name="recoverygroups-recoverygroupname-response-examples"></a>

#### RecoveryGroupOutput schema
<a name="recoverygroups-recoverygroupname-response-body-recoverygroupoutput-example"></a>

```
{
  "cells": [
    "string"
  ],
  "recoveryGroupName": "string",
  "recoveryGroupArn": "string",
  "tags": {
  }
}
```

## Properties
<a name="recoverygroups-recoverygroupname-properties"></a>

### RecoveryGroupOutput
<a name="recoverygroups-recoverygroupname-model-recoverygroupoutput"></a>

A representation of the application, typically containing multiple cells.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type string | True | A list of a cell's Amazon Resource Names (ARNs). |
| recoveryGroupArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the recovery group. |
| recoveryGroupName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | The name of the recovery group. |
| tags | [Tags](#recoverygroups-recoverygroupname-model-tags) | False | The tags associated with the recovery group. |

### RecoveryGroupUpdateParameters
<a name="recoverygroups-recoverygroupname-model-recoverygroupupdateparameters"></a>

Parameters used to update a recovery group.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type string | True | A list of cell Amazon Resource Names (ARNs). This list completely replaces the previous list. |

### Tags
<a name="recoverygroups-recoverygroupname-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="recoverygroups-recoverygroupname-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetRecoveryGroup
<a name="GetRecoveryGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/GetRecoveryGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/GetRecoveryGroup)

### UpdateRecoveryGroup
<a name="UpdateRecoveryGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/UpdateRecoveryGroup)

### DeleteRecoveryGroup
<a name="DeleteRecoveryGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/DeleteRecoveryGroup)

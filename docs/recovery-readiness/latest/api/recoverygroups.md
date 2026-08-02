---
source_url: https://docs.aws.amazon.com/recovery-readiness/latest/api/recoverygroups.html
---

# ListRecoveryGroups, CreateRecoveryGroup
<a name="recoverygroups"></a>

## URI
<a name="recoverygroups-url"></a>

`/recoverygroups`

## HTTP methods
<a name="recoverygroups-http-methods"></a>

### GET
<a name="recoverygroupsget"></a>

**Operation ID:** `ListRecoveryGroups`

Lists the recovery groups in an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The token that identifies which batch of results you want to see. |
| maxResults | String | False | The number of objects that you want to return with this call. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListRecoveryGroupsResult | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### POST
<a name="recoverygroupspost"></a>

**Operation ID:** `CreateRecoveryGroup`

Creates a recovery group in an account. A recovery group corresponds to an application and includes a list of the cells that make up the application.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | RecoveryGroupOutput | 200 response - Success. |
| 400 | None | 400 response - Multiple causes. For example, you might have a malformed query string, an input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | None | 403 response - Access denied exception. You do not have sufficient access to perform this action. |
| 409 | None | 409 response - Conflict exception. You might be using a predefined variable. |
| 429 | None | 429 response - Limit exceeded exception or too many requests exception.  |
| 500 | None | 500 response - Internal service error or temporary service error. Retry the request. |

### OPTIONS
<a name="recoverygroupsoptions"></a>

Enable CORS by returning correct headers

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="recoverygroups-schemas"></a>

### Request bodies
<a name="recoverygroups-request-examples"></a>

#### POST schema
<a name="recoverygroups-request-body-post-example"></a>

```
{
  "cells": [
    "string"
  ],
  "recoveryGroupName": "string",
  "tags": {
  }
}
```

### Response bodies
<a name="recoverygroups-response-examples"></a>

#### ListRecoveryGroupsResult schema
<a name="recoverygroups-response-body-listrecoverygroupsresult-example"></a>

```
{
  "nextToken": "string",
  "recoveryGroups": [
    {
      "cells": [
        "string"
      ],
      "recoveryGroupName": "string",
      "recoveryGroupArn": "string",
      "tags": {
      }
    }
  ]
}
```

#### RecoveryGroupOutput schema
<a name="recoverygroups-response-body-recoverygroupoutput-example"></a>

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
<a name="recoverygroups-properties"></a>

### ListRecoveryGroupsResult
<a name="recoverygroups-model-listrecoverygroupsresult"></a>

The result of a successful `ListRecoveryGroups` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | The token that identifies which batch of results you want to see. |
| recoveryGroups | Array of type [RecoveryGroupOutput](#recoverygroups-model-recoverygroupoutput) | False | A list of recovery groups. |

### RecoveryGroupCreateParameters
<a name="recoverygroups-model-recoverygroupcreateparameters"></a>

Parameters used to create a recovery group. A recovery group corresponds to your application and includes the cells that make up the application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type string | False | A list of the cell Amazon Resource Names (ARNs) in the recovery group. |
| recoveryGroupName | string | True | The name of the recovery group to create.  |
| tags | [Tags](#recoverygroups-model-tags) | False |  |

### RecoveryGroupOutput
<a name="recoverygroups-model-recoverygroupoutput"></a>

A representation of the application, typically containing multiple cells.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| cells | Array of type string | True | A list of a cell's Amazon Resource Names (ARNs). |
| recoveryGroupArn | string<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) for the recovery group. |
| recoveryGroupName | string<br />Pattern: `\A[a-zA-Z0-9_]+\z`<br />MaxLength: 64 | True | The name of the recovery group. |
| tags | [Tags](#recoverygroups-model-tags) | False | The tags associated with the recovery group. |

### Tags
<a name="recoverygroups-model-tags"></a>

A collection of tags associated with a resource.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| `*` | string | False |  |

## See also
<a name="recoverygroups-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListRecoveryGroups
<a name="ListRecoveryGroups-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/ListRecoveryGroups)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/ListRecoveryGroups)

### CreateRecoveryGroup
<a name="CreateRecoveryGroup-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for Python](/goto/boto3/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/aws-meridian-beta-2019-12-02/CreateRecoveryGroup)

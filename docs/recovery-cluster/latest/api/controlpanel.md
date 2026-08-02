---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel.html
---

# CreateControlPanel, UpdateControlPanel
<a name="controlpanel"></a>

## URI
<a name="controlpanel-url"></a>

`/controlpanel`

## HTTP methods
<a name="controlpanel-http-methods"></a>

### POST
<a name="controlpanelpost"></a>

**Operation ID:** `CreateControlPanel`

Creates a new control panel. A control panel represents a group of routing controls that can be changed together in a single transaction. You can use a control panel to centrally view the operational status of applications across your organization, and trigger multi-app failovers in a single transaction, for example, to fail over an Availability Zone or AWS Region.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateControlPanelResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 402 | ServiceQuotaExceededException | 402 response |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### PUT
<a name="controlpanelput"></a>

**Operation ID:** `UpdateControlPanel`

Updates a control panel. The only update that you can make to a control panel is to change its name.

Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateControlPanelResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="controlpaneloptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="controlpanel-schemas"></a>

### Request bodies
<a name="controlpanel-request-examples"></a>

#### POST schema
<a name="controlpanel-request-body-post-example"></a>

```
{
  "ClusterArn": "string",
  "ClientToken": "string",
  "ControlPanelName": "string",
  "Tags": {
  }
}
```

#### PUT schema
<a name="controlpanel-request-body-put-example"></a>

```
{
  "ControlPanelArn": "string",
  "ControlPanelName": "string"
}
```

### Response bodies
<a name="controlpanel-response-examples"></a>

#### CreateControlPanelResponse schema
<a name="controlpanel-response-body-createcontrolpanelresponse-example"></a>

```
{
  "ControlPanel": {
    "ClusterArn": "string",
    "Status": enum,
    "Owner": "string",
    "ControlPanelArn": "string",
    "DefaultControlPanel": boolean,
    "RoutingControlCount": integer,
    "Name": "string"
  }
}
```

#### UpdateControlPanelResponse schema
<a name="controlpanel-response-body-updatecontrolpanelresponse-example"></a>

```
{
  "ControlPanel": {
    "ClusterArn": "string",
    "Status": enum,
    "Owner": "string",
    "ControlPanelArn": "string",
    "DefaultControlPanel": boolean,
    "RoutingControlCount": integer,
    "Name": "string"
  }
}
```

#### ValidationException schema
<a name="controlpanel-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="controlpanel-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="controlpanel-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="controlpanel-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="controlpanel-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="controlpanel-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="controlpanel-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="controlpanel-properties"></a>

### AccessDeniedException
<a name="controlpanel-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ConflictException
<a name="controlpanel-model-conflictexception"></a>

409 response - ConflictException. You might be using a predefined variable.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ControlPanel
<a name="controlpanel-model-controlpanel"></a>

A control panel represents a group of routing controls that can be changed together in a single transaction.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the cluster that includes the control panel. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel. |
| DefaultControlPanel | boolean | False | A flag that Amazon Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the control panel. Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel. |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the control panel owner. |
| RoutingControlCount | integer<br />Format: int32 | False | The number of routing controls in the control panel. |
| Status | [Status](#controlpanel-model-status) | False | The deployment status of the control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### CreateControlPanelRequest
<a name="controlpanel-model-createcontrolpanelrequest"></a>

A request to create a control panel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClientToken | string<br />Pattern: `^[-a-z-A-z0-9 ]+$`<br />MinLength: 1<br />MaxLength: 64 | False | A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request. |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the cluster for the control panel. |
| ControlPanelName | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the control panel. Note that only ASCII characters are supported for control panel names. |
| Tags | object | False | The tags associated with the control panel. |

### CreateControlPanelResponse
<a name="controlpanel-model-createcontrolpanelresponse"></a>

The result of a successful `CreateControlPanel` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanel | [ControlPanel](#controlpanel-model-controlpanel) | True | Information about a control panel, including a list of the routing controls included in it. |

### InternalServerException
<a name="controlpanel-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ResourceNotFoundException
<a name="controlpanel-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ServiceQuotaExceededException
<a name="controlpanel-model-servicequotaexceededexception"></a>

402 response - You attempted to create more resources than the service allows based on service quotas.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Status
<a name="controlpanel-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="controlpanel-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### UpdateControlPanelRequest
<a name="controlpanel-model-updatecontrolpanelrequest"></a>

Updates an existing control panel.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the control panel. |
| ControlPanelName | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the control panel. Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel. |

### UpdateControlPanelResponse
<a name="controlpanel-model-updatecontrolpanelresponse"></a>

The result of a successful `UpdateControlPanel` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanel | [ControlPanel](#controlpanel-model-controlpanel) | True | The control panel to update. |

### ValidationException
<a name="controlpanel-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="controlpanel-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateControlPanel
<a name="CreateControlPanel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/CreateControlPanel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/CreateControlPanel)

### UpdateControlPanel
<a name="UpdateControlPanel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/UpdateControlPanel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/UpdateControlPanel)

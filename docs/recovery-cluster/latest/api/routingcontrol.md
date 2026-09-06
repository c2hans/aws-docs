---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol.html
---

# CreateRoutingControl, UpdateRoutingControl
<a name="routingcontrol"></a>

## URI
<a name="routingcontrol-url"></a>

`/routingcontrol`

## HTTP methods
<a name="routingcontrol-http-methods"></a>

### POST
<a name="routingcontrolpost"></a>

**Operation ID:** `CreateRoutingControl`

Creates a new routing control.

A routing control has one of two states: ON and OFF. You configure routing controls so they update Amazon Route 53 health checks, which reroute traffic for your application.

Note that a routing control name must be unique within a control panel.

To get or update the routing control state, see the [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html) API in the Routing Control (Recovery Cluster) API Reference Guide for Amazon Application Recovery Controller.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateRoutingControlResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 402 | ServiceQuotaExceededException | 402 response |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### PUT
<a name="routingcontrolput"></a>

**Operation ID:** `UpdateRoutingControl`

Updates a routing control. You can only update the name of the routing control. The name must be unique within a control panel. To get or update the routing control state, see the [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html) API in the Routing Control (Recovery Cluster) API Reference Guide for Amazon Application Recovery Controller.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateRoutingControlResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="routingcontroloptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="routingcontrol-schemas"></a>

### Request bodies
<a name="routingcontrol-request-examples"></a>

#### POST schema
<a name="routingcontrol-request-body-post-example"></a>

```
{
  "ClusterArn": "string",
  "RoutingControlName": "string",
  "ControlPanelArn": "string",
  "ClientToken": "string"
}
```

#### PUT schema
<a name="routingcontrol-request-body-put-example"></a>

```
{
  "RoutingControlName": "string",
  "RoutingControlArn": "string"
}
```

### Response bodies
<a name="routingcontrol-response-examples"></a>

#### CreateRoutingControlResponse schema
<a name="routingcontrol-response-body-createroutingcontrolresponse-example"></a>

```
{
  "RoutingControl": {
    "Status": enum,
    "Owner": "string",
    "RoutingControlArn": "string",
    "ControlPanelArn": "string",
    "Name": "string"
  }
}
```

#### UpdateRoutingControlResponse schema
<a name="routingcontrol-response-body-updateroutingcontrolresponse-example"></a>

```
{
  "RoutingControl": {
    "Status": enum,
    "Owner": "string",
    "RoutingControlArn": "string",
    "ControlPanelArn": "string",
    "Name": "string"
  }
}
```

#### ValidationException schema
<a name="routingcontrol-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="routingcontrol-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="routingcontrol-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="routingcontrol-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="routingcontrol-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="routingcontrol-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="routingcontrol-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="routingcontrol-properties"></a>

### AccessDeniedException
<a name="routingcontrol-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ConflictException
<a name="routingcontrol-model-conflictexception"></a>

409 response - ConflictException. You might be using a predefined variable.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### CreateRoutingControlRequest
<a name="routingcontrol-model-createroutingcontrolrequest"></a>

A request to create a routing control. If you don't specify `ControlPanelArn`, Amazon Application Recovery Controller creates the routing control in `DefaultControlPanel`.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClientToken | string<br />Pattern: `^[-a-z-A-z0-9 ]+$`<br />MinLength: 1<br />MaxLength: 64 | False | A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request. |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the cluster that includes the routing control. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel that includes the routing control. |
| RoutingControlName | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the routing control. Note that only ASCII characters are supported for routing control names. |

### CreateRoutingControlResponse
<a name="routingcontrol-model-createroutingcontrolresponse"></a>

The result of a successful `CreateRoutingControl` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| RoutingControl | [RoutingControl](#routingcontrol-model-routingcontrol) | False | The routing control that is created. |

### InternalServerException
<a name="routingcontrol-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ResourceNotFoundException
<a name="routingcontrol-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### RoutingControl
<a name="routingcontrol-model-routingcontrol"></a>

A routing control has one of two states: ON and OFF. You configure routing controls so they update Amazon Route 53 health checks, which reroute traffic for your application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel that includes the routing control. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the routing control. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the routing control owner. |
| RoutingControlArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the routing control. |
| Status | [Status](#routingcontrol-model-status) | False | The deployment status of a routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### ServiceQuotaExceededException
<a name="routingcontrol-model-servicequotaexceededexception"></a>

402 response - You attempted to create more resources than the service allows based on service quotas.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Status
<a name="routingcontrol-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="routingcontrol-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### UpdateRoutingControlRequest
<a name="routingcontrol-model-updateroutingcontrolrequest"></a>

A request to update a routing control.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| RoutingControlArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True | The Amazon Resource Name (ARN) of the routing control. |
| RoutingControlName | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the routing control. Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel. |

### UpdateRoutingControlResponse
<a name="routingcontrol-model-updateroutingcontrolresponse"></a>

The result of a successful `UpdateRoutingControl` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| RoutingControl | [RoutingControl](#routingcontrol-model-routingcontrol) | True | The routing control that was updated. |

### ValidationException
<a name="routingcontrol-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="routingcontrol-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### CreateRoutingControl
<a name="CreateRoutingControl-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/CreateRoutingControl)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/CreateRoutingControl)

### UpdateRoutingControl
<a name="UpdateRoutingControl-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/UpdateRoutingControl)

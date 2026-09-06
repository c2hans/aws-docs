---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn.html
---

# DescribeRoutingControl, DeleteRoutingControl
<a name="routingcontrol-routingcontrolarn"></a>

## URI
<a name="routingcontrol-routingcontrolarn-url"></a>

`/routingcontrol/{{RoutingControlArn}}`

## HTTP methods
<a name="routingcontrol-routingcontrolarn-http-methods"></a>

### GET
<a name="routingcontrol-routingcontrolarnget"></a>

**Operation ID:** `DescribeRoutingControl`

Displays details about a routing control. A routing control has one of two states: ON or OFF. When you change routing control states, ARC updates Amazon Route 53 health checks, which reroute traffic for your application.

To get or update the routing control state, see the [GetRoutingControlState](https://docs.aws.amazon.com/routing-control/latest/APIReference/API_GetRoutingControlState.html) API in the Routing Control (Recovery Cluster) API Reference Guide for Amazon Application Recovery Controller.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{RoutingControlArn}} | String | True | The Amazon Resource Name (ARN) of the routing control. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeRoutingControlResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### DELETE
<a name="routingcontrol-routingcontrolarndelete"></a>

**Operation ID:** `DeleteRoutingControl`

Deletes a routing control.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{RoutingControlArn}} | String | True | The Amazon Resource Name (ARN) of the routing control that you're deleting. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteRoutingControlResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="routingcontrol-routingcontrolarnoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{RoutingControlArn}} | String | True | The Amazon Resource Name (ARN) of a routing control. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="routingcontrol-routingcontrolarn-schemas"></a>

### Response bodies
<a name="routingcontrol-routingcontrolarn-response-examples"></a>

#### DescribeRoutingControlResponse schema
<a name="routingcontrol-routingcontrolarn-response-body-describeroutingcontrolresponse-example"></a>

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

#### DeleteRoutingControlResponse schema
<a name="routingcontrol-routingcontrolarn-response-body-deleteroutingcontrolresponse-example"></a>

```
{
}
```

#### ValidationException schema
<a name="routingcontrol-routingcontrolarn-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="routingcontrol-routingcontrolarn-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="routingcontrol-routingcontrolarn-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="routingcontrol-routingcontrolarn-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="routingcontrol-routingcontrolarn-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="routingcontrol-routingcontrolarn-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="routingcontrol-routingcontrolarn-properties"></a>

### AccessDeniedException
<a name="routingcontrol-routingcontrolarn-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ConflictException
<a name="routingcontrol-routingcontrolarn-model-conflictexception"></a>

409 response - ConflictException. You might be using a predefined variable.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### DeleteRoutingControlResponse
<a name="routingcontrol-routingcontrolarn-model-deleteroutingcontrolresponse"></a>

A successful `DeleteRoutingControl` request returns no response.

### DescribeRoutingControlResponse
<a name="routingcontrol-routingcontrolarn-model-describeroutingcontrolresponse"></a>

The result of a successful `DescribeRoutingControl` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| RoutingControl | [RoutingControl](#routingcontrol-routingcontrolarn-model-routingcontrol) | True | Information about the routing control. |

### InternalServerException
<a name="routingcontrol-routingcontrolarn-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ResourceNotFoundException
<a name="routingcontrol-routingcontrolarn-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### RoutingControl
<a name="routingcontrol-routingcontrolarn-model-routingcontrol"></a>

A routing control has one of two states: ON and OFF. You configure routing controls so they update Amazon Route 53 health checks, which reroute traffic for your application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel that includes the routing control. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the routing control. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the routing control owner. |
| RoutingControlArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the routing control. |
| Status | [Status](#routingcontrol-routingcontrolarn-model-status) | False | The deployment status of a routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### Status
<a name="routingcontrol-routingcontrolarn-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="routingcontrol-routingcontrolarn-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="routingcontrol-routingcontrolarn-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="routingcontrol-routingcontrolarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeRoutingControl
<a name="DescribeRoutingControl-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/DescribeRoutingControl)

### DeleteRoutingControl
<a name="DeleteRoutingControl-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/DeleteRoutingControl)

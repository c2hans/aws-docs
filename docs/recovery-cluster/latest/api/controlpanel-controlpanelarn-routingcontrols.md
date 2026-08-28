---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn-routingcontrols.html
---

# ListRoutingControls
<a name="controlpanel-controlpanelarn-routingcontrols"></a>

## URI
<a name="controlpanel-controlpanelarn-routingcontrols-url"></a>

`/controlpanel/{{ControlPanelArn}}/routingcontrols`

## HTTP methods
<a name="controlpanel-controlpanelarn-routingcontrols-http-methods"></a>

### GET
<a name="controlpanel-controlpanelarn-routingcontrolsget"></a>

**Operation ID:** `ListRoutingControls`

Returns an array of routing controls for a control panel. A routing control is an Amazon Application Recovery Controller construct that has one of two states: ON and OFF. You configure routing controls so they update Amazon Route 53 health checks, which reroute traffic for your application.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of the control panel. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| MaxResults | String | False | The number of objects that you want to return with this call. |
| NextToken | String | False | The token that identifies which batch of results you want to see. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListRoutingControlsResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="controlpanel-controlpanelarn-routingcontrolsoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of a control panel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="controlpanel-controlpanelarn-routingcontrols-schemas"></a>

### Response bodies
<a name="controlpanel-controlpanelarn-routingcontrols-response-examples"></a>

#### ListRoutingControlsResponse schema
<a name="controlpanel-controlpanelarn-routingcontrols-response-body-listroutingcontrolsresponse-example"></a>

```
{
  "NextToken": "string",
  "RoutingControls": [
    {
      "Status": enum,
      "Owner": "string",
      "RoutingControlArn": "string",
      "ControlPanelArn": "string",
      "Name": "string"
    }
  ]
}
```

#### ValidationException schema
<a name="controlpanel-controlpanelarn-routingcontrols-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="controlpanel-controlpanelarn-routingcontrols-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="controlpanel-controlpanelarn-routingcontrols-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="controlpanel-controlpanelarn-routingcontrols-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="controlpanel-controlpanelarn-routingcontrols-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="controlpanel-controlpanelarn-routingcontrols-properties"></a>

### AccessDeniedException
<a name="controlpanel-controlpanelarn-routingcontrols-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### InternalServerException
<a name="controlpanel-controlpanelarn-routingcontrols-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ListRoutingControlsResponse
<a name="controlpanel-controlpanelarn-routingcontrols-model-listroutingcontrolsresponse"></a>

The result of a successful `ListRoutingControl` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| NextToken | string<br />Pattern: `[\S]*`<br />MinLength: 1<br />MaxLength: 8096 | False | The token that identifies which batch of results you want to see. |
| RoutingControls | Array of type [RoutingControl](#controlpanel-controlpanelarn-routingcontrols-model-routingcontrol) | False | An array of routing controls. |

### ResourceNotFoundException
<a name="controlpanel-controlpanelarn-routingcontrols-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### RoutingControl
<a name="controlpanel-controlpanelarn-routingcontrols-model-routingcontrol"></a>

A routing control has one of two states: ON and OFF. You configure routing controls so they update Amazon Route 53 health checks, which reroute traffic for your application.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel that includes the routing control. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the routing control. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the routing control owner. |
| RoutingControlArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the routing control. |
| Status | [Status](#controlpanel-controlpanelarn-routingcontrols-model-status) | False | The deployment status of a routing control. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### Status
<a name="controlpanel-controlpanelarn-routingcontrols-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="controlpanel-controlpanelarn-routingcontrols-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="controlpanel-controlpanelarn-routingcontrols-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="controlpanel-controlpanelarn-routingcontrols-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListRoutingControls
<a name="ListRoutingControls-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/ListRoutingControls)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/ListRoutingControls)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

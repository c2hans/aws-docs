---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanels.html
---

# ListControlPanels
<a name="controlpanels"></a>

## URI
<a name="controlpanels-url"></a>

`/controlpanels`

## HTTP methods
<a name="controlpanels-http-methods"></a>

### GET
<a name="controlpanelsget"></a>

**Operation ID:** `ListControlPanels`

Returns an array of control panels in an account or in a cluster.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | String | False | The Amazon Resource Name (ARN) of a cluster. |
| MaxResults | String | False | The number of objects that you want to return with this call. |
| NextToken | String | False | The token that identifies which batch of results you want to see. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListControlPanelsResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="controlpanelsoptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="controlpanels-schemas"></a>

### Response bodies
<a name="controlpanels-response-examples"></a>

#### ListControlPanelsResponse schema
<a name="controlpanels-response-body-listcontrolpanelsresponse-example"></a>

```
{
  "ControlPanels": [
    {
      "ClusterArn": "string",
      "Status": enum,
      "Owner": "string",
      "ControlPanelArn": "string",
      "DefaultControlPanel": boolean,
      "RoutingControlCount": integer,
      "Name": "string"
    }
  ],
  "NextToken": "string"
}
```

#### ValidationException schema
<a name="controlpanels-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="controlpanels-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="controlpanels-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="controlpanels-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="controlpanels-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="controlpanels-properties"></a>

### AccessDeniedException
<a name="controlpanels-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ControlPanel
<a name="controlpanels-model-controlpanel"></a>

A control panel represents a group of routing controls that can be changed together in a single transaction.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the cluster that includes the control panel. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel. |
| DefaultControlPanel | boolean | False | A flag that Amazon Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the control panel. Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel. |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the control panel owner. |
| RoutingControlCount | integer<br />Format: int32 | False | The number of routing controls in the control panel. |
| Status | [Status](#controlpanels-model-status) | False | The deployment status of the control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### InternalServerException
<a name="controlpanels-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ListControlPanelsResponse
<a name="controlpanels-model-listcontrolpanelsresponse"></a>

The result of a successful `ListControlPanel` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanels | Array of type [ControlPanel](#controlpanels-model-controlpanel) | False | The result of a successful `ListControlPanel` request.  |
| NextToken | string<br />Pattern: `[\S]*`<br />MinLength: 1<br />MaxLength: 8096 | False | The token that identifies which batch of results you want to see. |

### ResourceNotFoundException
<a name="controlpanels-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Status
<a name="controlpanels-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="controlpanels-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="controlpanels-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="controlpanels-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListControlPanels
<a name="ListControlPanels-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/ListControlPanels)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/ListControlPanels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

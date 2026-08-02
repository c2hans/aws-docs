---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/controlpanel-controlpanelarn.html
---

# DescribeControlPanel, DeleteControlPanel
<a name="controlpanel-controlpanelarn"></a>

## URI
<a name="controlpanel-controlpanelarn-url"></a>

`/controlpanel/{{ControlPanelArn}}`

## HTTP methods
<a name="controlpanel-controlpanelarn-http-methods"></a>

### GET
<a name="controlpanel-controlpanelarnget"></a>

**Operation ID:** `DescribeControlPanel`

Displays details about a control panel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of the control panel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeControlPanelResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### DELETE
<a name="controlpanel-controlpanelarndelete"></a>

**Operation ID:** `DeleteControlPanel`

Deletes a control panel.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of the control panel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteControlPanelResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="controlpanel-controlpanelarnoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ControlPanelArn}} | String | True | The Amazon Resource Name (ARN) of a control panel. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="controlpanel-controlpanelarn-schemas"></a>

### Response bodies
<a name="controlpanel-controlpanelarn-response-examples"></a>

#### DescribeControlPanelResponse schema
<a name="controlpanel-controlpanelarn-response-body-describecontrolpanelresponse-example"></a>

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

#### DeleteControlPanelResponse schema
<a name="controlpanel-controlpanelarn-response-body-deletecontrolpanelresponse-example"></a>

```
{
}
```

#### ValidationException schema
<a name="controlpanel-controlpanelarn-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="controlpanel-controlpanelarn-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="controlpanel-controlpanelarn-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="controlpanel-controlpanelarn-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="controlpanel-controlpanelarn-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="controlpanel-controlpanelarn-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="controlpanel-controlpanelarn-properties"></a>

### AccessDeniedException
<a name="controlpanel-controlpanelarn-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ConflictException
<a name="controlpanel-controlpanelarn-model-conflictexception"></a>

409 response - ConflictException. You might be using a predefined variable.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ControlPanel
<a name="controlpanel-controlpanelarn-model-controlpanel"></a>

A control panel represents a group of routing controls that can be changed together in a single transaction.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the cluster that includes the control panel. |
| ControlPanelArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the control panel. |
| DefaultControlPanel | boolean | False | A flag that Amazon Application Recovery Controller sets to true to designate the default control panel for a cluster. When you create a cluster, Amazon Application Recovery Controller creates a control panel, and sets this flag for that control panel. If you create a control panel yourself, this flag is set to false. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the control panel. Note that only ASCII characters are supported for control panel names, and each name must be unique within a control panel. |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the control panel owner. |
| RoutingControlCount | integer<br />Format: int32 | False | The number of routing controls in the control panel. |
| Status | [Status](#controlpanel-controlpanelarn-model-status) | False | The deployment status of the control panel. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### DeleteControlPanelResponse
<a name="controlpanel-controlpanelarn-model-deletecontrolpanelresponse"></a>

A successful `DeleteControlPanel` request returns no response.

### DescribeControlPanelResponse
<a name="controlpanel-controlpanelarn-model-describecontrolpanelresponse"></a>

The result of a successful `DescribeControlPanel` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ControlPanel | [ControlPanel](#controlpanel-controlpanelarn-model-controlpanel) | True | Information about the control panel, including a list of the routing controls that it includes. |

### InternalServerException
<a name="controlpanel-controlpanelarn-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ResourceNotFoundException
<a name="controlpanel-controlpanelarn-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Status
<a name="controlpanel-controlpanelarn-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="controlpanel-controlpanelarn-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="controlpanel-controlpanelarn-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="controlpanel-controlpanelarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeControlPanel
<a name="DescribeControlPanel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/DescribeControlPanel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/DescribeControlPanel)

### DeleteControlPanel
<a name="DeleteControlPanel-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/DeleteControlPanel)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/DeleteControlPanel)

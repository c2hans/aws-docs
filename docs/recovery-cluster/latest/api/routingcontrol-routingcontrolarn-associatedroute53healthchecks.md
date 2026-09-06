---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/routingcontrol-routingcontrolarn-associatedroute53healthchecks.html
---

# ListAssociatedRoute53HealthChecks
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks"></a>

## URI
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-url"></a>

`/routingcontrol/{{RoutingControlArn}}/associatedRoute53HealthChecks`

## HTTP methods
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-http-methods"></a>

### GET
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecksget"></a>

**Operation ID:** `ListAssociatedRoute53HealthChecks`

Returns an array of all Amazon Route 53 health checks associated with a specific routing control.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{RoutingControlArn}} | String | True | The Amazon Resource Name (ARN) of the routing control. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| MaxResults | String | False | The number of objects that you want to return with this call. |
| NextToken | String | False | The token that identifies which batch of results you want to see. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListAssociatedRoute53HealthChecksResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecksoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{RoutingControlArn}} | String | True | The Amazon Resource Name (ARN) of a routing control. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-schemas"></a>

### Response bodies
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-response-examples"></a>

#### ListAssociatedRoute53HealthChecksResponse schema
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-response-body-listassociatedroute53healthchecksresponse-example"></a>

```
{
  "NextToken": "string",
  "HealthCheckIds": [
    "string"
  ]
}
```

#### ValidationException schema
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-properties"></a>

### InternalServerException
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ListAssociatedRoute53HealthChecksResponse
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-model-listassociatedroute53healthchecksresponse"></a>

The result of a successful `ListAssociatedRoute53HealthChecks` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| HealthCheckIds | Array of type string<br />Pattern: `^\S+$`<br />MaxLength: 36 | True | Identifiers for the health checks. |
| NextToken | string<br />Pattern: `[\S]*`<br />MinLength: 1<br />MaxLength: 8096 | False | Next token for listing health checks. |

### ResourceNotFoundException
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="routingcontrol-routingcontrolarn-associatedroute53healthchecks-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListAssociatedRoute53HealthChecks
<a name="ListAssociatedRoute53HealthChecks-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/ListAssociatedRoute53HealthChecks)

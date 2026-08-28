---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster-clusterarn.html
---

# DescribeCluster, DeleteCluster
<a name="cluster-clusterarn"></a>

## URI
<a name="cluster-clusterarn-url"></a>

`/cluster/{{ClusterArn}}`

## HTTP methods
<a name="cluster-clusterarn-http-methods"></a>

### GET
<a name="cluster-clusterarnget"></a>

**Operation ID:** `DescribeCluster`

Display the details about a cluster. The response includes the cluster name, endpoints, status, and Amazon Resource Name (ARN).

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ClusterArn}} | String | True | The Amazon Resource Name (ARN) of the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DescribeClusterResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### DELETE
<a name="cluster-clusterarndelete"></a>

**Operation ID:** `DeleteCluster`

Delete a cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ClusterArn}} | String | True | The Amazon Resource Name (ARN) of the cluster that you're deleting. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | DeleteClusterResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="cluster-clusterarnoptions"></a>

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{ClusterArn}} | String | True | The Amazon Resource Name (ARN) of a cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="cluster-clusterarn-schemas"></a>

### Response bodies
<a name="cluster-clusterarn-response-examples"></a>

#### DescribeClusterResponse schema
<a name="cluster-clusterarn-response-body-describeclusterresponse-example"></a>

```
{
  "Cluster": {
    "ClusterArn": "string",
    "Status": enum,
    "Owner": "string",
    "NetworkType": enum,
    "ClusterEndpoints": [
      {
        "Endpoint": "string",
        "Region": "string"
      }
    ],
    "Name": "string"
  }
}
```

#### DeleteClusterResponse schema
<a name="cluster-clusterarn-response-body-deleteclusterresponse-example"></a>

```
{
}
```

#### ValidationException schema
<a name="cluster-clusterarn-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="cluster-clusterarn-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="cluster-clusterarn-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="cluster-clusterarn-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="cluster-clusterarn-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="cluster-clusterarn-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="cluster-clusterarn-properties"></a>

### AccessDeniedException
<a name="cluster-clusterarn-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Cluster
<a name="cluster-clusterarn-model-cluster"></a>

A set of five redundant Regional endpoints against which you can execute API calls to update or get the state of routing controls. You can host multiple control panels and routing controls on one cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the cluster. |
| ClusterEndpoints | Array of type [ClusterEndpoint](#cluster-clusterarn-model-clusterendpoint) | False | Endpoints for a cluster. Specify one of these endpoints when you want to set or retrieve a routing control state in the cluster. To learn more, see [ Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html) in the Amazon Application Recovery Controller Developer Guide.<br />To learn more about getting or updating a routing control state, see [Routing control](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html) in the Amazon Application Recovery Controller Developer Guide. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the cluster. Note that only ASCII characters are supported for cluster names. |
| NetworkType | [NetworkType](#cluster-clusterarn-model-networktype) | False | The network-type can either be IPV4 or DUALSTACK. |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the cluster owner. |
| Status | [Status](#cluster-clusterarn-model-status) | False | Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### ClusterEndpoint
<a name="cluster-clusterarn-model-clusterendpoint"></a>

A cluster endpoint. Specify an endpoint when you want to set or retrieve a routing control state in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Endpoint | string<br />Pattern: `^[A-Za-z0-9:.\/_-]*$`<br />MinLength: 1<br />MaxLength: 128 | False | A cluster endpoint. Specify an endpoint and AWS Region when you want to set or retrieve a routing control state in the cluster.<br />To get or update the routing control state, see the Amazon Application Recovery Controller Routing Control Actions. |
| Region | string<br />Pattern: `^\S+$`<br />MinLength: 1<br />MaxLength: 32 | False | The AWS Region for a cluster endpoint. |

### ConflictException
<a name="cluster-clusterarn-model-conflictexception"></a>

409 response - ConflictException. You might be using a predefined variable.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### DeleteClusterResponse
<a name="cluster-clusterarn-model-deleteclusterresponse"></a>

A successful `DeleteCluster` request returns no response.

### DescribeClusterResponse
<a name="cluster-clusterarn-model-describeclusterresponse"></a>

The result of a successful `DescribeCluster` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Cluster | [Cluster](#cluster-clusterarn-model-cluster) | True | The cluster for the `DescribeCluster` request. |

### InternalServerException
<a name="cluster-clusterarn-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### NetworkType
<a name="cluster-clusterarn-model-networktype"></a>

The network-type of a cluster can either be IPV4 or DUALSTACK.
+ `IPV4`
+ `DUALSTACK`

### ResourceNotFoundException
<a name="cluster-clusterarn-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Status
<a name="cluster-clusterarn-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="cluster-clusterarn-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ValidationException
<a name="cluster-clusterarn-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="cluster-clusterarn-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### DescribeCluster
<a name="DescribeCluster-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/DescribeCluster)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/DescribeCluster)

### DeleteCluster
<a name="DeleteCluster-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/DeleteCluster)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/DeleteCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Application Recovery Controller. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query recovery-cluster` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

---
source_url: https://docs.aws.amazon.com/recovery-cluster/latest/api/cluster.html
---

# ListClusters, CreateCluster, UpdateCluster
<a name="cluster"></a>

## URI
<a name="cluster-url"></a>

`/cluster`

## HTTP methods
<a name="cluster-http-methods"></a>

### GET
<a name="clusterget"></a>

**Operation ID:** `ListClusters`

Returns an array of all the clusters in an account.

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| MaxResults | String | False | The number of objects that you want to return with this call. |
| NextToken | String | False | The token that identifies which batch of results you want to see. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | ListClustersResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### POST
<a name="clusterpost"></a>

**Operation ID:** `CreateCluster`

Create a new cluster. A cluster is a set of redundant Regional endpoints against which you can run API calls to update or get the state of one or more routing controls. Each cluster has a name, status, Amazon Resource Name (ARN), and an array of the five cluster endpoints (one for each supported AWS Region) that you can use with API calls to the cluster data plane.

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | CreateClusterResponse | 200 response - Success. |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 402 | ServiceQuotaExceededException | 402 response |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### PUT
<a name="clusterput"></a>

**Operation ID:** `UpdateCluster`

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | UpdateClusterResponse | 200 response |
| 400 | ValidationException | 400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you used parameters together incorrectly. |
| 403 | AccessDeniedException | 403 response - AccessDeniedException. You do not have sufficient access to perform this action. |
| 404 | ResourceNotFoundException | 404 response - MalformedQueryString. The query string contains a syntax error or resource not found. |
| 409 | ConflictException | 409 response - ConflictException. You might be using a predefined variable. |
| 429 | ThrottlingException | 429 response - LimitExceededException or TooManyRequestsException. |
| 500 | InternalServerException | 500 response - InternalServiceError. Temporary service error. Retry the request. |

### OPTIONS
<a name="clusteroptions"></a>

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | 200 response - Success. |

## Schemas
<a name="cluster-schemas"></a>

### Request bodies
<a name="cluster-request-examples"></a>

#### POST schema
<a name="cluster-request-body-post-example"></a>

```
{
  "UseRoute53GammaHealthChecks": boolean,
  "NetworkType": enum,
  "ClusterName": "string",
  "ClientToken": "string",
  "Tags": {
  }
}
```

#### PUT schema
<a name="cluster-request-body-put-example"></a>

```
{
  "ClusterArn": "string",
  "NetworkType": enum
}
```

### Response bodies
<a name="cluster-response-examples"></a>

#### ListClustersResponse schema
<a name="cluster-response-body-listclustersresponse-example"></a>

```
{
  "NextToken": "string",
  "Clusters": [
    {
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
  ]
}
```

#### CreateClusterResponse schema
<a name="cluster-response-body-createclusterresponse-example"></a>

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

#### UpdateClusterResponse schema
<a name="cluster-response-body-updateclusterresponse-example"></a>

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

#### ValidationException schema
<a name="cluster-response-body-validationexception-example"></a>

```
{
  "message": "string"
}
```

#### ServiceQuotaExceededException schema
<a name="cluster-response-body-servicequotaexceededexception-example"></a>

```
{
  "message": "string"
}
```

#### AccessDeniedException schema
<a name="cluster-response-body-accessdeniedexception-example"></a>

```
{
  "message": "string"
}
```

#### ResourceNotFoundException schema
<a name="cluster-response-body-resourcenotfoundexception-example"></a>

```
{
  "message": "string"
}
```

#### ConflictException schema
<a name="cluster-response-body-conflictexception-example"></a>

```
{
  "message": "string"
}
```

#### ThrottlingException schema
<a name="cluster-response-body-throttlingexception-example"></a>

```
{
  "message": "string"
}
```

#### InternalServerException schema
<a name="cluster-response-body-internalserverexception-example"></a>

```
{
  "message": "string"
}
```

## Properties
<a name="cluster-properties"></a>

### AccessDeniedException
<a name="cluster-model-accessdeniedexception"></a>

403 response - You do not have sufficient access to perform this action.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Cluster
<a name="cluster-model-cluster"></a>

A set of five redundant Regional endpoints against which you can execute API calls to update or get the state of routing controls. You can host multiple control panels and routing controls on one cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | False | The Amazon Resource Name (ARN) of the cluster. |
| ClusterEndpoints | Array of type [ClusterEndpoint](#cluster-model-clusterendpoint) | False | Endpoints for a cluster. Specify one of these endpoints when you want to set or retrieve a routing control state in the cluster. To learn more, see [ Best practices](https://docs.aws.amazon.com/r53recovery/latest/dg/route53-arc-best-practices.html) in the Amazon Application Recovery Controller Developer Guide.<br />To learn more about getting or updating a routing control state, see [Routing control](https://docs.aws.amazon.com/r53recovery/latest/dg/routing-control.html) in the Amazon Application Recovery Controller Developer Guide. |
| Name | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | False | The name of the cluster. Note that only ASCII characters are supported for cluster names. |
| NetworkType | [NetworkType](#cluster-model-networktype) | False | The network-type can either be IPV4 or DUALSTACK. |
| Owner | string<br />Pattern: `^\d{12}$`<br />MinLength: 12<br />MaxLength: 12 | False | The AWS account ID of the cluster owner. |
| Status | [Status](#cluster-model-status) | False | Deployment status of a resource. Status can be one of the following: PENDING, DEPLOYED, PENDING\_DELETION. |

### ClusterEndpoint
<a name="cluster-model-clusterendpoint"></a>

A cluster endpoint. Specify an endpoint when you want to set or retrieve a routing control state in the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Endpoint | string<br />Pattern: `^[A-Za-z0-9:.\/_-]*$`<br />MinLength: 1<br />MaxLength: 128 | False | A cluster endpoint. Specify an endpoint and AWS Region when you want to set or retrieve a routing control state in the cluster.<br />To get or update the routing control state, see the Amazon Application Recovery Controller Routing Control Actions. |
| Region | string<br />Pattern: `^\S+$`<br />MinLength: 1<br />MaxLength: 32 | False | The AWS Region for a cluster endpoint. |

### ConflictException
<a name="cluster-model-conflictexception"></a>

409 response - ConflictException. You might be using a predefined variable.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### CreateClusterRequest
<a name="cluster-model-createclusterrequest"></a>

The properties of a request to create a cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClientToken | string<br />Pattern: `^[-a-z-A-z0-9 ]+$`<br />MinLength: 1<br />MaxLength: 64 | False | A unique, case-sensitive string of up to 64 ASCII characters. To make an idempotent API request with an action, specify a client token in the request. |
| ClusterName | string<br />Pattern: `^((?![;'\s<>&"])[\u0021-\u007E])+$`<br />MinLength: 1<br />MaxLength: 64 | True | The name of the cluster. You can use any non-white space character in the name except the following: & > < ' (single quote) " (double quote) ; (semicolon) |
| NetworkType | [NetworkType](#cluster-model-networktype) | False | The network-type is optional, and can either be IPV4 or DUALSTACK. The default is IPV4. |
| Tags | object | False | The tags associated with the cluster. |
| UseRoute53GammaHealthChecks | boolean | False |  |

### CreateClusterResponse
<a name="cluster-model-createclusterresponse"></a>

The result of a successful `CreateCluster` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Cluster | [Cluster](#cluster-model-cluster) | True | The cluster that was created. |

### InternalServerException
<a name="cluster-model-internalserverexception"></a>

500 response - InternalServiceError. Temporary service error. Retry the request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ListClustersResponse
<a name="cluster-model-listclustersresponse"></a>

The result of a successful `ListClusters` request.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Clusters | Array of type [Cluster](#cluster-model-cluster) | False | An array of the clusters in an account. |
| NextToken | string<br />Pattern: `[\S]*`<br />MinLength: 1<br />MaxLength: 8096 | False | The token that identifies which batch of results you want to see. |

### NetworkType
<a name="cluster-model-networktype"></a>

The network-type of a cluster can either be IPV4 or DUALSTACK.
+ `IPV4`
+ `DUALSTACK`

### ResourceNotFoundException
<a name="cluster-model-resourcenotfoundexception"></a>

404 response - MalformedQueryString. The query string contains a syntax error or resource not found.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### ServiceQuotaExceededException
<a name="cluster-model-servicequotaexceededexception"></a>

402 response - You attempted to create more resources than the service allows based on service quotas.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### Status
<a name="cluster-model-status"></a>

The deployment status of a resource. Status can be one of the following:

PENDING: Amazon Application Recovery Controller is creating the resource.

DEPLOYED: The resource is deployed and ready to use.

PENDING\_DELETION: Amazon Application Recovery Controller is deleting the resource.
+ `PENDING`
+ `DEPLOYED`
+ `PENDING_DELETION`

### ThrottlingException
<a name="cluster-model-throttlingexception"></a>

429 response - LimitExceededException or TooManyRequestsException.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

### UpdateClusterRequest
<a name="cluster-model-updateclusterrequest"></a>

Updates an existing cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| ClusterArn | string<br />Pattern: `^[A-Za-z0-9:\/_-]*$`<br />MinLength: 1<br />MaxLength: 256 | True |  |
| NetworkType | [NetworkType](#cluster-model-networktype) | True | The network-type is required, and can either be IPV4 or DUALSTACK. |

### UpdateClusterResponse
<a name="cluster-model-updateclusterresponse"></a>

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| Cluster | [Cluster](#cluster-model-cluster) | True | The result of a successful UpdateCluster request. |

### ValidationException
<a name="cluster-model-validationexception"></a>

400 response - Multiple causes. For example, you might have a malformed query string and input parameter might be out of range, or you might have used parameters together incorrectly.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| message | string | True |  |

## See also
<a name="cluster-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListClusters
<a name="ListClusters-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/ListClusters)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/ListClusters)

### CreateCluster
<a name="CreateCluster-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/CreateCluster)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/CreateCluster)

### UpdateCluster
<a name="UpdateCluster-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for Python](/goto/boto3/route53-recovery-control-config-2020-11-02/UpdateCluster)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/route53-recovery-control-config-2020-11-02/UpdateCluster)

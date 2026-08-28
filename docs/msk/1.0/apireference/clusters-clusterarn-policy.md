---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-policy.html
---

# Clusters clusterArn Policy
<a name="clusters-clusterarn-policy"></a>

## URI
<a name="clusters-clusterarn-policy-url"></a>

`/v1/clusters/{{clusterArn}}/policy`

## HTTP methods
<a name="clusters-clusterarn-policy-http-methods"></a>

### GET
<a name="clusters-clusterarn-policyget"></a>

**Operation ID:** `GetClusterPolicy`

Get cluster policy.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  GetClusterPolicyResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### PUT
<a name="clusters-clusterarn-policyput"></a>

**Operation ID:** `PutClusterPolicy`

Create or update cluster policy.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  PutClusterPolicyResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### DELETE
<a name="clusters-clusterarn-policydelete"></a>

**Operation ID:** `DeleteClusterPolicy`

Delete cluster policy.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  DeleteClusterPolicyResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-policyoptions"></a>

Enable CORS by returning correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

## Schemas
<a name="clusters-clusterarn-policy-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-policy-request-examples"></a>

#### PUT schema
<a name="clusters-clusterarn-policy-request-body-put-example"></a>

```
{
  "currentVersion": "string",
  "policy": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-policy-response-examples"></a>

#### GetClusterPolicyResponse schema
<a name="clusters-clusterarn-policy-response-body-getclusterpolicyresponse-example"></a>

```
{
  "currentVersion": "string",
  "policy": "string"
}
```

#### PutClusterPolicyResponse schema
<a name="clusters-clusterarn-policy-response-body-putclusterpolicyresponse-example"></a>

```
{
  "currentVersion": "string"
}
```

#### DeleteClusterPolicyResponse schema
<a name="clusters-clusterarn-policy-response-body-deleteclusterpolicyresponse-example"></a>

```
{
}
```

#### Error schema
<a name="clusters-clusterarn-policy-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-policy-properties"></a>

### DeleteClusterPolicyResponse
<a name="clusters-clusterarn-policy-model-deleteclusterpolicyresponse"></a>

Delete resource policy for MSK cluster

### Error
<a name="clusters-clusterarn-policy-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### GetClusterPolicyResponse
<a name="clusters-clusterarn-policy-model-getclusterpolicyresponse"></a>

Returns resource policy for MSK cluster

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | False | Resource policy version |
| policy | string | False | Resource policy attached to the MSK cluster |

### PutClusterPolicyRequest
<a name="clusters-clusterarn-policy-model-putclusterpolicyrequest"></a>

Create or update resource policy for cluster

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string<br />MinLength: 1 | False | Current cluster policy version. |
| policy | string<br />MinLength: 1<br />MaxLength: 20480 | True | Resource policy for cluster |

### PutClusterPolicyResponse
<a name="clusters-clusterarn-policy-model-putclusterpolicyresponse"></a>

Create or update cluster policy

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| currentVersion | string | False | Resource policy version |

## See also
<a name="clusters-clusterarn-policy-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### GetClusterPolicy
<a name="GetClusterPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/GetClusterPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/GetClusterPolicy)

### PutClusterPolicy
<a name="PutClusterPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/PutClusterPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/PutClusterPolicy)

### DeleteClusterPolicy
<a name="DeleteClusterPolicy-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/DeleteClusterPolicy)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/DeleteClusterPolicy)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Managed Streaming for Apache Kafka. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query msk` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

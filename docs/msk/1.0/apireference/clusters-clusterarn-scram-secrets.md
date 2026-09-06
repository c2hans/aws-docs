---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-scram-secrets.html
---

# Scram Secrets
<a name="clusters-clusterarn-scram-secrets"></a>

Represents a secret stored in the Amazon Secrets Manager that can be used to authenticate with a cluster using your sign-in credentials.

## URI
<a name="clusters-clusterarn-scram-secrets-url"></a>

`/v1/clusters/{{clusterArn}}/scram-secrets`

## HTTP methods
<a name="clusters-clusterarn-scram-secrets-http-methods"></a>

### GET
<a name="clusters-clusterarn-scram-secretsget"></a>

**Operation ID:** `ListScramSecrets`

Returns a list of SCRAM secrets associated with the cluster. SCRAM secrets are stored in the Amazon Secrets Manager service, and are used to authenticate clients using sign-in credentials.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Query parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | String | False | The paginated results marker. When the result of the operation is truncated, the call returns `NextToken` in the response. To get the next batch, provide this token in your next request. |
| maxResults | String | False | The maximum number of results to return in the response (default maximum 100 results per API call). If there are more results, the response includes a `NextToken` parameter. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  ListScramSecretsResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### POST
<a name="clusters-clusterarn-scram-secretspost"></a>

**Operation ID:** `BatchAssociateScramSecret`

Associates a list of SCRAM secrets with a cluster. SCRAM secrets are stored in the Amazon Secrets Manager service, and are used to authenticate clients using sign-in credentials. You can associate up to 10 secrets with a cluster at a time.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  BatchAssociateScramSecretResponse | Successful response. |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

### OPTIONS
<a name="clusters-clusterarn-scram-secretsoptions"></a>

Enable CORS by returning the correct headers.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 | None | Default response for CORS method |

### PATCH
<a name="clusters-clusterarn-scram-secretspatch"></a>

**Operation ID:** `BatchDisassociateScramSecret`

Disassociates a list of SCRAM secrets from a cluster. SCRAM secrets are stored in the Amazon Secrets Manager service, and are used to authenticate clients using sign-in credentials. You can disassociate up to 10 secrets from a cluster at a time.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  BatchDisassociateScramSecretResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

## Schemas
<a name="clusters-clusterarn-scram-secrets-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-scram-secrets-request-examples"></a>

#### POST schema
<a name="clusters-clusterarn-scram-secrets-request-body-post-example"></a>

```
{
  "secretArnList": [
    "string"
  ]
}
```

#### PATCH schema
<a name="clusters-clusterarn-scram-secrets-request-body-patch-example"></a>

```
{
  "secretArnList": [
    "string"
  ]
}
```

### Response bodies
<a name="clusters-clusterarn-scram-secrets-response-examples"></a>

#### ListScramSecretsResponse schema
<a name="clusters-clusterarn-scram-secrets-response-body-listscramsecretsresponse-example"></a>

```
{
  "secretArnList": [
    "string"
  ],
  "nextToken": "string"
}
```

#### BatchAssociateScramSecretResponse schema
<a name="clusters-clusterarn-scram-secrets-response-body-batchassociatescramsecretresponse-example"></a>

```
{
  "clusterArn": "string",
  "unprocessedScramSecrets": [
    {
      "secretArn": "string",
      "errorMessage": "string",
      "errorCode": "string"
    }
  ]
}
```

#### BatchDisassociateScramSecretResponse schema
<a name="clusters-clusterarn-scram-secrets-response-body-batchdisassociatescramsecretresponse-example"></a>

```
{
  "clusterArn": "string",
  "unprocessedScramSecrets": [
    {
      "secretArn": "string",
      "errorMessage": "string",
      "errorCode": "string"
    }
  ]
}
```

#### Error schema
<a name="clusters-clusterarn-scram-secrets-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-scram-secrets-properties"></a>

### BatchAssociateScramSecretRequest
<a name="clusters-clusterarn-scram-secrets-model-batchassociatescramsecretrequest"></a>

Request body for BatchAssociateScramSecret.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| secretArnList | Array of type string | True | List of Amazon Secrets Manager secret Amazon Resource Name (ARN)s. |

### BatchAssociateScramSecretResponse
<a name="clusters-clusterarn-scram-secrets-model-batchassociatescramsecretresponse"></a>

Response body for BatchAssociateScramSecret.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| unprocessedScramSecrets | Array of type [UnprocessedScramSecret](#clusters-clusterarn-scram-secrets-model-unprocessedscramsecret) | False | List of errors when associating secrets to cluster. |

### BatchDisassociateScramSecretRequest
<a name="clusters-clusterarn-scram-secrets-model-batchdisassociatescramsecretrequest"></a>

Request body for BatchDisassociateScramSecret.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| secretArnList | Array of type string | True | List of Amazon Secrets Manager secret Amazon Resource Name (ARN)s. |

### BatchDisassociateScramSecretResponse
<a name="clusters-clusterarn-scram-secrets-model-batchdisassociatescramsecretresponse"></a>

Response body for BatchDisassociateScramSecret.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| unprocessedScramSecrets | Array of type [UnprocessedScramSecret](#clusters-clusterarn-scram-secrets-model-unprocessedscramsecret) | False | List of errors when disassociating secrets to cluster. |

### Error
<a name="clusters-clusterarn-scram-secrets-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### ListScramSecretsResponse
<a name="clusters-clusterarn-scram-secrets-model-listscramsecretsresponse"></a>

Information about scram secrets associated to the cluster.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| nextToken | string | False | Paginated results marker. |
| secretArnList | Array of type string | False | The list of scram secrets associated with the cluster. |

### UnprocessedScramSecret
<a name="clusters-clusterarn-scram-secrets-model-unprocessedscramsecret"></a>

Error info for scram secret associate/disassociate failure.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| errorCode | string | False | Error code for associate/disassociate failure. |
| errorMessage | string | False | Error message for associate/disassociate failure. |
| secretArn | string | False | Amazon Secrets Manager secret Amazon Resource Name (ARN). |

## See also
<a name="clusters-clusterarn-scram-secrets-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### ListScramSecrets
<a name="ListScramSecrets-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/ListScramSecrets)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/ListScramSecrets)

### BatchAssociateScramSecret
<a name="BatchAssociateScramSecret-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/BatchAssociateScramSecret)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/BatchAssociateScramSecret)

### BatchDisassociateScramSecret
<a name="BatchDisassociateScramSecret-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/BatchDisassociateScramSecret)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/BatchDisassociateScramSecret)

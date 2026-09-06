---
source_url: https://docs.aws.amazon.com/msk/1.0/apireference/clusters-clusterarn-security.html
---

# Cluster Security
<a name="clusters-clusterarn-security"></a>

Use this resource to update the security settings of a cluster.

## URI
<a name="clusters-clusterarn-security-url"></a>

`/v1/clusters/{{clusterArn}}/security`

## HTTP methods
<a name="clusters-clusterarn-security-http-methods"></a>

### OPTIONS
<a name="clusters-clusterarn-securityoptions"></a>

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
<a name="clusters-clusterarn-securitypatch"></a>

**Operation ID:** `UpdateSecurity`

Updates security settings of the specified cluster.

**Path parameters**

| Name | Type | Required | Description |
| --- |--- |--- |--- |
| {{clusterArn}} | String | True | The Amazon Resource Name (ARN) that uniquely identifies the cluster. |

**Responses**

| Status code | Response model | Description |
| --- |--- |--- |
| 200 |  UpdateSecurityResponse | 200 response |
| 400 | Error | The request isn't valid because the input is incorrect. Correct your input and then submit it again. |
| 401 | Error | The request is not authorized. The provided credentials couldn't be validated. |
| 403 | Error | Access forbidden. Check your credentials and then retry your request. |
| 404 | Error | The resource could not be found due to incorrect input. Correct the input, then retry the request. |
| 429 | Error | 429 response |
| 500 | Error | There was an unexpected internal server error. Retrying your request might resolve the issue. |
| 503 | Error | 503 response |

## Schemas
<a name="clusters-clusterarn-security-schemas"></a>

### Request bodies
<a name="clusters-clusterarn-security-request-examples"></a>

#### PATCH schema
<a name="clusters-clusterarn-security-request-body-patch-example"></a>

```
{
  "encryptionInfo": {
    "encryptionInTransit": {
      "inCluster": boolean,
      "clientBroker": enum
    },
    "encryptionAtRest": {
      "dataVolumeKMSKeyId": "string"
    }
  },
  "clientAuthentication": {
    "sasl": {
      "iam": {
        "enabled": boolean
      },
      "scram": {
        "enabled": boolean
      }
    },
    "unauthenticated": {
      "enabled": boolean
    },
    "tls": {
      "certificateAuthorityArnList": [
        "string"
      ],
      "enabled": boolean
    }
  },
  "currentVersion": "string"
}
```

### Response bodies
<a name="clusters-clusterarn-security-response-examples"></a>

#### UpdateSecurityResponse schema
<a name="clusters-clusterarn-security-response-body-updatesecurityresponse-example"></a>

```
{
  "clusterArn": "string",
  "clusterOperationArn": "string"
}
```

#### Error schema
<a name="clusters-clusterarn-security-response-body-error-example"></a>

```
{
  "message": "string",
  "invalidParameter": "string"
}
```

## Properties
<a name="clusters-clusterarn-security-properties"></a>

### ClientAuthentication
<a name="clusters-clusterarn-security-model-clientauthentication"></a>

Includes all client authentication information.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| sasl | [Sasl](#clusters-clusterarn-security-model-sasl) | False | Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true. |
| tls | [Tls](#clusters-clusterarn-security-model-tls) | False | Details for ClientAuthentication using TLS. To turn on TLS access control, you must also turn on `EncryptionInTransit` by setting `inCluster` to true and `clientBroker` to `TLS`. |
| unauthenticated | [Unauthenticated](#clusters-clusterarn-security-model-unauthenticated) | False | Details for ClientAuthentication using no authentication. |

### ClientBroker
<a name="clusters-clusterarn-security-model-clientbroker"></a>

Client-broker encryption in transit setting.
+ `TLS`
+ `TLS_PLAINTEXT`
+ `PLAINTEXT`

### EncryptionAtRest
<a name="clusters-clusterarn-security-model-encryptionatrest"></a>

The data-volume encryption details. You can't update encryption at rest settings for existing clusters.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| dataVolumeKMSKeyId | string | True | The Amazon Resource Name (ARN) of the Amazon KMS key for encrypting data at rest. If you don't specify a KMS key, MSK creates one for you and uses it. |

### EncryptionInTransit
<a name="clusters-clusterarn-security-model-encryptionintransit"></a>

The settings for encrypting data in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientBroker | [ClientBroker](#clusters-clusterarn-security-model-clientbroker) | False | Indicates the encryption setting for data in transit between clients and brokers. You must set it to one of the following values.<br /> `TLS` means that client-broker communication is enabled with TLS only.<br /> `TLS_PLAINTEXT` means that client-broker communication is enabled for both TLS-encrypted, as well as plaintext data.<br /> `PLAINTEXT` means that client-broker communication is enabled in plaintext only.<br />The default value is `TLS`. |
| inCluster | boolean | False | When set to true, it indicates that data communication among the broker nodes of the cluster is encrypted. When set to false, the communication happens in plaintext.<br />The default value is true. |

### EncryptionInfo
<a name="clusters-clusterarn-security-model-encryptioninfo"></a>

Includes encryption-related information, such as the Amazon KMS key used for encrypting data at rest and whether you want MSK to encrypt your data in transit.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| encryptionAtRest | [EncryptionAtRest](#clusters-clusterarn-security-model-encryptionatrest) | False | The data-volume encryption details. |
| encryptionInTransit | [EncryptionInTransit](#clusters-clusterarn-security-model-encryptionintransit) | False | The details for encryption in transit. |

### Error
<a name="clusters-clusterarn-security-model-error"></a>

Returns information about an error.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| invalidParameter | string | False | The parameter that caused the error. |
| message | string | False | The description of the error. |

### IAM
<a name="clusters-clusterarn-security-model-iam"></a>

Details for SASL/IAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/IAM authentication is enabled or not. |

### Sasl
<a name="clusters-clusterarn-security-model-sasl"></a>

Details for client authentication using SASL. To turn on SASL, you must also turn on `EncryptionInTransit` by setting `inCluster` to true. You must set `clientBroker` to either `TLS` or `TLS_PLAINTEXT`. If you choose `TLS_PLAINTEXT`, then you must also set `unauthenticated` to true.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| iam | [IAM](#clusters-clusterarn-security-model-iam) | False | Details for ClientAuthentication using IAM. |
| scram | [Scram](#clusters-clusterarn-security-model-scram) | False | Details for SASL/SCRAM client authentication. |

### Scram
<a name="clusters-clusterarn-security-model-scram"></a>

Details for SASL/SCRAM client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | SASL/SCRAM authentication is enabled or not. |

### Tls
<a name="clusters-clusterarn-security-model-tls"></a>

Details for client authentication using TLS.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| certificateAuthorityArnList | Array of type string | False | List of AWS Private CA Amazon Resource Name (ARN)s. |
| enabled | boolean | False | TLS authentication is enabled or not. |

### Unauthenticated
<a name="clusters-clusterarn-security-model-unauthenticated"></a>

Details for allowing no client authentication.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| enabled | boolean | False | Unauthenticated is enabled or not. |

### UpdateSecurityRequest
<a name="clusters-clusterarn-security-model-updatesecurityrequest"></a>

Request body for UpdateSecurity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clientAuthentication | [ClientAuthentication](#clusters-clusterarn-security-model-clientauthentication) | False | The client authentication info details. |
| currentVersion | string | True | Current cluster version. |
| encryptionInfo | [EncryptionInfo](#clusters-clusterarn-security-model-encryptioninfo) | False | The encryption info details. |

### UpdateSecurityResponse
<a name="clusters-clusterarn-security-model-updatesecurityresponse"></a>

Response body for UpdateSecurity.

| Property | Type | Required | Description |
| --- |--- |--- |--- |
| clusterArn | string | False | The Amazon Resource Name (ARN) of the cluster. |
| clusterOperationArn | string | False | The Amazon Resource Name (ARN) of the cluster operation. |

## See also
<a name="clusters-clusterarn-security-see-also"></a>

For more information about using this API in one of the language-specific AWS SDKs and references, see the following:

### UpdateSecurity
<a name="UpdateSecurity-see-also"></a>
+ [AWS Command Line Interface V2](/goto/cli2/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for .NET V4](/goto/DotNetSDKV4/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for C\+\+](/goto/SdkForCpp/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for Go v2](/goto/SdkForGoV2/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for Java V2](/goto/SdkForJavaV2/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for JavaScript V3](/goto/SdkForJavaScriptV3/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for Kotlin](/goto/SdkForKotlin/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for PHP V3](/goto/SdkForPHPV3/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for Python](/goto/boto3/kafka-2018-11-14/UpdateSecurity)
+ [AWS SDK for Ruby V3](/goto/SdkForRubyV3/kafka-2018-11-14/UpdateSecurity)

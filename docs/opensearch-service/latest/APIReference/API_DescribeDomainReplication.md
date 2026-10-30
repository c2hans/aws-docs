---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_DescribeDomainReplication.html
---

# DescribeDomainReplication
<a name="API_DescribeDomainReplication"></a>

Describes the replication arrangement that a domain participates in, including the domain's role and the state of its relationship with each peer.

A domain that is not replicating is returned with an empty `Peers` list and no `Role`. Returns `ResourceNotFoundException` if the domain does not exist.

## Request Syntax
<a name="API_DescribeDomainReplication_RequestSyntax"></a>

```
GET /2021-01-01/opensearch/domain/{{DomainName}}/replication HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeDomainReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_DescribeDomainReplication_RequestSyntax) **   <a name="opensearchservice-DescribeDomainReplication-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_DescribeDomainReplication_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeDomainReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainArn": "string",
   "Peers": [
      {
         "PeerDomainArn": "string",
         "PeerRole": "string",
         "Status": "string",
         "StatusMessage": "string"
      }
   ],
   "Role": "string"
}
```

## Response Elements
<a name="API_DescribeDomainReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainArn](#API_DescribeDomainReplication_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainReplication-response-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain described.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`

 ** [Peers](#API_DescribeDomainReplication_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainReplication-response-Peers"></a>
The domains that this domain replicates with. Each entry carries the state of that one relationship. Empty when the domain is not replicating.
Type: Array of [ReplicationPeer](API_ReplicationPeer.md) objects

 ** [Role](#API_DescribeDomainReplication_ResponseSyntax) **   <a name="opensearchservice-DescribeDomainReplication-response-Role"></a>
The domain's role in the arrangement, either `PRIMARY` or `SECONDARY`. Absent when the domain is not replicating.
Type: String
Valid Values: `PRIMARY | SECONDARY`

## Errors
<a name="API_DescribeDomainReplication_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_DescribeDomainReplication_Examples"></a>

### Example
<a name="API_DescribeDomainReplication_Example_1"></a>

This example illustrates one usage of DescribeDomainReplication.

#### Sample Request
<a name="API_DescribeDomainReplication_Example_1_Request"></a>

```
GET /2021-01-01/opensearch/domain/my-primary/replication HTTP/1.1
Host: es.us-east-1.amazonaws.com
```

#### Sample Response
<a name="API_DescribeDomainReplication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "DomainArn": "arn:aws:es:us-east-1:123456789012:domain/my-primary",
  "Role": "PRIMARY",
  "Peers": [
    {
      "PeerDomainArn": "arn:aws:es:us-west-2:123456789012:domain/my-secondary",
      "PeerRole": "SECONDARY",
      "Status": "ACTIVE"
    }
  ]
}
```

## See Also
<a name="API_DescribeDomainReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/DescribeDomainReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/DescribeDomainReplication)

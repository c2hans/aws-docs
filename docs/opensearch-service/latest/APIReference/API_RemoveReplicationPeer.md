---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_RemoveReplicationPeer.html
---

# RemoveReplicationPeer
<a name="API_RemoveReplicationPeer"></a>

Stops replicating a domain to its peer. Replication ends for both domains, and each domain keeps the data it holds at that point. Neither domain is deleted.

## Request Syntax
<a name="API_RemoveReplicationPeer_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/replication/removePeer HTTP/1.1
Content-type: application/json

{
   "PeerDomainArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_RemoveReplicationPeer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_RemoveReplicationPeer_RequestSyntax) **   <a name="opensearchservice-RemoveReplicationPeer-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_RemoveReplicationPeer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PeerDomainArn](#API_RemoveReplicationPeer_RequestSyntax) **   <a name="opensearchservice-RemoveReplicationPeer-request-PeerDomainArn"></a>
The Amazon Resource Name (ARN) of the peer to stop replicating with. Both domains are named so that the request identifies exactly one replication relationship.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_RemoveReplicationPeer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_RemoveReplicationPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainArn](#API_RemoveReplicationPeer_ResponseSyntax) **   <a name="opensearchservice-RemoveReplicationPeer-response-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain that is no longer replicating.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`

 ** [Status](#API_RemoveReplicationPeer_ResponseSyntax) **   <a name="opensearchservice-RemoveReplicationPeer-response-Status"></a>
The state of the replication relationship. This is `PENDING_REMOVAL` while replication is being stopped.
Type: String
Valid Values: `PENDING_SETUP | ACTIVE | SWITCHING_OVER | FAILING_OVER | PENDING_REMOVAL | DETACHED | EJECTED | FAILED`

## Errors
<a name="API_RemoveReplicationPeer_Errors"></a>

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
<a name="API_RemoveReplicationPeer_Examples"></a>

### Example
<a name="API_RemoveReplicationPeer_Example_1"></a>

This example illustrates one usage of RemoveReplicationPeer.

#### Sample Request
<a name="API_RemoveReplicationPeer_Example_1_Request"></a>

```
POST /2021-01-01/opensearch/domain/my-primary/replication/removePeer HTTP/1.1
Host: es.us-east-1.amazonaws.com
Content-Type: application/json
Content-Length: 74

{"PeerDomainArn": "arn:aws:es:us-west-2:123456789012:domain/my-secondary"}
```

#### Sample Response
<a name="API_RemoveReplicationPeer_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "DomainArn": "arn:aws:es:us-east-1:123456789012:domain/my-primary",
  "Status": "PENDING_REMOVAL"
}
```

## See Also
<a name="API_RemoveReplicationPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/RemoveReplicationPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/RemoveReplicationPeer)

---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_AddReplicationPeer.html
---

# AddReplicationPeer
<a name="API_AddReplicationPeer"></a>

Starts replicating a domain to a peer domain in another AWS Region. A domain can have one peer. The domain you call becomes the primary and the peer becomes the secondary, which receives a copy of the primary's indexes and serves read requests.

Replication is established asynchronously. Use the `DescribeDomainReplication` operation to check whether the relationship has reached the `ACTIVE` state.

## Request Syntax
<a name="API_AddReplicationPeer_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/replication/addPeer HTTP/1.1
Content-type: application/json

{
   "DryRun": {{boolean}},
   "PeerDomainArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_AddReplicationPeer_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_AddReplicationPeer_RequestSyntax) **   <a name="opensearchservice-AddReplicationPeer-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_AddReplicationPeer_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [DryRun](#API_AddReplicationPeer_RequestSyntax) **   <a name="opensearchservice-AddReplicationPeer-request-DryRun"></a>
When `true`, validates the request and reports whether replication could be established, without changing either domain.
Type: Boolean
Required: No

 ** [PeerDomainArn](#API_AddReplicationPeer_RequestSyntax) **   <a name="opensearchservice-AddReplicationPeer-request-PeerDomainArn"></a>
The Amazon Resource Name (ARN) of the domain to replicate to. The peer must be in a different Region from the domain you are calling, and in the same AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_AddReplicationPeer_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_AddReplicationPeer_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainArn](#API_AddReplicationPeer_ResponseSyntax) **   <a name="opensearchservice-AddReplicationPeer-response-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain that is now replicating to the peer.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`

 ** [Status](#API_AddReplicationPeer_ResponseSyntax) **   <a name="opensearchservice-AddReplicationPeer-response-Status"></a>
The state of the replication relationship. This is `PENDING_SETUP` immediately after the request is accepted.
Type: String
Valid Values: `PENDING_SETUP | ACTIVE | SWITCHING_OVER | FAILING_OVER | PENDING_REMOVAL | DETACHED | EJECTED | FAILED`

## Errors
<a name="API_AddReplicationPeer_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DisabledOperationException **
An error occured because the client wanted to access an unsupported operation.
HTTP Status Code: 409

 ** InternalException **
Request processing failed because of an unknown error, exception, or internal failure.
HTTP Status Code: 500

 ** ResourceAlreadyExistsException **
An exception for creating a resource that already exists.
HTTP Status Code: 409

 ** ResourceNotFoundException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 409

 ** ValidationException **
An exception for accessing or deleting a resource that doesn't exist.
HTTP Status Code: 400

## Examples
<a name="API_AddReplicationPeer_Examples"></a>

### Example
<a name="API_AddReplicationPeer_Example_1"></a>

This example illustrates one usage of AddReplicationPeer.

#### Sample Request
<a name="API_AddReplicationPeer_Example_1_Request"></a>

```
POST /2021-01-01/opensearch/domain/my-primary/replication/addPeer HTTP/1.1
Host: es.us-east-1.amazonaws.com
Content-Type: application/json
Content-Length: 74

{"PeerDomainArn": "arn:aws:es:us-west-2:123456789012:domain/my-secondary"}
```

#### Sample Response
<a name="API_AddReplicationPeer_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "DomainArn": "arn:aws:es:us-east-1:123456789012:domain/my-primary",
  "Status": "PENDING_SETUP"
}
```

## See Also
<a name="API_AddReplicationPeer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/AddReplicationPeer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/AddReplicationPeer)

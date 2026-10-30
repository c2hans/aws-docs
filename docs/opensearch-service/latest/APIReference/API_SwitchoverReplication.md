---
source_url: https://docs.aws.amazon.com/opensearch-service/latest/APIReference/API_SwitchoverReplication.html
---

# SwitchoverReplication
<a name="API_SwitchoverReplication"></a>

Promotes a secondary domain to primary, coordinating with the current primary so that no writes are lost. Use this operation for planned role changes, such as testing your recovery procedure or moving write traffic to another Region.

Call this operation in the Region of the domain you want to promote. If the current primary is unreachable, use the `FailoverReplication` operation instead.

## Request Syntax
<a name="API_SwitchoverReplication_RequestSyntax"></a>

```
POST /2021-01-01/opensearch/domain/{{DomainName}}/replication/switchover HTTP/1.1
Content-type: application/json

{
   "PeerDomainArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_SwitchoverReplication_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_SwitchoverReplication_RequestSyntax) **   <a name="opensearchservice-SwitchoverReplication-request-uri-DomainName"></a>
The name of an OpenSearch Service domain. Domain names are unique across the domains owned by an account within an AWS Region.
Length Constraints: Minimum length of 3. Maximum length of 28.
Pattern: `[a-z][a-z0-9\-]+`
Required: Yes

## Request Body
<a name="API_SwitchoverReplication_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [PeerDomainArn](#API_SwitchoverReplication_RequestSyntax) **   <a name="opensearchservice-SwitchoverReplication-request-PeerDomainArn"></a>
The Amazon Resource Name (ARN) of the relationship's current primary. The request is rejected if this domain is no longer the peer of the domain you are calling.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`
Required: Yes

## Response Syntax
<a name="API_SwitchoverReplication_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_SwitchoverReplication_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainArn](#API_SwitchoverReplication_ResponseSyntax) **   <a name="opensearchservice-SwitchoverReplication-response-DomainArn"></a>
The Amazon Resource Name (ARN) of the domain being promoted.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `arn:aws[a-z\-]*:[a-z]+:[a-z0-9\-]+:[0-9]+:domain\/[a-z0-9\-]+`

 ** [Status](#API_SwitchoverReplication_ResponseSyntax) **   <a name="opensearchservice-SwitchoverReplication-response-Status"></a>
The state of the replication relationship. This is `SWITCHING_OVER` while the promotion is in progress.
Type: String
Valid Values: `PENDING_SETUP | ACTIVE | SWITCHING_OVER | FAILING_OVER | PENDING_REMOVAL | DETACHED | EJECTED | FAILED`

## Errors
<a name="API_SwitchoverReplication_Errors"></a>

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
<a name="API_SwitchoverReplication_Examples"></a>

### Example
<a name="API_SwitchoverReplication_Example_1"></a>

This example illustrates one usage of SwitchoverReplication.

#### Sample Request
<a name="API_SwitchoverReplication_Example_1_Request"></a>

```
POST /2021-01-01/opensearch/domain/my-secondary/replication/switchover HTTP/1.1
Host: es.us-west-2.amazonaws.com
Content-Type: application/json
Content-Length: 72

{"PeerDomainArn": "arn:aws:es:us-east-1:123456789012:domain/my-primary"}
```

#### Sample Response
<a name="API_SwitchoverReplication_Example_1_Response"></a>

```
HTTP/1.1 200 OK
Content-Type: application/json

{
  "DomainArn": "arn:aws:es:us-west-2:123456789012:domain/my-secondary",
  "Status": "SWITCHING_OVER"
}
```

## See Also
<a name="API_SwitchoverReplication_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/opensearch-2021-01-01/SwitchoverReplication)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/opensearch-2021-01-01/SwitchoverReplication)

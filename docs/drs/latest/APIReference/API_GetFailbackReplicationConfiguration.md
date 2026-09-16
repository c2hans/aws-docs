---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_GetFailbackReplicationConfiguration.html
---

# GetFailbackReplicationConfiguration
<a name="API_GetFailbackReplicationConfiguration"></a>

Lists all Failback ReplicationConfigurations, filtered by Recovery Instance ID.

## Request Syntax
<a name="API_GetFailbackReplicationConfiguration_RequestSyntax"></a>

```
POST /GetFailbackReplicationConfiguration HTTP/1.1
Content-type: application/json

{
   "recoveryInstanceID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_GetFailbackReplicationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_GetFailbackReplicationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [recoveryInstanceID](#API_GetFailbackReplicationConfiguration_RequestSyntax) **   <a name="drs-GetFailbackReplicationConfiguration-request-recoveryInstanceID"></a>
The ID of the Recovery Instance whose failback replication configuration should be returned.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: Yes

## Response Syntax
<a name="API_GetFailbackReplicationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "bandwidthThrottling": number,
   "internetProtocol": "string",
   "name": "string",
   "recoveryInstanceID": "string",
   "usePrivateIP": boolean
}
```

## Response Elements
<a name="API_GetFailbackReplicationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [bandwidthThrottling](#API_GetFailbackReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetFailbackReplicationConfiguration-response-bandwidthThrottling"></a>
Configure bandwidth throttling for the outbound data transfer rate of the Recovery Instance in Mbps.
Type: Long
Valid Range: Minimum value of 0.

 ** [internetProtocol](#API_GetFailbackReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetFailbackReplicationConfiguration-response-internetProtocol"></a>
Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)
Type: String
Valid Values: `IPV4 | IPV6`

 ** [name](#API_GetFailbackReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetFailbackReplicationConfiguration-response-name"></a>
The name of the Failback Replication Configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [recoveryInstanceID](#API_GetFailbackReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetFailbackReplicationConfiguration-response-recoveryInstanceID"></a>
The ID of the Recovery Instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`

 ** [usePrivateIP](#API_GetFailbackReplicationConfiguration_ResponseSyntax) **   <a name="drs-GetFailbackReplicationConfiguration-response-usePrivateIP"></a>
Whether to use Private IP for the failback replication of the Recovery Instance.
Type: Boolean

## Errors
<a name="API_GetFailbackReplicationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The resource for this operation was not found.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
Quota code.
 ** retryAfterSeconds **
The number of seconds after which the request should be safe to retry.
 ** serviceCode **
Service code.
HTTP Status Code: 429

 ** UninitializedAccountException **
The account performing the request has not been initialized.
HTTP Status Code: 400

## See Also
<a name="API_GetFailbackReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/GetFailbackReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/GetFailbackReplicationConfiguration)

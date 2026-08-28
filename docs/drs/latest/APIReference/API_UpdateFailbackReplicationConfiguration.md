---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_UpdateFailbackReplicationConfiguration.html
---

# UpdateFailbackReplicationConfiguration
<a name="API_UpdateFailbackReplicationConfiguration"></a>

Allows you to update the failback replication configuration of a Recovery Instance by ID.

## Request Syntax
<a name="API_UpdateFailbackReplicationConfiguration_RequestSyntax"></a>

```
POST /UpdateFailbackReplicationConfiguration HTTP/1.1
Content-type: application/json

{
   "bandwidthThrottling": {{number}},
   "internetProtocol": "{{string}}",
   "name": "{{string}}",
   "recoveryInstanceID": "{{string}}",
   "usePrivateIP": {{boolean}}
}
```

## URI Request Parameters
<a name="API_UpdateFailbackReplicationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateFailbackReplicationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [bandwidthThrottling](#API_UpdateFailbackReplicationConfiguration_RequestSyntax) **   <a name="drs-UpdateFailbackReplicationConfiguration-request-bandwidthThrottling"></a>
Configure bandwidth throttling for the outbound data transfer rate of the Recovery Instance in Mbps.
Type: Long
Valid Range: Minimum value of 0.
Required: No

 ** [internetProtocol](#API_UpdateFailbackReplicationConfiguration_RequestSyntax) **   <a name="drs-UpdateFailbackReplicationConfiguration-request-internetProtocol"></a>
Which version of the Internet Protocol to use for replication of data. (IPv4 or IPv6)
Type: String
Valid Values: `IPV4 | IPV6`
Required: No

 ** [name](#API_UpdateFailbackReplicationConfiguration_RequestSyntax) **   <a name="drs-UpdateFailbackReplicationConfiguration-request-name"></a>
The name of the Failback Replication Configuration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** [recoveryInstanceID](#API_UpdateFailbackReplicationConfiguration_RequestSyntax) **   <a name="drs-UpdateFailbackReplicationConfiguration-request-recoveryInstanceID"></a>
The ID of the Recovery Instance.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 19.
Pattern: `i-[0-9a-fA-F]{8,}`
Required: Yes

 ** [usePrivateIP](#API_UpdateFailbackReplicationConfiguration_RequestSyntax) **   <a name="drs-UpdateFailbackReplicationConfiguration-request-usePrivateIP"></a>
Whether to use Private IP for the failback replication of the Recovery Instance.
Type: Boolean
Required: No

## Response Syntax
<a name="API_UpdateFailbackReplicationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateFailbackReplicationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateFailbackReplicationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

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
<a name="API_UpdateFailbackReplicationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/UpdateFailbackReplicationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/UpdateFailbackReplicationConfiguration)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Elastic Disaster Recovery. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query drs` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

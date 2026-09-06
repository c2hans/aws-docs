---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_DeleteReplicationConfigurationTemplate.html
---

# DeleteReplicationConfigurationTemplate
<a name="API_DeleteReplicationConfigurationTemplate"></a>

Deletes a single Replication Configuration Template by ID

## Request Syntax
<a name="API_DeleteReplicationConfigurationTemplate_RequestSyntax"></a>

```
POST /DeleteReplicationConfigurationTemplate HTTP/1.1
Content-type: application/json

{
   "replicationConfigurationTemplateID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteReplicationConfigurationTemplate_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteReplicationConfigurationTemplate_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [replicationConfigurationTemplateID](#API_DeleteReplicationConfigurationTemplate_RequestSyntax) **   <a name="drs-DeleteReplicationConfigurationTemplate-request-replicationConfigurationTemplateID"></a>
The ID of the Replication Configuration Template to be deleted.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `rct-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DeleteReplicationConfigurationTemplate_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteReplicationConfigurationTemplate_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteReplicationConfigurationTemplate_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** ConflictException **
The request could not be completed due to a conflict with the current state of the target resource.
 ** resourceId **
The ID of the resource.
 ** resourceType **
The type of the resource.
HTTP Status Code: 409

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
<a name="API_DeleteReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/drs-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/DeleteReplicationConfigurationTemplate)

---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteReplicationConfigurationTemplate.html
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

 ** [replicationConfigurationTemplateID](#API_DeleteReplicationConfigurationTemplate_RequestSyntax) **   <a name="mgn-DeleteReplicationConfigurationTemplate-request-replicationConfigurationTemplateID"></a>
Request to delete Replication Configuration Template from service by Replication Configuration Template ID.
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
 ** errors **
Conflict Exception specific errors.
 ** resourceId **
A conflict occurred when prompting for the Resource ID.
 ** resourceType **
A conflict occurred when prompting for resource type.
HTTP Status Code: 409

 ** ResourceNotFoundException **
Resource not found exception.
 ** resourceId **
Resource ID not found error.
 ** resourceType **
Resource type not found error.
HTTP Status Code: 404

 ** UninitializedAccountException **
Uninitialized account exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteReplicationConfigurationTemplate_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DeleteReplicationConfigurationTemplate)

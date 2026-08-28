---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_DeleteNetworkMigrationDefinition.html
---

# DeleteNetworkMigrationDefinition
<a name="API_DeleteNetworkMigrationDefinition"></a>

Deletes a network migration definition. This operation removes the migration definition and all associated metadata.

## Request Syntax
<a name="API_DeleteNetworkMigrationDefinition_RequestSyntax"></a>

```
POST /network-migration/DeleteNetworkMigrationDefinition HTTP/1.1
Content-type: application/json

{
   "networkMigrationDefinitionID": "{{string}}"
}
```

## URI Request Parameters
<a name="API_DeleteNetworkMigrationDefinition_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DeleteNetworkMigrationDefinition_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [networkMigrationDefinitionID](#API_DeleteNetworkMigrationDefinition_RequestSyntax) **   <a name="mgn-DeleteNetworkMigrationDefinition-request-networkMigrationDefinitionID"></a>
The unique identifier of the network migration definition to delete.
Type: String
Length Constraints: Fixed length of 21.
Pattern: `nmd-[0-9a-zA-Z]{17}`
Required: Yes

## Response Syntax
<a name="API_DeleteNetworkMigrationDefinition_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteNetworkMigrationDefinition_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteNetworkMigrationDefinition_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Operation denied due to a file permission or access check error.
HTTP Status Code: 403

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

## See Also
<a name="API_DeleteNetworkMigrationDefinition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/mgn-2020-02-26/DeleteNetworkMigrationDefinition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/DeleteNetworkMigrationDefinition)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for ApplicationMigrationService. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query mgn` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

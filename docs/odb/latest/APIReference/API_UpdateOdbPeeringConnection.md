---
source_url: https://docs.aws.amazon.com/odb/latest/APIReference/API_UpdateOdbPeeringConnection.html
---

# UpdateOdbPeeringConnection
<a name="API_UpdateOdbPeeringConnection"></a>

Modifies the settings of an Oracle Database@AWS peering connection. You can update the display name and add or remove CIDR blocks from the peering connection.

## Request Syntax
<a name="API_UpdateOdbPeeringConnection_RequestSyntax"></a>

```
{
   "displayName": "{{string}}",
   "odbPeeringConnectionId": "{{string}}",
   "peerNetworkCidrsToBeAdded": [ "{{string}}" ],
   "peerNetworkCidrsToBeRemoved": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_UpdateOdbPeeringConnection_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [displayName](#API_UpdateOdbPeeringConnection_RequestSyntax) **   <a name="odb-UpdateOdbPeeringConnection-request-displayName"></a>
A new display name for the peering connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[a-zA-Z_](?!.*--)[a-zA-Z0-9_-]*`
Required: No

 ** [odbPeeringConnectionId](#API_UpdateOdbPeeringConnection_RequestSyntax) **   <a name="odb-UpdateOdbPeeringConnection-request-odbPeeringConnectionId"></a>
The identifier of the Oracle Database@AWS peering connection to update.
Type: String
Length Constraints: Minimum length of 6. Maximum length of 2048.
Pattern: `(arn:(?:aws|aws-cn|aws-us-gov|aws-iso-{0,1}[a-z]{0,1}):[a-z0-9-]+:[a-z0-9-]*:[0-9]+:[a-z0-9-]+/[a-zA-Z0-9_~.-]{6,64}|[a-zA-Z0-9_~.-]{6,64})`
Required: Yes

 ** [peerNetworkCidrsToBeAdded](#API_UpdateOdbPeeringConnection_RequestSyntax) **   <a name="odb-UpdateOdbPeeringConnection-request-peerNetworkCidrsToBeAdded"></a>
A list of CIDR blocks to add to the peering connection. These CIDR blocks define the IP address ranges that can communicate through the peering connection. The CIDR blocks must not overlap with existing CIDR blocks in the Oracle Database@AWS network.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `(?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)\/(?:[1-2][0-9]|3[0-2]|[1-9])`
Required: No

 ** [peerNetworkCidrsToBeRemoved](#API_UpdateOdbPeeringConnection_RequestSyntax) **   <a name="odb-UpdateOdbPeeringConnection-request-peerNetworkCidrsToBeRemoved"></a>
A list of CIDR blocks to remove from the peering connection. The CIDR blocks must currently exist in the peering connection.
Type: Array of strings
Length Constraints: Minimum length of 1. Maximum length of 18.
Pattern: `(?:(?:\d|[01]?\d\d|2[0-4]\d|25[0-5])\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d|\d)\/(?:[1-2][0-9]|3[0-2]|[1-9])`
Required: No

## Response Syntax
<a name="API_UpdateOdbPeeringConnection_ResponseSyntax"></a>

```
{
   "displayName": "string",
   "odbPeeringConnectionId": "string",
   "status": "string",
   "statusReason": "string"
}
```

## Response Elements
<a name="API_UpdateOdbPeeringConnection_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [displayName](#API_UpdateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-UpdateOdbPeeringConnection-response-displayName"></a>
The display name of the peering connection.
Type: String

 ** [odbPeeringConnectionId](#API_UpdateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-UpdateOdbPeeringConnection-response-odbPeeringConnectionId"></a>
The identifier of the Oracle Database@AWS peering connection that was updated.
Type: String

 ** [status](#API_UpdateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-UpdateOdbPeeringConnection-response-status"></a>
The status of the peering connection update operation.
Type: String
Valid Values: `AVAILABLE | FAILED | PROVISIONING | TERMINATED | TERMINATING | UPDATING | MAINTENANCE_IN_PROGRESS`

 ** [statusReason](#API_UpdateOdbPeeringConnection_ResponseSyntax) **   <a name="odb-UpdateOdbPeeringConnection-response-statusReason"></a>
Additional information about the status of the peering connection update operation.
Type: String

## Errors
<a name="API_UpdateOdbPeeringConnection_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have sufficient access to perform this action. Make sure you have the required permissions and try again.
HTTP Status Code: 400

 ** ConflictException **
Occurs when a conflict with the current status of your resource. Fix any inconsistencies with your resource and try again.
 ** resourceId **
The identifier of the resource that caused the conflict.
 ** resourceType **
The type of resource that caused the conflict.
HTTP Status Code: 400

 ** InternalServerException **
Occurs when there is an internal failure in the Oracle Database@AWS service. Wait and try again.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after an internal server error.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The operation tried to access a resource that doesn't exist. Make sure you provided the correct resource and try again.
 ** resourceId **
The identifier of the resource that was not found.
 ** resourceType **
The type of resource that was not found.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request after being throttled.
HTTP Status Code: 400

 ** ValidationException **
The request has failed validation because it is missing required fields or has invalid inputs.
 ** fieldList **
A list of fields that failed validation.
 ** reason **
The reason why the validation failed.
HTTP Status Code: 400

## See Also
<a name="API_UpdateOdbPeeringConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/odb-2024-08-20/UpdateOdbPeeringConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/odb-2024-08-20/UpdateOdbPeeringConnection)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Oracle Database@AWS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query odb` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

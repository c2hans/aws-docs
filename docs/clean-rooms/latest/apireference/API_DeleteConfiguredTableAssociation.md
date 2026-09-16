---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_DeleteConfiguredTableAssociation.html
---

# DeleteConfiguredTableAssociation
<a name="API_DeleteConfiguredTableAssociation"></a>

Deletes a configured table association.

## Request Syntax
<a name="API_DeleteConfiguredTableAssociation_RequestSyntax"></a>

```
DELETE /memberships/{{membershipIdentifier}}/configuredTableAssociations/{{configuredTableAssociationIdentifier}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DeleteConfiguredTableAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredTableAssociationIdentifier](#API_DeleteConfiguredTableAssociation_RequestSyntax) **   <a name="API-DeleteConfiguredTableAssociation-request-uri-configuredTableAssociationIdentifier"></a>
The unique ID for the configured table association to be deleted. Currently accepts the configured table ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_DeleteConfiguredTableAssociation_RequestSyntax) **   <a name="API-DeleteConfiguredTableAssociation-request-uri-membershipIdentifier"></a>
A unique identifier for the membership that the configured table association belongs to. Currently accepts the membership ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_DeleteConfiguredTableAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DeleteConfiguredTableAssociation_ResponseSyntax"></a>

```
HTTP/1.1 204
```

## Response Elements
<a name="API_DeleteConfiguredTableAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors
<a name="API_DeleteConfiguredTableAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** ConflictException **
Updating or deleting a resource can cause an inconsistent state.
 ** reason **
A reason code for the exception.
 ** resourceId **
The ID of the conflicting resource.
 ** resourceType **
The type of the conflicting resource.
HTTP Status Code: 409

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
Request references a resource which does not exist.
 ** resourceId **
The Id of the missing resource.
 ** resourceType **
The type of the missing resource.
HTTP Status Code: 404

 ** ThrottlingException **
Request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The input fails to satisfy the specified constraints.
 ** fieldList **
Validation errors for specific input parameters.
 ** reason **
A reason code for the exception.
HTTP Status Code: 400

## See Also
<a name="API_DeleteConfiguredTableAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/DeleteConfiguredTableAssociation)

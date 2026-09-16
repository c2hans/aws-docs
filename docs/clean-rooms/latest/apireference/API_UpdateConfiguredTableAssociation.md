---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateConfiguredTableAssociation.html
---

# UpdateConfiguredTableAssociation
<a name="API_UpdateConfiguredTableAssociation"></a>

Updates a configured table association.

## Request Syntax
<a name="API_UpdateConfiguredTableAssociation_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/configuredTableAssociations/{{configuredTableAssociationIdentifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "roleArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateConfiguredTableAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredTableAssociationIdentifier](#API_UpdateConfiguredTableAssociation_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociation-request-uri-configuredTableAssociationIdentifier"></a>
The unique identifier for the configured table association to update. Currently accepts the configured table association ID.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_UpdateConfiguredTableAssociation_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociation-request-uri-membershipIdentifier"></a>
The unique ID for the membership that the configured table association belongs to.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateConfiguredTableAssociation_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateConfiguredTableAssociation_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociation-request-description"></a>
A new description for the configured table association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [roleArn](#API_UpdateConfiguredTableAssociation_RequestSyntax) **   <a name="API-UpdateConfiguredTableAssociation-request-roleArn"></a>
The service will assume this role to access catalog metadata and query the table.
Type: String
Length Constraints: Minimum length of 32. Maximum length of 512.
Pattern: `arn:aws:iam::[\w]+:role/[\w+=./@-]+`
Required: No

## Response Syntax
<a name="API_UpdateConfiguredTableAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "configuredTableAssociation": {
      "analysisRuleTypes": [ "string" ],
      "arn": "string",
      "childResources": [
         {
            "ownerAccountId": "string",
            "resourceId": "string",
            "resourceName": "string",
            "resourceStatus": "string",
            "resourceType": "string"
         }
      ],
      "configuredTableArn": "string",
      "configuredTableId": "string",
      "createTime": number,
      "description": "string",
      "id": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "name": "string",
      "roleArn": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_UpdateConfiguredTableAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [configuredTableAssociation](#API_UpdateConfiguredTableAssociation_ResponseSyntax) **   <a name="API-UpdateConfiguredTableAssociation-response-configuredTableAssociation"></a>
The entire updated configured table association.
Type: [ConfiguredTableAssociation](API_ConfiguredTableAssociation.md) object

## Errors
<a name="API_UpdateConfiguredTableAssociation_Errors"></a>

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
<a name="API_UpdateConfiguredTableAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateConfiguredTableAssociation)

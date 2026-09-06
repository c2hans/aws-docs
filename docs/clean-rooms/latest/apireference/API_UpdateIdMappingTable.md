---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateIdMappingTable.html
---

# UpdateIdMappingTable
<a name="API_UpdateIdMappingTable"></a>

Provides the details that are necessary to update an ID mapping table.

## Request Syntax
<a name="API_UpdateIdMappingTable_RequestSyntax"></a>

```
PATCH /memberships/{{membershipIdentifier}}/idmappingtables/{{idMappingTableIdentifier}} HTTP/1.1
Content-type: application/json

{
   "description": "{{string}}",
   "kmsKeyArn": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateIdMappingTable_RequestParameters"></a>

The request uses the following URI parameters.

 ** [idMappingTableIdentifier](#API_UpdateIdMappingTable_RequestSyntax) **   <a name="API-UpdateIdMappingTable-request-uri-idMappingTableIdentifier"></a>
The unique identifier of the ID mapping table that you want to update.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [membershipIdentifier](#API_UpdateIdMappingTable_RequestSyntax) **   <a name="API-UpdateIdMappingTable-request-uri-membershipIdentifier"></a>
The unique identifier of the membership that contains the ID mapping table that you want to update.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateIdMappingTable_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [description](#API_UpdateIdMappingTable_RequestSyntax) **   <a name="API-UpdateIdMappingTable-request-description"></a>
A new description for the ID mapping table.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [kmsKeyArn](#API_UpdateIdMappingTable_RequestSyntax) **   <a name="API-UpdateIdMappingTable-request-kmsKeyArn"></a>
The Amazon Resource Name (ARN) of the AWS KMS key.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[\w]{2}-[\w]{4,9}-[\d]:[\d]{12}:key/[a-zA-Z0-9-]+`
Required: No

## Response Syntax
<a name="API_UpdateIdMappingTable_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "idMappingTable": {
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
      "collaborationArn": "string",
      "collaborationId": "string",
      "createTime": number,
      "description": "string",
      "id": "string",
      "inputReferenceConfig": {
         "inputReferenceArn": "string",
         "manageResourcePolicies": boolean
      },
      "inputReferenceProperties": {
         "idMappingTableInputSource": [
            {
               "idNamespaceAssociationId": "string",
               "type": "string"
            }
         ]
      },
      "kmsKeyArn": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "name": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_UpdateIdMappingTable_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [idMappingTable](#API_UpdateIdMappingTable_ResponseSyntax) **   <a name="API-UpdateIdMappingTable-response-idMappingTable"></a>
The updated ID mapping table.
Type: [IdMappingTable](API_IdMappingTable.md) object

## Errors
<a name="API_UpdateIdMappingTable_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

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
<a name="API_UpdateIdMappingTable_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateIdMappingTable)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateIdMappingTable)

---
source_url: https://docs.aws.amazon.com/clean-rooms/latest/apireference/API_UpdateCollaboration.html
---

# UpdateCollaboration
<a name="API_UpdateCollaboration"></a>

Updates collaboration metadata and can only be called by the collaboration owner.

## Request Syntax
<a name="API_UpdateCollaboration_RequestSyntax"></a>

```
PATCH /collaborations/{{collaborationIdentifier}} HTTP/1.1
Content-type: application/json

{
   "analyticsEngine": "{{string}}",
   "description": "{{string}}",
   "name": "{{string}}"
}
```

## URI Request Parameters
<a name="API_UpdateCollaboration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_UpdateCollaboration_RequestSyntax) **   <a name="API-UpdateCollaboration-request-uri-collaborationIdentifier"></a>
The identifier for the collaboration.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_UpdateCollaboration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [analyticsEngine](#API_UpdateCollaboration_RequestSyntax) **   <a name="API-UpdateCollaboration-request-analyticsEngine"></a>
The analytics engine.
After July 16, 2025, the `CLEAN_ROOMS_SQL` parameter will no longer be available.
Type: String
Valid Values: `SPARK | CLEAN_ROOMS_SQL`
Required: No

 ** [description](#API_UpdateCollaboration_RequestSyntax) **   <a name="API-UpdateCollaboration-request-description"></a>
A description of the collaboration.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `(?!\s+$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`
Required: No

 ** [name](#API_UpdateCollaboration_RequestSyntax) **   <a name="API-UpdateCollaboration-request-name"></a>
A human-readable identifier provided by the collaboration owner. Display names are not unique.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`
Required: No

## Response Syntax
<a name="API_UpdateCollaboration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaboration": {
      "allowedResultRegions": [ "string" ],
      "analyticsEngine": "string",
      "arn": "string",
      "autoApprovedChangeTypes": [ "string" ],
      "createTime": number,
      "creatorAccountId": "string",
      "creatorDisplayName": "string",
      "dataEncryptionMetadata": {
         "allowCleartext": boolean,
         "allowDuplicates": boolean,
         "allowJoinsOnColumnsWithDifferentNames": boolean,
         "preserveNulls": boolean
      },
      "description": "string",
      "id": "string",
      "isMetricsEnabled": boolean,
      "jobLogStatus": "string",
      "membershipArn": "string",
      "membershipId": "string",
      "memberStatus": "string",
      "name": "string",
      "queryLogStatus": "string",
      "updateTime": number
   }
}
```

## Response Elements
<a name="API_UpdateCollaboration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaboration](#API_UpdateCollaboration_ResponseSyntax) **   <a name="API-UpdateCollaboration-response-collaboration"></a>
The entire collaboration that has been updated.
Type: [Collaboration](API_Collaboration.md) object

## Errors
<a name="API_UpdateCollaboration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Caller does not have sufficient access to perform this action.
 ** reason **
A reason code for the exception.
HTTP Status Code: 403

 ** InternalServerException **
Unexpected error during processing of request.
HTTP Status Code: 500

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
<a name="API_UpdateCollaboration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanrooms-2022-02-17/UpdateCollaboration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanrooms-2022-02-17/UpdateCollaboration)

---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetCollaborationConfiguredModelAlgorithmAssociation.html
---

# GetCollaborationConfiguredModelAlgorithmAssociation
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation"></a>

Returns information about the configured model algorithm association in a collaboration.

## Request Syntax
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_RequestSyntax"></a>

```
GET /collaborations/{{collaborationIdentifier}}/configured-model-algorithm-associations/{{configuredModelAlgorithmAssociationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [collaborationIdentifier](#API_GetCollaborationConfiguredModelAlgorithmAssociation_RequestSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-request-uri-collaborationIdentifier"></a>
The collaboration ID for the collaboration that contains the configured model algorithm association that you want to return information about.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

 ** [configuredModelAlgorithmAssociationArn](#API_GetCollaborationConfiguredModelAlgorithmAssociation_RequestSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-request-uri-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

## Request Body
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationIdentifier": "string",
   "configuredModelAlgorithmArn": "string",
   "configuredModelAlgorithmAssociationArn": "string",
   "createTime": "string",
   "creatorAccountId": "string",
   "description": "string",
   "membershipIdentifier": "string",
   "name": "string",
   "privacyConfiguration": {
      "policies": {
         "trainedModelExports": {
            "filesToExport": [ "string" ],
            "maxSize": {
               "unit": "string",
               "value": number
            }
         },
         "trainedModelInferenceJobs": {
            "containerLogs": [
               {
                  "allowedAccountIds": [ "string" ],
                  "filterPattern": "string",
                  "logRedactionConfiguration": {
                     "customEntityConfig": {
                        "customDataIdentifiers": [ "string" ]
                     },
                     "entitiesToRedact": [ "string" ]
                  },
                  "logType": "string"
               }
            ],
            "maxOutputSize": {
               "unit": "string",
               "value": number
            }
         },
         "trainedModels": {
            "containerLogs": [
               {
                  "allowedAccountIds": [ "string" ],
                  "filterPattern": "string",
                  "logRedactionConfiguration": {
                     "customEntityConfig": {
                        "customDataIdentifiers": [ "string" ]
                     },
                     "entitiesToRedact": [ "string" ]
                  },
                  "logType": "string"
               }
            ],
            "containerMetrics": {
               "noiseLevel": "string"
            },
            "maxArtifactSize": {
               "unit": "string",
               "value": number
            }
         }
      }
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationIdentifier](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [configuredModelAlgorithmArn](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`

 ** [configuredModelAlgorithmAssociationArn](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-createTime"></a>
The time at which the configured model algorithm association was created.
Type: Timestamp

 ** [creatorAccountId](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-creatorAccountId"></a>
The account ID of the member that created the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `[0-9]{12}`

 ** [description](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-description"></a>
The description of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [membershipIdentifier](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-membershipIdentifier"></a>
The membership ID of the member that created the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [name](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-name"></a>
The name of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [privacyConfiguration](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-privacyConfiguration"></a>
Information about the privacy configuration for a configured model algorithm association.
Type: [PrivacyConfiguration](API_PrivacyConfiguration.md) object

 ** [updateTime](#API_GetCollaborationConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetCollaborationConfiguredModelAlgorithmAssociation-response-updateTime"></a>
The most recent time at which the configured model algorithm association was updated.
Type: Timestamp

## Errors
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ResourceNotFoundException **
The resource you are requesting does not exist.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_GetCollaborationConfiguredModelAlgorithmAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetCollaborationConfiguredModelAlgorithmAssociation)

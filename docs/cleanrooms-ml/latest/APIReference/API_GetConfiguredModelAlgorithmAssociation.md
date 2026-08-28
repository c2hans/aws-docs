---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_GetConfiguredModelAlgorithmAssociation.html
---

# GetConfiguredModelAlgorithmAssociation
<a name="API_GetConfiguredModelAlgorithmAssociation"></a>

Returns information about a configured model algorithm association.

## Request Syntax
<a name="API_GetConfiguredModelAlgorithmAssociation_RequestSyntax"></a>

```
GET /memberships/{{membershipIdentifier}}/configured-model-algorithm-associations/{{configuredModelAlgorithmAssociationArn}} HTTP/1.1
```

## URI Request Parameters
<a name="API_GetConfiguredModelAlgorithmAssociation_RequestParameters"></a>

The request uses the following URI parameters.

 ** [configuredModelAlgorithmAssociationArn](#API_GetConfiguredModelAlgorithmAssociation_RequestSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-request-uri-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association that you want to return information about.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`
Required: Yes

 ** [membershipIdentifier](#API_GetConfiguredModelAlgorithmAssociation_RequestSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-request-uri-membershipIdentifier"></a>
The membership ID of the member that created the configured model algorithm association.
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: Yes

## Request Body
<a name="API_GetConfiguredModelAlgorithmAssociation_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "collaborationIdentifier": "string",
   "configuredModelAlgorithmArn": "string",
   "configuredModelAlgorithmAssociationArn": "string",
   "createTime": "string",
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
   "tags": {
      "string" : "string"
   },
   "updateTime": "string"
}
```

## Response Elements
<a name="API_GetConfiguredModelAlgorithmAssociation_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [collaborationIdentifier](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-collaborationIdentifier"></a>
The collaboration ID of the collaboration that contains the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [configuredModelAlgorithmArn](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-configuredModelAlgorithmArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm that was associated to the collaboration.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:configured-model-algorithm/[-a-zA-Z0-9_/.]+`

 ** [configuredModelAlgorithmAssociationArn](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-configuredModelAlgorithmAssociationArn"></a>
The Amazon Resource Name (ARN) of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:membership/[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}/configured-model-algorithm-association/[-a-zA-Z0-9_/.]+`

 ** [createTime](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-createTime"></a>
The time at which the configured model algorithm association was created.
Type: Timestamp

 ** [description](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-description"></a>
The description of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 255.
Pattern: `[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t\r\n]*`

 ** [membershipIdentifier](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-membershipIdentifier"></a>
The membership ID of the member that created the configured model algorithm association.
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`

 ** [name](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-name"></a>
The name of the configured model algorithm association.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 63.
Pattern: `(?!\s*$)[\u0020-\uD7FF\uE000-\uFFFD\uD800\uDBFF-\uDC00\uDFFF\t]*`

 ** [privacyConfiguration](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-privacyConfiguration"></a>
The privacy configuration information for the configured model algorithm association.
Type: [PrivacyConfiguration](API_PrivacyConfiguration.md) object

 ** [tags](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-tags"></a>
The optional metadata that you applied to the resource to help you categorize and organize them. Each tag consists of a key and an optional value, both of which you define.
The following basic restrictions apply to tags:
+ Maximum number of tags per resource - 50.
+ For each resource, each tag key must be unique, and each tag key can have only one value.
+ Maximum key length - 128 Unicode characters in UTF-8.
+ Maximum value length - 256 Unicode characters in UTF-8.
+ If your tagging schema is used across multiple services and resources, remember that other services may have restrictions on allowed characters. Generally allowed characters are: letters, numbers, and spaces representable in UTF-8, and the following characters: \+ - = . \_ : / @.
+ Tag keys and values are case sensitive.
+ Do not use aws:, AWS:, or any upper or lowercase combination of such as a prefix for keys as it is reserved for AWS use. You cannot edit or delete tag keys with this prefix. Values can have this prefix. If a tag value has aws as its prefix but the key does not, then Clean Rooms ML considers it to be a user tag and will count against the limit of 50 tags. Tags with only the key prefix of aws do not count against your tags per resource limit.
Type: String to string map
Map Entries: Minimum number of 0 items. Maximum number of 200 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Value Length Constraints: Minimum length of 0. Maximum length of 256.

 ** [updateTime](#API_GetConfiguredModelAlgorithmAssociation_ResponseSyntax) **   <a name="API-GetConfiguredModelAlgorithmAssociation-response-updateTime"></a>
The most recent time at which the configured model algorithm association was updated.
Type: Timestamp

## Errors
<a name="API_GetConfiguredModelAlgorithmAssociation_Errors"></a>

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
<a name="API_GetConfiguredModelAlgorithmAssociation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/GetConfiguredModelAlgorithmAssociation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

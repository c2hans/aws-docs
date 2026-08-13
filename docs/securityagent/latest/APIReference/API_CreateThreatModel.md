---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_CreateThreatModel.html
---

# CreateThreatModel
<a name="API_CreateThreatModel"></a>

Creates a new threat model configuration in an agent space. A threat model defines the parameters for automated threat analysis.

## Request Syntax
<a name="API_CreateThreatModel_RequestSyntax"></a>

```
POST /CreateThreatModel HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "assets": {
      "actors": [
         {
            "authentication": {
               "providerType": "{{string}}",
               "value": "{{string}}"
            },
            "description": "{{string}}",
            "enableEmailMfa": {{boolean}},
            "identifier": "{{string}}",
            "mfaForwardingAddress": "{{string}}",
            "uris": [ "{{string}}" ]
         }
      ],
      "documents": [
         {
            "artifactId": "{{string}}",
            "integratedDocument": {
               "integrationId": "{{string}}",
               "resourceId": "{{string}}"
            },
            "s3Location": "{{string}}"
         }
      ],
      "endpoints": [
         {
            "uri": "{{string}}"
         }
      ],
      "integratedRepositories": [
         {
            "branch": "{{string}}",
            "integrationId": "{{string}}",
            "providerResourceId": "{{string}}"
         }
      ],
      "sourceCode": [
         {
            "s3Location": "{{string}}"
         }
      ]
   },
   "description": "{{string}}",
   "logConfig": {
      "logGroup": "{{string}}",
      "logStream": "{{string}}"
   },
   "reportDestination": {
      "containerId": "{{string}}",
      "documentId": "{{string}}",
      "integrationId": "{{string}}",
      "parentId": "{{string}}"
   },
   "scopeDocs": [
      {
         "artifactId": "{{string}}",
         "integratedDocument": {
            "integrationId": "{{string}}",
            "resourceId": "{{string}}"
         },
         "s3Location": "{{string}}"
      }
   ],
   "serviceRole": "{{string}}",
   "title": "{{string}}"
}
```

## URI Request Parameters
<a name="API_CreateThreatModel_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_CreateThreatModel_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-agentSpaceId"></a>
The unique identifier of the agent space to create the threat model in.
Type: String
Required: Yes

 ** [assets](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-assets"></a>
The assets to include in the threat model.
Type: [Assets](API_Assets.md) object
Required: No

 ** [description](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-description"></a>
A description of the application or system being threat modeled.
Type: String
Required: No

 ** [logConfig](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-logConfig"></a>
The CloudWatch Logs configuration for the threat model.
Type: [CloudWatchLog](API_CloudWatchLog.md) object
Required: No

 ** [reportDestination](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-reportDestination"></a>
The destination for publishing scan reports to an integrated document provider.
Type: [ReportDestination](API_ReportDestination.md) object
Required: No

 ** [scopeDocs](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-scopeDocs"></a>
The scoped documents for the agent to focus on during threat modeling.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects
Required: No

 ** [serviceRole](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-serviceRole"></a>
The IAM service role to use for the threat model.
Type: String
Required: Yes

 ** [title](#API_CreateThreatModel_RequestSyntax) **   <a name="securityagent-CreateThreatModel-request-title"></a>
The title of the threat model.
Type: String
Required: Yes

## Response Syntax
<a name="API_CreateThreatModel_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "agentSpaceId": "string",
   "assets": {
      "actors": [
         {
            "authentication": {
               "providerType": "string",
               "value": "string"
            },
            "description": "string",
            "enableEmailMfa": boolean,
            "identifier": "string",
            "mfaForwardingAddress": "string",
            "uris": [ "string" ]
         }
      ],
      "documents": [
         {
            "artifactId": "string",
            "integratedDocument": {
               "integrationId": "string",
               "resourceId": "string"
            },
            "s3Location": "string"
         }
      ],
      "endpoints": [
         {
            "uri": "string"
         }
      ],
      "integratedRepositories": [
         {
            "branch": "string",
            "integrationId": "string",
            "providerResourceId": "string"
         }
      ],
      "sourceCode": [
         {
            "s3Location": "string"
         }
      ]
   },
   "createdAt": "string",
   "description": "string",
   "logConfig": {
      "logGroup": "string",
      "logStream": "string"
   },
   "scopeDocs": [
      {
         "artifactId": "string",
         "integratedDocument": {
            "integrationId": "string",
            "resourceId": "string"
         },
         "s3Location": "string"
      }
   ],
   "serviceRole": "string",
   "threatModelId": "string",
   "title": "string",
   "updatedAt": "string"
}
```

## Response Elements
<a name="API_CreateThreatModel_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [agentSpaceId](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-agentSpaceId"></a>
The unique identifier of the agent space that contains the threat model.
Type: String

 ** [assets](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-assets"></a>
The assets included in the threat model.
Type: [Assets](API_Assets.md) object

 ** [createdAt](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-createdAt"></a>
The date and time the threat model was created, in UTC format.
Type: Timestamp

 ** [description](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-description"></a>
A description of the application or system being threat modeled.
Type: String

 ** [logConfig](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-logConfig"></a>
The CloudWatch Logs configuration for the threat model.
Type: [CloudWatchLog](API_CloudWatchLog.md) object

 ** [scopeDocs](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-scopeDocs"></a>
The scoped documents for the agent to focus on during threat modeling.
Type: Array of [DocumentInfo](API_DocumentInfo.md) objects

 ** [serviceRole](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-serviceRole"></a>
The IAM service role used for the threat model.
Type: String

 ** [threatModelId](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-threatModelId"></a>
The unique identifier of the created threat model.
Type: String

 ** [title](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-title"></a>
The title of the threat model.
Type: String

 ** [updatedAt](#API_CreateThreatModel_ResponseSyntax) **   <a name="securityagent-CreateThreatModel-response-updatedAt"></a>
The date and time the threat model was last updated, in UTC format.
Type: Timestamp

## Errors
<a name="API_CreateThreatModel_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_CreateThreatModel_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/CreateThreatModel)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/CreateThreatModel)

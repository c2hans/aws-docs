---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetThreatModels.html
---

# BatchGetThreatModels
<a name="API_BatchGetThreatModels"></a>

Retrieves information about one or more threat models in an agent space.

## Request Syntax
<a name="API_BatchGetThreatModels_RequestSyntax"></a>

```
POST /BatchGetThreatModels HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "threatModelIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetThreatModels_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetThreatModels_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetThreatModels_RequestSyntax) **   <a name="securityagent-BatchGetThreatModels-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the threat models.
Type: String
Required: Yes

 ** [threatModelIds](#API_BatchGetThreatModels_RequestSyntax) **   <a name="securityagent-BatchGetThreatModels-request-threatModelIds"></a>
The list of threat model identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetThreatModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "notFound": [ "string" ],
   "threatModels": [
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
   ]
}
```

## Response Elements
<a name="API_BatchGetThreatModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [notFound](#API_BatchGetThreatModels_ResponseSyntax) **   <a name="securityagent-BatchGetThreatModels-response-notFound"></a>
The list of threat model identifiers that were not found.
Type: Array of strings

 ** [threatModels](#API_BatchGetThreatModels_ResponseSyntax) **   <a name="securityagent-BatchGetThreatModels-response-threatModels"></a>
The list of threat models that were found.
Type: Array of [ThreatModel](API_ThreatModel.md) objects

## Errors
<a name="API_BatchGetThreatModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetThreatModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetThreatModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetThreatModels)

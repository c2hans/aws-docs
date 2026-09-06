---
source_url: https://docs.aws.amazon.com/securityagent/latest/APIReference/API_BatchGetCodeReviews.html
---

# BatchGetCodeReviews
<a name="API_BatchGetCodeReviews"></a>

Retrieves information about one or more code reviews in an agent space.

## Request Syntax
<a name="API_BatchGetCodeReviews_RequestSyntax"></a>

```
POST /BatchGetCodeReviews HTTP/1.1
Content-type: application/json

{
   "agentSpaceId": "{{string}}",
   "codeReviewIds": [ "{{string}}" ]
}
```

## URI Request Parameters
<a name="API_BatchGetCodeReviews_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_BatchGetCodeReviews_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [agentSpaceId](#API_BatchGetCodeReviews_RequestSyntax) **   <a name="securityagent-BatchGetCodeReviews-request-agentSpaceId"></a>
The unique identifier of the agent space that contains the code reviews.
Type: String
Required: Yes

 ** [codeReviewIds](#API_BatchGetCodeReviews_RequestSyntax) **   <a name="securityagent-BatchGetCodeReviews-request-codeReviewIds"></a>
The list of code review identifiers to retrieve.
Type: Array of strings
Required: Yes

## Response Syntax
<a name="API_BatchGetCodeReviews_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "codeReviews": [
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
         "codeRemediationStrategy": "string",
         "codeReviewId": "string",
         "createdAt": "string",
         "logConfig": {
            "logGroup": "string",
            "logStream": "string"
         },
         "maxTaskHours": number,
         "serviceRole": "string",
         "title": "string",
         "updatedAt": "string",
         "validationMode": "string"
      }
   ],
   "notFound": [ "string" ]
}
```

## Response Elements
<a name="API_BatchGetCodeReviews_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [codeReviews](#API_BatchGetCodeReviews_ResponseSyntax) **   <a name="securityagent-BatchGetCodeReviews-response-codeReviews"></a>
The list of code reviews that were found.
Type: Array of [CodeReview](API_CodeReview.md) objects

 ** [notFound](#API_BatchGetCodeReviews_ResponseSyntax) **   <a name="securityagent-BatchGetCodeReviews-response-notFound"></a>
The list of code review identifiers that were not found.
Type: Array of strings

## Errors
<a name="API_BatchGetCodeReviews_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_BatchGetCodeReviews_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/securityagent-2025-09-06/BatchGetCodeReviews)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityagent-2025-09-06/BatchGetCodeReviews)

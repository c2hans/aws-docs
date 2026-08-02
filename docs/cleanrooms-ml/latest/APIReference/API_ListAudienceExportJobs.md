---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListAudienceExportJobs.html
---

# ListAudienceExportJobs
<a name="API_ListAudienceExportJobs"></a>

Returns a list of the audience export jobs.

## Request Syntax
<a name="API_ListAudienceExportJobs_RequestSyntax"></a>

```
GET /audience-export-job?audienceGenerationJobArn={{audienceGenerationJobArn}}&maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAudienceExportJobs_RequestParameters"></a>

The request uses the following URI parameters.

 ** [audienceGenerationJobArn](#API_ListAudienceExportJobs_RequestSyntax) **   <a name="API-ListAudienceExportJobs-request-uri-audienceGenerationJobArn"></a>
The Amazon Resource Name (ARN) of the audience generation job that you are interested in.
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws[-a-z]*:cleanrooms-ml:[-a-z0-9]+:[0-9]{12}:audience-generation-job/[-a-zA-Z0-9_/.]+`

 ** [maxResults](#API_ListAudienceExportJobs_RequestSyntax) **   <a name="API-ListAudienceExportJobs-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAudienceExportJobs_RequestSyntax) **   <a name="API-ListAudienceExportJobs-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Request Body
<a name="API_ListAudienceExportJobs_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAudienceExportJobs_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceExportJobs": [
      {
         "audienceGenerationJobArn": "string",
         "audienceSize": {
            "type": "string",
            "value": number
         },
         "createTime": "string",
         "description": "string",
         "name": "string",
         "outputLocation": "string",
         "status": "string",
         "statusDetails": {
            "message": "string",
            "statusCode": "string"
         },
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAudienceExportJobs_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceExportJobs](#API_ListAudienceExportJobs_ResponseSyntax) **   <a name="API-ListAudienceExportJobs-response-audienceExportJobs"></a>
The audience export jobs that match the request.
Type: Array of [AudienceExportJobSummary](API_AudienceExportJobSummary.md) objects

 ** [nextToken](#API_ListAudienceExportJobs_ResponseSyntax) **   <a name="API-ListAudienceExportJobs-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Errors
<a name="API_ListAudienceExportJobs_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListAudienceExportJobs_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListAudienceExportJobs)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListAudienceExportJobs)

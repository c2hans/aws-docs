---
source_url: https://docs.aws.amazon.com/cleanrooms-ml/latest/APIReference/API_ListAudienceModels.html
---

# ListAudienceModels
<a name="API_ListAudienceModels"></a>

Returns a list of audience models.

## Request Syntax
<a name="API_ListAudienceModels_RequestSyntax"></a>

```
GET /audience-model?maxResults={{maxResults}}&nextToken={{nextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_ListAudienceModels_RequestParameters"></a>

The request uses the following URI parameters.

 ** [maxResults](#API_ListAudienceModels_RequestSyntax) **   <a name="API-ListAudienceModels-request-uri-maxResults"></a>
The maximum size of the results that is returned per call.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [nextToken](#API_ListAudienceModels_RequestSyntax) **   <a name="API-ListAudienceModels-request-uri-nextToken"></a>
The token value retrieved from a previous call to access the next page of results.
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Request Body
<a name="API_ListAudienceModels_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_ListAudienceModels_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "audienceModels": [
      {
         "audienceModelArn": "string",
         "createTime": "string",
         "description": "string",
         "name": "string",
         "status": "string",
         "trainingDatasetArn": "string",
         "updateTime": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListAudienceModels_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [audienceModels](#API_ListAudienceModels_ResponseSyntax) **   <a name="API-ListAudienceModels-response-audienceModels"></a>
The audience models that match the request.
Type: Array of [AudienceModelSummary](API_AudienceModelSummary.md) objects

 ** [nextToken](#API_ListAudienceModels_ResponseSyntax) **   <a name="API-ListAudienceModels-response-nextToken"></a>
The token value used to access the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 10240.

## Errors
<a name="API_ListAudienceModels_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ValidationException **
The request parameters for this request are incorrect.
HTTP Status Code: 400

## See Also
<a name="API_ListAudienceModels_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/cleanroomsml-2023-09-06/ListAudienceModels)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/cleanroomsml-2023-09-06/ListAudienceModels)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Clean Rooms ML. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query cleanrooms-ml` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

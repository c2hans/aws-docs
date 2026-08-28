---
source_url: https://docs.aws.amazon.com/datazone/latest/APIReference/API_RejectPredictions.html
---

# RejectPredictions
<a name="API_RejectPredictions"></a>

Rejects automatically generated business-friendly metadata for your Amazon DataZone assets.

## Request Syntax
<a name="API_RejectPredictions_RequestSyntax"></a>

```
PUT /v2/domains/{{domainIdentifier}}/assets/{{identifier}}/reject-predictions?revision={{revision}} HTTP/1.1
Content-type: application/json

{
   "clientToken": "{{string}}",
   "rejectChoices": [
      {
         "predictionChoices": [ {{number}} ],
         "predictionTarget": "{{string}}"
      }
   ],
   "rejectRule": {
      "rule": "{{string}}",
      "threshold": {{number}}
   }
}
```

## URI Request Parameters
<a name="API_RejectPredictions_RequestParameters"></a>

The request uses the following URI parameters.

 ** [domainIdentifier](#API_RejectPredictions_RequestSyntax) **   <a name="datazone-RejectPredictions-request-uri-domainIdentifier"></a>
The identifier of the Amazon DataZone domain.
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [identifier](#API_RejectPredictions_RequestSyntax) **   <a name="datazone-RejectPredictions-request-uri-identifier"></a>
The identifier of the prediction.
Pattern: `[a-zA-Z0-9_-]{1,36}`
Required: Yes

 ** [revision](#API_RejectPredictions_RequestSyntax) **   <a name="datazone-RejectPredictions-request-uri-revision"></a>
The revision that is to be made to the asset.
Length Constraints: Minimum length of 1. Maximum length of 64.

## Request Body
<a name="API_RejectPredictions_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [clientToken](#API_RejectPredictions_RequestSyntax) **   <a name="datazone-RejectPredictions-request-clientToken"></a>
A unique, case-sensitive identifier that is provided to ensure the idempotency of the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7E]+`
Required: No

 ** [rejectChoices](#API_RejectPredictions_RequestSyntax) **   <a name="datazone-RejectPredictions-request-rejectChoices"></a>
Specifies the prediction (aka, the automatically generated piece of metadata) and the target (for example, a column name) that can be rejected.
Type: Array of [RejectChoice](API_RejectChoice.md) objects
Required: No

 ** [rejectRule](#API_RejectPredictions_RequestSyntax) **   <a name="datazone-RejectPredictions-request-rejectRule"></a>
Specifies the rule (or the conditions) under which a prediction can be rejected.
Type: [RejectRule](API_RejectRule.md) object
Required: No

## Response Syntax
<a name="API_RejectPredictions_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "assetId": "string",
   "assetRevision": "string",
   "domainId": "string"
}
```

## Response Elements
<a name="API_RejectPredictions_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [assetId](#API_RejectPredictions_ResponseSyntax) **   <a name="datazone-RejectPredictions-response-assetId"></a>
The ID of the asset.
Type: String
Pattern: `[a-zA-Z0-9_-]{1,36}`

 ** [assetRevision](#API_RejectPredictions_ResponseSyntax) **   <a name="datazone-RejectPredictions-response-assetRevision"></a>
The revision that is to be made to the asset.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.

 ** [domainId](#API_RejectPredictions_ResponseSyntax) **   <a name="datazone-RejectPredictions-response-domainId"></a>
The ID of the Amazon DataZone domain.
Type: String
Pattern: `dzd[-_][a-zA-Z0-9_-]{1,36}`

## Errors
<a name="API_RejectPredictions_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** ConflictException **
There is a conflict while performing this action.
HTTP Status Code: 409

 ** InternalServerException **
The request has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found.
HTTP Status Code: 404

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 429

 ** UnauthorizedException **
You do not have permission to perform this action.
HTTP Status Code: 401

 ** ValidationException **
The input fails to satisfy the constraints specified by the AWS service.
HTTP Status Code: 400

## See Also
<a name="API_RejectPredictions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/datazone-2018-05-10/RejectPredictions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datazone-2018-05-10/RejectPredictions)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon DataZone. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query datazone` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

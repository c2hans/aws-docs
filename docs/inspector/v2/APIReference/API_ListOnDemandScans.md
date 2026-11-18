---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListOnDemandScans.html
---

# ListOnDemandScans
<a name="API_ListOnDemandScans"></a>

Lists the on-demand scans for a resource.

## Request Syntax
<a name="API_ListOnDemandScans_RequestSyntax"></a>

```
POST /ondemand/scans HTTP/1.1
Content-type: application/json

{
   "maxResults": {{number}},
   "nextToken": "{{string}}",
   "resourceId": "{{string}}",
   "resourceType": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListOnDemandScans_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListOnDemandScans_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListOnDemandScans_RequestSyntax) **   <a name="inspector2-ListOnDemandScans-request-maxResults"></a>
The maximum number of results to return in a single page of the response.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListOnDemandScans_RequestSyntax) **   <a name="inspector2-ListOnDemandScans-request-nextToken"></a>
A pagination token from a previous response used to retrieve the next page of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000000.
Required: No

 ** [resourceId](#API_ListOnDemandScans_RequestSyntax) **   <a name="inspector2-ListOnDemandScans-request-resourceId"></a>
The ID of the resource whose on-demand scans are being listed.
Type: String
Length Constraints: Minimum length of 10. Maximum length of 1024.
Pattern: `.*(^arn:.*:ecr:.*:\d{12}:repository\/[a-zA-Z0-9._\/-]+(\/sha256:[a-z0-9]{64})?$)|(^i-([a-z0-9]{8}|[a-z0-9]{17}|\\*)$|(^arn:(aws[a-zA-Z-]*)?:lambda:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:function:[a-zA-Z0-9-_\.]+(:(\$LATEST|[a-zA-Z0-9-_]+))?$)|(^arn:(aws[a-zA-Z-]*)?:inspector2:[a-z]{2}(-gov)?-[a-z]+-\d{1}:\d{12}:codesecurity-integration\/[a-f0-9-]{36}\/project-[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}$))|(^\/subscriptions\/[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}\/resourcegroups\/[a-z0-9_\-\.()]+\/providers\/(microsoft\.compute\/virtualmachines\/[a-z0-9_\-]+|microsoft\.web\/sites\/[a-z0-9_\-]+|microsoft\.containerregistry\/registries\/[a-z0-9_\-]+(\/repositories\/[a-z0-9_\-\/]+\/images?\/sha256:[a-f0-9]{64})?)$).*`
Required: Yes

 ** [resourceType](#API_ListOnDemandScans_RequestSyntax) **   <a name="inspector2-ListOnDemandScans-request-resourceType"></a>
The type of the resource whose on-demand scans are being listed.
Type: String
Valid Values: `AMI`
Required: Yes

## Response Syntax
<a name="API_ListOnDemandScans_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "items": [
      {
         "completedAt": "string",
         "resourceId": "string",
         "resourceType": "string",
         "scanId": "string",
         "scanStatus": "string",
         "scanStatusReason": "string",
         "startedAt": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListOnDemandScans_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [items](#API_ListOnDemandScans_ResponseSyntax) **   <a name="inspector2-ListOnDemandScans-response-items"></a>
The list of on-demand scans that match the request.
Type: Array of [OnDemandScan](API_OnDemandScan.md) objects

 ** [nextToken](#API_ListOnDemandScans_ResponseSyntax) **   <a name="inspector2-ListOnDemandScans-response-nextToken"></a>
A pagination token to use in a subsequent request to retrieve the next page of results. This field is absent when there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000000.

## Errors
<a name="API_ListOnDemandScans_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
 For `Enable`, you receive this error if you attempt to use a feature in an unsupported AWS Region.
HTTP Status Code: 403

 ** InternalServerException **
The request has failed due to an internal failure of the Amazon Inspector service.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 500

 ** ThrottlingException **
The limit on the number of requests per second was exceeded.
 ** retryAfterSeconds **
The number of seconds to wait before retrying the request.
HTTP Status Code: 429

 ** ValidationException **
The request has failed validation due to missing required fields or having invalid inputs.
 ** fields **
The fields that failed validation.
 ** reason **
The reason for the validation failure.
HTTP Status Code: 400

## See Also
<a name="API_ListOnDemandScans_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/inspector2-2020-06-08/ListOnDemandScans)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/ListOnDemandScans)

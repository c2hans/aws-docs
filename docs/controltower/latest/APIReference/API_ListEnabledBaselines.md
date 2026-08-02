---
source_url: https://docs.aws.amazon.com/controltower/latest/APIReference/API_ListEnabledBaselines.html
---

# ListEnabledBaselines
<a name="API_ListEnabledBaselines"></a>

Returns a list of summaries describing `EnabledBaseline` resources. You can filter the list by the corresponding `Baseline` or `Target` of the `EnabledBaseline` resources. For usage examples, see [https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html](https://docs.aws.amazon.com/controltower/latest/userguide/baseline-api-examples.html).

## Request Syntax
<a name="API_ListEnabledBaselines_RequestSyntax"></a>

```
POST /list-enabled-baselines HTTP/1.1
Content-type: application/json

{
   "filter": {
      "baselineIdentifiers": [ "{{string}}" ],
      "inheritanceDriftStatuses": [ "{{string}}" ],
      "parentIdentifiers": [ "{{string}}" ],
      "statuses": [ "{{string}}" ],
      "targetIdentifiers": [ "{{string}}" ]
   },
   "includeChildren": {{boolean}},
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## URI Request Parameters
<a name="API_ListEnabledBaselines_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_ListEnabledBaselines_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [filter](#API_ListEnabledBaselines_RequestSyntax) **   <a name="controltower-ListEnabledBaselines-request-filter"></a>
A filter applied on the `ListEnabledBaseline` operation. Allowed filters are `baselineIdentifiers` and `targetIdentifiers`. The filter can be applied for either, or both.
Type: [EnabledBaselineFilter](API_EnabledBaselineFilter.md) object
Required: No

 ** [includeChildren](#API_ListEnabledBaselines_RequestSyntax) **   <a name="controltower-ListEnabledBaselines-request-includeChildren"></a>
A value that can be set to include the child enabled baselines in responses. The default value is false.
Type: Boolean
Required: No

 ** [maxResults](#API_ListEnabledBaselines_RequestSyntax) **   <a name="controltower-ListEnabledBaselines-request-maxResults"></a>
The maximum number of results to be shown.
Type: Integer
Valid Range: Minimum value of 5. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListEnabledBaselines_RequestSyntax) **   <a name="controltower-ListEnabledBaselines-request-nextToken"></a>
A pagination token.
Type: String
Pattern: `.*\S+.*`
Required: No

## Response Syntax
<a name="API_ListEnabledBaselines_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "enabledBaselines": [
      {
         "arn": "string",
         "baselineIdentifier": "string",
         "baselineVersion": "string",
         "driftStatusSummary": {
            "types": {
               "inheritance": {
                  "status": "string"
               }
            }
         },
         "parentIdentifier": "string",
         "statusSummary": {
            "lastOperationIdentifier": "string",
            "status": "string"
         },
         "targetIdentifier": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListEnabledBaselines_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [enabledBaselines](#API_ListEnabledBaselines_ResponseSyntax) **   <a name="controltower-ListEnabledBaselines-response-enabledBaselines"></a>
Retuens a list of summaries of `EnabledBaseline` resources.
Type: Array of [EnabledBaselineSummary](API_EnabledBaselineSummary.md) objects

 ** [nextToken](#API_ListEnabledBaselines_ResponseSyntax) **   <a name="controltower-ListEnabledBaselines-response-nextToken"></a>
A pagination token.
Type: String
Pattern: `.*\S+.*`

## Errors
<a name="API_ListEnabledBaselines_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** InternalServerException **
An unexpected error occurred during processing of a request.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling.
 ** quotaCode **
The ID of the service quota that was exceeded.
 ** retryAfterSeconds **
The number of seconds the caller should wait before retrying.
 ** serviceCode **
The ID of the service that is associated with the error.
HTTP Status Code: 429

 ** ValidationException **
The input does not satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## See Also
<a name="API_ListEnabledBaselines_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListEnabledBaselines)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/controltower-2018-05-10/ListEnabledBaselines)

---
source_url: https://docs.aws.amazon.com/step-functions/latest/apireference/API_ListActivities.html
---

# ListActivities
<a name="API_ListActivities"></a>

Lists the existing activities.

If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.

**Note**
This operation is eventually consistent. The results are best effort and may not reflect very recent updates and changes.

## Request Syntax
<a name="API_ListActivities_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListActivities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListActivities_RequestSyntax) **   <a name="StepFunctions-ListActivities-request-maxResults"></a>
The maximum number of results that are returned per call. You can use `nextToken` to obtain further pages of results. The default is 100 and the maximum allowed page size is 1000. A value of 0 uses the default.
This is only an upper limit. The actual number of results returned per call might be fewer than the specified maximum.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 1000.
Required: No

 ** [nextToken](#API_ListActivities_RequestSyntax) **   <a name="StepFunctions-ListActivities-request-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListActivities_ResponseSyntax"></a>

```
{
   "activities": [
      {
         "activityArn": "string",
         "creationDate": number,
         "name": "string"
      }
   ],
   "nextToken": "string"
}
```

## Response Elements
<a name="API_ListActivities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [activities](#API_ListActivities_ResponseSyntax) **   <a name="StepFunctions-ListActivities-response-activities"></a>
The list of activities.
Type: Array of [ActivityListItem](API_ActivityListItem.md) objects

 ** [nextToken](#API_ListActivities_ResponseSyntax) **   <a name="StepFunctions-ListActivities-response-nextToken"></a>
If `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours. Using an expired pagination token will return an *HTTP 400 InvalidToken* error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Errors
<a name="API_ListActivities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidToken **
The provided token is not valid.
HTTP Status Code: 400

## See Also
<a name="API_ListActivities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/states-2016-11-23/ListActivities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/states-2016-11-23/ListActivities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/states-2016-11-23/ListActivities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/states-2016-11-23/ListActivities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/ListActivities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/states-2016-11-23/ListActivities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/states-2016-11-23/ListActivities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/states-2016-11-23/ListActivities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/ListActivities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/states-2016-11-23/ListActivities)

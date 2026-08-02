---
source_url: https://docs.aws.amazon.com/redshift-serverless/latest/APIReference/API_ListTracks.html
---

# ListTracks
<a name="API_ListTracks"></a>

List the Amazon Redshift Serverless versions.

## Request Syntax
<a name="API_ListTracks_RequestSyntax"></a>

```
{
   "maxResults": {{number}},
   "nextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListTracks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [maxResults](#API_ListTracks_RequestSyntax) **   <a name="redshiftserverless-ListTracks-request-maxResults"></a>
The maximum number of response records to return in each call. If the number of remaining response records exceeds the specified MaxRecords value, a value is returned in a marker field of the response. You can retrieve the next set of records by retrying the command with the returned marker value.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [nextToken](#API_ListTracks_RequestSyntax) **   <a name="redshiftserverless-ListTracks-request-nextToken"></a>
If your initial `ListTracksRequest` operation returns a `nextToken`, you can include the returned `nextToken` in following `ListTracksRequest` operations, which returns results in the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.
Required: No

## Response Syntax
<a name="API_ListTracks_ResponseSyntax"></a>

```
{
   "nextToken": "string",
   "tracks": [
      {
         "trackName": "string",
         "updateTargets": [
            {
               "trackName": "string",
               "workgroupVersion": "string"
            }
         ],
         "workgroupVersion": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListTracks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [nextToken](#API_ListTracks_ResponseSyntax) **   <a name="redshiftserverless-ListTracks-response-nextToken"></a>
When `nextToken` is returned, there are more results available. The value of `nextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 1024.

 ** [tracks](#API_ListTracks_ResponseSyntax) **   <a name="redshiftserverless-ListTracks-response-tracks"></a>
The returned tracks.
Type: Array of [ServerlessTrack](API_ServerlessTrack.md) objects

## Errors
<a name="API_ListTracks_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 400

 ** InternalServerException **
The request processing has failed because of an unknown error, exception or failure.
HTTP Status Code: 500

 ** InvalidPaginationException **
The provided pagination token is invalid.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling.
HTTP Status Code: 400

 ** ValidationException **
The input failed to satisfy the constraints specified by an AWS service.
HTTP Status Code: 400

## Examples
<a name="API_ListTracks_Examples"></a>

### Example
<a name="API_ListTracks_Example_1"></a>

This example illustrates one usage of ListTracks.

#### Sample Request
<a name="API_ListTracks_Example_1_Request"></a>

```
aws redshift-serverless list-tracks
--region us-east-1
```

#### Sample Response
<a name="API_ListTracks_Example_1_Response"></a>

```
{
    "tracks": [
        {
            "trackName": "current",
            "workgroupVersion": "1.0.106980",
            "updateTargets": [
                {
                    "trackName": "trailing",
                    "workgroupVersion": "1.0.106452"
                }
            ]
        },
        {
            "trackName": "trailing",
            "workgroupVersion": "1.0.106452",
            "updateTargets": [
                {
                    "trackName": "current",
                    "workgroupVersion": "1.0.106980"
                }
            ]
        }
    ]
}
```

## See Also
<a name="API_ListTracks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/redshift-serverless-2021-04-21/ListTracks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/redshift-serverless-2021-04-21/ListTracks)

---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListArchives.html
---

# ListArchives
<a name="API_ListArchives"></a>

Lists your archives. You can either list all the archives or you can provide a prefix to match to the archive names. Filter parameters are exclusive.

## Request Syntax
<a name="API_ListArchives_RequestSyntax"></a>

```
{
   "EventSourceArn": "{{string}}",
   "Limit": {{number}},
   "NamePrefix": "{{string}}",
   "NextToken": "{{string}}",
   "State": "{{string}}"
}
```

## Request Parameters
<a name="API_ListArchives_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventSourceArn](#API_ListArchives_RequestSyntax) **   <a name="eventbridge-ListArchives-request-EventSourceArn"></a>
The ARN of the event source associated with the archive.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws([a-z]|\-)*:events:([a-z]|\d|\-)*:([0-9]{12})?:.+\/.+$`
Required: No

 ** [Limit](#API_ListArchives_RequestSyntax) **   <a name="eventbridge-ListArchives-request-Limit"></a>
The maximum number of results to return.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NamePrefix](#API_ListArchives_RequestSyntax) **   <a name="eventbridge-ListArchives-request-NamePrefix"></a>
A name prefix to filter the archives returned. Only archives with name that match the prefix are returned.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 48.
Pattern: `[\.\-_A-Za-z0-9]+`
Required: No

 ** [NextToken](#API_ListArchives_RequestSyntax) **   <a name="eventbridge-ListArchives-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

 ** [State](#API_ListArchives_RequestSyntax) **   <a name="eventbridge-ListArchives-request-State"></a>
The state of the archive.
Type: String
Valid Values: `ENABLED | DISABLED | CREATING | UPDATING | CREATE_FAILED | UPDATE_FAILED`
Required: No

## Response Syntax
<a name="API_ListArchives_ResponseSyntax"></a>

```
{
   "Archives": [
      {
         "ArchiveName": "string",
         "CreationTime": number,
         "EventCount": number,
         "EventSourceArn": "string",
         "RetentionDays": number,
         "SizeBytes": number,
         "State": "string",
         "StateReason": "string"
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_ListArchives_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Archives](#API_ListArchives_ResponseSyntax) **   <a name="eventbridge-ListArchives-response-Archives"></a>
An array of `Archive` objects that include details about an archive.
Type: Array of [Archive](API_Archive.md) objects

 ** [NextToken](#API_ListArchives_ResponseSyntax) **   <a name="eventbridge-ListArchives-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

## Errors
<a name="API_ListArchives_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ListArchives_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListArchives)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListArchives)

---
source_url: https://docs.aws.amazon.com/voiceid/latest/APIReference/API_ListFraudsters.html
---

# ListFraudsters
<a name="API_connect-voice-id_ListFraudsters"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Lists all fraudsters in a specified watchlist or domain.

## Request Syntax
<a name="API_connect-voice-id_ListFraudsters_RequestSyntax"></a>

```
{
   "DomainId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "WatchlistId": "{{string}}"
}
```

## Request Parameters
<a name="API_connect-voice-id_ListFraudsters_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainId](#API_connect-voice-id_ListFraudsters_RequestSyntax) **   <a name="connect-connect-voice-id_ListFraudsters-request-DomainId"></a>
The identifier of the domain.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: Yes

 ** [MaxResults](#API_connect-voice-id_ListFraudsters_RequestSyntax) **   <a name="connect-connect-voice-id_ListFraudsters-request-MaxResults"></a>
The maximum number of results that are returned per call. You can use `NextToken` to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_connect-voice-id_ListFraudsters_RequestSyntax) **   <a name="connect-connect-voice-id_ListFraudsters-request-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`
Required: No

 ** [WatchlistId](#API_connect-voice-id_ListFraudsters_RequestSyntax) **   <a name="connect-connect-voice-id_ListFraudsters-request-WatchlistId"></a>
The identifier of the watchlist. If provided, all fraudsters in the watchlist are listed. If not provided, all fraudsters in the domain are listed.
Type: String
Length Constraints: Fixed length of 22.
Pattern: `[a-zA-Z0-9]{22}`
Required: No

## Response Syntax
<a name="API_connect-voice-id_ListFraudsters_ResponseSyntax"></a>

```
{
   "FraudsterSummaries": [
      {
         "CreatedAt": number,
         "DomainId": "string",
         "GeneratedFraudsterId": "string",
         "WatchlistIds": [ "string" ]
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-voice-id_ListFraudsters_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [FraudsterSummaries](#API_connect-voice-id_ListFraudsters_ResponseSyntax) **   <a name="connect-connect-voice-id_ListFraudsters-response-FraudsterSummaries"></a>
A list that contains details about each fraudster in the AWS account.
Type: Array of [FraudsterSummary](API_connect-voice-id_FraudsterSummary.md) objects

 ** [NextToken](#API_connect-voice-id_ListFraudsters_ResponseSyntax) **   <a name="connect-connect-voice-id_ListFraudsters-response-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_connect-voice-id_ListFraudsters_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Check the error message and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request failed due to an unknown error on the server side.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The specified resource cannot be found. Check the `ResourceType` and error message for more details.
 ** ResourceType **
The type of resource which cannot not be found. Possible types are `BATCH_JOB`, `COMPLIANCE_CONSENT`, `DOMAIN`, `FRAUDSTER`, `SESSION` and `SPEAKER`.
HTTP Status Code: 400

 ** ThrottlingException **
The request was denied due to request throttling. Please slow down your request rate. Refer to [ Connect Customer Voice ID Service API throttling quotas ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas) and try your request again.
HTTP Status Code: 400

 ** ValidationException **
The request failed one or more validations; check the error message for more details.
HTTP Status Code: 400

## See Also
<a name="API_connect-voice-id_ListFraudsters_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/ListFraudsters)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/ListFraudsters)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

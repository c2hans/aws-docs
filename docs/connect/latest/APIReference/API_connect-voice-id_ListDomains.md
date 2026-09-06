---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-voice-id_ListDomains.html
---

# ListDomains
<a name="API_connect-voice-id_ListDomains"></a>

**Important**
End of support notice: On May 20, 2026, AWS will end support for Connect Customer Voice ID. After May 20, 2026, you will no longer be able to access Voice ID on the Connect Customer console, access Voice ID features on the Connect Customer admin website or Contact Control Panel, or access Voice ID resources. For more information, visit [ Connect Customer Voice ID end of support](https://docs.aws.amazon.com/connect/latest/adminguide/amazonconnect-voiceid-end-of-support.html).

Lists all the domains in the AWS account.

## Request Syntax
<a name="API_connect-voice-id_ListDomains_RequestSyntax"></a>

```
{
   "MaxResults": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_connect-voice-id_ListDomains_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [MaxResults](#API_connect-voice-id_ListDomains_RequestSyntax) **   <a name="connect-connect-voice-id_ListDomains-request-MaxResults"></a>
The maximum number of results that are returned per call. You can use `NextToken` to obtain more pages of results. The default is 100; the maximum allowed page size is also 100.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: No

 ** [NextToken](#API_connect-voice-id_ListDomains_RequestSyntax) **   <a name="connect-connect-voice-id_ListDomains-request-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 8192.
Pattern: `\p{ASCII}{0,8192}`
Required: No

## Response Syntax
<a name="API_connect-voice-id_ListDomains_ResponseSyntax"></a>

```
{
   "DomainSummaries": [
      {
         "Arn": "string",
         "CreatedAt": number,
         "Description": "string",
         "DomainId": "string",
         "DomainStatus": "string",
         "Name": "string",
         "ServerSideEncryptionConfiguration": {
            "KmsKeyId": "string"
         },
         "ServerSideEncryptionUpdateDetails": {
            "Message": "string",
            "OldKmsKeyId": "string",
            "UpdateStatus": "string"
         },
         "UpdatedAt": number,
         "WatchlistDetails": {
            "DefaultWatchlistId": "string"
         }
      }
   ],
   "NextToken": "string"
}
```

## Response Elements
<a name="API_connect-voice-id_ListDomains_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainSummaries](#API_connect-voice-id_ListDomains_ResponseSyntax) **   <a name="connect-connect-voice-id_ListDomains-response-DomainSummaries"></a>
A list containing details about each domain in the AWS account.
Type: Array of [DomainSummary](API_connect-voice-id_DomainSummary.md) objects

 ** [NextToken](#API_connect-voice-id_ListDomains_ResponseSyntax) **   <a name="connect-connect-voice-id_ListDomains-response-NextToken"></a>
If `NextToken` is returned, there are more results available. The value of `NextToken` is a unique pagination token for each page. Make the call again using the returned token to retrieve the next page. Keep all other arguments unchanged. Each pagination token expires after 24 hours.
Type: String
Length Constraints: Minimum length of 1.

## Errors
<a name="API_connect-voice-id_ListDomains_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient permissions to perform this action. Check the error message and try again.
HTTP Status Code: 400

 ** InternalServerException **
The request failed due to an unknown error on the server side.
HTTP Status Code: 500

 ** ThrottlingException **
The request was denied due to request throttling. Please slow down your request rate. Refer to [ Connect Customer Voice ID Service API throttling quotas ](https://docs.aws.amazon.com/connect/latest/adminguide/amazon-connect-service-limits.html##voiceid-api-quotas) and try your request again.
HTTP Status Code: 400

 ** ValidationException **
The request failed one or more validations; check the error message for more details.
HTTP Status Code: 400

## See Also
<a name="API_connect-voice-id_ListDomains_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/voice-id-2021-09-27/ListDomains)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/voice-id-2021-09-27/ListDomains)

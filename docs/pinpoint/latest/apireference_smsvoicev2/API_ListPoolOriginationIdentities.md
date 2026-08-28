---
source_url: https://docs.aws.amazon.com/pinpoint/latest/apireference_smsvoicev2/API_ListPoolOriginationIdentities.html
---

# ListPoolOriginationIdentities
<a name="API_ListPoolOriginationIdentities"></a>

Lists all associated origination identities in your pool.

If you specify filters, the output includes information for only those origination identities that meet the filter criteria.

## Request Syntax
<a name="API_ListPoolOriginationIdentities_RequestSyntax"></a>

```
{
   "Filters": [
      {
         "Name": "{{string}}",
         "Values": [ "{{string}}" ]
      }
   ],
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "PoolId": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPoolOriginationIdentities_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_ListPoolOriginationIdentities_RequestSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-request-Filters"></a>
An array of PoolOriginationIdentitiesFilter objects to filter the results..
Type: Array of [PoolOriginationIdentitiesFilter](API_PoolOriginationIdentitiesFilter.md) objects
Array Members: Minimum number of 0 items. Maximum number of 20 items.
Required: No

 ** [MaxResults](#API_ListPoolOriginationIdentities_RequestSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-request-MaxResults"></a>
The maximum number of results to return per each request.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPoolOriginationIdentities_RequestSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-request-NextToken"></a>
The token to be used for the next set of paginated results. You don't need to supply a value for this field in the initial request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`
Required: No

 ** [PoolId](#API_ListPoolOriginationIdentities_RequestSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-request-PoolId"></a>
The unique identifier for the pool. This value can be either the PoolId or PoolArn.
If you are using a shared AWS End User Messaging SMS resource then you must use the full Amazon Resource Name(ARN).
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Pattern: `[A-Za-z0-9_:/-]*`
Required: Yes

## Response Syntax
<a name="API_ListPoolOriginationIdentities_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OriginationIdentities": [
      {
         "IsoCountryCode": "string",
         "NumberCapabilities": [ "string" ],
         "OriginationIdentity": "string",
         "OriginationIdentityArn": "string",
         "PhoneNumber": "string"
      }
   ],
   "PoolArn": "string",
   "PoolId": "string"
}
```

## Response Elements
<a name="API_ListPoolOriginationIdentities_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPoolOriginationIdentities_ResponseSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-response-NextToken"></a>
The token to be used for the next set of paginated results. If this field is empty then there are no more results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `.+`

 ** [OriginationIdentities](#API_ListPoolOriginationIdentities_ResponseSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-response-OriginationIdentities"></a>
An array of any OriginationIdentityMetadata objects.
Type: Array of [OriginationIdentityMetadata](API_OriginationIdentityMetadata.md) objects

 ** [PoolArn](#API_ListPoolOriginationIdentities_ResponseSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-response-PoolArn"></a>
The Amazon Resource Name (ARN) for the pool.
Type: String

 ** [PoolId](#API_ListPoolOriginationIdentities_ResponseSyntax) **   <a name="pinpoint-ListPoolOriginationIdentities-response-PoolId"></a>
The unique PoolId of the pool.
Type: String

## Errors
<a name="API_ListPoolOriginationIdentities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
The request was denied because you don't have sufficient permissions to access the resource.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

 ** InternalServerException **
The API encountered an unexpected error and couldn't complete the request. You might be able to successfully issue the request again in the future.
 ** RequestId **
The unique identifier of the request.
HTTP Status Code: 500

 ** ResourceNotFoundException **
A requested resource couldn't be found.
 ** ResourceId **
The unique identifier of the resource.
 ** ResourceType **
The type of resource that caused the exception.
HTTP Status Code: 400

 ** ThrottlingException **
An error that occurred because too many requests were sent during a certain amount of time.
HTTP Status Code: 400

 ** ValidationException **
A validation exception for a field.
 ** Fields **
The field that failed validation.
 ** Reason **
The reason for the exception.
HTTP Status Code: 400

## See Also
<a name="API_ListPoolOriginationIdentities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pinpoint-sms-voice-v2-2022-03-31/ListPoolOriginationIdentities)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS End User Messaging SMS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pinpoint` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

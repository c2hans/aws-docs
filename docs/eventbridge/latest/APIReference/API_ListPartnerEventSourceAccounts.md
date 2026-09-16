---
source_url: https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_ListPartnerEventSourceAccounts.html
---

# ListPartnerEventSourceAccounts
<a name="API_ListPartnerEventSourceAccounts"></a>

An SaaS partner can use this operation to display the AWS account ID that a particular partner event source name is associated with. This operation is not used by AWS customers.

## Request Syntax
<a name="API_ListPartnerEventSourceAccounts_RequestSyntax"></a>

```
{
   "EventSourceName": "{{string}}",
   "Limit": {{number}},
   "NextToken": "{{string}}"
}
```

## Request Parameters
<a name="API_ListPartnerEventSourceAccounts_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [EventSourceName](#API_ListPartnerEventSourceAccounts_RequestSyntax) **   <a name="eventbridge-ListPartnerEventSourceAccounts-request-EventSourceName"></a>
The name of the partner event source to display account information about.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `aws\.partner(/[\.\-_A-Za-z0-9]+){2,}`
Required: Yes

 ** [Limit](#API_ListPartnerEventSourceAccounts_RequestSyntax) **   <a name="eventbridge-ListPartnerEventSourceAccounts-request-Limit"></a>
Specifying this limits the number of results returned by this operation. The operation also returns a NextToken which you can use in a subsequent operation to retrieve the next set of results.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_ListPartnerEventSourceAccounts_RequestSyntax) **   <a name="eventbridge-ListPartnerEventSourceAccounts-request-NextToken"></a>
The token returned by a previous call, which you can use to retrieve the next set of results.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.
Required: No

## Response Syntax
<a name="API_ListPartnerEventSourceAccounts_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "PartnerEventSourceAccounts": [
      {
         "Account": "string",
         "CreationTime": number,
         "ExpirationTime": number,
         "State": "string"
      }
   ]
}
```

## Response Elements
<a name="API_ListPartnerEventSourceAccounts_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_ListPartnerEventSourceAccounts_ResponseSyntax) **   <a name="eventbridge-ListPartnerEventSourceAccounts-response-NextToken"></a>
A token indicating there are more results available. If there are no more results, no token is included in the response.
The value of `nextToken` is a unique pagination token for each page. To retrieve the next page of results, make the call again using the returned token. Keep all other arguments unchanged.
 Using an expired pagination token results in an `HTTP 400 InvalidToken` error.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2048.

 ** [PartnerEventSourceAccounts](#API_ListPartnerEventSourceAccounts_ResponseSyntax) **   <a name="eventbridge-ListPartnerEventSourceAccounts-response-PartnerEventSourceAccounts"></a>
The list of partner event sources returned by the operation.
Type: Array of [PartnerEventSourceAccount](API_PartnerEventSourceAccount.md) objects

## Errors
<a name="API_ListPartnerEventSourceAccounts_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
This exception occurs due to unexpected causes.
HTTP Status Code: 500

 ** OperationDisabledException **
The operation you are attempting is not available in this region.
HTTP Status Code: 400

 ** ResourceNotFoundException **
An entity that you specified does not exist.
HTTP Status Code: 400

## See Also
<a name="API_ListPartnerEventSourceAccounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eventbridge-2015-10-07/ListPartnerEventSourceAccounts)

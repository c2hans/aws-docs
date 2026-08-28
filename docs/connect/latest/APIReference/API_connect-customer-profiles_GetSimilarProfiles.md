---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetSimilarProfiles.html
---

# GetSimilarProfiles
<a name="API_connect-customer-profiles_GetSimilarProfiles"></a>

Returns a set of profiles that belong to the same matching group using the `matchId` or `profileId`. You can also specify the type of matching that you want for finding similar profiles using either `RULE_BASED_MATCHING` or `ML_BASED_MATCHING`.

## Request Syntax
<a name="API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/matches?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
Content-type: application/json

{
   "MatchType": "{{string}}",
   "SearchKey": "{{string}}",
   "SearchValue": "{{string}}"
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetSimilarProfiles_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-request-uri-MaxResults"></a>
The maximum number of objects returned per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-request-uri-NextToken"></a>
The pagination token from the previous `GetSimilarProfiles` API call.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_GetSimilarProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [MatchType](#API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-request-MatchType"></a>
Specify the type of matching to get similar profiles for.
Type: String
Valid Values: `RULE_BASED_MATCHING | ML_BASED_MATCHING`
Required: Yes

 ** [SearchKey](#API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-request-SearchKey"></a>
The string indicating the search key to be used.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

 ** [SearchValue](#API_connect-customer-profiles_GetSimilarProfiles_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-request-SearchValue"></a>
The string based on `SearchKey` to be searched for similar profiles.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Required: Yes

## Response Syntax
<a name="API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ConfidenceScore": number,
   "MatchId": "string",
   "MatchType": "string",
   "NextToken": "string",
   "ProfileIds": [ "string" ],
   "RuleLevel": number
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetSimilarProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ConfidenceScore](#API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-response-ConfidenceScore"></a>
It only has value when the `MatchType` is `ML_BASED_MATCHING`.A number between 0 and 1, where a higher score means higher similarity. Examining match confidence scores lets you distinguish between groups of similar records in which the system is highly confident (which you may decide to merge), groups of similar records about which the system is uncertain (which you may decide to have reviewed by a human), and groups of similar records that the system deems to be unlikely (which you may decide to reject). Given confidence scores vary as per the data input, it should not be used as an absolute measure of matching quality.
Type: Double

 ** [MatchId](#API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-response-MatchId"></a>
The string `matchId` that the similar profiles belong to.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.

 ** [MatchType](#API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-response-MatchType"></a>
Specify the type of matching to get similar profiles for.
Type: String
Valid Values: `RULE_BASED_MATCHING | ML_BASED_MATCHING`

 ** [NextToken](#API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-response-NextToken"></a>
The pagination token from the previous `GetSimilarProfiles` API call.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [ProfileIds](#API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-response-ProfileIds"></a>
Set of `profileId`s that belong to the same matching group.
Type: Array of strings
Pattern: `[a-f0-9]{32}`

 ** [RuleLevel](#API_connect-customer-profiles_GetSimilarProfiles_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetSimilarProfiles-response-RuleLevel"></a>
The integer rule level that the profiles matched on.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 15.

## Errors
<a name="API_connect-customer-profiles_GetSimilarProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You do not have sufficient access to perform this action.
HTTP Status Code: 403

 ** BadRequestException **
The input you provided is invalid.
HTTP Status Code: 400

 ** InternalServerException **
An internal service error occurred.
HTTP Status Code: 500

 ** ResourceNotFoundException **
The requested resource does not exist, or access was denied.
HTTP Status Code: 404

 ** ThrottlingException **
You exceeded the maximum number of requests.
HTTP Status Code: 429

## See Also
<a name="API_connect-customer-profiles_GetSimilarProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetSimilarProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetSimilarProfiles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

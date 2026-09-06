---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetMatches.html
---

# GetMatches
<a name="API_connect-customer-profiles_GetMatches"></a>

Before calling this API, use [CreateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_CreateDomain.html) or [UpdateDomain](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_UpdateDomain.html) to enable identity resolution: set `Matching` to true.

GetMatches returns potentially matching profiles, based on the results of the latest run of a machine learning process.

**Important**
The process of matching duplicate profiles. If `Matching` = `true`, Amazon Connect Customer Profiles starts a weekly batch process called Identity Resolution Job. If you do not specify a date and time for Identity Resolution Job to run, by default it runs every Saturday at 12AM UTC to detect duplicate profiles in your domains.
After the Identity Resolution Job completes, use the [GetMatches](https://docs.aws.amazon.com/customerprofiles/latest/APIReference/API_GetMatches.html) API to return and review the results. Or, if you have configured `ExportingConfig` in the `MatchingRequest`, you can download the results from S3.

Amazon Connect uses the following profile attributes to identify matches:
+ PhoneNumber
+ HomePhoneNumber
+ BusinessPhoneNumber
+ MobilePhoneNumber
+ EmailAddress
+ PersonalEmailAddress
+ BusinessEmailAddress
+ FullName

For example, two or more profiles—with spelling mistakes such as **John Doe** and **Jhn Doe**, or different casing email addresses such as **JOHN\_DOE@ANYCOMPANY.COM** and **johndoe@anycompany.com**, or different phone number formats such as **555-010-0000** and **\+1-555-010-0000**—can be detected as belonging to the same customer **John Doe** and merged into a unified profile.

## Request Syntax
<a name="API_connect-customer-profiles_GetMatches_RequestSyntax"></a>

```
GET /domains/{{DomainName}}/matches?max-results={{MaxResults}}&next-token={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetMatches_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetMatches_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

 ** [MaxResults](#API_connect-customer-profiles_GetMatches_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-request-uri-MaxResults"></a>
The maximum number of results to return per page.
Valid Range: Minimum value of 1. Maximum value of 100.

 ** [NextToken](#API_connect-customer-profiles_GetMatches_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-request-uri-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Length Constraints: Minimum length of 1. Maximum length of 1024.

## Request Body
<a name="API_connect-customer-profiles_GetMatches_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_connect-customer-profiles_GetMatches_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "Matches": [
      {
         "ConfidenceScore": number,
         "MatchId": "string",
         "ProfileIds": [ "string" ]
      }
   ],
   "MatchGenerationDate": number,
   "NextToken": "string",
   "PotentialMatches": number
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetMatches_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Matches](#API_connect-customer-profiles_GetMatches_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-response-Matches"></a>
The list of matched profiles for this instance.
Type: Array of [MatchItem](API_connect-customer-profiles_MatchItem.md) objects

 ** [MatchGenerationDate](#API_connect-customer-profiles_GetMatches_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-response-MatchGenerationDate"></a>
The timestamp this version of Match Result generated.
Type: Timestamp

 ** [NextToken](#API_connect-customer-profiles_GetMatches_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.

 ** [PotentialMatches](#API_connect-customer-profiles_GetMatches_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetMatches-response-PotentialMatches"></a>
The number of potential matches found.
Type: Integer
Valid Range: Minimum value of 0.

## Errors
<a name="API_connect-customer-profiles_GetMatches_Errors"></a>

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
<a name="API_connect-customer-profiles_GetMatches_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetMatches)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetMatches)

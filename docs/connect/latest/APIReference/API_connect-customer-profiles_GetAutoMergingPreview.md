---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_connect-customer-profiles_GetAutoMergingPreview.html
---

# GetAutoMergingPreview
<a name="API_connect-customer-profiles_GetAutoMergingPreview"></a>

Tests the auto-merging settings of your Identity Resolution Job without merging your data. It randomly selects a sample of matching groups from the existing matching results, and applies the automerging settings that you provided. You can then view the number of profiles in the sample, the number of matches, and the number of profiles identified to be merged. This enables you to evaluate the accuracy of the attributes in your matching list.

You can't view which profiles are matched and would be merged.

**Important**
We strongly recommend you use this API to do a dry run of the automerging process before running the Identity Resolution Job. Include **at least** two matching attributes. If your matching list includes too few attributes (such as only `FirstName` or only `LastName`), there may be a large number of matches. This increases the chances of erroneous merges.

## Request Syntax
<a name="API_connect-customer-profiles_GetAutoMergingPreview_RequestSyntax"></a>

```
POST /domains/{{DomainName}}/identity-resolution-jobs/auto-merging-preview HTTP/1.1
Content-type: application/json

{
   "ConflictResolution": {
      "ConflictResolvingModel": "{{string}}",
      "SourceName": "{{string}}"
   },
   "Consolidation": {
      "MatchingAttributesList": [
         [ "{{string}}" ]
      ]
   },
   "MinAllowedConfidenceScoreForMerging": {{number}}
}
```

## URI Request Parameters
<a name="API_connect-customer-profiles_GetAutoMergingPreview_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DomainName](#API_connect-customer-profiles_GetAutoMergingPreview_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-request-uri-DomainName"></a>
The unique name of the domain.
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## Request Body
<a name="API_connect-customer-profiles_GetAutoMergingPreview_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ConflictResolution](#API_connect-customer-profiles_GetAutoMergingPreview_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-request-ConflictResolution"></a>
How the auto-merging process should resolve conflicts between different profiles.
Type: [ConflictResolution](API_connect-customer-profiles_ConflictResolution.md) object
Required: Yes

 ** [Consolidation](#API_connect-customer-profiles_GetAutoMergingPreview_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-request-Consolidation"></a>
A list of matching attributes that represent matching criteria.
Type: [Consolidation](API_connect-customer-profiles_Consolidation.md) object
Required: Yes

 ** [MinAllowedConfidenceScoreForMerging](#API_connect-customer-profiles_GetAutoMergingPreview_RequestSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-request-MinAllowedConfidenceScoreForMerging"></a>
Minimum confidence score required for profiles within a matching group to be merged during the auto-merge process.
Type: Double
Valid Range: Minimum value of 0.0. Maximum value of 1.0.
Required: No

## Response Syntax
<a name="API_connect-customer-profiles_GetAutoMergingPreview_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "DomainName": "string",
   "NumberOfMatchesInSample": number,
   "NumberOfProfilesInSample": number,
   "NumberOfProfilesWillBeMerged": number
}
```

## Response Elements
<a name="API_connect-customer-profiles_GetAutoMergingPreview_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DomainName](#API_connect-customer-profiles_GetAutoMergingPreview_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-response-DomainName"></a>
The unique name of the domain.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`

 ** [NumberOfMatchesInSample](#API_connect-customer-profiles_GetAutoMergingPreview_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-response-NumberOfMatchesInSample"></a>
The number of match groups in the domain that have been reviewed in this preview dry run.
Type: Long

 ** [NumberOfProfilesInSample](#API_connect-customer-profiles_GetAutoMergingPreview_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-response-NumberOfProfilesInSample"></a>
The number of profiles found in this preview dry run.
Type: Long

 ** [NumberOfProfilesWillBeMerged](#API_connect-customer-profiles_GetAutoMergingPreview_ResponseSyntax) **   <a name="connect-connect-customer-profiles_GetAutoMergingPreview-response-NumberOfProfilesWillBeMerged"></a>
The number of profiles that would be merged if this wasn't a preview dry run.
Type: Long

## Errors
<a name="API_connect-customer-profiles_GetAutoMergingPreview_Errors"></a>

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
<a name="API_connect-customer-profiles_GetAutoMergingPreview_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/customer-profiles-2020-08-15/GetAutoMergingPreview)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/customer-profiles-2020-08-15/GetAutoMergingPreview)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

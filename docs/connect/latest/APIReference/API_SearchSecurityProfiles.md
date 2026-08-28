---
source_url: https://docs.aws.amazon.com/connect/latest/APIReference/API_SearchSecurityProfiles.html
---

# SearchSecurityProfiles
<a name="API_SearchSecurityProfiles"></a>

Searches security profiles in an Connect Customer instance, with optional filtering.

For information about security profiles, see [Security Profiles](https://docs.aws.amazon.com/connect/latest/adminguide/connect-security-profiles.html) in the *Connect Customer Administrator Guide*. For a mapping of the API name and user interface name of the security profile permissions, see [List of security profile permissions](https://docs.aws.amazon.com/connect/latest/adminguide/security-profile-list.html).

## Request Syntax
<a name="API_SearchSecurityProfiles_RequestSyntax"></a>

```
POST /search-security-profiles HTTP/1.1
Content-type: application/json

{
   "InstanceId": "{{string}}",
   "MaxResults": {{number}},
   "NextToken": "{{string}}",
   "SearchCriteria": {
      "AndConditions": [
         "SecurityProfileSearchCriteria"
      ],
      "OrConditions": [
         "SecurityProfileSearchCriteria"
      ],
      "StringCondition": {
         "ComparisonType": "{{string}}",
         "FieldName": "{{string}}",
         "Value": "{{string}}"
      }
   },
   "SearchFilter": {
      "TagFilter": {
         "AndConditions": [
            {
               "TagKey": "{{string}}",
               "TagValue": "{{string}}"
            }
         ],
         "OrConditions": [
            [
               {
                  "TagKey": "{{string}}",
                  "TagValue": "{{string}}"
               }
            ]
         ],
         "TagCondition": {
            "TagKey": "{{string}}",
            "TagValue": "{{string}}"
         }
      }
   }
}
```

## URI Request Parameters
<a name="API_SearchSecurityProfiles_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_SearchSecurityProfiles_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [InstanceId](#API_SearchSecurityProfiles_RequestSyntax) **   <a name="connect-SearchSecurityProfiles-request-InstanceId"></a>
The identifier of the Connect Customer instance. You can [find the instance ID](https://docs.aws.amazon.com/connect/latest/adminguide/find-instance-arn.html) in the Amazon Resource Name (ARN) of the instance.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 100.
Required: Yes

 ** [MaxResults](#API_SearchSecurityProfiles_RequestSyntax) **   <a name="connect-SearchSecurityProfiles-request-MaxResults"></a>
The maximum number of results to return per page.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 100.
Required: No

 ** [NextToken](#API_SearchSecurityProfiles_RequestSyntax) **   <a name="connect-SearchSecurityProfiles-request-NextToken"></a>
The token for the next set of results. Use the value returned in the previous response in the next request to retrieve the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.
Required: No

 ** [SearchCriteria](#API_SearchSecurityProfiles_RequestSyntax) **   <a name="connect-SearchSecurityProfiles-request-SearchCriteria"></a>
The search criteria to be used to return security profiles.
The `name` field support "contains" queries with a minimum of 2 characters and maximum of 25 characters. Any queries with character lengths outside of this range will throw invalid results.
The currently supported value for `FieldName`: `name`
Type: [SecurityProfileSearchCriteria](API_SecurityProfileSearchCriteria.md) object
Required: No

 ** [SearchFilter](#API_SearchSecurityProfiles_RequestSyntax) **   <a name="connect-SearchSecurityProfiles-request-SearchFilter"></a>
Filters to be applied to search results.
Type: [SecurityProfilesSearchFilter](API_SecurityProfilesSearchFilter.md) object
Required: No

## Response Syntax
<a name="API_SearchSecurityProfiles_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "ApproximateTotalCount": number,
   "NextToken": "string",
   "SecurityProfiles": [
      {
         "Arn": "string",
         "Description": "string",
         "Id": "string",
         "OrganizationResourceId": "string",
         "SecurityProfileName": "string",
         "Tags": {
            "string" : "string"
         }
      }
   ]
}
```

## Response Elements
<a name="API_SearchSecurityProfiles_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [ApproximateTotalCount](#API_SearchSecurityProfiles_ResponseSyntax) **   <a name="connect-SearchSecurityProfiles-response-ApproximateTotalCount"></a>
The total number of security profiles which matched your search query.
Type: Long

 ** [NextToken](#API_SearchSecurityProfiles_ResponseSyntax) **   <a name="connect-SearchSecurityProfiles-response-NextToken"></a>
If there are additional results, this is the token for the next set of results.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 2500.

 ** [SecurityProfiles](#API_SearchSecurityProfiles_ResponseSyntax) **   <a name="connect-SearchSecurityProfiles-response-SecurityProfiles"></a>
Information about the security profiles.
Type: Array of [SecurityProfileSearchSummary](API_SecurityProfileSearchSummary.md) objects

## Errors
<a name="API_SearchSecurityProfiles_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalServiceException **
Request processing failed because of an error or failure with the service.
 ** Message **
The message.
HTTP Status Code: 500

 ** InvalidParameterException **
One or more of the specified parameters are not valid.
 ** Message **
The message about the parameters.
HTTP Status Code: 400

 ** InvalidRequestException **
The request is not valid.
 ** Message **
The message about the request.
 ** Reason **
Reason why the request was invalid.
HTTP Status Code: 400

 ** ResourceNotFoundException **
The specified resource was not found.
 ** Message **
The message about the resource.
HTTP Status Code: 404

 ** ThrottlingException **
The throttling limit has been exceeded.
HTTP Status Code: 429

## See Also
<a name="API_SearchSecurityProfiles_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/connect-2017-08-08/SearchSecurityProfiles)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/connect-2017-08-08/SearchSecurityProfiles)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Connect Customer. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query connect` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

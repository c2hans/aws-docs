---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_GetOrganizationConformancePackDetailedStatus.html
---

# GetOrganizationConformancePackDetailedStatus
<a name="API_GetOrganizationConformancePackDetailedStatus"></a>

Returns detailed status for each member account within an organization for a given organization conformance pack.

## Request Syntax
<a name="API_GetOrganizationConformancePackDetailedStatus_RequestSyntax"></a>

```
{
   "Filters": {
      "AccountId": "{{string}}",
      "Status": "{{string}}"
   },
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "OrganizationConformancePackName": "{{string}}"
}
```

## Request Parameters
<a name="API_GetOrganizationConformancePackDetailedStatus_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Filters](#API_GetOrganizationConformancePackDetailedStatus_RequestSyntax) **   <a name="config-GetOrganizationConformancePackDetailedStatus-request-Filters"></a>
An `OrganizationResourceDetailedStatusFilters` object.
Type: [OrganizationResourceDetailedStatusFilters](API_OrganizationResourceDetailedStatusFilters.md) object
Required: No

 ** [Limit](#API_GetOrganizationConformancePackDetailedStatus_RequestSyntax) **   <a name="config-GetOrganizationConformancePackDetailedStatus-request-Limit"></a>
The maximum number of `OrganizationConformancePackDetailedStatuses` returned on each page. If you do not specify a number, AWS Config uses the default. The default is 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_GetOrganizationConformancePackDetailedStatus_RequestSyntax) **   <a name="config-GetOrganizationConformancePackDetailedStatus-request-NextToken"></a>
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [OrganizationConformancePackName](#API_GetOrganizationConformancePackDetailedStatus_RequestSyntax) **   <a name="config-GetOrganizationConformancePackDetailedStatus-request-OrganizationConformancePackName"></a>
The name of organization conformance pack for which you want status details for member accounts.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: Yes

## Response Syntax
<a name="API_GetOrganizationConformancePackDetailedStatus_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OrganizationConformancePackDetailedStatuses": [
      {
         "AccountId": "string",
         "ConformancePackName": "string",
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "LastUpdateTime": number,
         "Status": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetOrganizationConformancePackDetailedStatus_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_GetOrganizationConformancePackDetailedStatus_ResponseSyntax) **   <a name="config-GetOrganizationConformancePackDetailedStatus-response-NextToken"></a>
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [OrganizationConformancePackDetailedStatuses](#API_GetOrganizationConformancePackDetailedStatus_ResponseSyntax) **   <a name="config-GetOrganizationConformancePackDetailedStatus-response-OrganizationConformancePackDetailedStatuses"></a>
A list of `OrganizationConformancePackDetailedStatus` objects.
Type: Array of [OrganizationConformancePackDetailedStatus](API_OrganizationConformancePackDetailedStatus.md) objects

## Errors
<a name="API_GetOrganizationConformancePackDetailedStatus_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** NoSuchOrganizationConformancePackException **
 AWS Config organization conformance pack that you passed in the filter does not exist.
For DeleteOrganizationConformancePack, you tried to delete an organization conformance pack that does not exist.
HTTP Status Code: 400

 ** OrganizationAccessDeniedException **
For `PutConfigurationAggregator` API, you can see this exception for the following reasons:
+ No permission to call `EnableAWSServiceAccess` API
+ The configuration aggregator cannot be updated because your AWS Organization management account or the delegated administrator role changed. Delete this aggregator and create a new one with the current AWS Organization.
+ The configuration aggregator is associated with a previous AWS Organization and AWS Config cannot aggregate data with current AWS Organization. Delete this aggregator and create a new one with the current AWS Organization.
+ You are not a registered delegated administrator for AWS Config with permissions to call `ListDelegatedAdministrators` API. Ensure that the management account registers delagated administrator for AWS Config service principal name before the delegated administrator creates an aggregator.
For all `OrganizationConfigRule` and `OrganizationConformancePack` APIs, AWS Config throws an exception if APIs are called from member accounts. All APIs must be called from organization management account.
HTTP Status Code: 400

## See Also
<a name="API_GetOrganizationConformancePackDetailedStatus_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/GetOrganizationConformancePackDetailedStatus)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Config. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query config` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

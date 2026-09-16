---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConfigRuleStatuses.html
---

# DescribeOrganizationConfigRuleStatuses
<a name="API_DescribeOrganizationConfigRuleStatuses"></a>

Provides organization AWS Config rule deployment status for an organization.

**Note**
The status is not considered successful until organization AWS Config rule is successfully deployed in all the member accounts with an exception of excluded accounts.
When you specify the limit and the next token, you receive a paginated response. Limit and next token are not applicable if you specify organization AWS Config rule names. It is only applicable, when you request all the organization AWS Config rules.

## Request Syntax
<a name="API_DescribeOrganizationConfigRuleStatuses_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "OrganizationConfigRuleNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeOrganizationConfigRuleStatuses_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_DescribeOrganizationConfigRuleStatuses_RequestSyntax) **   <a name="config-DescribeOrganizationConfigRuleStatuses-request-Limit"></a>
The maximum number of `OrganizationConfigRuleStatuses` returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeOrganizationConfigRuleStatuses_RequestSyntax) **   <a name="config-DescribeOrganizationConfigRuleStatuses-request-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [OrganizationConfigRuleNames](#API_DescribeOrganizationConfigRuleStatuses_RequestSyntax) **   <a name="config-DescribeOrganizationConfigRuleStatuses-request-OrganizationConfigRuleNames"></a>
The names of organization AWS Config rules for which you want status details. If you do not specify any names, AWS Config returns details for all your organization AWS Config rules.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

## Response Syntax
<a name="API_DescribeOrganizationConfigRuleStatuses_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OrganizationConfigRuleStatuses": [
      {
         "ErrorCode": "string",
         "ErrorMessage": "string",
         "LastUpdateTime": number,
         "OrganizationConfigRuleName": "string",
         "OrganizationRuleStatus": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeOrganizationConfigRuleStatuses_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeOrganizationConfigRuleStatuses_ResponseSyntax) **   <a name="config-DescribeOrganizationConfigRuleStatuses-response-NextToken"></a>
The `nextToken` string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [OrganizationConfigRuleStatuses](#API_DescribeOrganizationConfigRuleStatuses_ResponseSyntax) **   <a name="config-DescribeOrganizationConfigRuleStatuses-response-OrganizationConfigRuleStatuses"></a>
A list of `OrganizationConfigRuleStatus` objects.
Type: Array of [OrganizationConfigRuleStatus](API_OrganizationConfigRuleStatus.md) objects

## Errors
<a name="API_DescribeOrganizationConfigRuleStatuses_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidLimitException **
The specified limit is outside the allowable range.
HTTP Status Code: 400

 ** InvalidNextTokenException **
The specified next token is not valid. Specify the `nextToken` string that was returned in the previous response to get the next page of results.
HTTP Status Code: 400

 ** NoSuchOrganizationConfigRuleException **
The AWS Config rule in the request is not valid. Verify that the rule is an organization AWS Config Process Check rule, that the rule name is correct, and that valid Amazon Resouce Names (ARNs) are used before trying again.
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
<a name="API_DescribeOrganizationConfigRuleStatuses_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeOrganizationConfigRuleStatuses)

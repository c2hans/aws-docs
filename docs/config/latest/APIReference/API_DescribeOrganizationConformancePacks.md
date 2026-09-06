---
source_url: https://docs.aws.amazon.com/config/latest/APIReference/API_DescribeOrganizationConformancePacks.html
---

# DescribeOrganizationConformancePacks
<a name="API_DescribeOrganizationConformancePacks"></a>

Returns a list of organization conformance packs.

**Note**
When you specify the limit and the next token, you receive a paginated response.
Limit and next token are not applicable if you specify organization conformance packs names. They are only applicable, when you request all the organization conformance packs.
 *For accounts within an organization*
If you deploy an organizational rule or conformance pack in an organization administrator account, and then establish a delegated administrator and deploy an organizational rule or conformance pack in the delegated administrator account, you won't be able to see the organizational rule or conformance pack in the organization administrator account from the delegated administrator account or see the organizational rule or conformance pack in the delegated administrator account from organization administrator account. The `DescribeOrganizationConfigRules` and `DescribeOrganizationConformancePacks` APIs can only see and interact with the organization-related resource that were deployed from within the account calling those APIs.

## Request Syntax
<a name="API_DescribeOrganizationConformancePacks_RequestSyntax"></a>

```
{
   "Limit": {{number}},
   "NextToken": "{{string}}",
   "OrganizationConformancePackNames": [ "{{string}}" ]
}
```

## Request Parameters
<a name="API_DescribeOrganizationConformancePacks_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Limit](#API_DescribeOrganizationConformancePacks_RequestSyntax) **   <a name="config-DescribeOrganizationConformancePacks-request-Limit"></a>
The maximum number of organization config packs returned on each page. If you do no specify a number, AWS Config uses the default. The default is 100.
Type: Integer
Valid Range: Minimum value of 0. Maximum value of 100.
Required: No

 ** [NextToken](#API_DescribeOrganizationConformancePacks_RequestSyntax) **   <a name="config-DescribeOrganizationConformancePacks-request-NextToken"></a>
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String
Required: No

 ** [OrganizationConformancePackNames](#API_DescribeOrganizationConformancePacks_RequestSyntax) **   <a name="config-DescribeOrganizationConformancePacks-request-OrganizationConformancePackNames"></a>
The name that you assign to an organization conformance pack.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 25 items.
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z][-a-zA-Z0-9]*`
Required: No

## Response Syntax
<a name="API_DescribeOrganizationConformancePacks_ResponseSyntax"></a>

```
{
   "NextToken": "string",
   "OrganizationConformancePacks": [
      {
         "ConformancePackInputParameters": [
            {
               "ParameterName": "string",
               "ParameterValue": "string"
            }
         ],
         "DeliveryS3Bucket": "string",
         "DeliveryS3KeyPrefix": "string",
         "ExcludedAccounts": [ "string" ],
         "LastUpdateTime": number,
         "OrganizationConformancePackArn": "string",
         "OrganizationConformancePackName": "string"
      }
   ]
}
```

## Response Elements
<a name="API_DescribeOrganizationConformancePacks_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [NextToken](#API_DescribeOrganizationConformancePacks_ResponseSyntax) **   <a name="config-DescribeOrganizationConformancePacks-response-NextToken"></a>
The nextToken string returned on a previous page that you use to get the next page of results in a paginated response.
Type: String

 ** [OrganizationConformancePacks](#API_DescribeOrganizationConformancePacks_ResponseSyntax) **   <a name="config-DescribeOrganizationConformancePacks-response-OrganizationConformancePacks"></a>
Returns a list of OrganizationConformancePacks objects.
Type: Array of [OrganizationConformancePack](API_OrganizationConformancePack.md) objects

## Errors
<a name="API_DescribeOrganizationConformancePacks_Errors"></a>

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
<a name="API_DescribeOrganizationConformancePacks_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/config-2014-11-12/DescribeOrganizationConformancePacks)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/config-2014-11-12/DescribeOrganizationConformancePacks)

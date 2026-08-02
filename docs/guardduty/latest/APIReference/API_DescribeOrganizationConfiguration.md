---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_DescribeOrganizationConfiguration.html
---

# DescribeOrganizationConfiguration
<a name="API_DescribeOrganizationConfiguration"></a>

Returns information about the account selected as the delegated administrator for GuardDuty.

There might be regional differences because some data sources might not be available in all the AWS Regions where GuardDuty is presently supported. For more information, see [Regions and endpoints](https://docs.aws.amazon.com/guardduty/latest/ug/guardduty_regions.html).

## Request Syntax
<a name="API_DescribeOrganizationConfiguration_RequestSyntax"></a>

```
GET /detector/{{DetectorId}}/admin?maxResults={{MaxResults}}&nextToken={{NextToken}} HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeOrganizationConfiguration_RequestParameters"></a>

The request uses the following URI parameters.

 ** [DetectorId](#API_DescribeOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-request-uri-DetectorId"></a>
The detector ID of the delegated administrator for which you need to retrieve the information.
To find the `detectorId` in the current Region, see the Settings page in the GuardDuty console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.
Length Constraints: Minimum length of 1. Maximum length of 300.
Required: Yes

 ** [MaxResults](#API_DescribeOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-request-uri-MaxResults"></a>
You can use this parameter to indicate the maximum number of items that you want in the response.
Valid Range: Minimum value of 1. Maximum value of 50.

 ** [NextToken](#API_DescribeOrganizationConfiguration_RequestSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-request-uri-NextToken"></a>
You can use this parameter when paginating results. Set the value of this parameter to null on your first call to the list action. For subsequent calls to the action, fill `nextToken` in the request with the value of `NextToken` from the previous response to continue listing data.

## Request Body
<a name="API_DescribeOrganizationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeOrganizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "autoEnable": boolean,
   "autoEnableOrganizationMembers": "string",
   "dataSources": {
      "kubernetes": {
         "auditLogs": {
            "autoEnable": boolean
         }
      },
      "malwareProtection": {
         "scanEc2InstanceWithFindings": {
            "ebsVolumes": {
               "autoEnable": boolean
            }
         }
      },
      "s3Logs": {
         "autoEnable": boolean
      }
   },
   "features": [
      {
         "additionalConfiguration": [
            {
               "autoEnable": "string",
               "name": "string"
            }
         ],
         "autoEnable": "string",
         "name": "string"
      }
   ],
   "memberAccountLimitReached": boolean,
   "nextToken": "string"
}
```

## Response Elements
<a name="API_DescribeOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [autoEnable](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-response-autoEnable"></a>
 *This parameter has been deprecated.*
Indicates whether GuardDuty is automatically enabled for accounts added to the organization.
Even though this is still supported, we recommend using `AutoEnableOrganizationMembers` to achieve the similar results.
Type: Boolean

 ** [autoEnableOrganizationMembers](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-response-autoEnableOrganizationMembers"></a>
Indicates the auto-enablement configuration of GuardDuty or any of the corresponding protection plans for the member accounts in the organization.
+  `NEW`: Indicates that when a new account joins the organization, they will have GuardDuty or any of the corresponding protection plans enabled automatically.
+  `ALL`: Indicates that all accounts in the organization have GuardDuty and any of the corresponding protection plans enabled automatically. This includes `NEW` accounts that join the organization and accounts that may have been suspended or removed from the organization in GuardDuty.
+  `NONE`: Indicates that GuardDuty or any of the corresponding protection plans will not be automatically enabled for any account in the organization. The administrator must manage GuardDuty for each account in the organization individually.

  When you update the auto-enable setting from `ALL` or `NEW` to `NONE`, this action doesn't disable the corresponding option for your existing accounts. This configuration will apply to the new accounts that join the organization. After you update the auto-enable settings, no new account will have the corresponding option as enabled.
Type: String
Valid Values: `NEW | ALL | NONE`

 ** [dataSources](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-response-dataSources"></a>
 *This parameter has been deprecated.*
Describes which data sources are enabled automatically for member accounts.
Type: [OrganizationDataSourceConfigurationsResult](API_OrganizationDataSourceConfigurationsResult.md) object

 ** [features](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-response-features"></a>
A list of features that are configured for this organization.
Type: Array of [OrganizationFeatureConfigurationResult](API_OrganizationFeatureConfigurationResult.md) objects

 ** [memberAccountLimitReached](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-response-memberAccountLimitReached"></a>
Indicates whether the maximum number of allowed member accounts are already associated with the delegated administrator account for your organization.
Type: Boolean

 ** [nextToken](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="guardduty-DescribeOrganizationConfiguration-response-nextToken"></a>
The pagination parameter to be used on the next list operation to retrieve more items.
Type: String

## Errors
<a name="API_DescribeOrganizationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** BadRequestException **
A bad request exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 400

 ** InternalServerErrorException **
An internal server error exception object.
 ** Message **
The error message.
 ** Type **
The error type.
HTTP Status Code: 500

## See Also
<a name="API_DescribeOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/guardduty-2017-11-28/DescribeOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/DescribeOrganizationConfiguration)

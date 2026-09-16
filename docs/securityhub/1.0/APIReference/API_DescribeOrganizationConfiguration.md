---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_DescribeOrganizationConfiguration.html
---

# DescribeOrganizationConfiguration
<a name="API_DescribeOrganizationConfiguration"></a>

Returns information about the way your organization is configured in AWS Security Hub CSPM. Only the Security Hub CSPM administrator account can invoke this operation.

## Request Syntax
<a name="API_DescribeOrganizationConfiguration_RequestSyntax"></a>

```
GET /organization/configuration HTTP/1.1
```

## URI Request Parameters
<a name="API_DescribeOrganizationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_DescribeOrganizationConfiguration_RequestBody"></a>

The request does not have a request body.

## Response Syntax
<a name="API_DescribeOrganizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
Content-type: application/json

{
   "AutoEnable": boolean,
   "AutoEnableStandards": "string",
   "MemberAccountLimitReached": boolean,
   "OrganizationConfiguration": {
      "ConfigurationType": "string",
      "Status": "string",
      "StatusMessage": "string"
   }
}
```

## Response Elements
<a name="API_DescribeOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AutoEnable](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="securityhub-DescribeOrganizationConfiguration-response-AutoEnable"></a>
Whether to automatically enable Security Hub CSPM in new member accounts when they join the organization.
If set to `true`, then Security Hub CSPM is automatically enabled in new accounts. If set to `false`, then Security Hub CSPM isn't enabled in new accounts automatically. The default value is `false`.
If the `ConfigurationType` of your organization is set to `CENTRAL`, then this field is set to `false` and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which Security Hub CSPM is enabled and associate the policy with new organization accounts.
Type: Boolean

 ** [AutoEnableStandards](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="securityhub-DescribeOrganizationConfiguration-response-AutoEnableStandards"></a>
Whether to automatically enable Security Hub CSPM [default standards](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html) in new member accounts when they join the organization.
If equal to `DEFAULT`, then Security Hub CSPM default standards are automatically enabled for new member accounts. If equal to `NONE`, then default standards are not automatically enabled for new member accounts. The default value of this parameter is equal to `DEFAULT`.
If the `ConfigurationType` of your organization is set to `CENTRAL`, then this field is set to `NONE` and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which specific security standards are enabled and associate the policy with new organization accounts.
Type: String
Valid Values: `NONE | DEFAULT`

 ** [MemberAccountLimitReached](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="securityhub-DescribeOrganizationConfiguration-response-MemberAccountLimitReached"></a>
Whether the maximum number of allowed member accounts are already associated with the Security Hub CSPM administrator account.
Type: Boolean

 ** [OrganizationConfiguration](#API_DescribeOrganizationConfiguration_ResponseSyntax) **   <a name="securityhub-DescribeOrganizationConfiguration-response-OrganizationConfiguration"></a>
 Provides information about the way an organization is configured in AWS Security Hub CSPM.
Type: [OrganizationConfiguration](API_OrganizationConfiguration.md) object

## Errors
<a name="API_DescribeOrganizationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InternalException **
Internal server error.
HTTP Status Code: 500

 ** InvalidAccessException **
The account doesn't have permission to perform this action.
HTTP Status Code: 401

 ** InvalidInputException **
The request was rejected because you supplied an invalid or out-of-range value for an input parameter.
HTTP Status Code: 400

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

## See Also
<a name="API_DescribeOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/DescribeOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/DescribeOrganizationConfiguration)

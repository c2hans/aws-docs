---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_UpdateOrganizationConfiguration.html
---

# UpdateOrganizationConfiguration
<a name="API_UpdateOrganizationConfiguration"></a>

Updates the configuration of your organization in AWS Security Hub CSPM. Only the Security Hub CSPM administrator account can invoke this operation.

## Request Syntax
<a name="API_UpdateOrganizationConfiguration_RequestSyntax"></a>

```
POST /organization/configuration HTTP/1.1
Content-type: application/json

{
   "AutoEnable": {{boolean}},
   "AutoEnableStandards": "{{string}}",
   "OrganizationConfiguration": {
      "ConfigurationType": "{{string}}",
      "Status": "{{string}}",
      "StatusMessage": "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_UpdateOrganizationConfiguration_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_UpdateOrganizationConfiguration_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [AutoEnable](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="securityhub-UpdateOrganizationConfiguration-request-AutoEnable"></a>
Whether to automatically enable Security Hub CSPM in new member accounts when they join the organization.
If set to `true`, then Security Hub CSPM is automatically enabled in new accounts. If set to `false`, then Security Hub CSPM isn't enabled in new accounts automatically. The default value is `false`.
If the `ConfigurationType` of your organization is set to `CENTRAL`, then this field is set to `false` and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which Security Hub CSPM is enabled and associate the policy with new organization accounts.
Type: Boolean
Required: Yes

 ** [AutoEnableStandards](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="securityhub-UpdateOrganizationConfiguration-request-AutoEnableStandards"></a>
Whether to automatically enable Security Hub CSPM [default standards](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-standards-enable-disable.html) in new member accounts when they join the organization.
The default value of this parameter is equal to `DEFAULT`.
If equal to `DEFAULT`, then Security Hub CSPM default standards are automatically enabled for new member accounts. If equal to `NONE`, then default standards are not automatically enabled for new member accounts.
If the `ConfigurationType` of your organization is set to `CENTRAL`, then this field is set to `NONE` and can't be changed in the home Region and linked Regions. However, in that case, the delegated administrator can create a configuration policy in which specific security standards are enabled and associate the policy with new organization accounts.
Type: String
Valid Values: `NONE | DEFAULT`
Required: No

 ** [OrganizationConfiguration](#API_UpdateOrganizationConfiguration_RequestSyntax) **   <a name="securityhub-UpdateOrganizationConfiguration-request-OrganizationConfiguration"></a>
 Provides information about the way an organization is configured in AWS Security Hub CSPM.
Type: [OrganizationConfiguration](API_OrganizationConfiguration.md) object
Required: No

## Response Syntax
<a name="API_UpdateOrganizationConfiguration_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_UpdateOrganizationConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_UpdateOrganizationConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
You don't have permission to perform the action specified in the request.
HTTP Status Code: 403

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

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

 ** ResourceNotFoundException **
The request was rejected because we can't find the specified resource.
HTTP Status Code: 404

## See Also
<a name="API_UpdateOrganizationConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/UpdateOrganizationConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/UpdateOrganizationConfiguration)

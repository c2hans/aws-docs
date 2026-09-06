---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeIdentityProviderConfiguration.html
---

# DescribeIdentityProviderConfiguration
<a name="API_DescribeIdentityProviderConfiguration"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

 Returns detailed information on the current IdC setup for the WorkMail organization.

## Request Syntax
<a name="API_DescribeIdentityProviderConfiguration_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeIdentityProviderConfiguration_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_DescribeIdentityProviderConfiguration_RequestSyntax) **   <a name="workmail-DescribeIdentityProviderConfiguration-request-OrganizationId"></a>
 The Organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_DescribeIdentityProviderConfiguration_ResponseSyntax"></a>

```
{
   "AuthenticationMode": "string",
   "IdentityCenterConfiguration": {
      "ApplicationArn": "string",
      "InstanceArn": "string"
   },
   "PersonalAccessTokenConfiguration": {
      "LifetimeInDays": number,
      "Status": "string"
   }
}
```

## Response Elements
<a name="API_DescribeIdentityProviderConfiguration_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [AuthenticationMode](#API_DescribeIdentityProviderConfiguration_ResponseSyntax) **   <a name="workmail-DescribeIdentityProviderConfiguration-response-AuthenticationMode"></a>
 The authentication mode used in WorkMail.
Type: String
Valid Values: `IDENTITY_PROVIDER_ONLY | IDENTITY_PROVIDER_AND_DIRECTORY`

 ** [IdentityCenterConfiguration](#API_DescribeIdentityProviderConfiguration_ResponseSyntax) **   <a name="workmail-DescribeIdentityProviderConfiguration-response-IdentityCenterConfiguration"></a>
 The details of the IAM Identity Center configuration.
Type: [IdentityCenterConfiguration](API_IdentityCenterConfiguration.md) object

 ** [PersonalAccessTokenConfiguration](#API_DescribeIdentityProviderConfiguration_ResponseSyntax) **   <a name="workmail-DescribeIdentityProviderConfiguration-response-PersonalAccessTokenConfiguration"></a>
 The details of the Personal Access Token configuration.
Type: [PersonalAccessTokenConfiguration](API_PersonalAccessTokenConfiguration.md) object

## Errors
<a name="API_DescribeIdentityProviderConfiguration_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

 ** ResourceNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The resource cannot be found.
HTTP Status Code: 400

## See Also
<a name="API_DescribeIdentityProviderConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeIdentityProviderConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeIdentityProviderConfiguration)

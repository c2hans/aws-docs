---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DeleteOrganization.html
---

# DeleteOrganization
<a name="API_DeleteOrganization"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Deletes an WorkMail organization and all underlying AWS resources managed by WorkMail as part of the organization. You can choose whether to delete the associated directory. For more information, see [Removing an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/remove_organization.html) in the *WorkMail Administrator Guide*.

## Request Syntax
<a name="API_DeleteOrganization_RequestSyntax"></a>

```
{
   "ClientToken": "{{string}}",
   "DeleteDirectory": {{boolean}},
   "DeleteIdentityCenterApplication": {{boolean}},
   "ForceDelete": {{boolean}},
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DeleteOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [ClientToken](#API_DeleteOrganization_RequestSyntax) **   <a name="workmail-DeleteOrganization-request-ClientToken"></a>
The idempotency token associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7e]+`
Required: No

 ** [DeleteDirectory](#API_DeleteOrganization_RequestSyntax) **   <a name="workmail-DeleteOrganization-request-DeleteDirectory"></a>
If true, deletes the AWS Directory Service directory associated with the organization.
Type: Boolean
Required: Yes

 ** [DeleteIdentityCenterApplication](#API_DeleteOrganization_RequestSyntax) **   <a name="workmail-DeleteOrganization-request-DeleteIdentityCenterApplication"></a>
Deletes IAM Identity Center application for WorkMail. This action does not affect authentication settings for any organization.
Type: Boolean
Required: No

 ** [ForceDelete](#API_DeleteOrganization_RequestSyntax) **   <a name="workmail-DeleteOrganization-request-ForceDelete"></a>
Deletes a WorkMail organization even if the organization has enabled users.
Type: Boolean
Required: No

 ** [OrganizationId](#API_DeleteOrganization_RequestSyntax) **   <a name="workmail-DeleteOrganization-request-OrganizationId"></a>
The organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_DeleteOrganization_ResponseSyntax"></a>

```
{
   "OrganizationId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DeleteOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OrganizationId](#API_DeleteOrganization_ResponseSyntax) **   <a name="workmail-DeleteOrganization-response-OrganizationId"></a>
The organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`

 ** [State](#API_DeleteOrganization_ResponseSyntax) **   <a name="workmail-DeleteOrganization-response-State"></a>
The state of the organization.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_DeleteOrganization_Errors"></a>

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

## See Also
<a name="API_DeleteOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DeleteOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DeleteOrganization)

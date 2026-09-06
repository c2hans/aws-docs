---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_CreateOrganization.html
---

# CreateOrganization
<a name="API_CreateOrganization"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Creates a new WorkMail organization. Optionally, you can choose to associate an existing AWS Directory Service directory with your organization. If an AWS Directory Service directory ID is specified, the organization alias must match the directory alias. If you choose not to associate an existing directory with your organization, then we create a new WorkMail directory for you. For more information, see [Adding an organization](https://docs.aws.amazon.com/workmail/latest/adminguide/add_new_organization.html) in the *WorkMail Administrator Guide*.

You can associate multiple email domains with an organization, then choose your default email domain from the WorkMail console. You can also associate a domain that is managed in an Amazon Route 53 public hosted zone. For more information, see [Adding a domain](https://docs.aws.amazon.com/workmail/latest/adminguide/add_domain.html) and [Choosing the default domain](https://docs.aws.amazon.com/workmail/latest/adminguide/default_domain.html) in the *WorkMail Administrator Guide*.

Optionally, you can use a customer managed key from AWS Key Management Service (AWS KMS) to encrypt email for your organization. If you don't associate an AWS KMS key, WorkMail creates a default, AWS managed key for you.

## Request Syntax
<a name="API_CreateOrganization_RequestSyntax"></a>

```
{
   "Alias": "{{string}}",
   "ClientToken": "{{string}}",
   "DirectoryId": "{{string}}",
   "Domains": [
      {
         "DomainName": "{{string}}",
         "HostedZoneId": "{{string}}"
      }
   ],
   "EnableInteroperability": {{boolean}},
   "KmsKeyArn": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [Alias](#API_CreateOrganization_RequestSyntax) **   <a name="workmail-CreateOrganization-request-Alias"></a>
The organization alias.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 62.
Pattern: `^(?!d-)([\da-zA-Z]+)([-][\da-zA-Z]+)*`
Required: Yes

 ** [ClientToken](#API_CreateOrganization_RequestSyntax) **   <a name="workmail-CreateOrganization-request-ClientToken"></a>
The idempotency token associated with the request.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[\x21-\x7e]+`
Required: No

 ** [DirectoryId](#API_CreateOrganization_RequestSyntax) **   <a name="workmail-CreateOrganization-request-DirectoryId"></a>
The AWS Directory Service directory ID.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `^d-[0-9a-f]{10}$`
Required: No

 ** [Domains](#API_CreateOrganization_RequestSyntax) **   <a name="workmail-CreateOrganization-request-Domains"></a>
The email domains to associate with the organization.
Type: Array of [Domain](API_Domain.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

 ** [EnableInteroperability](#API_CreateOrganization_RequestSyntax) **   <a name="workmail-CreateOrganization-request-EnableInteroperability"></a>
When `true`, allows organization interoperability between WorkMail and Microsoft Exchange. If `true`, you must include a AD Connector directory ID in the request.
Type: Boolean
Required: No

 ** [KmsKeyArn](#API_CreateOrganization_RequestSyntax) **   <a name="workmail-CreateOrganization-request-KmsKeyArn"></a>
The Amazon Resource Name (ARN) of a customer managed key from AWS KMS.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:aws:kms:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`
Required: No

## Response Syntax
<a name="API_CreateOrganization_ResponseSyntax"></a>

```
{
   "OrganizationId": "string"
}
```

## Response Elements
<a name="API_CreateOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [OrganizationId](#API_CreateOrganization_ResponseSyntax) **   <a name="workmail-CreateOrganization-response-OrganizationId"></a>
The organization ID.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`

## Errors
<a name="API_CreateOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DirectoryInUseException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory is already in use by another WorkMail organization in the same account and Region.
HTTP Status Code: 400

 ** DirectoryUnavailableException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The directory is unavailable. It might be located in another Region or deleted.
HTTP Status Code: 400

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** LimitExceededException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The request exceeds the limit of the resource.
HTTP Status Code: 400

 ** NameAvailabilityException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The user, group, or resource name isn't unique in WorkMail.
HTTP Status Code: 400

## See Also
<a name="API_CreateOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/CreateOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/CreateOrganization)

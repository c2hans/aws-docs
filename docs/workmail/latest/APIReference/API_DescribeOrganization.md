---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeOrganization.html
---

# DescribeOrganization
<a name="API_DescribeOrganization"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Provides more information regarding a given organization based on its identifier.

## Request Syntax
<a name="API_DescribeOrganization_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeOrganization_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_DescribeOrganization_RequestSyntax) **   <a name="workmail-DescribeOrganization-request-OrganizationId"></a>
The identifier for the organization to be described.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_DescribeOrganization_ResponseSyntax"></a>

```
{
   "Alias": "string",
   "ARN": "string",
   "CompletedDate": number,
   "DefaultMailDomain": "string",
   "DirectoryId": "string",
   "DirectoryType": "string",
   "ErrorMessage": "string",
   "InteroperabilityEnabled": boolean,
   "MigrationAdmin": "string",
   "OrganizationId": "string",
   "State": "string"
}
```

## Response Elements
<a name="API_DescribeOrganization_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Alias](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-Alias"></a>
The alias for an organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 62.
Pattern: `^(?!d-)([\da-zA-Z]+)([-][\da-zA-Z]+)*`

 ** [ARN](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-ARN"></a>
The Amazon Resource Name (ARN) of the organization.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1011.
Pattern: `arn:aws:workmail:[a-z0-9-]*:[a-z0-9-]+:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}`

 ** [CompletedDate](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-CompletedDate"></a>
The date at which the organization became usable in the WorkMail context, in UNIX epoch time format.
Type: Timestamp

 ** [DefaultMailDomain](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-DefaultMailDomain"></a>
The default mail domain associated with the organization.
Type: String
Length Constraints: Maximum length of 256.

 ** [DirectoryId](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-DirectoryId"></a>
The identifier for the directory associated with an WorkMail organization.
Type: String
Length Constraints: Maximum length of 256.

 ** [DirectoryType](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-DirectoryType"></a>
The type of directory associated with the WorkMail organization.
Type: String
Length Constraints: Maximum length of 256.

 ** [ErrorMessage](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-ErrorMessage"></a>
(Optional) The error message indicating if unexpected behavior was encountered with regards to the organization.
Type: String
Length Constraints: Maximum length of 256.

 ** [InteroperabilityEnabled](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-InteroperabilityEnabled"></a>
Indicates if interoperability is enabled for this organization.
Type: Boolean

 ** [MigrationAdmin](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-MigrationAdmin"></a>
The user ID of the migration admin if migration is enabled for the organization.
Type: String
Length Constraints: Minimum length of 12. Maximum length of 256.

 ** [OrganizationId](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-OrganizationId"></a>
The identifier of an organization.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`

 ** [State](#API_DescribeOrganization_ResponseSyntax) **   <a name="workmail-DescribeOrganization-response-State"></a>
The state of an organization.
Type: String
Length Constraints: Maximum length of 256.

## Errors
<a name="API_DescribeOrganization_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

## See Also
<a name="API_DescribeOrganization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeOrganization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeOrganization)

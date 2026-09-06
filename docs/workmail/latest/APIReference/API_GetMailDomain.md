---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_GetMailDomain.html
---

# GetMailDomain
<a name="API_GetMailDomain"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Gets details for a mail domain, including domain records required to configure your domain with recommended security.

## Request Syntax
<a name="API_GetMailDomain_RequestSyntax"></a>

```
{
   "DomainName": "{{string}}",
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_GetMailDomain_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [DomainName](#API_GetMailDomain_RequestSyntax) **   <a name="workmail-GetMailDomain-request-DomainName"></a>
The domain from which you want to retrieve details.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 209.
Pattern: `[a-zA-Z0-9.-]+`
Required: Yes

 ** [OrganizationId](#API_GetMailDomain_RequestSyntax) **   <a name="workmail-GetMailDomain-request-OrganizationId"></a>
The WorkMail organization for which the domain is retrieved.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_GetMailDomain_ResponseSyntax"></a>

```
{
   "DkimVerificationStatus": "string",
   "IsDefault": boolean,
   "IsTestDomain": boolean,
   "OwnershipVerificationStatus": "string",
   "Records": [
      {
         "Hostname": "string",
         "Type": "string",
         "Value": "string"
      }
   ]
}
```

## Response Elements
<a name="API_GetMailDomain_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [DkimVerificationStatus](#API_GetMailDomain_ResponseSyntax) **   <a name="workmail-GetMailDomain-response-DkimVerificationStatus"></a>
Indicates the status of a DKIM verification.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED`

 ** [IsDefault](#API_GetMailDomain_ResponseSyntax) **   <a name="workmail-GetMailDomain-response-IsDefault"></a>
Specifies whether the domain is the default domain for your organization.
Type: Boolean

 ** [IsTestDomain](#API_GetMailDomain_ResponseSyntax) **   <a name="workmail-GetMailDomain-response-IsTestDomain"></a>
Specifies whether the domain is a test domain provided by WorkMail, or a custom domain.
Type: Boolean

 ** [OwnershipVerificationStatus](#API_GetMailDomain_ResponseSyntax) **   <a name="workmail-GetMailDomain-response-OwnershipVerificationStatus"></a>
 Indicates the status of the domain ownership verification.
Type: String
Valid Values: `PENDING | VERIFIED | FAILED`

 ** [Records](#API_GetMailDomain_ResponseSyntax) **   <a name="workmail-GetMailDomain-response-Records"></a>
A list of the DNS records that WorkMail recommends adding in your DNS provider for the best user experience. The records configure your domain with DMARC, SPF, DKIM, and direct incoming email traffic to SES. See admin guide for more details.
Type: Array of [DnsRecord](API_DnsRecord.md) objects

## Errors
<a name="API_GetMailDomain_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** InvalidParameterException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
One or more of the input parameters don't match the service's restrictions.
HTTP Status Code: 400

 ** MailDomainNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The domain specified is not found in your organization.
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
<a name="API_GetMailDomain_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/GetMailDomain)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/GetMailDomain)

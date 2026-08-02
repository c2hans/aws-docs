---
source_url: https://docs.aws.amazon.com/workmail/latest/APIReference/API_DescribeInboundDmarcSettings.html
---

# DescribeInboundDmarcSettings
<a name="API_DescribeInboundDmarcSettings"></a>

**Important**
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).

Lists the settings in a DMARC policy for a specified organization.

## Request Syntax
<a name="API_DescribeInboundDmarcSettings_RequestSyntax"></a>

```
{
   "OrganizationId": "{{string}}"
}
```

## Request Parameters
<a name="API_DescribeInboundDmarcSettings_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [OrganizationId](#API_DescribeInboundDmarcSettings_RequestSyntax) **   <a name="workmail-DescribeInboundDmarcSettings-request-OrganizationId"></a>
Lists the ID of the given organization.
Type: String
Length Constraints: Fixed length of 34.
Pattern: `^m-[0-9a-f]{32}$`
Required: Yes

## Response Syntax
<a name="API_DescribeInboundDmarcSettings_ResponseSyntax"></a>

```
{
   "Enforced": boolean
}
```

## Response Elements
<a name="API_DescribeInboundDmarcSettings_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [Enforced](#API_DescribeInboundDmarcSettings_ResponseSyntax) **   <a name="workmail-DescribeInboundDmarcSettings-response-Enforced"></a>
Lists the enforcement setting of the applied policy.
Type: Boolean

## Errors
<a name="API_DescribeInboundDmarcSettings_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** OrganizationNotFoundException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
An operation received a valid organization identifier that either doesn't belong or exist in the system.
HTTP Status Code: 400

 ** OrganizationStateException **
End of support notice: On March 31, 2027, AWS will end support for Amazon WorkMail. After March 31, 2027, you will no longer be able to access the WorkMail console or WorkMail resources. For more information, see [Amazon WorkMail end of support](https://docs.aws.amazon.com/workmail/latest/adminguide/workmail-end-of-support.html).
The organization must have a valid state to perform certain operations on the organization or its members.
HTTP Status Code: 400

## See Also
<a name="API_DescribeInboundDmarcSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/workmail-2017-10-01/DescribeInboundDmarcSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/workmail-2017-10-01/DescribeInboundDmarcSettings)

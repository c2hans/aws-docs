---
source_url: https://docs.aws.amazon.com/ses/latest/APIReference/API_ListIdentities.html
---

# ListIdentities
<a name="API_ListIdentities"></a>

Returns a list containing all of the identities (email addresses and domains) for your AWS account in the current AWS Region, regardless of verification status.

You can execute this operation no more than once per second.

**Note**
It's recommended that for successive pagination calls of this API, you continue to the use the same parameter/value pairs as used in the original call, e.g., if you used `IdentityType=Domain` in the the original call and received a `NextToken` in the response, you should continue providing the `IdentityType=Domain` parameter for further `NextToken` calls; however, if you didn't provide the `IdentityType` parameter in the original call, then continue to not provide it for successive pagination calls. Using this protocol will ensure consistent results.

## Request Parameters
<a name="API_ListIdentities_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** IdentityType **
The type of the identities to list. Possible values are "EmailAddress" and "Domain". If this parameter is omitted, then all identities are listed.
Type: String
Valid Values: `EmailAddress | Domain`
Required: No

 ** MaxItems **
The maximum number of identities per page. Possible values are 1-1000 inclusive.
Type: Integer
Required: No

 ** NextToken **
The token to use for pagination.
Type: String
Required: No

## Response Elements
<a name="API_ListIdentities_ResponseElements"></a>

The following elements are returned by the service.

 **Identities.member.N**
A list of identities.
Type: Array of strings

 ** NextToken **
The token used for pagination.
Type: String

## Errors
<a name="API_ListIdentities_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_ListIdentities_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/email-2010-12-01/ListIdentities)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/email-2010-12-01/ListIdentities)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/email-2010-12-01/ListIdentities)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/email-2010-12-01/ListIdentities)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/email-2010-12-01/ListIdentities)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/email-2010-12-01/ListIdentities)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/email-2010-12-01/ListIdentities)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/email-2010-12-01/ListIdentities)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/email-2010-12-01/ListIdentities)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/email-2010-12-01/ListIdentities)

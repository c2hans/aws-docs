---
source_url: https://docs.aws.amazon.com/sns/latest/api/API_GetSMSAttributes.html
---

# GetSMSAttributes
<a name="API_GetSMSAttributes"></a>

Returns the settings for sending SMS messages from your AWS account.

These settings are set with the `SetSMSAttributes` action.

## Request Parameters
<a name="API_GetSMSAttributes_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 **attributes.member.N**
A list of the individual attribute names, such as `MonthlySpendLimit`, for which you want values.
For all attribute names, see [SetSMSAttributes](https://docs.aws.amazon.com/sns/latest/api/API_SetSMSAttributes.html).
If you don't use this parameter, Amazon SNS returns all SMS attributes.
Type: Array of strings
Required: No

## Response Elements
<a name="API_GetSMSAttributes_ResponseElements"></a>

The following element is returned by the service.

 **attributes** attributes.entry.N.key (key)attributes.entry.N.value (value)
The SMS attribute names and their values.
Type: String to string map

## Errors
<a name="API_GetSMSAttributes_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AuthorizationError **
Indicates that the user has been denied access to the requested resource.
HTTP Status Code: 403

 ** InternalError **
Indicates an internal service error.
HTTP Status Code: 500

 ** InvalidParameter **
Indicates that a request parameter does not comply with the associated constraints.
HTTP Status Code: 400

 ** Throttled **
Indicates that the rate at which requests have been submitted for this action exceeds the limit for your Amazon Web Services account.
 ** message **
Throttled request.
HTTP Status Code: 429

## See Also
<a name="API_GetSMSAttributes_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/sns-2010-03-31/GetSMSAttributes)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/sns-2010-03-31/GetSMSAttributes)

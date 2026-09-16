---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_EnableSecurityHub.html
---

# EnableSecurityHub
<a name="API_EnableSecurityHub"></a>

Enables Security Hub CSPM for your account in the current Region or the Region you specify in the request.

When you enable Security Hub CSPM, you grant to Security Hub CSPM the permissions necessary to gather findings from other services that are integrated with Security Hub CSPM.

When you use the `EnableSecurityHub` operation to enable Security Hub CSPM, you also automatically enable the following standards:
+ Center for Internet Security (CIS) AWS Foundations Benchmark v1.2.0
+  AWS Foundational Security Best Practices

Other standards are not automatically enabled.

To opt out of automatically enabled standards, set `EnableDefaultStandards` to `false`.

After you enable Security Hub CSPM, to enable a standard, use the `BatchEnableStandards` operation. To disable a standard, use the `BatchDisableStandards` operation.

To learn more, see the [setup information](https://docs.aws.amazon.com/securityhub/latest/userguide/securityhub-settingup.html) in the * AWS Security Hub CSPM User Guide*.

## Request Syntax
<a name="API_EnableSecurityHub_RequestSyntax"></a>

```
POST /accounts HTTP/1.1
Content-type: application/json

{
   "ControlFindingGenerator": "{{string}}",
   "EnableDefaultStandards": {{boolean}},
   "Tags": {
      "{{string}}" : "{{string}}"
   }
}
```

## URI Request Parameters
<a name="API_EnableSecurityHub_RequestParameters"></a>

The request does not use any URI parameters.

## Request Body
<a name="API_EnableSecurityHub_RequestBody"></a>

The request accepts the following data in JSON format.

 ** [ControlFindingGenerator](#API_EnableSecurityHub_RequestSyntax) **   <a name="securityhub-EnableSecurityHub-request-ControlFindingGenerator"></a>
This field, used when enabling Security Hub CSPM, specifies whether the calling account has consolidated control findings turned on. If the value for this field is set to `SECURITY_CONTROL`, Security Hub CSPM generates a single finding for a control check even when the check applies to multiple enabled standards.
If the value for this field is set to `STANDARD_CONTROL`, Security Hub CSPM generates separate findings for a control check when the check applies to multiple enabled standards.
The value for this field in a member account matches the value in the administrator account. For accounts that aren't part of an organization, the default value of this field is `SECURITY_CONTROL` if you enabled Security Hub CSPM on or after February 23, 2023.
Type: String
Valid Values: `STANDARD_CONTROL | SECURITY_CONTROL`
Required: No

 ** [EnableDefaultStandards](#API_EnableSecurityHub_RequestSyntax) **   <a name="securityhub-EnableSecurityHub-request-EnableDefaultStandards"></a>
Whether to enable the security standards that Security Hub CSPM has designated as automatically enabled. If you don't provide a value for `EnableDefaultStandards`, it is set to `true`. To not enable the automatically enabled standards, set `EnableDefaultStandards` to `false`.
Type: Boolean
Required: No

 ** [Tags](#API_EnableSecurityHub_RequestSyntax) **   <a name="securityhub-EnableSecurityHub-request-Tags"></a>
The tags to add to the hub resource when you enable Security Hub CSPM.
Type: String to string map
Map Entries: Maximum number of 50 items.
Key Length Constraints: Minimum length of 1. Maximum length of 128.
Key Pattern: `^(?!aws:)[a-zA-Z+-=._:/]+$`
Value Length Constraints: Maximum length of 256.
Required: No

## Response Syntax
<a name="API_EnableSecurityHub_ResponseSyntax"></a>

```
HTTP/1.1 200
```

## Response Elements
<a name="API_EnableSecurityHub_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors
<a name="API_EnableSecurityHub_Errors"></a>

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

 ** LimitExceededException **
The request was rejected because it attempted to create resources beyond the current AWS account or throttling limits. The error code describes the limit exceeded.
HTTP Status Code: 429

 ** ResourceConflictException **
The resource specified in the request conflicts with an existing resource.
HTTP Status Code: 409

## See Also
<a name="API_EnableSecurityHub_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/securityhub-2018-10-26/EnableSecurityHub)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/EnableSecurityHub)

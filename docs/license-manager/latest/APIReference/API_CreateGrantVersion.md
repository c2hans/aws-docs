---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrantVersion.html
---

# CreateGrantVersion
<a name="API_CreateGrantVersion"></a>

Creates a new version of the specified grant. For more information, see [Granted licenses in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html) in the * AWS License Manager User Guide*.

## Request Syntax
<a name="API_CreateGrantVersion_RequestSyntax"></a>

```
{
   "AllowedOperations": [ "{{string}}" ],
   "ClientToken": "{{string}}",
   "GrantArn": "{{string}}",
   "GrantName": "{{string}}",
   "Options": {
      "ActivationOverrideBehavior": "{{string}}"
   },
   "SourceVersion": "{{string}}",
   "Status": "{{string}}",
   "StatusReason": "{{string}}"
}
```

## Request Parameters
<a name="API_CreateGrantVersion_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowedOperations](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-AllowedOperations"></a>
Allowed operations for the grant.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Valid Values: `CreateGrant | CheckoutLicense | CheckoutBorrowLicense | CheckInLicense | ExtendConsumptionLicense | ListPurchasedLicenses | CreateToken`
Required: No

 ** [ClientToken](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [GrantArn](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-GrantArn"></a>
Amazon Resource Name (ARN) of the grant.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [GrantName](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-GrantName"></a>
Grant name.
Type: String
Required: No

 ** [Options](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-Options"></a>
The options specified for the grant.
Type: [Options](API_Options.md) object
Required: No

 ** [SourceVersion](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-SourceVersion"></a>
Current version of the grant.
Type: String
Required: No

 ** [Status](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-Status"></a>
Grant status.
Type: String
Valid Values: `PENDING_WORKFLOW | PENDING_ACCEPT | REJECTED | ACTIVE | FAILED_WORKFLOW | DELETED | PENDING_DELETE | DISABLED | WORKFLOW_COMPLETED`
Required: No

 ** [StatusReason](#API_CreateGrantVersion_RequestSyntax) **   <a name="licensemanager-CreateGrantVersion-request-StatusReason"></a>
Grant status reason.
Type: String
Length Constraints: Maximum length of 400.
Pattern: `[\s\S]+`
Required: No

## Response Syntax
<a name="API_CreateGrantVersion_ResponseSyntax"></a>

```
{
   "GrantArn": "string",
   "Status": "string",
   "Version": "string"
}
```

## Response Elements
<a name="API_CreateGrantVersion_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GrantArn](#API_CreateGrantVersion_ResponseSyntax) **   <a name="licensemanager-CreateGrantVersion-response-GrantArn"></a>
Grant ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [Status](#API_CreateGrantVersion_ResponseSyntax) **   <a name="licensemanager-CreateGrantVersion-response-Status"></a>
Grant status.
Type: String
Valid Values: `PENDING_WORKFLOW | PENDING_ACCEPT | REJECTED | ACTIVE | FAILED_WORKFLOW | DELETED | PENDING_DELETE | DISABLED | WORKFLOW_COMPLETED`

 ** [Version](#API_CreateGrantVersion_ResponseSyntax) **   <a name="licensemanager-CreateGrantVersion-response-Version"></a>
New version of the grant.
Type: String

## Errors
<a name="API_CreateGrantVersion_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** AccessDeniedException **
Access to resource denied.
HTTP Status Code: 400

 ** AuthorizationException **
The AWS user account does not have permission to perform the action. Check the IAM policy associated with this account.
HTTP Status Code: 400

 ** InvalidParameterValueException **
One or more parameter values are not valid.
HTTP Status Code: 400

 ** RateLimitExceededException **
Too many requests have been submitted. Try again after a brief wait.
HTTP Status Code: 400

 ** ResourceLimitExceededException **
Your resource limits have been exceeded.
HTTP Status Code: 400

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_CreateGrantVersion_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateGrantVersion)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateGrantVersion)

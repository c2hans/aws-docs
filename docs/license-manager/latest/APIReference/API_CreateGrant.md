---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateGrant.html
---

# CreateGrant
<a name="API_CreateGrant"></a>

Creates a grant for the specified license. A grant shares the use of license entitlements with a specific AWS account, an organization, or an organizational unit (OU). For more information, see [Granted licenses in License Manager](https://docs.aws.amazon.com/license-manager/latest/userguide/granted-licenses.html) in the * AWS License Manager User Guide*.

## Request Syntax
<a name="API_CreateGrant_RequestSyntax"></a>

```
{
   "AllowedOperations": [ "{{string}}" ],
   "ClientToken": "{{string}}",
   "GrantName": "{{string}}",
   "HomeRegion": "{{string}}",
   "LicenseArn": "{{string}}",
   "Principals": [ "{{string}}" ],
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateGrant_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AllowedOperations](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-AllowedOperations"></a>
Allowed operations for the grant.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Valid Values: `CreateGrant | CheckoutLicense | CheckoutBorrowLicense | CheckInLicense | ExtendConsumptionLicense | ListPurchasedLicenses | CreateToken`
Required: Yes

 ** [ClientToken](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `\S+`
Required: Yes

 ** [GrantName](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-GrantName"></a>
Grant name.
Type: String
Required: Yes

 ** [HomeRegion](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-HomeRegion"></a>
Home Region of the grant.
Type: String
Required: Yes

 ** [LicenseArn](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-LicenseArn"></a>
Amazon Resource Name (ARN) of the license.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [Principals](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-Principals"></a>
The grant principals. You can specify one of the following as an Amazon Resource Name (ARN):
+ An AWS account, which includes only the account specified.
+ An organizational unit (OU), which includes all accounts in the OU.
+ An organization, which will include all accounts across your organization.
Type: Array of strings
Array Members: Fixed number of 1 item.
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [Tags](#API_CreateGrant_RequestSyntax) **   <a name="licensemanager-CreateGrant-request-Tags"></a>
Tags to add to the grant. For more information about tagging support in License Manager, see the [TagResource](https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TagResource.html) operation.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateGrant_ResponseSyntax"></a>

```
{
   "GrantArn": "string",
   "Status": "string",
   "Version": "string"
}
```

## Response Elements
<a name="API_CreateGrant_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [GrantArn](#API_CreateGrant_ResponseSyntax) **   <a name="licensemanager-CreateGrant-response-GrantArn"></a>
Grant ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`

 ** [Status](#API_CreateGrant_ResponseSyntax) **   <a name="licensemanager-CreateGrant-response-Status"></a>
Grant status.
Type: String
Valid Values: `PENDING_WORKFLOW | PENDING_ACCEPT | REJECTED | ACTIVE | FAILED_WORKFLOW | DELETED | PENDING_DELETE | DISABLED | WORKFLOW_COMPLETED`

 ** [Version](#API_CreateGrant_ResponseSyntax) **   <a name="licensemanager-CreateGrant-response-Version"></a>
Grant version.
Type: String

## Errors
<a name="API_CreateGrant_Errors"></a>

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
<a name="API_CreateGrant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateGrant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateGrant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

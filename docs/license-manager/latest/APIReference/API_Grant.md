---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_Grant.html
---

# Grant
<a name="API_Grant"></a>

Describes a grant.

## Contents
<a name="API_Grant_Contents"></a>

 ** GrantArn **   <a name="licensemanager-Type-Grant-GrantArn"></a>
Amazon Resource Name (ARN) of the grant.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** GrantedOperations **   <a name="licensemanager-Type-Grant-GrantedOperations"></a>
Granted operations.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 8 items.
Valid Values: `CreateGrant | CheckoutLicense | CheckoutBorrowLicense | CheckInLicense | ExtendConsumptionLicense | ListPurchasedLicenses | CreateToken`
Required: Yes

 ** GranteePrincipalArn **   <a name="licensemanager-Type-Grant-GranteePrincipalArn"></a>
The grantee principal ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** GrantName **   <a name="licensemanager-Type-Grant-GrantName"></a>
Grant name.
Type: String
Required: Yes

 ** GrantStatus **   <a name="licensemanager-Type-Grant-GrantStatus"></a>
Grant status.
Type: String
Valid Values: `PENDING_WORKFLOW | PENDING_ACCEPT | REJECTED | ACTIVE | FAILED_WORKFLOW | DELETED | PENDING_DELETE | DISABLED | WORKFLOW_COMPLETED`
Required: Yes

 ** HomeRegion **   <a name="licensemanager-Type-Grant-HomeRegion"></a>
Home Region of the grant.
Type: String
Required: Yes

 ** LicenseArn **   <a name="licensemanager-Type-Grant-LicenseArn"></a>
License ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** ParentArn **   <a name="licensemanager-Type-Grant-ParentArn"></a>
Parent ARN.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** Version **   <a name="licensemanager-Type-Grant-Version"></a>
Grant version.
Type: String
Required: Yes

 ** Options **   <a name="licensemanager-Type-Grant-Options"></a>
The options specified for the grant.
Type: [Options](API_Options.md) object
Required: No

 ** StatusReason **   <a name="licensemanager-Type-Grant-StatusReason"></a>
Grant status reason.
Type: String
Length Constraints: Maximum length of 400.
Pattern: `[\s\S]+`
Required: No

## See Also
<a name="API_Grant_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/Grant)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/Grant)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/Grant)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

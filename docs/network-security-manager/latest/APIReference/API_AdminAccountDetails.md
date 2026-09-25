---
source_url: https://docs.aws.amazon.com/network-security-manager/latest/APIReference/API_AdminAccountDetails.html
---

# AdminAccountDetails
<a name="API_AdminAccountDetails"></a>

The details of an AWS Network Security Manager administrator account.

## Contents
<a name="API_AdminAccountDetails_Contents"></a>

 ** adminAccount **   <a name="networksecuritymanager-Type-AdminAccountDetails-adminAccount"></a>
The AWS account ID of the administrator account.
Type: String
Length Constraints: Fixed length of 12.
Pattern: `(?:[0-9]{12})`
Required: Yes

 ** priority **   <a name="networksecuritymanager-Type-AdminAccountDetails-priority"></a>
The priority assigned to the administrator account.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 10.
Required: Yes

 ** adminScope **   <a name="networksecuritymanager-Type-AdminAccountDetails-adminScope"></a>
The administrative scope, which defines the accounts, organizational units, and firewall types that the administrator can manage.
Type: [AdminScope](API_AdminScope.md) object
Required: No

 ** status **   <a name="networksecuritymanager-Type-AdminAccountDetails-status"></a>
The status of the administrator account, either `ONBOARDED` or `OFFBOARDED`.
Type: String
Valid Values: `ONBOARDED | OFFBOARDED`
Required: No

## See Also
<a name="API_AdminAccountDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/network-security-manager-2025-10-30/AdminAccountDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/network-security-manager-2025-10-30/AdminAccountDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/network-security-manager-2025-10-30/AdminAccountDetails)

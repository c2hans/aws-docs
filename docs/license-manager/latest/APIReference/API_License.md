---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_License.html
---

# License
<a name="API_License"></a>

Software license that is managed in AWS License Manager.

## Contents
<a name="API_License_Contents"></a>

 ** Beneficiary **   <a name="licensemanager-Type-License-Beneficiary"></a>
License beneficiary.
Type: String
Required: No

 ** ConsumptionConfiguration **   <a name="licensemanager-Type-License-ConsumptionConfiguration"></a>
Configuration for consumption of the license.
Type: [ConsumptionConfiguration](API_ConsumptionConfiguration.md) object
Required: No

 ** CreateTime **   <a name="licensemanager-Type-License-CreateTime"></a>
License creation time.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`
Required: No

 ** Entitlements **   <a name="licensemanager-Type-License-Entitlements"></a>
License entitlements.
Type: Array of [Entitlement](API_Entitlement.md) objects
Required: No

 ** HomeRegion **   <a name="licensemanager-Type-License-HomeRegion"></a>
Home Region of the license.
Type: String
Required: No

 ** Issuer **   <a name="licensemanager-Type-License-Issuer"></a>
License issuer.
Type: [IssuerDetails](API_IssuerDetails.md) object
Required: No

 ** LicenseArn **   <a name="licensemanager-Type-License-LicenseArn"></a>
Amazon Resource Name (ARN) of the license.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** LicenseMetadata **   <a name="licensemanager-Type-License-LicenseMetadata"></a>
License metadata.
Type: Array of [Metadata](API_Metadata.md) objects
Required: No

 ** LicenseName **   <a name="licensemanager-Type-License-LicenseName"></a>
License name.
Type: String
Required: No

 ** ProductName **   <a name="licensemanager-Type-License-ProductName"></a>
Product name.
Type: String
Required: No

 ** ProductSKU **   <a name="licensemanager-Type-License-ProductSKU"></a>
Product SKU.
Type: String
Required: No

 ** Status **   <a name="licensemanager-Type-License-Status"></a>
License status.
Type: String
Valid Values: `AVAILABLE | PENDING_AVAILABLE | DEACTIVATED | SUSPENDED | EXPIRED | PENDING_DELETE | DELETED`
Required: No

 ** Validity **   <a name="licensemanager-Type-License-Validity"></a>
Date and time range during which the license is valid, in ISO8601-UTC format.
Type: [DatetimeRange](API_DatetimeRange.md) object
Required: No

 ** Version **   <a name="licensemanager-Type-License-Version"></a>
License version.
Type: String
Required: No

## See Also
<a name="API_License_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/License)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/License)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/License)

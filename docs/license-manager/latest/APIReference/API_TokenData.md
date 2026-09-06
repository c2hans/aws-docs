---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_TokenData.html
---

# TokenData
<a name="API_TokenData"></a>

Describes a token.

## Contents
<a name="API_TokenData_Contents"></a>

 ** ExpirationTime **   <a name="licensemanager-Type-TokenData-ExpirationTime"></a>
Token expiration time, in ISO8601-UTC format.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^(-?(?:[1-9][0-9]*)?[0-9]{4})-(1[0-2]|0[1-9])-(3[0-1]|0[1-9]|[1-2][0-9])T(2[0-3]|[0-1][0-9]):([0-5][0-9]):([0-5][0-9])(\.[0-9]+)?(Z|[+-](?:2[ 0-3]|[0-1][0-9]):[0-5][0-9])+$`
Required: No

 ** LicenseArn **   <a name="licensemanager-Type-TokenData-LicenseArn"></a>
Amazon Resource Name (ARN) of the license.
Type: String
Required: No

 ** RoleArns **   <a name="licensemanager-Type-TokenData-RoleArns"></a>
Amazon Resource Names (ARN) of the roles included in the token.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: No

 ** Status **   <a name="licensemanager-Type-TokenData-Status"></a>
Token status. The possible values are `AVAILABLE` and `DELETED`.
Type: String
Required: No

 ** TokenId **   <a name="licensemanager-Type-TokenData-TokenId"></a>
Token ID.
Type: String
Required: No

 ** TokenProperties **   <a name="licensemanager-Type-TokenData-TokenProperties"></a>
Data specified by the caller.
Type: Array of strings
Array Members: Maximum number of 3 items.
Required: No

 ** TokenType **   <a name="licensemanager-Type-TokenData-TokenType"></a>
Type of token generated. The supported value is `REFRESH_TOKEN`.
Type: String
Required: No

## See Also
<a name="API_TokenData_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/TokenData)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/TokenData)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/TokenData)

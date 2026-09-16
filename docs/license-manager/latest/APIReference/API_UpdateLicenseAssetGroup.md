---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_UpdateLicenseAssetGroup.html
---

# UpdateLicenseAssetGroup
<a name="API_UpdateLicenseAssetGroup"></a>

Updates a license asset group.

## Request Syntax
<a name="API_UpdateLicenseAssetGroup_RequestSyntax"></a>

```
{
   "AssociatedLicenseAssetRulesetARNs": [ "{{string}}" ],
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
   "LicenseAssetGroupArn": "{{string}}",
   "LicenseAssetGroupConfigurations": [
      {
         "UsageDimension": "{{string}}"
      }
   ],
   "Name": "{{string}}",
   "Properties": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ],
   "Status": "{{string}}"
}
```

## Request Parameters
<a name="API_UpdateLicenseAssetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociatedLicenseAssetRulesetARNs](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-AssociatedLicenseAssetRulesetARNs"></a>
ARNs of associated license asset rulesets.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [ClientToken](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: Yes

 ** [Description](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-Description"></a>
License asset group description.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [LicenseAssetGroupArn](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-LicenseAssetGroupArn"></a>
Amazon Resource Name (ARN) of the license asset group.
Type: String
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [LicenseAssetGroupConfigurations](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-LicenseAssetGroupConfigurations"></a>
License asset group configurations.
Type: Array of [LicenseAssetGroupConfiguration](API_LicenseAssetGroupConfiguration.md) objects
Required: No

 ** [Name](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-Name"></a>
License asset group name.
Type: String
Length Constraints: Maximum length of 128.
Required: No

 ** [Properties](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-Properties"></a>
License asset group properties.
Type: Array of [LicenseAssetGroupProperty](API_LicenseAssetGroupProperty.md) objects
Required: No

 ** [Status](#API_UpdateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-request-Status"></a>
License asset group status. The possible values are `ACTIVE` \| `DISABLED`.
Type: String
Valid Values: `ACTIVE | DISABLED | DELETED`
Required: No

## Response Syntax
<a name="API_UpdateLicenseAssetGroup_ResponseSyntax"></a>

```
{
   "LicenseAssetGroupArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_UpdateLicenseAssetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseAssetGroupArn](#API_UpdateLicenseAssetGroup_ResponseSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-response-LicenseAssetGroupArn"></a>
Amazon Resource Name (ARN) of the license asset group.
Type: String

 ** [Status](#API_UpdateLicenseAssetGroup_ResponseSyntax) **   <a name="licensemanager-UpdateLicenseAssetGroup-response-Status"></a>
License asset group status.
Type: String

## Errors
<a name="API_UpdateLicenseAssetGroup_Errors"></a>

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

 ** ServerInternalException **
The server experienced an internal error. Try again.
HTTP Status Code: 500

 ** ValidationException **
The provided input is not valid. Try your request again.
HTTP Status Code: 400

## See Also
<a name="API_UpdateLicenseAssetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/UpdateLicenseAssetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/UpdateLicenseAssetGroup)

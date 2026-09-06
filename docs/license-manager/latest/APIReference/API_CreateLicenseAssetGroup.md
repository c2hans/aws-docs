---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_CreateLicenseAssetGroup.html
---

# CreateLicenseAssetGroup
<a name="API_CreateLicenseAssetGroup"></a>

Creates a license asset group.

## Request Syntax
<a name="API_CreateLicenseAssetGroup_RequestSyntax"></a>

```
{
   "AssociatedLicenseAssetRulesetARNs": [ "{{string}}" ],
   "ClientToken": "{{string}}",
   "Description": "{{string}}",
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
   "Tags": [
      {
         "Key": "{{string}}",
         "Value": "{{string}}"
      }
   ]
}
```

## Request Parameters
<a name="API_CreateLicenseAssetGroup_RequestParameters"></a>

For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

The request accepts the following data in JSON format.

 ** [AssociatedLicenseAssetRulesetARNs](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-AssociatedLicenseAssetRulesetARNs"></a>
ARNs of associated license asset rulesets.
Type: Array of strings
Length Constraints: Maximum length of 2048.
Pattern: `^arn:aws[a-zA-Z-]*:[A-Za-z0-9][A-Za-z0-9_/.-]{0,62}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9_/.-]{0,63}:[A-Za-z0-9][A-Za-z0-9:_/+=,@.-]{0,1023}$`
Required: Yes

 ** [ClientToken](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-ClientToken"></a>
Unique, case-sensitive identifier that you provide to ensure the idempotency of the request.
Type: String
Required: Yes

 ** [Description](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-Description"></a>
License asset group description.
Type: String
Length Constraints: Maximum length of 1024.
Required: No

 ** [LicenseAssetGroupConfigurations](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-LicenseAssetGroupConfigurations"></a>
License asset group configurations.
Type: Array of [LicenseAssetGroupConfiguration](API_LicenseAssetGroupConfiguration.md) objects
Required: Yes

 ** [Name](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-Name"></a>
License asset group name.
Type: String
Length Constraints: Maximum length of 128.
Required: Yes

 ** [Properties](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-Properties"></a>
License asset group properties.
Type: Array of [LicenseAssetGroupProperty](API_LicenseAssetGroupProperty.md) objects
Required: No

 ** [Tags](#API_CreateLicenseAssetGroup_RequestSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-request-Tags"></a>
Tags to add to the license asset group.
Type: Array of [Tag](API_Tag.md) objects
Required: No

## Response Syntax
<a name="API_CreateLicenseAssetGroup_ResponseSyntax"></a>

```
{
   "LicenseAssetGroupArn": "string",
   "Status": "string"
}
```

## Response Elements
<a name="API_CreateLicenseAssetGroup_ResponseElements"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

 ** [LicenseAssetGroupArn](#API_CreateLicenseAssetGroup_ResponseSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-response-LicenseAssetGroupArn"></a>
Amazon Resource Name (ARN) of the license asset group.
Type: String

 ** [Status](#API_CreateLicenseAssetGroup_ResponseSyntax) **   <a name="licensemanager-CreateLicenseAssetGroup-response-Status"></a>
License asset group status.
Type: String

## Errors
<a name="API_CreateLicenseAssetGroup_Errors"></a>

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
<a name="API_CreateLicenseAssetGroup_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/license-manager-2018-08-01/CreateLicenseAssetGroup)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/CreateLicenseAssetGroup)

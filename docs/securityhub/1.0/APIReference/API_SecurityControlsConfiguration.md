---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SecurityControlsConfiguration.html
---

# SecurityControlsConfiguration
<a name="API_SecurityControlsConfiguration"></a>

 An object that defines which security controls are enabled in an AWS Security Hub CSPM configuration policy. The enablement status of a control is aligned across all of the enabled standards in an account.

## Contents
<a name="API_SecurityControlsConfiguration_Contents"></a>

 ** DisabledSecurityControlIdentifiers **   <a name="securityhub-Type-SecurityControlsConfiguration-DisabledSecurityControlIdentifiers"></a>
 A list of security controls that are disabled in the configuration policy. Security Hub CSPM enables all other controls (including newly released controls) other than the listed controls.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** EnabledSecurityControlIdentifiers **   <a name="securityhub-Type-SecurityControlsConfiguration-EnabledSecurityControlIdentifiers"></a>
 A list of security controls that are enabled in the configuration policy. Security Hub CSPM disables all other controls (including newly released controls) other than the listed controls.
Type: Array of strings
Pattern: `.*\S.*`
Required: No

 ** SecurityControlCustomParameters **   <a name="securityhub-Type-SecurityControlsConfiguration-SecurityControlCustomParameters"></a>
 A list of security controls and control parameter values that are included in a configuration policy.
Type: Array of [SecurityControlCustomParameter](API_SecurityControlCustomParameter.md) objects
Required: No

## See Also
<a name="API_SecurityControlsConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SecurityControlsConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SecurityControlsConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SecurityControlsConfiguration)

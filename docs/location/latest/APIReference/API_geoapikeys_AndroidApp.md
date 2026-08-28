---
source_url: https://docs.aws.amazon.com/location/latest/APIReference/API_geoapikeys_AndroidApp.html
---

# AndroidApp
<a name="API_geoapikeys_AndroidApp"></a>

Unique identifying information for an Android app. Consists of a package name and a 20 byte SHA-1 certificate fingerprint.

## Contents
<a name="API_geoapikeys_AndroidApp_Contents"></a>

 ** CertificateFingerprint **   <a name="location-Type-geoapikeys_AndroidApp-CertificateFingerprint"></a>
20 byte SHA-1 certificate fingerprint associated with the Android app signing certificate.
Example: `BB:0D:AC:74:D3:21:E1:43:67:71:9B:62:91:AF:A1:66:6E:44:5D:75`
Type: String
Length Constraints: Fixed length of 59.
Pattern: `([A-Fa-f0-9]{2}:){19}[A-Fa-f0-9]{2}`
Required: Yes

 ** Package **   <a name="location-Type-geoapikeys_AndroidApp-Package"></a>
Unique package name identifier for an Android app.
Example: `com.mydomain.appname`
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `([A-Za-z][A-Za-z\d_]*\.)+[A-Za-z][A-Za-z\d_]*`
Required: Yes

## See Also
<a name="API_geoapikeys_AndroidApp_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/geoapikeys-2020-11-19/AndroidApp)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/geoapikeys-2020-11-19/AndroidApp)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/geoapikeys-2020-11-19/AndroidApp)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Location Service. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query location` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

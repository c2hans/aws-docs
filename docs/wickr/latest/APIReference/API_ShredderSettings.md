---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_ShredderSettings.html
---

# ShredderSettings
<a name="API_ShredderSettings"></a>

Configuration for the Wickr shredder feature, which writes random data over free memory and disk space on client devices. You can configure your Wickr shredder intensity using the parameters below.

**Note**
Secure Shredder will not write over files that are permanently stored on the device or saved outside of the Wickr client. Wickr Network Administrators are able to disable file downloads within Security Group Settings.

## Contents
<a name="API_ShredderSettings_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** canProcessManually **   <a name="wickr-Type-ShredderSettings-canProcessManually"></a>
Specifies whether users can manually trigger the shredder to delete content.
Type: Boolean
Required: No

 ** intensity **   <a name="wickr-Type-ShredderSettings-intensity"></a>
Controls the rate (MB/minute) at which the shredder function runs on clients. Valid Values: Must be one of [0, 20, 60, 100].
A higher intensity setting could lead to higher battery usage on mobile devices.
Type: Integer
Required: No

## See Also
<a name="API_ShredderSettings_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/ShredderSettings)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/ShredderSettings)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/ShredderSettings)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

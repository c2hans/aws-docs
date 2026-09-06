---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_ProvisioningTemplateSummary.html
---

# ProvisioningTemplateSummary
<a name="API_ProvisioningTemplateSummary"></a>

A summary of information about a provisioning template.

## Contents
<a name="API_ProvisioningTemplateSummary_Contents"></a>

 ** creationDate **   <a name="iot-Type-ProvisioningTemplateSummary-creationDate"></a>
The date when the provisioning template summary was created.
Type: Timestamp
Required: No

 ** description **   <a name="iot-Type-ProvisioningTemplateSummary-description"></a>
The description of the provisioning template.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 500.
Pattern: `[^\p{C}]*`
Required: No

 ** enabled **   <a name="iot-Type-ProvisioningTemplateSummary-enabled"></a>
True if the fleet provision template is enabled, otherwise false.
Type: Boolean
Required: No

 ** lastModifiedDate **   <a name="iot-Type-ProvisioningTemplateSummary-lastModifiedDate"></a>
The date when the provisioning template summary was last modified.
Type: Timestamp
Required: No

 ** templateArn **   <a name="iot-Type-ProvisioningTemplateSummary-templateArn"></a>
The ARN of the provisioning template.
Type: String
Required: No

 ** templateName **   <a name="iot-Type-ProvisioningTemplateSummary-templateName"></a>
The name of the provisioning template.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 36.
Pattern: `^[0-9A-Za-z_-]+$`
Required: No

 ** type **   <a name="iot-Type-ProvisioningTemplateSummary-type"></a>
The type you define in a provisioning template. You can create a template with only one type. You can't change the template type after its creation. The default value is `FLEET_PROVISIONING`. For more information about provisioning template, see: [Provisioning template](https://docs.aws.amazon.com/iot/latest/developerguide/provision-template.html).
Type: String
Valid Values: `FLEET_PROVISIONING | JITP`
Required: No

## See Also
<a name="API_ProvisioningTemplateSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/ProvisioningTemplateSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/ProvisioningTemplateSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/ProvisioningTemplateSummary)

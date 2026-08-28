---
source_url: https://docs.aws.amazon.com/license-manager/latest/APIReference/API_LicenseConversionTask.html
---

# LicenseConversionTask
<a name="API_LicenseConversionTask"></a>

Information about a license type conversion task.

## Contents
<a name="API_LicenseConversionTask_Contents"></a>

 ** DestinationLicenseContext **   <a name="licensemanager-Type-LicenseConversionTask-DestinationLicenseContext"></a>
Information about the license type this conversion task converted to.
Type: [LicenseConversionContext](API_LicenseConversionContext.md) object
Required: No

 ** EndTime **   <a name="licensemanager-Type-LicenseConversionTask-EndTime"></a>
The time the conversion task was completed.
Type: Timestamp
Required: No

 ** LicenseConversionTaskId **   <a name="licensemanager-Type-LicenseConversionTask-LicenseConversionTaskId"></a>
The ID of the license type conversion task.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^lct-[a-zA-Z0-9]*`
Required: No

 ** LicenseConversionTime **   <a name="licensemanager-Type-LicenseConversionTask-LicenseConversionTime"></a>
The time the usage operation value of the resource was changed.
Type: Timestamp
Required: No

 ** ResourceArn **   <a name="licensemanager-Type-LicenseConversionTask-ResourceArn"></a>
The Amazon Resource Name (ARN) of the resource associated with the license type conversion task.
Type: String
Required: No

 ** SourceLicenseContext **   <a name="licensemanager-Type-LicenseConversionTask-SourceLicenseContext"></a>
Information about the license type this conversion task converted from.
Type: [LicenseConversionContext](API_LicenseConversionContext.md) object
Required: No

 ** StartTime **   <a name="licensemanager-Type-LicenseConversionTask-StartTime"></a>
The time the conversion task was started at.
Type: Timestamp
Required: No

 ** Status **   <a name="licensemanager-Type-LicenseConversionTask-Status"></a>
The status of the conversion task.
Type: String
Valid Values: `IN_PROGRESS | SUCCEEDED | FAILED`
Required: No

 ** StatusMessage **   <a name="licensemanager-Type-LicenseConversionTask-StatusMessage"></a>
The status message for the conversion task.
Type: String
Required: No

## See Also
<a name="API_LicenseConversionTask_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/license-manager-2018-08-01/LicenseConversionTask)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/license-manager-2018-08-01/LicenseConversionTask)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/license-manager-2018-08-01/LicenseConversionTask)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS License Manager. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query license-manager` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

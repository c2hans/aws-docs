---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_PackageVersionSummary.html
---

# PackageVersionSummary
<a name="API_PackageVersionSummary"></a>

A summary of information about a package version.

## Contents
<a name="API_PackageVersionSummary_Contents"></a>

 ** creationDate **   <a name="iot-Type-PackageVersionSummary-creationDate"></a>
The date that the package version was created.
Type: Timestamp
Required: No

 ** lastModifiedDate **   <a name="iot-Type-PackageVersionSummary-lastModifiedDate"></a>
The date that the package version was last updated.
Type: Timestamp
Required: No

 ** packageName **   <a name="iot-Type-PackageVersionSummary-packageName"></a>
The name of the associated software package.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `[a-zA-Z0-9-_.]+`
Required: No

 ** status **   <a name="iot-Type-PackageVersionSummary-status"></a>
The status of the package version. For more information, see [Package version lifecycle](https://docs.aws.amazon.com/iot/latest/developerguide/preparing-to-use-software-package-catalog.html#package-version-lifecycle).
Type: String
Valid Values: `DRAFT | PUBLISHED | DEPRECATED`
Required: No

 ** versionName **   <a name="iot-Type-PackageVersionSummary-versionName"></a>
The name of the target package version.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `[a-zA-Z0-9-_.]+`
Required: No

## See Also
<a name="API_PackageVersionSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/PackageVersionSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/PackageVersionSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/PackageVersionSummary)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

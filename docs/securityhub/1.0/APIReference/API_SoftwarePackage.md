---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwarePackage.html
---

# SoftwarePackage
<a name="API_SoftwarePackage"></a>

Information about a software package.

## Contents
<a name="API_SoftwarePackage_Contents"></a>

 ** Architecture **   <a name="securityhub-Type-SoftwarePackage-Architecture"></a>
The architecture used for the software package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Epoch **   <a name="securityhub-Type-SoftwarePackage-Epoch"></a>
The epoch of the software package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FilePath **   <a name="securityhub-Type-SoftwarePackage-FilePath"></a>
The file system path to the package manager inventory file.
Type: String
Pattern: `.*\S.*`
Required: No

 ** FixedInVersion **   <a name="securityhub-Type-SoftwarePackage-FixedInVersion"></a>
The version of the software package in which the vulnerability has been resolved.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Name **   <a name="securityhub-Type-SoftwarePackage-Name"></a>
The name of the software package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** PackageManager **   <a name="securityhub-Type-SoftwarePackage-PackageManager"></a>
The source of the package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Release **   <a name="securityhub-Type-SoftwarePackage-Release"></a>
The release of the software package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Remediation **   <a name="securityhub-Type-SoftwarePackage-Remediation"></a>
Describes the actions a customer can take to resolve the vulnerability in the software package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceLayerArn **   <a name="securityhub-Type-SoftwarePackage-SourceLayerArn"></a>
The Amazon Resource Name (ARN) of the source layer.
Type: String
Pattern: `.*\S.*`
Required: No

 ** SourceLayerHash **   <a name="securityhub-Type-SoftwarePackage-SourceLayerHash"></a>
The source layer hash of the vulnerable package.
Type: String
Pattern: `.*\S.*`
Required: No

 ** Version **   <a name="securityhub-Type-SoftwarePackage-Version"></a>
The version of the software package.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SoftwarePackage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwarePackage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwarePackage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwarePackage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Security Hub. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query securityhub` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

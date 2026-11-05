---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_SoftwareResult.html
---

# SoftwareResult
<a name="API_SoftwareResult"></a>

Provides information about a software package installed on one or more of your resources.

## Contents
<a name="API_SoftwareResult_Contents"></a>

 ** PackageName **   <a name="securityhub-Type-SoftwareResult-PackageName"></a>
The name of the software package.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** PackageType **   <a name="securityhub-Type-SoftwareResult-PackageType"></a>
The type of the software package, for example `operating-system`, `application`, or `library`.
Type: String
Pattern: `.*\S.*`
Required: Yes

 ** ResourceCount **   <a name="securityhub-Type-SoftwareResult-ResourceCount"></a>
The number of resources that contain this software package. To list these resources, call `GetSoftwareResourcesV2`.
Type: Integer
Required: Yes

 ** PackageVersion **   <a name="securityhub-Type-SoftwareResult-PackageVersion"></a>
The version of the software package.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_SoftwareResult_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/SoftwareResult)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/SoftwareResult)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/SoftwareResult)

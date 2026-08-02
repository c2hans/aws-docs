---
source_url: https://docs.aws.amazon.com/inspector/v2/APIReference/API_EcrRepositoryMetadata.html
---

# EcrRepositoryMetadata
<a name="API_EcrRepositoryMetadata"></a>

Information on the Amazon ECR repository metadata associated with a finding.

## Contents
<a name="API_EcrRepositoryMetadata_Contents"></a>

 ** name **   <a name="inspector2-Type-EcrRepositoryMetadata-name"></a>
The name of the Amazon ECR repository.
Type: String
Required: No

 ** scanFrequency **   <a name="inspector2-Type-EcrRepositoryMetadata-scanFrequency"></a>
The frequency of scans.
Type: String
Valid Values: `MANUAL | SCAN_ON_PUSH | CONTINUOUS_SCAN`
Required: No

## See Also
<a name="API_EcrRepositoryMetadata_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/inspector2-2020-06-08/EcrRepositoryMetadata)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/inspector2-2020-06-08/EcrRepositoryMetadata)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/inspector2-2020-06-08/EcrRepositoryMetadata)

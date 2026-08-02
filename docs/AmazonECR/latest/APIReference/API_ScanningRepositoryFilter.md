---
source_url: https://docs.aws.amazon.com/AmazonECR/latest/APIReference/API_ScanningRepositoryFilter.html
---

# ScanningRepositoryFilter
<a name="API_ScanningRepositoryFilter"></a>

The details of a scanning repository filter. For more information on how to use filters, see [Using filters](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html#image-scanning-filters) in the *Amazon Elastic Container Registry User Guide*.

## Contents
<a name="API_ScanningRepositoryFilter_Contents"></a>

 ** filter **   <a name="ECR-Type-ScanningRepositoryFilter-filter"></a>
The filter to use when scanning.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-z0-9*](?:[._\-/a-z0-9*]?[a-z0-9*]+)*$`
Required: Yes

 ** filterType **   <a name="ECR-Type-ScanningRepositoryFilter-filterType"></a>
The type associated with the filter.
Type: String
Valid Values: `WILDCARD`
Required: Yes

## See Also
<a name="API_ScanningRepositoryFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecr-2015-09-21/ScanningRepositoryFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecr-2015-09-21/ScanningRepositoryFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecr-2015-09-21/ScanningRepositoryFilter)

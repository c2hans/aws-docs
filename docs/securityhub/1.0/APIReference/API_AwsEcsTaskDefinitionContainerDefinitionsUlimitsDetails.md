---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails.html
---

# AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails"></a>

A ulimit to set in the container.

## Contents
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails_Contents"></a>

 ** HardLimit **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails-HardLimit"></a>
The hard limit for the ulimit type.
Type: Integer
Required: No

 ** Name **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails-Name"></a>
The type of the ulimit. Valid values are as follows:
+  `core`
+  `cpu`
+  `data`
+  `fsize`
+  `locks`
+  `memlock`
+  `msgqueue`
+  `nice`
+  `nofile`
+  `nproc`
+  `rss`
+  `rtprio`
+  `rttime`
+  `sigpending`
+  `stack`
Type: String
Pattern: `.*\S.*`
Required: No

 ** SoftLimit **   <a name="securityhub-Type-AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails-SoftLimit"></a>
The soft limit for the ulimit type.
Type: Integer
Required: No

## See Also
<a name="API_AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsEcsTaskDefinitionContainerDefinitionsUlimitsDetails)

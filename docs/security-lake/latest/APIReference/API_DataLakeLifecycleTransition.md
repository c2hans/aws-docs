---
source_url: https://docs.aws.amazon.com/security-lake/latest/APIReference/API_DataLakeLifecycleTransition.html
---

# DataLakeLifecycleTransition
<a name="API_DataLakeLifecycleTransition"></a>

Provide transition lifecycle details of Amazon Security Lake object.

## Contents
<a name="API_DataLakeLifecycleTransition_Contents"></a>

 ** days **   <a name="securitylake-Type-DataLakeLifecycleTransition-days"></a>
Number of days before data transitions to a different S3 Storage Class in the Amazon Security Lake object.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** storageClass **   <a name="securitylake-Type-DataLakeLifecycleTransition-storageClass"></a>
The range of storage classes that you can choose from based on the data access, resiliency, and cost requirements of your workloads.
Type: String
Required: No

## See Also
<a name="API_DataLakeLifecycleTransition_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securitylake-2018-05-10/DataLakeLifecycleTransition)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securitylake-2018-05-10/DataLakeLifecycleTransition)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securitylake-2018-05-10/DataLakeLifecycleTransition)

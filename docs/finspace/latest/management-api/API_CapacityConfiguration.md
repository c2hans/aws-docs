---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_CapacityConfiguration.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# CapacityConfiguration
<a name="API_CapacityConfiguration"></a>

A structure for the metadata of a cluster. It includes information like the CPUs needed, memory of instances, and number of instances.

## Contents
<a name="API_CapacityConfiguration_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** nodeCount **   <a name="finspace-Type-CapacityConfiguration-nodeCount"></a>
The number of instances running in a cluster.
Type: Integer
Valid Range: Minimum value of 1.
Required: No

 ** nodeType **   <a name="finspace-Type-CapacityConfiguration-nodeType"></a>
The type that determines the hardware of the host computer used for your cluster instance. Each node type offers different memory and storage capabilities. Choose a node type based on the requirements of the application or software that you plan to run on your instance.
You can only specify one of the following values:
+  `kx.s.large` – The node type with a configuration of 12 GiB memory and 2 vCPUs.
+  `kx.s.xlarge` – The node type with a configuration of 27 GiB memory and 4 vCPUs.
+  `kx.s.2xlarge` – The node type with a configuration of 54 GiB memory and 8 vCPUs.
+  `kx.s.4xlarge` – The node type with a configuration of 108 GiB memory and 16 vCPUs.
+  `kx.s.8xlarge` – The node type with a configuration of 216 GiB memory and 32 vCPUs.
+  `kx.s.16xlarge` – The node type with a configuration of 432 GiB memory and 64 vCPUs.
+  `kx.s.32xlarge` – The node type with a configuration of 864 GiB memory and 128 vCPUs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 32.
Pattern: `^[a-zA-Z0-9._]+$`
Required: No

## See Also
<a name="API_CapacityConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/CapacityConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/CapacityConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/CapacityConfiguration)

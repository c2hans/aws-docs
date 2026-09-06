---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxNode.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxNode
<a name="API_KxNode"></a>

A structure that stores metadata for a kdb node.

## Contents
<a name="API_KxNode_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** availabilityZoneId **   <a name="finspace-Type-KxNode-availabilityZoneId"></a>
The identifier of the availability zones where subnets for the environment are created.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** launchTime **   <a name="finspace-Type-KxNode-launchTime"></a>
The time when a particular node is started. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** nodeId **   <a name="finspace-Type-KxNode-nodeId"></a>
A unique identifier for the node.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 40.
Required: No

 ** status **   <a name="finspace-Type-KxNode-status"></a>
 Specifies the status of the cluster nodes.
+  `RUNNING` – The node is actively serving.
+  `PROVISIONING` – The node is being prepared.
Type: String
Valid Values: `RUNNING | PROVISIONING`
Required: No

## See Also
<a name="API_KxNode_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxNode)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxNode)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxNode)

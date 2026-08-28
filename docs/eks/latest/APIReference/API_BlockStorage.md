---
source_url: https://docs.aws.amazon.com/eks/latest/APIReference/API_BlockStorage.html
---

# BlockStorage
<a name="API_BlockStorage"></a>

Indicates the current configuration of the block storage capability on your EKS Auto Mode cluster. For example, if the capability is enabled or disabled. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account. For more information, see EKS Auto Mode block storage capability in the *Amazon EKS User Guide*.

## Contents
<a name="API_BlockStorage_Contents"></a>

 ** enabled **   <a name="AmazonEKS-Type-BlockStorage-enabled"></a>
Indicates if the block storage capability is enabled on your EKS Auto Mode cluster. If the block storage capability is enabled, EKS Auto Mode will create and delete EBS volumes in your AWS account.
Type: Boolean
Required: No

## See Also
<a name="API_BlockStorage_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/eks-2017-11-01/BlockStorage)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/eks-2017-11-01/BlockStorage)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/eks-2017-11-01/BlockStorage)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EKS. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query eks` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

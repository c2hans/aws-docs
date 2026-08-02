---
source_url: https://docs.aws.amazon.com/datapipeline/latest/APIReference/API_InstanceIdentity.html
---

# InstanceIdentity
<a name="API_InstanceIdentity"></a>

Identity information for the EC2 instance that is hosting the task runner. You can get this value by calling a metadata URI from the EC2 instance. For more information, see [Instance Metadata](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AESDG-chapter-instancedata.html) in the *Amazon Elastic Compute Cloud User Guide.* Passing in this value proves that your task runner is running on an EC2 instance, and ensures the proper AWS Data Pipeline service charges are applied to your pipeline.

## Contents
<a name="API_InstanceIdentity_Contents"></a>

 ** document **   <a name="DP-Type-InstanceIdentity-document"></a>
A description of an EC2 instance that is generated when the instance is launched and exposed to the instance via the instance metadata service in the form of a JSON representation of an object.
Type: String
Required: No

 ** signature **   <a name="DP-Type-InstanceIdentity-signature"></a>
A signature which can be used to verify the accuracy and authenticity of the information provided in the instance identity document.
Type: String
Required: No

## See Also
<a name="API_InstanceIdentity_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/datapipeline-2012-10-29/InstanceIdentity)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/datapipeline-2012-10-29/InstanceIdentity)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/datapipeline-2012-10-29/InstanceIdentity)

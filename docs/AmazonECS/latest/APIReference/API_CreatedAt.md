---
source_url: https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_CreatedAt.html
---

# CreatedAt
<a name="API_CreatedAt"></a>

The optional filter to narrow the `ListServiceDeployment` results.

 If you do not specify a value, service deployments that were created before the current time are included in the result.

## Contents
<a name="API_CreatedAt_Contents"></a>

 ** after **   <a name="ECS-Type-CreatedAt-after"></a>
Include service deployments in the result that were created after this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

 ** before **   <a name="ECS-Type-CreatedAt-before"></a>
Include service deployments in the result that were created before this time. The format is yyyy-MM-dd HH:mm:ss.SSSSSS.
Type: Timestamp
Required: No

## See Also
<a name="API_CreatedAt_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ecs-2014-11-13/CreatedAt)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ecs-2014-11-13/CreatedAt)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ecs-2014-11-13/CreatedAt)

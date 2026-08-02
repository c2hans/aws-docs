---
source_url: https://docs.aws.amazon.com/snowball/latest/api-reference/API_DependentService.html
---

# DependentService
<a name="API_DependentService"></a>

**Note**
 AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/) for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/) for secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/).

The name and version of the service dependant on the requested service.

## Contents
<a name="API_DependentService_Contents"></a>

 ** ServiceName **   <a name="Snowball-Type-DependentService-ServiceName"></a>
The name of the dependent service.
Type: String
Valid Values: `KUBERNETES | EKS_ANYWHERE`
Required: No

 ** ServiceVersion **   <a name="Snowball-Type-DependentService-ServiceVersion"></a>
The version of the dependent service.
Type: [ServiceVersion](API_ServiceVersion.md) object
Required: No

## See Also
<a name="API_DependentService_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/snowball-2016-06-30/DependentService)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/snowball-2016-06-30/DependentService)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/snowball-2016-06-30/DependentService)

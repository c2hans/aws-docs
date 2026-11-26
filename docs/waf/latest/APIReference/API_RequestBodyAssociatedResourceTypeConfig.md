---
source_url: https://docs.aws.amazon.com/waf/latest/APIReference/API_RequestBodyAssociatedResourceTypeConfig.html
---

# RequestBodyAssociatedResourceTypeConfig

Customizes the maximum size of the request body that your protected Application Load Balancer, CloudFront, API Gateway, Amazon Cognito, App Runner, Verified Access, and Elastic Load Balancing for Envoy resources forward to AWS WAF for inspection. The default size is 8 KB (8,192 bytes) for Application Load Balancer and 16 KB (16,384 bytes) for the other resource types. You can change the setting for any of the available resource types.

**Note**
You are charged additional fees when your protected resources forward body sizes that are larger than the default. For more information, see [AWS WAF Pricing](http://aws.amazon.com/waf/pricing/).

Example JSON: ` { "API_GATEWAY": "KB_48", "APP_RUNNER_SERVICE": "KB_32", "APPLICATION_LOAD_BALANCER": "KB_16" }`

For AWS AppSync, the limit is fixed at 8 KB (8,192 bytes).

This is used in the `AssociationConfig` of the web ACL.

## Contents
<a name="API_RequestBodyAssociatedResourceTypeConfig_Contents"></a>

 ** DefaultSizeInspectionLimit **   <a name="WAF-Type-RequestBodyAssociatedResourceTypeConfig-DefaultSizeInspectionLimit"></a>
Specifies the maximum size of the web request body component that an associated Application Load Balancer, CloudFront, API Gateway, Amazon Cognito, App Runner, Verified Access, or Elastic Load Balancing for Envoy resource should send to AWS WAF for inspection. This applies to statements in the web ACL that inspect the body or JSON body.
You can specify `KB_8` only for Application Load Balancer, with the `APPLICATION_LOAD_BALANCER` resource type.
Default: `8 KB (8,192 bytes)` for Application Load Balancer and `16 KB (16,384 bytes)` for the other resource types
Type: String
Valid Values: `KB_8 | KB_16 | KB_32 | KB_48 | KB_64`
Required: Yes

## See Also
<a name="API_RequestBodyAssociatedResourceTypeConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wafv2-2019-07-29/RequestBodyAssociatedResourceTypeConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wafv2-2019-07-29/RequestBodyAssociatedResourceTypeConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wafv2-2019-07-29/RequestBodyAssociatedResourceTypeConfig)

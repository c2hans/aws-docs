---
source_url: https://docs.aws.amazon.com/firehose/latest/APIReference/API_DatabaseSourceVPCConfiguration.html
---

# DatabaseSourceVPCConfiguration
<a name="API_DatabaseSourceVPCConfiguration"></a>

 The structure for details of the VPC Endpoint Service which Firehose uses to create a PrivateLink to the database.

Amazon Data Firehose is in preview release and is subject to change.

## Contents
<a name="API_DatabaseSourceVPCConfiguration_Contents"></a>

 ** VpcEndpointServiceName **   <a name="Firehose-Type-DatabaseSourceVPCConfiguration-VpcEndpointServiceName"></a>
 The VPC endpoint service name which Firehose uses to create a PrivateLink to the database. The endpoint service must have the Firehose service principle `firehose.amazonaws.com` as an allowed principal on the VPC endpoint service. The VPC endpoint service name is a string that looks like `com.amazonaws.vpce.<region>.<vpc-endpoint-service-id>`.
Amazon Data Firehose is in preview release and is subject to change.
Type: String
Length Constraints: Minimum length of 47. Maximum length of 255.
Pattern: `([a-zA-Z0-9\-\_]+\.){2,3}vpce\.[a-zA-Z0-9\-]*\.vpce-svc\-[a-zA-Z0-9\-]{17}$`
Required: Yes

## See Also
<a name="API_DatabaseSourceVPCConfiguration_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/firehose-2015-08-04/DatabaseSourceVPCConfiguration)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/firehose-2015-08-04/DatabaseSourceVPCConfiguration)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/firehose-2015-08-04/DatabaseSourceVPCConfiguration)

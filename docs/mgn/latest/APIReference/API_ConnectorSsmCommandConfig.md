---
source_url: https://docs.aws.amazon.com/mgn/latest/APIReference/API_ConnectorSsmCommandConfig.html
---

# ConnectorSsmCommandConfig
<a name="API_ConnectorSsmCommandConfig"></a>

Connector SSM command config.

## Contents
<a name="API_ConnectorSsmCommandConfig_Contents"></a>

 ** cloudWatchOutputEnabled **   <a name="mgn-Type-ConnectorSsmCommandConfig-cloudWatchOutputEnabled"></a>
Connector SSM command config CloudWatch output enabled.
Type: Boolean
Required: Yes

 ** s3OutputEnabled **   <a name="mgn-Type-ConnectorSsmCommandConfig-s3OutputEnabled"></a>
Connector SSM command config S3 output enabled.
Type: Boolean
Required: Yes

 ** cloudWatchLogGroupName **   <a name="mgn-Type-ConnectorSsmCommandConfig-cloudWatchLogGroupName"></a>
Connector SSM command config CloudWatch log group name.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `[\.\-_/#A-Za-z0-9]+`
Required: No

 ** outputS3BucketName **   <a name="mgn-Type-ConnectorSsmCommandConfig-outputS3BucketName"></a>
Connector SSM command config output S3 bucket name.
Type: String
Pattern: `[a-zA-Z0-9.\-_]{1,255}`
Required: No

## See Also
<a name="API_ConnectorSsmCommandConfig_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/mgn-2020-02-26/ConnectorSsmCommandConfig)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/mgn-2020-02-26/ConnectorSsmCommandConfig)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/mgn-2020-02-26/ConnectorSsmCommandConfig)

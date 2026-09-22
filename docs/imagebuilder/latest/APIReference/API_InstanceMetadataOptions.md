---
source_url: https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_InstanceMetadataOptions.html
---

# InstanceMetadataOptions
<a name="API_InstanceMetadataOptions"></a>

The instance metadata service (IMDS) settings that Image Builder applies to the EC2 build and test instances it launches. These settings control how software on those instances retrieves instance metadata and IAM role credentials.

## Contents
<a name="API_InstanceMetadataOptions_Contents"></a>

 ** httpPutResponseHopLimit **   <a name="imagebuilder-Type-InstanceMetadataOptions-httpPutResponseHopLimit"></a>
Limit the number of hops that an instance metadata request can traverse to reach its destination. If you don't set a value, the EC2 launch default for the instance applies. If HTTP tokens are required, container image builds need a minimum of two hops.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 64.
Required: No

 ** httpTokens **   <a name="imagebuilder-Type-InstanceMetadataOptions-httpTokens"></a>
Indicates whether a signed token header is required for instance metadata retrieval requests. The values affect the response as follows:
+  **required** – When you retrieve the IAM role credentials, version 2.0 credentials are returned in all cases.
+  **optional** – You can include a signed token header in your request to retrieve instance metadata, or you can leave it out. If you include it, version 2.0 credentials are returned for the IAM role. Otherwise, version 1.0 credentials are returned.
If you don't set a value, the EC2 launch default applies to the build and test instances. That default depends on the base AMI and any account-level instance metadata defaults. For more information, see [Configure the instance metadata options](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configuring-instance-metadata-options.html) in the * *Amazon EC2 User Guide* *.
Type: String
Pattern: `optional|required`
Required: No

## See Also
<a name="API_InstanceMetadataOptions_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/imagebuilder-2019-12-02/InstanceMetadataOptions)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/imagebuilder-2019-12-02/InstanceMetadataOptions)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/imagebuilder-2019-12-02/InstanceMetadataOptions)

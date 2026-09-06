---
source_url: https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPointPolicyInput.html
---

# PutMultiRegionAccessPointPolicyInput
<a name="API_control_PutMultiRegionAccessPointPolicyInput"></a>

A container for the information associated with a [PutMultiRegionAccessPoint](https://docs.aws.amazon.com/AmazonS3/latest/API/API_control_PutMultiRegionAccessPoint.html) request.

## Contents
<a name="API_control_PutMultiRegionAccessPointPolicyInput_Contents"></a>

 ** Name **   <a name="AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Name"></a>
The name of the Multi-Region Access Point associated with the request.
Type: String
Length Constraints: Maximum length of 50.
Pattern: `^[a-z0-9][-a-z0-9]{1,48}[a-z0-9]$`
Required: Yes

 ** Policy **   <a name="AmazonS3-Type-control_PutMultiRegionAccessPointPolicyInput-Policy"></a>
The policy details for the `PutMultiRegionAccessPoint` request.
Type: String
Required: Yes

## See Also
<a name="API_control_PutMultiRegionAccessPointPolicyInput_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/s3control-2018-08-20/PutMultiRegionAccessPointPolicyInput)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/s3control-2018-08-20/PutMultiRegionAccessPointPolicyInput)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/s3control-2018-08-20/PutMultiRegionAccessPointPolicyInput)

---
source_url: https://docs.aws.amazon.com/drs/latest/APIReference/API_StagingSourceServer.html
---

# StagingSourceServer
<a name="API_StagingSourceServer"></a>

Source server in staging account that extended source server connected to.

## Contents
<a name="API_StagingSourceServer_Contents"></a>

 ** arn **   <a name="drs-Type-StagingSourceServer-arn"></a>
The ARN of the source server.
Type: String
Length Constraints: Minimum length of 20. Maximum length of 2048.
Pattern: `arn:(?:[0-9a-zA-Z_-]+:){3}([0-9]{12,}):source-server/(s-[0-9a-zA-Z]{17})`
Required: No

 ** hostname **   <a name="drs-Type-StagingSourceServer-hostname"></a>
Hostname of staging source server.
Type: String
Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

 ** tags **   <a name="drs-Type-StagingSourceServer-tags"></a>
A list of tags associated with the staging source server.
Type: String to string map
Key Length Constraints: Minimum length of 0. Maximum length of 256.
Value Length Constraints: Minimum length of 0. Maximum length of 256.
Required: No

## See Also
<a name="API_StagingSourceServer_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/drs-2020-02-26/StagingSourceServer)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/drs-2020-02-26/StagingSourceServer)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/drs-2020-02-26/StagingSourceServer)

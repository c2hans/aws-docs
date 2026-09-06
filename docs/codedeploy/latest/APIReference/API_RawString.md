---
source_url: https://docs.aws.amazon.com/codedeploy/latest/APIReference/API_RawString.html
---

# RawString
<a name="API_RawString"></a>

 *This data type has been deprecated.*

A revision for an AWS Lambda deployment that is a YAML-formatted or JSON-formatted string. For AWS Lambda deployments, the revision is the same as the AppSpec file.

## Contents
<a name="API_RawString_Contents"></a>

 ** content **   <a name="CodeDeploy-Type-RawString-content"></a>
The YAML-formatted or JSON-formatted revision string. It includes information about which Lambda function to update and optional Lambda functions that validate deployment lifecycle events.
Type: String
Required: No

 ** sha256 **   <a name="CodeDeploy-Type-RawString-sha256"></a>
The SHA256 hash value of the revision content.
Type: String
Required: No

## See Also
<a name="API_RawString_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/codedeploy-2014-10-06/RawString)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/codedeploy-2014-10-06/RawString)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/codedeploy-2014-10-06/RawString)

---
source_url: https://docs.aws.amazon.com/elasticloadbalancing/2012-06-01/APIReference/API_BackendServerDescription.html
---

# BackendServerDescription
<a name="API_BackendServerDescription"></a>

Information about the configuration of an EC2 instance.

## Contents
<a name="API_BackendServerDescription_Contents"></a>

 ** InstancePort **
The port on which the EC2 instance is listening.
Type: Integer
Valid Range: Minimum value of 1. Maximum value of 65535.
Required: No

 ** PolicyNames.member.N **
The names of the policies enabled for the EC2 instance.
Type: Array of strings
Required: No

## See Also
<a name="API_BackendServerDescription_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticloadbalancing-2012-06-01/BackendServerDescription)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticloadbalancing-2012-06-01/BackendServerDescription)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticloadbalancing-2012-06-01/BackendServerDescription)

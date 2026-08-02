---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_InstanceCredentials.html
---

# InstanceCredentials
<a name="API_InstanceCredentials"></a>

A set of credentials that allow remote access to an instance in an EC2 managed fleet. These credentials are returned in response to a call to [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetInstanceAccess), which requests access for instances that are running game servers with the Amazon GameLift Servers server SDK version 4.x or earlier.

## Contents
<a name="API_InstanceCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Secret **   <a name="gameliftservers-Type-InstanceCredentials-Secret"></a>
Secret string. For Windows instances, the secret is a password for use with Windows Remote Desktop. For Linux instances, it's a private key for use with SSH.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** UserName **   <a name="gameliftservers-Type-InstanceCredentials-UserName"></a>
A user name for logging in.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_InstanceCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/InstanceCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/InstanceCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/InstanceCredentials)

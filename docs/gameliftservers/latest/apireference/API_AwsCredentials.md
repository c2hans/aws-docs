---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_AwsCredentials.html
---

# AwsCredentials
<a name="API_AwsCredentials"></a>

 AWS account security credentials that allow interactions with Amazon GameLift Servers resources. The credentials are temporary and valid for a limited time span. You can request fresh credentials at any time.

 AWS security credentials consist of three parts: an access key ID, a secret access key, and a session token. You must use all three parts together to authenticate your access requests.

You need AWS credentials for the following tasks:
+ To upload a game server build directly to Amazon GameLift Servers S3 storage using `CreateBuild`. To get access for this task, call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_RequestUploadCredentials.html).
+ To remotely connect to an active Amazon GameLift Servers fleet instances. To get remote access, call [https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess.html](https://docs.aws.amazon.com/gamelift/latest/apireference/API_GetComputeAccess.html).

## Contents
<a name="API_AwsCredentials_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AccessKeyId **   <a name="gameliftservers-Type-AwsCredentials-AccessKeyId"></a>
The access key ID that identifies the temporary security credentials.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** SecretAccessKey **   <a name="gameliftservers-Type-AwsCredentials-SecretAccessKey"></a>
The secret access key that can be used to sign requests.
Type: String
Length Constraints: Minimum length of 1.
Required: No

 ** SessionToken **   <a name="gameliftservers-Type-AwsCredentials-SessionToken"></a>
The token that users must pass to the service API to use the temporary credentials.
Type: String
Length Constraints: Minimum length of 1.
Required: No

## See Also
<a name="API_AwsCredentials_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/AwsCredentials)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/AwsCredentials)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/AwsCredentials)

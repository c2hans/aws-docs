---
source_url: https://docs.aws.amazon.com/ground-station/latest/APIReference/API_SecurityDetails.html
---

# SecurityDetails
<a name="API_SecurityDetails"></a>

Information about endpoints.

## Contents
<a name="API_SecurityDetails_Contents"></a>

 ** roleArn **   <a name="groundstation-Type-SecurityDetails-roleArn"></a>
ARN to a role needed for connecting streams to your instances.
Type: String
Length Constraints: Minimum length of 30. Maximum length of 165.
Pattern: `arn:[a-z0-9-.]{1,63}:iam::[0-9]{12}:role/[\w+=,.@-]{1,64}`
Required: Yes

 ** securityGroupIds **   <a name="groundstation-Type-SecurityDetails-securityGroupIds"></a>
The security groups to attach to the elastic network interfaces.
Type: Array of strings
Required: Yes

 ** subnetIds **   <a name="groundstation-Type-SecurityDetails-subnetIds"></a>
A list of subnets where AWS Ground Station places elastic network interfaces to send streams to your instances.
Type: Array of strings
Required: Yes

## See Also
<a name="API_SecurityDetails_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/groundstation-2019-05-23/SecurityDetails)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/groundstation-2019-05-23/SecurityDetails)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/groundstation-2019-05-23/SecurityDetails)

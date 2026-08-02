---
source_url: https://docs.aws.amazon.com/securityhub/1.0/APIReference/API_AwsApiCallAction.html
---

# AwsApiCallAction
<a name="API_AwsApiCallAction"></a>

Provided if `ActionType` is `AWS_API_CALL`. It provides details about the API call that was detected.

## Contents
<a name="API_AwsApiCallAction_Contents"></a>

 ** AffectedResources **   <a name="securityhub-Type-AwsApiCallAction-AffectedResources"></a>
Identifies the resources that were affected by the API call.
Type: String to string map
Key Pattern: `.*\S.*`
Value Pattern: `.*\S.*`
Required: No

 ** Api **   <a name="securityhub-Type-AwsApiCallAction-Api"></a>
The name of the API method that was issued.
Length Constraints: 128.
Type: String
Pattern: `.*\S.*`
Required: No

 ** CallerType **   <a name="securityhub-Type-AwsApiCallAction-CallerType"></a>
Indicates whether the API call originated from a remote IP address (`remoteip`) or from a DNS domain (`domain`).
Type: String
Pattern: `.*\S.*`
Required: No

 ** DomainDetails **   <a name="securityhub-Type-AwsApiCallAction-DomainDetails"></a>
Provided if `CallerType` is `domain`. Provides information about the DNS domain that the API call originated from.
Type: [AwsApiCallActionDomainDetails](API_AwsApiCallActionDomainDetails.md) object
Required: No

 ** FirstSeen **   <a name="securityhub-Type-AwsApiCallAction-FirstSeen"></a>
A timestamp that indicates when the API call was first observed.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** LastSeen **   <a name="securityhub-Type-AwsApiCallAction-LastSeen"></a>
A timestamp that indicates when the API call was most recently observed.
For more information about the validation and formatting of timestamp fields in AWS Security Hub CSPM, see [Timestamps](https://docs.aws.amazon.com/securityhub/1.0/APIReference/Welcome.html#timestamps).
Type: String
Pattern: `.*\S.*`
Required: No

 ** RemoteIpDetails **   <a name="securityhub-Type-AwsApiCallAction-RemoteIpDetails"></a>
Provided if `CallerType` is `remoteip`. Provides information about the remote IP address that the API call originated from.
Type: [ActionRemoteIpDetails](API_ActionRemoteIpDetails.md) object
Required: No

 ** ServiceName **   <a name="securityhub-Type-AwsApiCallAction-ServiceName"></a>
The name of the AWS service that the API method belongs to.
Length Constraints: 128.
Type: String
Pattern: `.*\S.*`
Required: No

## See Also
<a name="API_AwsApiCallAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/securityhub-2018-10-26/AwsApiCallAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/securityhub-2018-10-26/AwsApiCallAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/securityhub-2018-10-26/AwsApiCallAction)

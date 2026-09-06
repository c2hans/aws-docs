---
source_url: https://docs.aws.amazon.com/guardduty/latest/APIReference/API_AwsApiCallAction.html
---

# AwsApiCallAction
<a name="API_AwsApiCallAction"></a>

Contains information about the API action.

## Contents
<a name="API_AwsApiCallAction_Contents"></a>

 ** affectedResources **   <a name="guardduty-Type-AwsApiCallAction-affectedResources"></a>
The details of the AWS account that made the API call. This field identifies the resources that were affected by this API call.
Type: String to string map
Required: No

 ** api **   <a name="guardduty-Type-AwsApiCallAction-api"></a>
The AWS API name.
Type: String
Required: No

 ** callerType **   <a name="guardduty-Type-AwsApiCallAction-callerType"></a>
The AWS API caller type.
Type: String
Required: No

 ** domainDetails **   <a name="guardduty-Type-AwsApiCallAction-domainDetails"></a>
The domain information for the AWS API call.
Type: [DomainDetails](API_DomainDetails.md) object
Required: No

 ** errorCode **   <a name="guardduty-Type-AwsApiCallAction-errorCode"></a>
The error code of the failed AWS API action.
Type: String
Required: No

 ** remoteAccountDetails **   <a name="guardduty-Type-AwsApiCallAction-remoteAccountDetails"></a>
The details of the AWS account that made the API call. This field appears if the call was made from outside your account.
Type: [RemoteAccountDetails](API_RemoteAccountDetails.md) object
Required: No

 ** remoteIpDetails **   <a name="guardduty-Type-AwsApiCallAction-remoteIpDetails"></a>
The remote IP information of the connection that initiated the AWS API call.
Type: [RemoteIpDetails](API_RemoteIpDetails.md) object
Required: No

 ** serviceName **   <a name="guardduty-Type-AwsApiCallAction-serviceName"></a>
The AWS service name whose API was invoked.
Type: String
Required: No

 ** userAgent **   <a name="guardduty-Type-AwsApiCallAction-userAgent"></a>
The agent through which the API request was made.
Type: String
Required: No

## See Also
<a name="API_AwsApiCallAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/guardduty-2017-11-28/AwsApiCallAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/guardduty-2017-11-28/AwsApiCallAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/guardduty-2017-11-28/AwsApiCallAction)

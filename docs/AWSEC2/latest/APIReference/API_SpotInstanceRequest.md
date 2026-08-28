---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_SpotInstanceRequest.html
---

# SpotInstanceRequest
<a name="API_SpotInstanceRequest"></a>

Describes a Spot Instance request.

## Contents
<a name="API_SpotInstanceRequest_Contents"></a>

 ** actualBlockHourlyPrice **
Deprecated.
Type: String
Required: No

 ** availabilityZoneGroup **
The Availability Zone group. If you specify the same Availability Zone group for all Spot Instance requests, all Spot Instances are launched in the same Availability Zone.
Type: String
Required: No

 ** blockDurationMinutes **
Deprecated.
Type: Integer
Required: No

 ** createTime **
The date and time when the Spot Instance request was created, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z).
Type: Timestamp
Required: No

 ** fault **
The fault codes for the Spot Instance request, if any.
Type: [SpotInstanceStateFault](API_SpotInstanceStateFault.md) object
Required: No

 ** instanceId **
The instance ID, if an instance has been launched to fulfill the Spot Instance request.
Type: String
Required: No

 ** instanceInterruptionBehavior **
The behavior when a Spot Instance is interrupted.
Type: String
Valid Values: `hibernate | stop | terminate`
Required: No

 ** launchedAvailabilityZone **
The Availability Zone in which the request is launched.
Either `launchedAvailabilityZone` or `launchedAvailabilityZoneId` can be specified, but not both
Type: String
Required: No

 ** launchedAvailabilityZoneId **
The ID of the Availability Zone in which the request is launched.
Either `launchedAvailabilityZone` or `launchedAvailabilityZoneId` can be specified, but not both
Type: String
Required: No

 ** launchGroup **
The instance launch group. Launch groups are Spot Instances that launch together and terminate together.
Type: String
Required: No

 ** launchSpecification **
Additional information for launching instances.
Type: [LaunchSpecification](API_LaunchSpecification.md) object
Required: No

 ** productDescription **
The product description associated with the Spot Instance.
Type: String
Valid Values: `Linux/UNIX | Linux/UNIX (Amazon VPC) | Windows | Windows (Amazon VPC)`
Required: No

 ** spotInstanceRequestId **
The ID of the Spot Instance request.
Type: String
Required: No

 ** spotPrice **
The maximum price per unit hour that you are willing to pay for a Spot Instance. We do not recommend using this parameter because it can lead to increased interruptions. If you do not specify this parameter, you will pay the current Spot price.
If you specify a maximum price, your instances will be interrupted more frequently than if you do not specify this parameter.
Type: String
Required: No

 ** state **
The state of the Spot Instance request. Spot request status information helps track your Spot Instance requests. For more information, see [Spot request status](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-request-status.html) in the *Amazon EC2 User Guide*.
Type: String
Valid Values: `open | active | closed | cancelled | failed`
Required: No

 ** status **
The status code and status message describing the Spot Instance request.
Type: [SpotInstanceStatus](API_SpotInstanceStatus.md) object
Required: No

 ** TagSet.N **
Any tags assigned to the resource.
Type: Array of [Tag](API_Tag.md) objects
Required: No

 ** type **
The Spot Instance request type.
Type: String
Valid Values: `one-time | persistent`
Required: No

 ** validFrom **
The start date of the request, in UTC format (for example, *YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z). The request becomes active at this date and time.
Type: Timestamp
Required: No

 ** validUntil **
The end date of the request, in UTC format (*YYYY*-*MM*-*DD*T*HH*:*MM*:*SS*Z).
+ For a persistent request, the request remains active until the `validUntil` date and time is reached. Otherwise, the request remains active until you cancel it.
+ For a one-time request, the request remains active until all instances launch, the request is canceled, or the `validUntil` date and time is reached. By default, the request is valid for 7 days from the date the request was created.
Type: Timestamp
Required: No

## See Also
<a name="API_SpotInstanceRequest_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/SpotInstanceRequest)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/SpotInstanceRequest)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/SpotInstanceRequest)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

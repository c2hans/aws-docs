---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_EC2InstanceCounts.html
---

# EC2InstanceCounts
<a name="API_EC2InstanceCounts"></a>

Resource capacity settings. Fleet capacity is measured in Amazon EC2 instances. Pending and terminating counts are non-zero when the fleet capacity is adjusting to a scaling event or if access to resources is temporarily affected.

## Contents
<a name="API_EC2InstanceCounts_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ACTIVE **   <a name="gameliftservers-Type-EC2InstanceCounts-ACTIVE"></a>
Actual number of instances that are ready to host game sessions.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** DESIRED **   <a name="gameliftservers-Type-EC2InstanceCounts-DESIRED"></a>
Requested number of active instances. Amazon GameLift Servers takes action as needed to maintain the desired number of instances. Capacity is scaled up or down by changing the desired instances. A change in the desired instances value can take up to 1 minute to be reflected when viewing a fleet's capacity settings.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** IDLE **   <a name="gameliftservers-Type-EC2InstanceCounts-IDLE"></a>
Number of active instances that are not currently hosting a game session.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MAXIMUM **   <a name="gameliftservers-Type-EC2InstanceCounts-MAXIMUM"></a>
The maximum instance count value allowed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** MINIMUM **   <a name="gameliftservers-Type-EC2InstanceCounts-MINIMUM"></a>
The minimum instance count value allowed.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** PENDING **   <a name="gameliftservers-Type-EC2InstanceCounts-PENDING"></a>
Number of instances that are starting but not yet active.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** TERMINATING **   <a name="gameliftservers-Type-EC2InstanceCounts-TERMINATING"></a>
Number of instances that are no longer active but haven't yet been terminated.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_EC2InstanceCounts_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/EC2InstanceCounts)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/EC2InstanceCounts)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/EC2InstanceCounts)

---
source_url: https://docs.aws.amazon.com/gameliftservers/latest/apireference/API_FleetUtilization.html
---

# FleetUtilization
<a name="API_FleetUtilization"></a>

Current resource utilization statistics in a specified fleet or location. The location value might refer to a fleet's remote location or its home region.

## Contents
<a name="API_FleetUtilization_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** ActiveGameSessionCount **   <a name="gameliftservers-Type-FleetUtilization-ActiveGameSessionCount"></a>
The number of active game sessions that are currently being hosted across all instances in the fleet location.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** ActiveServerProcessCount **   <a name="gameliftservers-Type-FleetUtilization-ActiveServerProcessCount"></a>
The number of server processes in `ACTIVE` status that are currently running across all instances in the fleet location.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** CurrentPlayerSessionCount **   <a name="gameliftservers-Type-FleetUtilization-CurrentPlayerSessionCount"></a>
The number of active player sessions that are currently being hosted across all instances in the fleet location.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

 ** FleetArn **   <a name="gameliftservers-Type-FleetUtilization-FleetArn"></a>
The Amazon Resource Name ([ARN](https://docs.aws.amazon.com/AmazonS3/latest/dev/s3-arn-format.html)) that is assigned to a Amazon GameLift Servers fleet resource and uniquely identifies it. ARNs are unique across all Regions. Format is `arn:aws:gamelift:<region>::fleet/fleet-a1234567-b8c9-0d1e-2fa3-b45c6d7e8912`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 512.
Pattern: `^arn:.*:[a-z]*fleet\/[a-z]*fleet-[a-zA-Z0-9\-]+$`
Required: No

 ** FleetId **   <a name="gameliftservers-Type-FleetUtilization-FleetId"></a>
A unique identifier for the fleet associated with the location.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Pattern: `^[a-z]*fleet-[a-zA-Z0-9\-]+`
Required: No

 ** Location **   <a name="gameliftservers-Type-FleetUtilization-Location"></a>
The fleet location for the fleet utilization information, expressed as an AWS Region code, such as `us-west-2`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[A-Za-z0-9\-]+`
Required: No

 ** MaximumPlayerSessionCount **   <a name="gameliftservers-Type-FleetUtilization-MaximumPlayerSessionCount"></a>
The maximum number of players allowed across all game sessions that are currently being hosted across all instances in the fleet location.
Type: Integer
Valid Range: Minimum value of 0.
Required: No

## See Also
<a name="API_FleetUtilization_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/gamelift-2015-10-01/FleetUtilization)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/gamelift-2015-10-01/FleetUtilization)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/gamelift-2015-10-01/FleetUtilization)

---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_GetCapacityManagerSupportabilityScores.html
---

# GetCapacityManagerSupportabilityScores

 Scores how well each instance type and Availability Zone combination can support a capacity request, based on current Amazon EC2 capacity. The response includes a score for each combination and an aggregate score for all combinations in the request. This action doesn't launch or reserve instances, and a score doesn't guarantee that a later launch will succeed.

 Call this action in the Region where you turned on Capacity Manager. A single request can include Availability Zones in any Region. Real-time supportability checks are available only to AWS Support customers on the Unified Operations plan.

For more information, see [Check supportability](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/capacity-manager-supportability.html) in the *Amazon EC2 User Guide*.

## Request Parameters
<a name="API_GetCapacityManagerSupportabilityScores_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **CapacityAmount**
 The amount of capacity that you need, in the unit that you specify for `CapacityUnit`. Each score is relative to this amount.
Type: Integer
Valid Range: Minimum value of 1.
Required: Yes

 **CapacityAvailabilityZoneId.N**
 The IDs of the Availability Zones to score, such as `use1-az1`. You can specify Availability Zones in different Regions. You can specify up to 10 Availability Zones.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 10 items.
Required: Yes

 **CapacityUnit**
 The unit for `CapacityAmount`.
Type: String
Valid Values: `vcpus | instances`
Required: Yes

 **DryRun**
 Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceRequirementsWithMetadata**
 The attributes that the instance types must have, such as vCPU and memory ranges. Capacity Manager resolves the attributes into matching instance types and scores each one.
 Specify either `InstanceTypes` or `InstanceRequirementsWithMetadata`, but not both.
Type: [InstanceRequirementsWithMetadataRequest](API_InstanceRequirementsWithMetadataRequest.md) object
Required: No

 **InstanceType.N**
 The instance types to score. You can specify up to 50 instance types.
 Specify either `InstanceTypes` or `InstanceRequirementsWithMetadata`, but not both.
Type: Array of strings
Array Members: Minimum number of 0 items. Maximum number of 50 items.
Required: No

 **MarketType**
 The capacity market to score.
Type: String
Valid Values: `on-demand | spot`
Required: Yes

## Response Elements
<a name="API_GetCapacityManagerSupportabilityScores_ResponseElements"></a>

The following elements are returned by the service.

 **aggregateScore**
 The score for all instance type and Availability Zone combinations in the request together. A `high` aggregate score with lower individual scores means that no single combination can support the full request, but the combinations together can.
Type: String
Valid Values: `high | medium | low`

 **capacityManagerSupportabilityScoreSet**
 The score for each instance type and Availability Zone combination in the request.
Type: Array of [CapacityManagerSupportabilityScore](API_CapacityManagerSupportabilityScore.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_GetCapacityManagerSupportabilityScores_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_GetCapacityManagerSupportabilityScores_Examples"></a>

### Example
<a name="API_GetCapacityManagerSupportabilityScores_Example_1"></a>

This example scores three instance types in one Availability Zone for a request of 50 On-Demand Instances.

#### Sample Request
<a name="API_GetCapacityManagerSupportabilityScores_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=GetCapacityManagerSupportabilityScores
&MarketType=on-demand
&CapacityAmount=50
&CapacityUnit=instances
&CapacityAvailabilityZoneId.1=use1-az1
&InstanceType.1=c6g.xlarge
&InstanceType.2=c7g.xlarge
&InstanceType.3=m6g.xlarge
&AUTHPARAMS
```

#### Sample Response
<a name="API_GetCapacityManagerSupportabilityScores_Example_1_Response"></a>

```
<GetCapacityManagerSupportabilityScoresResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>d4904fd9-82c2-4ea5-adfe-a9cc3EXAMPLE</requestId>
    <aggregateScore>high</aggregateScore>
    <capacityManagerSupportabilityScoreSet>
        <item>
            <instanceType>c6g.xlarge</instanceType>
            <availabilityZoneId>use1-az1</availabilityZoneId>
            <score>high</score>
        </item>
        <item>
            <instanceType>c7g.xlarge</instanceType>
            <availabilityZoneId>use1-az1</availabilityZoneId>
            <score>high</score>
        </item>
        <item>
            <instanceType>m6g.xlarge</instanceType>
            <availabilityZoneId>use1-az1</availabilityZoneId>
            <score>medium</score>
        </item>
    </capacityManagerSupportabilityScoreSet>
</GetCapacityManagerSupportabilityScoresResponse>
```

## See Also
<a name="API_GetCapacityManagerSupportabilityScores_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/GetCapacityManagerSupportabilityScores)

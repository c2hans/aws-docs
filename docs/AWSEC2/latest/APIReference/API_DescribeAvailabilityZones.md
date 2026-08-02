---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html
---

# DescribeAvailabilityZones
<a name="API_DescribeAvailabilityZones"></a>

Describes the Availability Zones, Local Zones, and Wavelength Zones that are available to you.

For more information about Availability Zones, Local Zones, and Wavelength Zones, see [Regions and zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the *Amazon EC2 User Guide*.

**Note**
The order of the elements in the response, including those within nested structures, might vary. Applications should not assume the elements appear in a particular order.

## Request Parameters
<a name="API_DescribeAvailabilityZones_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **AllAvailabilityZones**
Include all Availability Zones, Local Zones, and Wavelength Zones regardless of your opt-in status.
If you do not use this parameter, the results include only the zones for the Regions where you have chosen the option to opt in.
Type: Boolean
Required: No

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **Filter.N**
The filters.
+  `group-long-name` - The long name of the zone group for the Availability Zone (for example, `US West (Oregon) 1`), the Local Zone (for example, for Zone group `us-west-2-lax-1`, it is `US West (Los Angeles)`, or the Wavelength Zone (for example, for Zone group `us-east-1-wl1`, it is `US East (Verizon)`.
+  `group-name` - The name of the zone group for the Availability Zone (for example, `us-east-1-zg-1`), the Local Zone (for example, `us-west-2-lax-1`), or the Wavelength Zone (for example, `us-east-1-wl1`).
+  `message` - The Zone message.
+  `opt-in-status` - The opt-in status (`opted-in` \| `not-opted-in` \| `opt-in-not-required`).
+  `parent-zone-id` - The ID of the zone that handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls.
+  `parent-zone-name` - The ID of the zone that handles some of the Local Zone and Wavelength Zone control plane operations, such as API calls.
+  `region-name` - The name of the Region for the Zone (for example, `us-east-1`).
+  `state` - The state of the Availability Zone, the Local Zone, or the Wavelength Zone (`available` \| `unavailable` \| `constrained`).
+  `zone-id` - The ID of the Availability Zone (for example, `use1-az1`), the Local Zone (for example, `usw2-lax1-az1`), or the Wavelength Zone (for example, `us-east-1-wl1-bos-wlz-1`).
+  `zone-name` - The name of the Availability Zone (for example, `us-east-1a`), the Local Zone (for example, `us-west-2-lax-1a`), or the Wavelength Zone (for example, `us-east-1-wl1-bos-wlz-1`).
+  `zone-type` - The type of zone (`availability-zone` \| `local-zone` \| `wavelength-zone`).
Type: Array of [Filter](API_Filter.md) objects
Required: No

 **ZoneId.N**
The IDs of the Availability Zones, Local Zones, and Wavelength Zones.
Type: Array of strings
Required: No

 **ZoneName.N**
The names of the Availability Zones, Local Zones, and Wavelength Zones.
Type: Array of strings
Required: No

## Response Elements
<a name="API_DescribeAvailabilityZones_ResponseElements"></a>

The following elements are returned by the service.

 **availabilityZoneInfo**
Information about the Availability Zones, Local Zones, and Wavelength Zones.
Type: Array of [AvailabilityZone](API_AvailabilityZone.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_DescribeAvailabilityZones_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## Examples
<a name="API_DescribeAvailabilityZones_Examples"></a>

### Example
<a name="API_DescribeAvailabilityZones_Example_1"></a>

This example request describes the zones in the current Region that are enabled for your account.

#### Sample Request
<a name="API_DescribeAvailabilityZones_Example_1_Request"></a>

```
https://ec2.amazonaws.com/?Action=DescribeAvailabilityZones
&AUTHPARAMS
```

#### Sample Response
<a name="API_DescribeAvailabilityZones_Example_1_Response"></a>

```
<DescribeAvailabilityZonesResponse xmlns="http://ec2.amazonaws.com/doc/2016-11-15/">
    <requestId>e23c5a54-a29c-43ee-8b55-0c13c26e9e01</requestId>
    <availabilityZoneInfo>
        <item>
            <groupName>us-west-2-zg-1</groupName>
            <optInStatus>opt-in-not-required</optInStatus>
            <zoneName>us-west-2a</zoneName>
            <zoneId>usw2-az1</zoneId>
            <zoneState>available</zoneState>
            <zoneType>availability-zone</zoneType>
            <regionName>us-west-2</regionName>
            <messageSet/>
            <networkBorderGroup>us-west-2</networkBorderGroup>
            <groupLongName>US West (Oregon) 1</groupLongName>
            <geographySet>
                <item>
                    <name>United States of America</name>
                </item>
            </geographySet>
            <subGeographySet>
                <item>
                    <name>Oregon</name>
                </item>
            </subGeographySet>
        </item>
        <item>
            <groupName>us-west-2-zg-1</groupName>
            <optInStatus>opt-in-not-required</optInStatus>
            <zoneName>us-west-2b</zoneName>
            <zoneId>usw2-az2</zoneId>
            <zoneState>available</zoneState>
            <zoneType>availability-zone</zoneType>
            <regionName>us-west-2</regionName>
            <messageSet/>
            <networkBorderGroup>us-west-2</networkBorderGroup>
            <groupLongName>US West (Oregon) 1</groupLongName>
            <geographySet>
                <item>
                    <name>United States of America</name>
                </item>
            </geographySet>
            <subGeographySet>
                <item>
                    <name>Oregon</name>
                </item>
            </subGeographySet>
        </item>
        <item>
            <groupName>us-west-2-zg-1</groupName>
            <optInStatus>opt-in-not-required</optInStatus>
            <zoneName>us-west-2c</zoneName>
            <zoneId>usw2-az3</zoneId>
            <zoneState>available</zoneState>
            <zoneType>availability-zone</zoneType>
            <regionName>us-west-2</regionName>
            <messageSet/>
            <networkBorderGroup>us-west-2</networkBorderGroup>
            <groupLongName>US West (Oregon) 1</groupLongName>
            <geographySet>
                <item>
                    <name>United States of America</name>
                </item>
            </geographySet>
            <subGeographySet>
                <item>
                    <name>Oregon</name>
                </item>
            </subGeographySet>
        </item>
        <item>
            <groupName>us-west-2-zg-1</groupName>
            <optInStatus>opt-in-not-required</optInStatus>
            <zoneName>us-west-2d</zoneName>
            <zoneId>usw2-az4</zoneId>
            <zoneState>available</zoneState>
            <zoneType>availability-zone</zoneType>
            <regionName>us-west-2</regionName>
            <messageSet/>
            <networkBorderGroup>us-west-2</networkBorderGroup>
            <groupLongName>US West (Oregon) 1</groupLongName>
            <geographySet>
                <item>
                    <name>United States of America</name>
                </item>
            </geographySet>
            <subGeographySet>
                <item>
                    <name>Oregon</name>
                </item>
            </subGeographySet>
        </item>
    </availabilityZoneInfo>
</DescribeAvailabilityZonesResponse>
```

## See Also
<a name="API_DescribeAvailabilityZones_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/DescribeAvailabilityZones)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DescribeAvailabilityZones)

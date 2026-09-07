---
source_url: https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/using-regions-and-availability-zones.html
---

Version 4 (V4) of the AWS SDK for .NET has been released\!

For information about breaking changes and migrating your applications, see the [migration topic](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html).

 [![Orange button with text "Click here for details".](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/images/BannerButton_less-round.png)](https://docs.aws.amazon.com/sdk-for-net/v4/developer-guide/net-dg-v4.html)

# Seeing your Amazon EC2 Regions and Availability Zones
<a name="using-regions-and-availability-zones"></a>

Amazon EC2 is hosted in multiple locations worldwide. These locations are composed of Regions and Availability Zones. Each Region is a separate geographic area that has multiple, isolated locations known as Availability Zones.

To read more about Regions and Availability Zones, see [Regions and Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the [Amazon EC2 User Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/).

This example shows you how to use the AWS SDK for .NET to get details about the Regions and Availability Zones related to an EC2 client. The application displays lists of the Regions and Availability Zones available to an EC2 client.

## SDK references
<a name="w2aac19c15c21c17b9b1"></a>

NuGet packages:
+ [AWSSDK.EC2](https://www.nuget.org/packages/AWSSDK.EC2)

Programming elements:
+ Namespace [Amazon.EC2](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/NEC2.html)

  Class [AmazonEC2Client](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TEC2Client.html)
+ Namespace [Amazon.EC2.Model](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/NEC2Model.html)

  Class [DescribeAvailabilityZonesResponse](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TDescribeAvailabilityZonesResponse.html)

  Class [DescribeRegionsResponse](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TDescribeRegionsResponse.html)

  Class [AvailabilityZone](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TAvailabilityZone.html)

  Class [Region](https://docs.aws.amazon.com/sdkfornet/v4/apidocs/items/EC2/TRegion.html)

```
using System;
using System.Threading.Tasks;
using Amazon.EC2;
using Amazon.EC2.Model;

namespace EC2RegionsAndZones
{
  class Program
  {
    static async Task Main(string[] args)
    {
      Console.WriteLine(
        "Finding the Regions and Availability Zones available to an EC2 client...");

      // Create the EC2 client
      var ec2Client = new AmazonEC2Client();

      // Display the Regions and Availability Zones
      await DescribeRegions(ec2Client);
      await DescribeAvailabilityZones(ec2Client);
    }

    //
    // Method to display Regions
    private static async Task DescribeRegions(IAmazonEC2 ec2Client)
    {
      Console.WriteLine("\nRegions that are enabled for the EC2 client:");
      DescribeRegionsResponse response = await ec2Client.DescribeRegionsAsync();
      foreach (Region region in response.Regions)
        Console.WriteLine(region.RegionName);
    }

    //
    // Method to display Availability Zones
    private static async Task DescribeAvailabilityZones(IAmazonEC2 ec2Client)
    {
      Console.WriteLine("\nAvailability Zones for the EC2 client's region:");
      DescribeAvailabilityZonesResponse response =
        await ec2Client.DescribeAvailabilityZonesAsync();
      foreach (AvailabilityZone az in response.AvailabilityZones)
        Console.WriteLine(az.ZoneName);
    }
  }
}
```

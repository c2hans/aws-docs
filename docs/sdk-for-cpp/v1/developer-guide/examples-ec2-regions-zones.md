---
source_url: https://docs.aws.amazon.com/sdk-for-cpp/v1/developer-guide/examples-ec2-regions-zones.html
---

# Using Regions and Availability Zones for Amazon EC2
<a name="examples-ec2-regions-zones"></a>

## Prerequisites
<a name="codeExamplePrereq"></a>

Before you begin, we recommend you read [Getting started using the AWS SDK for C\+\+](getting-started.md).

Download the example code and build the solution as described in [Getting started on code examples](getting-started-code-examples.md).

To run the examples, the user profile your code uses to make the requests must have proper permissions in AWS (for the service and the action). For more information, see [Providing AWS credentials](credentials.md).

## Describe Regions
<a name="describe-regions"></a>

To list the AWS Regions available to your AWS account, call the EC2Client’s `DescribeRegions` function with a [DescribeRegionsRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-ec2/html/class_aws_1_1_e_c2_1_1_model_1_1_describe_regions_request.html).

You will receive a [DescribeRegionsResponse](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-ec2/html/class_aws_1_1_e_c2_1_1_model_1_1_describe_regions_response.html) in the outcome object. Call its `GetRegions` function to get a list of [Region](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-ec2/html/class_aws_1_1_e_c2_1_1_model_1_1_region.html) objects that represent each Region.

 **Includes**

```
#include <aws/ec2/EC2Client.h>
#include <aws/ec2/model/DescribeRegionsRequest.h>
```

 **Code**

```
    Aws::EC2::EC2Client ec2Client(clientConfiguration);

    Aws::EC2::Model::DescribeRegionsRequest request;
    Aws::EC2::Model::DescribeRegionsOutcome outcome = ec2Client.DescribeRegions(request);
    if (outcome.IsSuccess()) {
        std::cout << std::left <<
                  std::setw(32) << "RegionName" <<
                  std::setw(64) << "Endpoint" << std::endl;

        const auto &regions = outcome.GetResult().GetRegions();
        for (const auto &region: regions) {
            std::cout << std::left <<
                      std::setw(32) << region.GetRegionName() <<
                      std::setw(64) << region.GetEndpoint() << std::endl;
        }
    } else {
        std::cerr << "Failed to describe regions:" <<
                  outcome.GetError().GetMessage() << std::endl;
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/ec2/describe_regions_and_zones.cpp).

## Describe Availability Zones
<a name="describe-availability-zones"></a>

To list each availability zone available to your account, call the EC2Client’s `DescribeAvailabilityZones` function with a [DescribeAvailabilityZonesRequest](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-ec2/html/class_aws_1_1_e_c2_1_1_model_1_1_describe_availability_zones_request.html).

You will receive a [DescribeAvailabilityZonesResponse](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-ec2/html/class_aws_1_1_e_c2_1_1_model_1_1_describe_availability_zones_response.html) in the outcome object. Call its `GetAvailabilityZones` function to get a list of [AvailabilityZone](https://docs.aws.amazon.com/sdk-for-cpp/latest/api/aws-cpp-sdk-ec2/html/class_aws_1_1_e_c2_1_1_model_1_1_availability_zone.html) objects that represent each availability zone.

 **Includes**

```
#include <aws/ec2/model/DescribeAvailabilityZonesRequest.h>
```

 **Code**

```
    Aws::EC2::Model::DescribeAvailabilityZonesRequest request;
    Aws::EC2::Model::DescribeAvailabilityZonesOutcome outcome = ec2Client.DescribeAvailabilityZones(request);

    if (outcome.IsSuccess()) {
        std::cout << std::left <<
                  std::setw(32) << "ZoneName" <<
                  std::setw(20) << "State" <<
                  std::setw(32) << "Region" << std::endl;

        const auto &zones =
                outcome.GetResult().GetAvailabilityZones();

        for (const auto &zone: zones) {
            Aws::String stateString =
                    Aws::EC2::Model::AvailabilityZoneStateMapper::GetNameForAvailabilityZoneState(
                            zone.GetState());
            std::cout << std::left <<
                      std::setw(32) << zone.GetZoneName() <<
                      std::setw(20) << stateString <<
                      std::setw(32) << zone.GetRegionName() << std::endl;
        }
    } else {
        std::cerr << "Failed to describe availability zones:" <<
                  outcome.GetError().GetMessage() << std::endl;

    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/ec2/describe_regions_and_zones.cpp).

## More Information
<a name="more-information"></a>
+  [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the Amazon EC2 User Guide
+  [DescribeRegions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html) in the Amazon EC2 API Reference
+  [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) in the Amazon EC2 API Reference

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for C++. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-cpp` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

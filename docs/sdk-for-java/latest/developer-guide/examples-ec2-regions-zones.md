---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2-regions-zones.html
---

# Use AWS Regions and Availability Zones
<a name="examples-ec2-regions-zones"></a>

## Describe Regions
<a name="describe-regions"></a>

To list the Regions available to your account, call the Ec2Client’s `describeRegions` method. It returns a [DescribeRegionsResponse](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/DescribeRegionsResponse.html). Call the returned object’s `regions` method to get a list of [Region](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/Region.html) objects that represent each Region.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeRegionsResponse;
import software.amazon.awssdk.services.ec2.model.DescribeAvailabilityZonesResponse;
import java.util.concurrent.CompletableFuture;
```

 **Code**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeRegionsResponse;
import software.amazon.awssdk.services.ec2.model.DescribeAvailabilityZonesResponse;
import java.util.concurrent.CompletableFuture;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DescribeRegionsAndZones {
    public static void main(String[] args) {
        Ec2AsyncClient ec2AsyncClient = Ec2AsyncClient.builder()
            .region(Region.US_EAST_1)
            .build();

        try {
            CompletableFuture<Void> future = describeEC2RegionsAndZonesAsync(ec2AsyncClient);
            future.join(); // Wait for both async operations to complete.
        } catch (RuntimeException rte) {
            System.err.println("An exception occurred: " + (rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage()));
        }
    }

    /**
     * Asynchronously describes the EC2 regions and availability zones.
     *
     * @param ec2AsyncClient the EC2 async client used to make the API calls
     * @return a {@link CompletableFuture} that completes when both the region and availability zone descriptions are complete
     */
    public static CompletableFuture<Void> describeEC2RegionsAndZonesAsync(Ec2AsyncClient ec2AsyncClient) {
        // Initiate the asynchronous request to describe regions
        CompletableFuture<DescribeRegionsResponse> regionsResponse = ec2AsyncClient.describeRegions();

        // Handle the response or exception for regions
        CompletableFuture<DescribeRegionsResponse> regionsFuture = regionsResponse.whenComplete((regionsResp, ex) -> {
            if (ex != null) {
                // Handle the exception by throwing a RuntimeException
                throw new RuntimeException("Failed to describe EC2 regions.", ex);
            } else if (regionsResp == null || regionsResp.regions().isEmpty()) {
                // Throw an exception if the response is null or the result is empty
                throw new RuntimeException("No EC2 regions found.");
            } else {
                // Process the response if no exception occurred and the result is not empty
                regionsResp.regions().forEach(region -> {
                    System.out.printf(
                        "Found Region %s with endpoint %s%n",
                        region.regionName(),
                        region.endpoint());
                });
            }
        });

        CompletableFuture<DescribeAvailabilityZonesResponse> zonesResponse = ec2AsyncClient.describeAvailabilityZones();
        CompletableFuture<DescribeAvailabilityZonesResponse> zonesFuture = zonesResponse.whenComplete((zonesResp, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to describe EC2 availability zones.", ex);
            } else if (zonesResp == null || zonesResp.availabilityZones().isEmpty()) {
                throw new RuntimeException("No EC2 availability zones found.");
            } else {
                zonesResp.availabilityZones().forEach(zone -> {
                    System.out.printf(
                        "Found Availability Zone %s with status %s in region %s%n",
                        zone.zoneName(),
                        zone.state(),
                        zone.regionName()
                    );
                });
            }
        });

        return CompletableFuture.allOf(regionsFuture, zonesFuture);
    }
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/7486a1a092aa8e16a21698ef26f9d524fef62e55/javav2/example_code/ec2/src/main/java/com/example/ec2/DescribeRegionsAndZones.java) on GitHub.

## Describe availability zones
<a name="describe-availability-zones"></a>

To list each Availability Zone available to your account, call the Ec2Client’s `describeAvailabilityZones` method. It returns a [DescribeAvailabilityZonesResponse](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/DescribeAvailabilityZonesResponse.html). Call its `availabilityZones` method to get a list of [AvailabilityZone](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/AvailabilityZone.html) objects that represent each Availability Zone.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeRegionsResponse;
import software.amazon.awssdk.services.ec2.model.DescribeAvailabilityZonesResponse;
import java.util.concurrent.CompletableFuture;
```

 **Code**

Create the Ec2Client.

```
        Ec2AsyncClient ec2AsyncClient = Ec2AsyncClient.builder()
            .region(Region.US_EAST_1)
            .build();
```

Then call describeAvailabilityZones() and retrieve results.

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeRegionsResponse;
import software.amazon.awssdk.services.ec2.model.DescribeAvailabilityZonesResponse;
import java.util.concurrent.CompletableFuture;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DescribeRegionsAndZones {
    public static void main(String[] args) {
        Ec2AsyncClient ec2AsyncClient = Ec2AsyncClient.builder()
            .region(Region.US_EAST_1)
            .build();

        try {
            CompletableFuture<Void> future = describeEC2RegionsAndZonesAsync(ec2AsyncClient);
            future.join(); // Wait for both async operations to complete.
        } catch (RuntimeException rte) {
            System.err.println("An exception occurred: " + (rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage()));
        }
    }

    /**
     * Asynchronously describes the EC2 regions and availability zones.
     *
     * @param ec2AsyncClient the EC2 async client used to make the API calls
     * @return a {@link CompletableFuture} that completes when both the region and availability zone descriptions are complete
     */
    public static CompletableFuture<Void> describeEC2RegionsAndZonesAsync(Ec2AsyncClient ec2AsyncClient) {
        // Initiate the asynchronous request to describe regions
        CompletableFuture<DescribeRegionsResponse> regionsResponse = ec2AsyncClient.describeRegions();

        // Handle the response or exception for regions
        CompletableFuture<DescribeRegionsResponse> regionsFuture = regionsResponse.whenComplete((regionsResp, ex) -> {
            if (ex != null) {
                // Handle the exception by throwing a RuntimeException
                throw new RuntimeException("Failed to describe EC2 regions.", ex);
            } else if (regionsResp == null || regionsResp.regions().isEmpty()) {
                // Throw an exception if the response is null or the result is empty
                throw new RuntimeException("No EC2 regions found.");
            } else {
                // Process the response if no exception occurred and the result is not empty
                regionsResp.regions().forEach(region -> {
                    System.out.printf(
                        "Found Region %s with endpoint %s%n",
                        region.regionName(),
                        region.endpoint());
                });
            }
        });

        CompletableFuture<DescribeAvailabilityZonesResponse> zonesResponse = ec2AsyncClient.describeAvailabilityZones();
        CompletableFuture<DescribeAvailabilityZonesResponse> zonesFuture = zonesResponse.whenComplete((zonesResp, ex) -> {
            if (ex != null) {
                throw new RuntimeException("Failed to describe EC2 availability zones.", ex);
            } else if (zonesResp == null || zonesResp.availabilityZones().isEmpty()) {
                throw new RuntimeException("No EC2 availability zones found.");
            } else {
                zonesResp.availabilityZones().forEach(zone -> {
                    System.out.printf(
                        "Found Availability Zone %s with status %s in region %s%n",
                        zone.zoneName(),
                        zone.state(),
                        zone.regionName()
                    );
                });
            }
        });

        return CompletableFuture.allOf(regionsFuture, zonesFuture);
    }
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/7486a1a092aa8e16a21698ef26f9d524fef62e55/javav2/example_code/ec2/src/main/java/com/example/ec2/DescribeRegionsAndZones.java) on GitHub.

## Describe accounts
<a name="describe-accounts"></a>

To list EC2-related information about your account, call the Ec2Client’s `describeAccountAttributes` method. This method returns a [DescribeAccountAttributesResponse](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/DescribeAccountAttributesResponse.html) object. Invoke this objects `accountAttributes` method to get a list of [AccountAttribute](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/AccountAttribute.html) objects. You can iterate through the list to retrieve an `AccountAttribute` object.

You can get your account’s attribute values by invoking the `AccountAttribute` object’s `attributeValues` method. This method returns a list of [AccountAttributeValue](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/AccountAttributeValue.html) objects. You can iterate through this second list to display the value of attributes (see the following code example).

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeAccountAttributesResponse;
import java.util.concurrent.CompletableFuture;
```

 **Code**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2AsyncClient;
import software.amazon.awssdk.services.ec2.model.DescribeAccountAttributesResponse;
import java.util.concurrent.CompletableFuture;

/**
 * Before running this Java V2 code example, set up your development
 * environment, including your credentials.
 *
 * For more information, see the following documentation topic:
 *
 * https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/get-started.html
 */
public class DescribeAccount {
    public static void main(String[] args) {
        Ec2AsyncClient ec2AsyncClient = Ec2AsyncClient.builder()
            .region(Region.US_EAST_1)
            .build();

        try {
            CompletableFuture<DescribeAccountAttributesResponse> future = describeEC2AccountAsync(ec2AsyncClient);
            future.join();
            System.out.println("EC2 Account attributes described successfully.");
        } catch (RuntimeException rte) {
            System.err.println("An exception occurred: " + (rte.getCause() != null ? rte.getCause().getMessage() : rte.getMessage()));
        }
    }

    /**
     * Describes the EC2 account attributes asynchronously.
     *
     * @param ec2AsyncClient the EC2 asynchronous client to use for the operation
     * @return a {@link CompletableFuture} containing the {@link DescribeAccountAttributesResponse} with the account attributes
     */
    public static CompletableFuture<DescribeAccountAttributesResponse> describeEC2AccountAsync(Ec2AsyncClient ec2AsyncClient) {
        CompletableFuture<DescribeAccountAttributesResponse> response = ec2AsyncClient.describeAccountAttributes();
        return response.whenComplete((accountResults, ex) -> {
            if (ex != null) {
                // Handle the exception by throwing a RuntimeException.
                throw new RuntimeException("Failed to describe EC2 account attributes.", ex);
            } else if (accountResults == null || accountResults.accountAttributes().isEmpty()) {
                // Throw an exception if the response is null or no account attributes are found.
                throw new RuntimeException("No account attributes found.");
            } else {
                // Process the response if no exception occurred.
                accountResults.accountAttributes().forEach(attribute -> {
                    System.out.println("\nThe name of the attribute is " + attribute.attributeName());
                    attribute.attributeValues().forEach(
                        myValue -> System.out.println("The value of the attribute is " + myValue.attributeValue()));
                });
            }
        });
    }
}
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/7486a1a092aa8e16a21698ef26f9d524fef62e55/javav2/example_code/ec2/src/main/java/com/example/ec2/DescribeAccount.java) on GitHub.

## More information
<a name="more-information"></a>
+  [Regions and Availability Zones](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html) in the Amazon EC2 User Guide for Linux Instances
+  [DescribeRegions](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeRegions.html) in the Amazon EC2 API Reference
+  [DescribeAvailabilityZones](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeAvailabilityZones.html) in the Amazon EC2 API Reference

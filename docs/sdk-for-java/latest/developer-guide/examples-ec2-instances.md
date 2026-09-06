---
source_url: https://docs.aws.amazon.com/sdk-for-java/latest/developer-guide/examples-ec2-instances.html
---

# Manage Amazon EC2 instances
<a name="examples-ec2-instances"></a>

## Create an instance
<a name="create-an-instance"></a>

Create a new Amazon EC2 instance by calling the [Ec2Client](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html)’s [`runInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#runInstances(software.amazon.awssdk.services.ec2.model.RunInstancesRequest)) method, providing it with a [RunInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/RunInstancesRequest.html) containing the [Amazon Machine Image (AMI)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) to use and an [instance type](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-types.html).

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.InstanceType;
import software.amazon.awssdk.services.ec2.model.RunInstancesRequest;
import software.amazon.awssdk.services.ec2.model.RunInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Tag;
import software.amazon.awssdk.services.ec2.model.CreateTagsRequest;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;
```

 **Code**

```
   public static String createEC2Instance(Ec2Client ec2,String name, String amiId ) {

        RunInstancesRequest runRequest = RunInstancesRequest.builder()
                .imageId(amiId)
                .instanceType(InstanceType.T1_MICRO)
                .maxCount(1)
                .minCount(1)
                .build();

        RunInstancesResponse response = ec2.runInstances(runRequest);
        String instanceId = response.instances().get(0).instanceId();

        Tag tag = Tag.builder()
                .key("Name")
                .value(name)
                .build();

        CreateTagsRequest tagRequest = CreateTagsRequest.builder()
                .resources(instanceId)
                .tags(tag)
                .build();

        try {
            ec2.createTags(tagRequest);
            System.out.printf(
                    "Successfully started EC2 Instance %s based on AMI %s",
                    instanceId, amiId);

          return instanceId;

        } catch (Ec2Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }

        return "";
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/CreateInstance.java) on GitHub.

## Start an instance
<a name="start-an-instance"></a>

To start an Amazon EC2 instance, call the Ec2Client’s [`startInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#startInstances(software.amazon.awssdk.services.ec2.model.StartInstancesRequest)) method, providing it with a [StartInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/StartInstancesRequest.html) containing the ID of the instance to start.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.StartInstancesRequest;
import software.amazon.awssdk.services.ec2.model.StopInstancesRequest;
```

 **Code**

```
    public static void startInstance(Ec2Client ec2, String instanceId) {

        StartInstancesRequest request = StartInstancesRequest.builder()
                .instanceIds(instanceId)
                .build();

        ec2.startInstances(request);
        System.out.printf("Successfully started instance %s", instanceId);
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/StartStopInstance.java) on GitHub.

## Stop an instance
<a name="stop-an-instance"></a>

To stop an Amazon EC2 instance, call the Ec2Client’s [`stopInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#stopInstances(software.amazon.awssdk.services.ec2.model.StopInstancesRequest)) method, providing it with a [StopInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/StopInstancesRequest.html) containing the ID of the instance to stop.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.StartInstancesRequest;
import software.amazon.awssdk.services.ec2.model.StopInstancesRequest;
```

 **Code**

```
    public static void stopInstance(Ec2Client ec2, String instanceId) {

        StopInstancesRequest request = StopInstancesRequest.builder()
                .instanceIds(instanceId)
                .build();

        ec2.stopInstances(request);
        System.out.printf("Successfully stopped instance %s", instanceId);
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/StartStopInstance.java) on GitHub.

## Reboot an instance
<a name="reboot-an-instance"></a>

To reboot an Amazon EC2 instance, call the Ec2Client’s [`rebootInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#rebootInstances(software.amazon.awssdk.services.ec2.model.RebootInstancesRequest)) method, providing it with a [RebootInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/RebootInstancesRequest.html) containing the ID of the instance to reboot.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;
import software.amazon.awssdk.services.ec2.model.RebootInstancesRequest;
```

 **Code**

```
    public static void rebootEC2Instance(Ec2Client ec2, String instanceId) {

      try {
            RebootInstancesRequest request = RebootInstancesRequest.builder()
                .instanceIds(instanceId)
                    .build();

            ec2.rebootInstances(request);
            System.out.printf(
                "Successfully rebooted instance %s", instanceId);
    } catch (Ec2Exception e) {
          System.err.println(e.awsErrorDetails().errorMessage());
          System.exit(1);
     }
  }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/RebootInstance.java) on GitHub.

## Describe instances
<a name="describe-instances"></a>

To list your instances, create a [DescribeInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/DescribeInstancesRequest.html) and call the Ec2Client’s [`describeInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#describeInstances(software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest)) method. It will return a [DescribeInstancesResponse](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/DescribeInstancesResponse.html) object that you can use to list the Amazon EC2 instances for your account and region.

Instances are grouped by *reservation*. Each reservation corresponds to the call to `startInstances` that launched the instance. To list your instances, you must first call the `DescribeInstancesResponse` class' `reservations` method, and then call `instances` on each returned [Reservation](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/Reservation.html) object.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesRequest;
import software.amazon.awssdk.services.ec2.model.DescribeInstancesResponse;
import software.amazon.awssdk.services.ec2.model.Instance;
import software.amazon.awssdk.services.ec2.model.Reservation;
import software.amazon.awssdk.services.ec2.model.Ec2Exception;
```

 **Code**

```
    public static void describeEC2Instances( Ec2Client ec2){

        String nextToken = null;

        try {

            do {
                DescribeInstancesRequest request = DescribeInstancesRequest.builder().maxResults(6).nextToken(nextToken).build();
                DescribeInstancesResponse response = ec2.describeInstances(request);

                for (Reservation reservation : response.reservations()) {
                    for (Instance instance : reservation.instances()) {
                        System.out.println("Instance Id is " + instance.instanceId());
                        System.out.println("Image id is "+  instance.imageId());
                        System.out.println("Instance type is "+  instance.instanceType());
                        System.out.println("Instance state name is "+  instance.state().name());
                        System.out.println("monitoring information is "+  instance.monitoring().state());

                }
            }
                nextToken = response.nextToken();
            } while (nextToken != null);

        } catch (Ec2Exception e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```

Results are paged; you can get further results by passing the value returned from the result object’s `nextToken` method to a new request object’s `nextToken` method, then using the new request object in your next call to `describeInstances`.

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/DescribeInstances.java) on GitHub.

## Monitor an instance
<a name="monitor-an-instance"></a>

You can monitor various aspects of your Amazon EC2 instances, such as CPU and network utilization, available memory, and disk space remaining. To learn more about instance monitoring, see [Monitoring Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/monitoring_ec2.html) in the Amazon EC2 User Guide for Linux Instances.

To start monitoring an instance, you must create a [MonitorInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/MonitorInstancesRequest.html) with the ID of the instance to monitor, and pass it to the Ec2Client’s [`monitorInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#monitorInstances(software.amazon.awssdk.services.ec2.model.MonitorInstancesRequest)) method.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.MonitorInstancesRequest;
import software.amazon.awssdk.services.ec2.model.UnmonitorInstancesRequest;
```

 **Code**

```
    public static void monitorInstance( Ec2Client ec2, String instanceId) {

        MonitorInstancesRequest request = MonitorInstancesRequest.builder()
                .instanceIds(instanceId).build();

        ec2.monitorInstances(request);
        System.out.printf(
                "Successfully enabled monitoring for instance %s",
                instanceId);
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/MonitorInstance.java) on GitHub.

## Stop instance monitoring
<a name="stop-instance-monitoring"></a>

To stop monitoring an instance, create an [UnmonitorInstancesRequest](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/model/UnmonitorInstancesRequest.html) with the ID of the instance to stop monitoring, and pass it to the Ec2Client’s [`unmonitorInstances`](https://sdk.amazonaws.com/java/api/latest/software/amazon/awssdk/services/ec2/Ec2Client.html#unmonitorInstances(software.amazon.awssdk.services.ec2.model.UnmonitorInstancesRequest)) method.

 **Imports**

```
import software.amazon.awssdk.regions.Region;
import software.amazon.awssdk.services.ec2.Ec2Client;
import software.amazon.awssdk.services.ec2.model.MonitorInstancesRequest;
import software.amazon.awssdk.services.ec2.model.UnmonitorInstancesRequest;
```

 **Code**

```
    public static void unmonitorInstance(Ec2Client ec2, String instanceId) {
        UnmonitorInstancesRequest request = UnmonitorInstancesRequest.builder()
                .instanceIds(instanceId).build();

        ec2.unmonitorInstances(request);

        System.out.printf(
                "Successfully disabled monitoring for instance %s",
                instanceId);
    }
```

See the [complete example](https://github.com/awsdocs/aws-doc-sdk-examples/blob/ac748d8ef99cd17e297cb74fe13aa671e2679088/javav2/example_code/ec2/src/main/java/com/example/ec2/MonitorInstance.java) on GitHub.

## More information
<a name="more-information"></a>
+  [RunInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RunInstances.html) in the Amazon EC2 API Reference
+  [DescribeInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DescribeInstances.html) in the Amazon EC2 API Reference
+  [StartInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StartInstances.html) in the Amazon EC2 API Reference
+  [StopInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) in the Amazon EC2 API Reference
+  [RebootInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html) in the Amazon EC2 API Reference
+  [MonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_MonitorInstances.html) in the Amazon EC2 API Reference
+  [UnmonitorInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_UnmonitorInstances.html) in the Amazon EC2 API Reference

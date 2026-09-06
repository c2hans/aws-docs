---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/scheduler_example_scheduler_hello_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Hello EventBridge Scheduler
<a name="scheduler_example_scheduler_hello_section"></a>

The following code examples show how to get started using EventBridge Scheduler.

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge Scheduler#code-examples).

```
public static class HelloScheduler
{
    static async Task Main(string[] args)
    {
        // Use the AWS .NET Core Setup package to set up dependency injection for the EventBridge Scheduler service.
        // Use your AWS profile name, or leave it blank to use the default profile.
        using var host = Host.CreateDefaultBuilder(args)
            .ConfigureServices((_, services) =>
                services.AddAWSService<IAmazonScheduler>()
            ).Build();

        // Now the client is available for injection.
        var schedulerClient = host.Services.GetRequiredService<IAmazonScheduler>();

        // You can use await and any of the async methods to get a response, or a paginator to list schedules or groups.
        var results = new List<ScheduleSummary>();
        var paginateSchedules = schedulerClient.Paginators.ListSchedules(
            new ListSchedulesRequest());
        Console.WriteLine(
            $"Hello AWS Scheduler! Let's list schedules in your account.");
        // Get the entire list using the paginator.
        await foreach (var schedule in paginateSchedules.Schedules)
        {
            results.Add(schedule);
        }
        Console.WriteLine($"\tTotal of {results.Count} schedule(s) available.");
        results.ForEach(s => Console.WriteLine($"\tSchedule: {s.Name}"));
    }
}
```
+  For API details, see [ListSchedules](https://docs.aws.amazon.com/goto/DotNetSDKV3/scheduler-2021-06-30/ListSchedules) in *AWS SDK for .NET API Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/scheduler#code-examples).

```
import software.amazon.awssdk.services.scheduler.SchedulerAsyncClient;
import software.amazon.awssdk.services.scheduler.model.ListSchedulesRequest;
import software.amazon.awssdk.services.scheduler.model.ScheduleSummary;
import software.amazon.awssdk.services.scheduler.paginators.ListSchedulesPublisher;
import java.util.ArrayList;
import java.util.List;
import java.util.concurrent.CompletableFuture;

public class HelloScheduler {

    public static void main(String [] args) {
        listSchedulesAsync();
    }

    /**
     * Lists all the schedules available.
     * <p>
     * This method uses the {@link SchedulerAsyncClient} to make an asynchronous request to
     * list all the schedules available. The method uses the {@link ListSchedulesPublisher}
     * to fetch the schedules in a paginated manner, and then processes the responses
     * asynchronously.
     */
    public static void listSchedulesAsync() {
        SchedulerAsyncClient schedulerAsyncClient = SchedulerAsyncClient.create();

        // Build the request to list schedules
        ListSchedulesRequest listSchedulesRequest = ListSchedulesRequest.builder().build();

        // Use the paginator to fetch all schedules asynchronously.
        ListSchedulesPublisher paginator = schedulerAsyncClient.listSchedulesPaginator(listSchedulesRequest);
        List<ScheduleSummary> results = new ArrayList<>();

        // Subscribe to the paginator to process the response asynchronously
        CompletableFuture<Void> future = paginator.subscribe(response -> {
            response.schedules().forEach(schedule -> {
                results.add(schedule);
                System.out.printf("Schedule: %s%n", schedule.name());
            });
        });

        // Wait for the asynchronous operation to complete.
        future.join();

        // After all schedules are fetched, print the total count.
        System.out.printf("Total of %d schedule(s) available.%n", results.size());
    }
}
```
+  For API details, see [ListSchedules](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/ListSchedules) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/scheduler#code-examples).

```
import boto3

def hello_scheduler(scheduler_client):
    """
    Use the AWS SDK for Python (Boto3) to create an Amazon EventBridge Scheduler
    client and list the schedules in your account.
    This example uses the default settings specified in your shared credentials
    and config files.

    :param scheduler_client: A Boto3 Amazon EventBridge Scheduler Client object. This object wraps
                             the low-level Amazon EventBridge Scheduler service API.
    """
    print("Hello, Amazon EventBridge Scheduler! Let's list some of your schedules:\n")
    paginator = scheduler_client.get_paginator("list_schedules")
    page_iterator = paginator.paginate(PaginationConfig={"MaxItems": 10})

    schedule_names: [str] = []
    for page in page_iterator:
        for schedule in page["Schedules"]:
            schedule_names.append(schedule["Name"])

    print(f"{len(schedule_names)} schedule(s) retrieved.")
    for schedule_name in schedule_names:
        print(f"\t{schedule_name}")

if __name__ == "__main__":
    hello_scheduler(boto3.client("scheduler"))
```
+  For API details, see [ListSchedules](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/ListSchedules) in *AWS SDK for Python (Boto3) API Reference*.

------

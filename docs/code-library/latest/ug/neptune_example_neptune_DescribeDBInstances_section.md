---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/neptune_example_neptune_DescribeDBInstances_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeDBInstances` with an AWS SDK
<a name="neptune_example_neptune_DescribeDBInstances_section"></a>

The following code examples show how to use `DescribeDBInstances`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](neptune_example_neptune_Scenario_section.md)

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/neptune#code-examples).

```
    /**
     * Checks the status of a Neptune instance recursively until the desired status is reached or a timeout occurs.
     *
     * @param instanceId     the ID of the Neptune instance to check
     * @param desiredStatus  the desired status of the Neptune instance
     * @param startTime      the start time of the operation, used to calculate the elapsed time
     * @param future         a {@link CompletableFuture} that will be completed when the desired status is reached
     */
    private void checkStatusRecursive(String instanceId, String desiredStatus, long startTime, CompletableFuture<Void> future) {
        DescribeDbInstancesRequest request = DescribeDbInstancesRequest.builder()
                .dbInstanceIdentifier(instanceId)
                .build();

        getAsyncClient().describeDBInstances(request)
                .whenComplete((response, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause();
                        future.completeExceptionally(
                                new CompletionException("Error checking Neptune instance status", cause)
                        );
                        return;
                    }

                    List<DBInstance> instances = response.dbInstances();
                    if (instances.isEmpty()) {
                        future.completeExceptionally(new RuntimeException("Instance not found: " + instanceId));
                        return;
                    }

                    String currentStatus = instances.get(0).dbInstanceStatus();
                    long elapsedSeconds = (System.currentTimeMillis() - startTime) / 1000;
                    System.out.printf("\r Elapsed: %-20s  Status: %-20s", formatElapsedTime((int) elapsedSeconds), currentStatus);
                    System.out.flush();

                    if (desiredStatus.equalsIgnoreCase(currentStatus)) {
                        System.out.printf("\r Neptune instance reached desired status '%s' after %s.\n", desiredStatus, formatElapsedTime((int) elapsedSeconds));
                        future.complete(null);
                    } else {
                        CompletableFuture.delayedExecutor(20, TimeUnit.SECONDS)
                                .execute(() -> checkStatusRecursive(instanceId, desiredStatus, startTime, future));
                    }
                });
    }
```
+  For API details, see [DescribeDBInstances](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/DescribeDBInstances) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/neptune#code-examples).

```
def check_instance_status(neptune_client, instance_id: str, desired_status: str):
    """
    Polls the status of a Neptune DB instance until it reaches desired_status.
    Uses pagination via describe_db_instances — even for a single instance.

    Raises:
      ClientError: If describe_db_instances fails (e.g., instance not found).
      RuntimeError: If timeout expires before reaching desired status.
    """
    paginator = neptune_client.get_paginator('describe_db_instances')
    start_time = time.time()

    while True:
        try:
            pages = paginator.paginate(DBInstanceIdentifier=instance_id)
            instances = []
            for page in pages:
                instances.extend(page.get('DBInstances', []))

        except ClientError as err:
            code = err.response["Error"]["Code"]
            message = err.response["Error"]["Message"]

            if code == "DBInstanceNotFound":
                print(f"Instance '{instance_id}' not found. Please verify the instance ID.")
            else:
                print(f"Failed to describe DB instance. {code}: {message}")
            raise

        current_status = instances[0].get('DBInstanceStatus') if instances else None
        elapsed = int(time.time() - start_time)

        print(f"\rElapsed: {format_elapsed_time(elapsed)}  Status: {current_status}", end="", flush=True)

        if current_status and current_status.lower() == desired_status.lower():
            print(f"\nInstance '{instance_id}' reached '{desired_status}' in {format_elapsed_time(elapsed)}.")
            return

        if elapsed > TIMEOUT_SECONDS:
            raise RuntimeError(f"Timeout waiting for '{instance_id}' to reach '{desired_status}'")

        time.sleep(POLL_INTERVAL_SECONDS)
```
+  For API details, see [DescribeDBInstances](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/DescribeDBInstances) in *AWS SDK for Python (Boto3) API Reference*.

------

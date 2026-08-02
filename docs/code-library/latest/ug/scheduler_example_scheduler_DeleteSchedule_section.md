---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/scheduler_example_scheduler_DeleteSchedule_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteSchedule` with an AWS SDK
<a name="scheduler_example_scheduler_DeleteSchedule_section"></a>

The following code examples show how to use `DeleteSchedule`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Scheduled Events](scheduler_example_scheduler_ScheduledEventsScenario_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge Scheduler#code-examples).

```
    /// <summary>
    /// Deletes an existing schedule from Amazon EventBridge Scheduler.
    /// </summary>
    /// <param name="name">The name of the schedule to delete.</param>
    /// <param name="groupName">The group name of the schedule to delete.</param>
    /// <returns>True if the schedule was deleted successfully, false otherwise.</returns>
    public async Task<bool> DeleteScheduleAsync(string name, string groupName)
    {
        try
        {
            var request = new DeleteScheduleRequest
            {
                Name = name,
                GroupName = groupName
            };

            await _amazonScheduler.DeleteScheduleAsync(request);

            Console.WriteLine($"Successfully deleted schedule with name '{name}'.");
            return true;

        }
        catch (ResourceNotFoundException ex)
        {
            _logger.LogError(
                $"Failed to delete schedule with ID '{name}' because the resource was not found: {ex.Message}");
            return true;
        }
        catch (Exception ex)
        {
            _logger.LogError(
                $"An error occurred while deleting schedule with ID '{name}': {ex.Message}");
            return false;
        }
    }
```
+  For API details, see [DeleteSchedule](https://docs.aws.amazon.com/goto/DotNetSDKV3/scheduler-2021-06-30/DeleteSchedule) in *AWS SDK for .NET API Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/scheduler#code-examples).

```
    /**
     * Deletes a schedule with the specified name and group name.
     *
     * @param name      the name of the schedule to be deleted
     * @param groupName the group name of the schedule to be deleted
     * @return a {@link CompletableFuture} that, when completed, indicates whether the schedule was successfully deleted
     * @throws CompletionException if an error occurs while deleting the schedule, except for the case where the schedule is not found
     */
    public CompletableFuture<Boolean> deleteScheduleAsync(String name, String groupName) {
        DeleteScheduleRequest request = DeleteScheduleRequest.builder()
            .name(name)
            .groupName(groupName)
            .build();

        CompletableFuture<DeleteScheduleResponse> response = getAsyncClient().deleteSchedule(request);
        return response.handle((result, ex) -> {
            if (ex != null) {
                if (ex instanceof ResourceNotFoundException) {
                    throw new CompletionException("Resource not found while deleting schedule with ID: " + name, ex);
                } else {
                    throw new CompletionException("Failed to delete schedule.", ex);
                }
            }
            logger.info("Successfully deleted schedule with name {}.", name);
            return true;
        });
    }
```
+  For API details, see [DeleteSchedule](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/DeleteSchedule) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/scheduler#code-examples).

```
class SchedulerWrapper:
    def __init__(self, eventbridge_scheduler_client: client):
        self.scheduler_client = eventbridge_scheduler_client

    @classmethod
    def from_client(cls) -> "SchedulerWrapper":
        """
        Creates a SchedulerWrapper instance with a default EventBridge Scheduler client.

        :return: An instance of SchedulerWrapper initialized with the default EventBridge Scheduler client.
        """
        eventbridge_scheduler_client = boto3.client("scheduler")
        return cls(eventbridge_scheduler_client)

    def delete_schedule(self, name: str, schedule_group_name: str) -> None:
        """
        Deletes the schedule with the specified name and schedule group.

        :param name: The name of the schedule.
        :param schedule_group_name: The name of the schedule group.
        """
        try:
            self.scheduler_client.delete_schedule(
                Name=name, GroupName=schedule_group_name
            )
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Failed to delete schedule with ID '%s' because the resource was not found: %s",
                    name,
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error deleting schedule: %s", err.response["Error"]["Message"]
                )
                raise
```
+  For API details, see [DeleteSchedule](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/DeleteSchedule) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/scd#code-examples).

```
    TRY.
        " Example iv_name = 'my-schedule'
        " Example iv_schedule_group_name = 'my-schedule-group'
        lo_scd->deleteschedule(
          iv_name = iv_name
          iv_groupname = iv_schedule_group_name ).
        MESSAGE 'Schedule deleted successfully.' TYPE 'I'.

      CATCH /aws1/cx_scdresourcenotfoundex INTO DATA(lo_not_found_ex).
        DATA(lv_error) = |Schedule not found: { lo_not_found_ex->if_message~get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_generic_ex).
        DATA(lv_generic_error) = |Error deleting schedule: { lo_generic_ex->if_message~get_text( ) }|.
        MESSAGE lv_generic_error TYPE 'I'.
    ENDTRY.
```
+  For API details, see [DeleteSchedule](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

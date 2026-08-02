---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/scheduler_example_scheduler_CreateScheduleGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateScheduleGroup` with an AWS SDK
<a name="scheduler_example_scheduler_CreateScheduleGroup_section"></a>

The following code examples show how to use `CreateScheduleGroup`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Scheduled Events](scheduler_example_scheduler_ScheduledEventsScenario_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge Scheduler#code-examples).

```
    /// <summary>
    /// Creates a new schedule group in Amazon EventBridge Scheduler.
    /// </summary>
    /// <param name="name">The name of the schedule group.</param>
    /// <returns>True if the schedule group was created successfully, false otherwise.</returns>
    public async Task<bool> CreateScheduleGroupAsync(string name)
    {
        try
        {
            var request = new CreateScheduleGroupRequest { Name = name };

            var response = await _amazonScheduler.CreateScheduleGroupAsync(request);

            Console.WriteLine($"Successfully created schedule group '{name}': {response.ScheduleGroupArn}.");
            return true;

        }
        catch (ConflictException ex)
        {
            // If the name is not unique, a ConflictException will be thrown.
            _logger.LogError($"Failed to create schedule group '{name}' due to a conflict. {ex.Message}");
            return false;
        }
        catch (Exception ex)
        {
            _logger.LogError(
                $"An error occurred while creating schedule group '{name}': {ex.Message}");
            return false;
        }
    }
```
+  For API details, see [CreateScheduleGroup](https://docs.aws.amazon.com/goto/DotNetSDKV3/scheduler-2021-06-30/CreateScheduleGroup) in *AWS SDK for .NET API Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/scheduler#code-examples).

```
    /**
     * Creates a new schedule group.
     *
     * @param name the name of the schedule group to be created
     * @return a {@link CompletableFuture} representing the asynchronous operation of creating the schedule group
     */
    public CompletableFuture<CreateScheduleGroupResponse> createScheduleGroup(String name) {
        CreateScheduleGroupRequest request = CreateScheduleGroupRequest.builder()
            .name(name)
            .build();

        logger.info("Initiating createScheduleGroup call for group: {}", name);
        CompletableFuture<CreateScheduleGroupResponse> futureResponse = getAsyncClient().createScheduleGroup(request);
        futureResponse.whenComplete((response, ex) -> {
            if (ex != null) {
                if (ex instanceof CompletionException && ex.getCause() instanceof ConflictException) {
                    // Rethrow the ConflictException
                    throw (ConflictException) ex.getCause();
                } else {
                    throw new CompletionException("Failed to create schedule group: " + name, ex);
                }
            } else if (response == null) {
                throw new RuntimeException("Failed to create schedule group: response was null");
            } else {
                logger.info("Successfully created schedule group '{}': {}", name, response.scheduleGroupArn());
            }
        });

        return futureResponse;
    }
```
+  For API details, see [CreateScheduleGroup](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/CreateScheduleGroup) in *AWS SDK for Java 2.x API Reference*.

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

    def create_schedule_group(self, name: str) -> str:
        """
        Creates a new schedule group with the specified name and description.

        :param name: The name of the schedule group.
        :param description: The description of the schedule group.

        :return: The ARN of the created schedule group.
        """
        try:
            response = self.scheduler_client.create_schedule_group(Name=name)
            return response["ScheduleGroupArn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                logger.error(
                    "Failed to create schedule group '%s' due to a conflict. %s",
                    name,
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error creating schedule group: %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateScheduleGroup](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/CreateScheduleGroup) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/scd#code-examples).

```
    TRY.
        " Example iv_name = 'my-schedule-group'
        DATA(lo_result) = lo_scd->createschedulegroup(
          iv_name = iv_name ).

        ov_schedule_group_arn = lo_result->get_schedulegrouparn( ).
        MESSAGE 'Schedule group created successfully.' TYPE 'I'.

      CATCH /aws1/cx_scdconflictexception INTO DATA(lo_conflict_ex).
        DATA(lv_error) = |Conflict creating schedule group: { lo_conflict_ex->if_message~get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_generic_ex).
        DATA(lv_generic_error) = |Error creating schedule group: { lo_generic_ex->if_message~get_text( ) }|.
        MESSAGE lv_generic_error TYPE 'I'.
    ENDTRY.
```
+  For API details, see [CreateScheduleGroup](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

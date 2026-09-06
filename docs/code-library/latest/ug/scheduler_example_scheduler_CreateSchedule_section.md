---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/scheduler_example_scheduler_CreateSchedule_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateSchedule` with an AWS SDK
<a name="scheduler_example_scheduler_CreateSchedule_section"></a>

The following code examples show how to use `CreateSchedule`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Scheduled Events](scheduler_example_scheduler_ScheduledEventsScenario_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/EventBridge Scheduler#code-examples).

```
    /// <summary>
    /// Creates a new schedule in Amazon EventBridge Scheduler.
    /// </summary>
    /// <param name="name">The name of the schedule.</param>
    /// <param name="scheduleExpression">The schedule expression that defines when the schedule should run.</param>
    /// <param name="scheduleGroupName">The name of the schedule group to which the schedule should be added.</param>
    /// <param name="deleteAfterCompletion">Indicates whether to delete the schedule after completion.</param>
    /// <param name="useFlexibleTimeWindow">Indicates whether to use a flexible time window for the schedule.</param>
    /// <param name="targetArn">ARN of the event target.</param>
    /// <param name="roleArn">Execution Role ARN.</param>
    /// <returns>True if the schedule was created successfully, false otherwise.</returns>
    public async Task<bool> CreateScheduleAsync(
            string name,
            string scheduleExpression,
            string scheduleGroupName,
            string targetArn,
            string roleArn,
            string input,
            bool deleteAfterCompletion = false,
            bool useFlexibleTimeWindow = false)
    {
        try
        {
            int hoursToRun = 1;
            int flexibleTimeWindowMinutes = 10;

            var request = new CreateScheduleRequest
            {
                Name = name,
                ScheduleExpression = scheduleExpression,
                GroupName = scheduleGroupName,
                Target = new Target { Arn = targetArn, RoleArn = roleArn, Input = input },
                ActionAfterCompletion = deleteAfterCompletion
                    ? ActionAfterCompletion.DELETE
                    : ActionAfterCompletion.NONE,
                StartDate = DateTime.UtcNow, // Ignored for one-time schedules.
                EndDate =
                    DateTime.UtcNow
                        .AddHours(hoursToRun) // Ignored for one-time schedules.
            };
            // Allow a flexible time window if the caller specifies it.
            request.FlexibleTimeWindow = new FlexibleTimeWindow
            {
                Mode = useFlexibleTimeWindow
                    ? FlexibleTimeWindowMode.FLEXIBLE
                    : FlexibleTimeWindowMode.OFF,
                MaximumWindowInMinutes = useFlexibleTimeWindow
                    ? flexibleTimeWindowMinutes
                    : null
            };

            var response = await _amazonScheduler.CreateScheduleAsync(request);

            Console.WriteLine($"Successfully created schedule '{name}' " +
                              $"in schedule group '{scheduleGroupName}': {response.ScheduleArn}.");
            return true;
        }
        catch (ConflictException ex)
        {
            // If the name is not unique, a ConflictException will be thrown.
            _logger.LogError($"Failed to create schedule '{name}' due to a conflict. {ex.Message}");
            return false;
        }
        catch (Exception ex)
        {
            _logger.LogError($"An error occurred while creating schedule '{name}' " +
                             $"in schedule group '{scheduleGroupName}': {ex.Message}");
            return false;
        }
    }
```
+  For API details, see [CreateSchedule](https://docs.aws.amazon.com/goto/DotNetSDKV3/scheduler-2021-06-30/CreateSchedule) in *AWS SDK for .NET API Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/scheduler#code-examples).

```
    /**
     * Creates a new schedule for a target task.
     *
     * @param name                  the name of the schedule
     * @param scheduleExpression    The schedule expression that defines when the schedule should run.
     * @param scheduleGroupName     the name of the schedule group to which the schedule belongs
     * @param targetArn             the Amazon Resource Name (ARN) of the target task
     * @param roleArn               the ARN of the IAM role to be used for the schedule
     * @param input                 the input data for the target task
     * @param deleteAfterCompletion whether to delete the schedule after it's executed
     * @param useFlexibleTimeWindow whether to use a flexible time window for the schedule execution
     * @return true if the schedule was successfully created, false otherwise
     */
    public CompletableFuture<Boolean> createScheduleAsync(
        String name,
        String scheduleExpression,
        String scheduleGroupName,
        String targetArn,
        String roleArn,
        String input,
        boolean deleteAfterCompletion,
        boolean useFlexibleTimeWindow) {

        int hoursToRun = 1;
        int flexibleTimeWindowMinutes = 10;

        Target target = Target.builder()
            .arn(targetArn)
            .roleArn(roleArn)
            .input(input)
            .build();

        FlexibleTimeWindow flexibleTimeWindow = FlexibleTimeWindow.builder()
            .mode(useFlexibleTimeWindow
                ? FlexibleTimeWindowMode.FLEXIBLE
                : FlexibleTimeWindowMode.OFF)
            .maximumWindowInMinutes(useFlexibleTimeWindow
                ? flexibleTimeWindowMinutes
                : null)
            .build();

        Instant startDate = Instant.now();
        Instant endDate = startDate.plus(Duration.ofHours(hoursToRun));

        CreateScheduleRequest request = CreateScheduleRequest.builder()
            .name(name)
            .scheduleExpression(scheduleExpression)
            .groupName(scheduleGroupName)
            .target(target)
            .actionAfterCompletion(deleteAfterCompletion
                ? ActionAfterCompletion.DELETE
                : ActionAfterCompletion.NONE)
            .startDate(startDate)
            .endDate(endDate)
            .flexibleTimeWindow(flexibleTimeWindow)
            .build();

        return getAsyncClient().createSchedule(request)
            .thenApply(response -> {
                logger.info("Successfully created schedule {} in schedule group {}, The ARN is {} ", name, scheduleGroupName, response.scheduleArn());
                return true;
            })
            .whenComplete((result, ex) -> {
                if (ex != null) {
                    if (ex instanceof ConflictException) {
                        // Handle ConflictException
                        logger.error("A conflict exception occurred while creating the schedule: {}", ex.getMessage());
                        throw new CompletionException("A conflict exception occurred while creating the schedule: " + ex.getMessage(), ex);
                    } else {
                        throw new CompletionException("Error creating schedule: " + ex.getMessage(), ex);
                    }
                }
            });
    }
```
+  For API details, see [CreateSchedule](https://docs.aws.amazon.com/goto/SdkForJavaV2/scheduler-2021-06-30/CreateSchedule) in *AWS SDK for Java 2.x API Reference*.

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

    def create_schedule(
        self,
        name: str,
        schedule_expression: str,
        schedule_group_name: str,
        target_arn: str,
        role_arn: str,
        input: str,
        delete_after_completion: bool = False,
        use_flexible_time_window: bool = False,
    ) -> str:
        """
        Creates a new schedule with the specified parameters.

        :param name: The name of the schedule.
        :param schedule_expression: The expression that defines when the schedule runs.
        :param schedule_group_name: The name of the schedule group.
        :param target_arn: The Amazon Resource Name (ARN) of the target.
        :param role_arn: The Amazon Resource Name (ARN) of the execution IAM role.
        :param input: The input for the target.
        :param delete_after_completion: Whether to delete the schedule after it completes.
        :param use_flexible_time_window: Whether to use a flexible time window.

        :return The ARN of the created schedule.
        """
        try:
            hours_to_run = 1
            flexible_time_window_minutes = 10
            parameters = {
                "Name": name,
                "ScheduleExpression": schedule_expression,
                "GroupName": schedule_group_name,
                "Target": {"Arn": target_arn, "RoleArn": role_arn, "Input": input},
                "StartDate": datetime.now(timezone.utc),
                "EndDate": datetime.now(timezone.utc) + timedelta(hours=hours_to_run),
            }

            if delete_after_completion:
                parameters["ActionAfterCompletion"] = "DELETE"

            if use_flexible_time_window:
                parameters["FlexibleTimeWindow"] = {
                    "Mode": "FLEXIBLE",
                    "MaximumWindowInMinutes": flexible_time_window_minutes,
                }
            else:
                parameters["FlexibleTimeWindow"] = {"Mode": "OFF"}

            response = self.scheduler_client.create_schedule(**parameters)
            return response["ScheduleArn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ConflictException":
                logger.error(
                    "Failed to create schedule '%s' due to a conflict. %s",
                    name,
                    err.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Error creating schedule: %s", err.response["Error"]["Message"]
                )
            raise
```
+  For API details, see [CreateSchedule](https://docs.aws.amazon.com/goto/boto3/scheduler-2021-06-30/CreateSchedule) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/scd#code-examples).

```
    TRY.
        " Constants for time calculations
        DATA lv_start_date TYPE /aws1/scdstartdate.
        DATA lv_end_date TYPE /aws1/scdenddate.
        DATA lv_start_timestamp TYPE timestamp.
        DATA lv_end_timestamp TYPE timestamp.
        DATA lv_hours_to_run TYPE i VALUE 1.

        " Get current timestamp
        GET TIME STAMP FIELD lv_start_timestamp.

        " Add 1 hour to the current timestamp using CL_ABAP_TSTMP
        lv_end_timestamp = cl_abap_tstmp=>add(
          tstmp = lv_start_timestamp
          secs = lv_hours_to_run * 3600 ).

        " Convert timestamps to decimal format for AWS API
        lv_start_date = lv_start_timestamp.
        lv_end_date = lv_end_timestamp.

        " Prepare flexible time window configuration
        DATA lo_flexible_time_window TYPE REF TO /aws1/cl_scdflexibletimewindow.
        IF iv_use_flexible_time_win = abap_true.
          " iv_use_flexible_time_win = ABAP_TRUE
          " Example: Set MaximumWindowInMinutes to 10 for flexible window
          lo_flexible_time_window = NEW /aws1/cl_scdflexibletimewindow(
            iv_mode = 'FLEXIBLE'
            iv_maximumwindowinminutes = 10 ).
        ELSE.
          lo_flexible_time_window = NEW /aws1/cl_scdflexibletimewindow(
            iv_mode = 'OFF' ).
        ENDIF.

        " Prepare target configuration
        " Example iv_target_arn = 'arn:aws:sqs:us-east-1:123456789012:my-queue'
        " Example iv_role_arn = 'arn:aws:iam::123456789012:role/SchedulerRole'
        " Example iv_input = '{"message": "Hello from EventBridge Scheduler"}'
        DATA(lo_target) = NEW /aws1/cl_scdtarget(
          iv_arn = iv_target_arn
          iv_rolearn = iv_role_arn
          iv_input = iv_input ).

        " Set action after completion if needed
        DATA lv_action_after_completion TYPE /aws1/scdactionaftercompletion.
        IF iv_delete_after_completion = abap_true.
          " iv_delete_after_completion = ABAP_TRUE
          lv_action_after_completion = 'DELETE'.
        ELSE.
          lv_action_after_completion = 'NONE'.
        ENDIF.

        " Create the schedule
        " Example iv_name = 'my-schedule'
        " Example iv_schedule_expression = 'rate(15 minutes)'
        " Example iv_schedule_group_name = 'my-schedule-group'
        DATA(lo_result) = lo_scd->createschedule(
          iv_name = iv_name
          iv_scheduleexpression = iv_schedule_expression
          iv_groupname = iv_schedule_group_name
          io_target = lo_target
          io_flexibletimewindow = lo_flexible_time_window
          iv_startdate = lv_start_date
          iv_enddate = lv_end_date
          iv_actionaftercompletion = lv_action_after_completion ).

        ov_schedule_arn = lo_result->get_schedulearn( ).
        MESSAGE 'Schedule created successfully.' TYPE 'I'.

      CATCH /aws1/cx_scdconflictexception INTO DATA(lo_conflict_ex).
        DATA(lv_error) = |Conflict creating schedule: { lo_conflict_ex->if_message~get_text( ) }|.
        MESSAGE lv_error TYPE 'I'.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_generic_ex).
        DATA(lv_generic_error) = |Error creating schedule: { lo_generic_ex->if_message~get_text( ) }|.
        MESSAGE lv_generic_error TYPE 'I'.
    ENDTRY.
```
+  For API details, see [CreateSchedule](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

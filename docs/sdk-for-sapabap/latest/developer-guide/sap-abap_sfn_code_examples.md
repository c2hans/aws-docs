---
source_url: https://docs.aws.amazon.com/sdk-for-sapabap/latest/developer-guide/sap-abap_sfn_code_examples.html
---

# Step Functions examples using SDK for SAP ABAP
<a name="sap-abap_sfn_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS SDK for SAP ABAP with Step Functions.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `CreateActivity`
<a name="sfn_CreateActivity_sap-abap_topic"></a>

The following code example shows how to use `CreateActivity`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        DATA(lo_result) = lo_sfn->createactivity(
          iv_name = iv_name
        ).
        ov_activity_arn = lo_result->get_activityarn( ).
        MESSAGE 'Activity created successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfnactivityalrdyex.
        MESSAGE 'Activity already exists.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidname.
        MESSAGE 'Invalid activity name.' TYPE 'E'.
      CATCH /aws1/cx_sfnactivitylimitexcd.
        MESSAGE 'Activity limit exceeded.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreateActivity](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `CreateStateMachine`
<a name="sfn_CreateStateMachine_sap-abap_topic"></a>

The following code example shows how to use `CreateStateMachine`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        DATA(lo_result) = lo_sfn->createstatemachine(
          iv_name = iv_name
          iv_definition = iv_definition
          iv_rolearn = iv_role_arn
        ).
        ov_state_machine_arn = lo_result->get_statemachinearn( ).
        MESSAGE 'State machine created successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfnstatemachinealrex.
        MESSAGE 'State machine already exists.' TYPE 'E'.
      CATCH /aws1/cx_sfninvaliddefinition.
        MESSAGE 'Invalid state machine definition.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidname.
        MESSAGE 'Invalid state machine name.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid role ARN.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [CreateStateMachine](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteActivity`
<a name="sfn_DeleteActivity_sap-abap_topic"></a>

The following code example shows how to use `DeleteActivity`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        lo_sfn->deleteactivity(
          iv_activityarn = iv_activity_arn
        ).
        MESSAGE 'Activity deleted successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid activity ARN.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteActivity](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DeleteStateMachine`
<a name="sfn_DeleteStateMachine_sap-abap_topic"></a>

The following code example shows how to use `DeleteStateMachine`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        lo_sfn->deletestatemachine(
          iv_statemachinearn = iv_state_machine_arn
        ).
        MESSAGE 'State machine deleted successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid state machine ARN.' TYPE 'E'.
      CATCH /aws1/cx_sfnvalidationex.
        MESSAGE 'Validation error occurred.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DeleteStateMachine](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeExecution`
<a name="sfn_DescribeExecution_sap-abap_topic"></a>

The following code example shows how to use `DescribeExecution`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        oo_result = lo_sfn->describeexecution(
          iv_executionarn = iv_execution_arn
        ).
        MESSAGE 'Execution described successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfnexecdoesnotexist.
        MESSAGE 'Execution does not exist.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid execution ARN.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeExecution](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `DescribeStateMachine`
<a name="sfn_DescribeStateMachine_sap-abap_topic"></a>

The following code example shows how to use `DescribeStateMachine`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        oo_result = lo_sfn->describestatemachine(
          iv_statemachinearn = iv_state_machine_arn
        ).
        MESSAGE 'State machine described successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfnstatemachinedoes00.
        MESSAGE 'State machine does not exist.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid state machine ARN.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [DescribeStateMachine](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `GetActivityTask`
<a name="sfn_GetActivityTask_sap-abap_topic"></a>

The following code example shows how to use `GetActivityTask`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        oo_result = lo_sfn->getactivitytask(
          iv_activityarn = iv_activity_arn
        ).
        MESSAGE 'Activity task retrieved successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfnactivitydoesnotex.
        MESSAGE 'Activity does not exist.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid activity ARN.' TYPE 'E'.
      CATCH /aws1/cx_sfnactivityworkerlm00.
        MESSAGE 'Activity worker limit exceeded.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [GetActivityTask](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListActivities`
<a name="sfn_ListActivities_sap-abap_topic"></a>

The following code example shows how to use `ListActivities`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        DATA(lo_result) = lo_sfn->listactivities( ).
        DATA(lt_activities) = lo_result->get_activities( ).
        LOOP AT lt_activities INTO DATA(lo_activity).
          IF lo_activity->get_name( ) = iv_name.
            ov_activity_arn = lo_activity->get_activityarn( ).
            EXIT.
          ENDIF.
        ENDLOOP.
        MESSAGE 'Activities listed successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfninvalidtoken.
        MESSAGE 'Invalid pagination token.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListActivities](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `ListStateMachines`
<a name="sfn_ListStateMachines_sap-abap_topic"></a>

The following code example shows how to use `ListStateMachines`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        DATA(lo_result) = lo_sfn->liststatemachines( ).
        DATA(lt_state_machines) = lo_result->get_statemachines( ).
        LOOP AT lt_state_machines INTO DATA(lo_state_machine).
          IF lo_state_machine->get_name( ) = iv_name.
            ov_state_machine_arn = lo_state_machine->get_statemachinearn( ).
            EXIT.
          ENDIF.
        ENDLOOP.
        MESSAGE 'State machines listed successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfninvalidtoken.
        MESSAGE 'Invalid pagination token.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [ListStateMachines](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `SendTaskSuccess`
<a name="sfn_SendTaskSuccess_sap-abap_topic"></a>

The following code example shows how to use `SendTaskSuccess`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        lo_sfn->sendtasksuccess(
          iv_tasktoken = iv_task_token
          iv_output = iv_task_response
        ).
        MESSAGE 'Task success sent successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfninvalidtoken.
        MESSAGE 'Invalid task token.' TYPE 'E'.
      CATCH /aws1/cx_sfntaskdoesnotexist.
        MESSAGE 'Task does not exist.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidoutput.
        MESSAGE 'Invalid task output.' TYPE 'E'.
      CATCH /aws1/cx_sfntasktimedout.
        MESSAGE 'Task timed out.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [SendTaskSuccess](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

### `StartExecution`
<a name="sfn_StartExecution_sap-abap_topic"></a>

The following code example shows how to use `StartExecution`.

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/sfn#code-examples).

```
    TRY.
        DATA(lo_result) = lo_sfn->startexecution(
          iv_statemachinearn = iv_state_machine_arn
          iv_input = iv_input
        ).
        ov_execution_arn = lo_result->get_executionarn( ).
        MESSAGE 'Execution started successfully.' TYPE 'I'.
      CATCH /aws1/cx_sfnstatemachinedoes00.
        MESSAGE 'State machine does not exist.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidarn.
        MESSAGE 'Invalid state machine ARN.' TYPE 'E'.
      CATCH /aws1/cx_sfninvalidexecinput.
        MESSAGE 'Invalid execution input.' TYPE 'E'.
      CATCH /aws1/cx_sfnexeclimitexceeded.
        MESSAGE 'Execution limit exceeded.' TYPE 'E'.
    ENDTRY.
```
+  For API details, see [StartExecution](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS SDK for SAP ABAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query sdk-for-sapabap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

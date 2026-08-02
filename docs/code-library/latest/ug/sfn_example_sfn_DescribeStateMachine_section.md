---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sfn_example_sfn_DescribeStateMachine_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DescribeStateMachine` with an AWS SDK
<a name="sfn_example_sfn_DescribeStateMachine_section"></a>

The following code examples show how to use `DescribeStateMachine`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](sfn_example_sfn_Scenario_GetStartedStateMachines_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/StepFunctions#code-examples).

```
    /// <summary>
    /// Retrieve information about the specified Step Functions state machine.
    /// </summary>
    /// <param name="StateMachineArn">The Amazon Resource Name (ARN) of the
    /// Step Functions state machine to retrieve.</param>
    /// <returns>Information about the specified Step Functions state machine.</returns>
    public async Task<DescribeStateMachineResponse> DescribeStateMachineAsync(string StateMachineArn)
    {
        var response = await _amazonStepFunctions.DescribeStateMachineAsync(new DescribeStateMachineRequest { StateMachineArn = StateMachineArn });
        return response;
    }
```
+  For API details, see [DescribeStateMachine](https://docs.aws.amazon.com/goto/DotNetSDKV3/states-2016-11-23/DescribeStateMachine) in *AWS SDK for .NET API Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/stepfunctions#code-examples).

```
    public static void describeStateMachine(SfnClient sfnClient, String stateMachineArn) {
        try {
            DescribeStateMachineRequest stateMachineRequest = DescribeStateMachineRequest.builder()
                .stateMachineArn(stateMachineArn)
                .build();

            DescribeStateMachineResponse response = sfnClient.describeStateMachine(stateMachineRequest);
            System.out.println("The name of the State machine is " + response.name());
            System.out.println("The status of the State machine is " + response.status());
            System.out.println("The ARN value of the State machine is " + response.stateMachineArn());
            System.out.println("The role ARN value is " + response.roleArn());

        } catch (SfnException e) {
            System.err.println(e.getMessage());
        }
    }
```
+  For API details, see [DescribeStateMachine](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/DescribeStateMachine) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/stepfunctions#code-examples).

```
suspend fun describeStateMachine(stateMachineArnVal: String?) {
    val stateMachineRequest =
        DescribeStateMachineRequest {
            stateMachineArn = stateMachineArnVal
        }
    SfnClient.fromEnvironment { region = "us-east-1" }.use { sfnClient ->
        val response = sfnClient.describeStateMachine(stateMachineRequest)
        println("The name of the State machine is ${response.name}")
        println("The status of the State machine is ${response.status}")
        println("The ARN value of the State machine is ${response.stateMachineArn}")
        println("The role ARN value is ${response.roleArn}")
    }
}
```
+  For API details, see [DescribeStateMachine](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/stepfunctions#code-examples).

```
class StateMachine:
    """Encapsulates Step Functions state machine actions."""

    def __init__(self, stepfunctions_client):
        """
        :param stepfunctions_client: A Boto3 Step Functions client.
        """
        self.stepfunctions_client = stepfunctions_client

    def describe(self, state_machine_arn):
        """
        Get data about a state machine.

        :param state_machine_arn: The ARN of the state machine to look up.
        :return: The retrieved state machine data.
        """
        try:
            response = self.stepfunctions_client.describe_state_machine(
                stateMachineArn=state_machine_arn
            )
        except ClientError as err:
            logger.error(
                "Couldn't describe state machine %s. Here's why: %s: %s",
                state_machine_arn,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response
```
+  For API details, see [DescribeStateMachine](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/DescribeStateMachine) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

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

------

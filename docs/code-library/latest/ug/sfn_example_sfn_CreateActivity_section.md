---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/sfn_example_sfn_CreateActivity_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateActivity` with an AWS SDK
<a name="sfn_example_sfn_CreateActivity_section"></a>

The following code examples show how to use `CreateActivity`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](sfn_example_sfn_Scenario_GetStartedStateMachines_section.md)

------
#### [ .NET ]

**SDK for .NET**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/StepFunctions#code-examples).

```
    /// <summary>
    /// Create a Step Functions activity using the supplied name.
    /// </summary>
    /// <param name="activityName">The name for the new Step Functions activity.</param>
    /// <returns>The Amazon Resource Name (ARN) for the new activity.</returns>
    public async Task<string> CreateActivity(string activityName)
    {
        var response = await _amazonStepFunctions.CreateActivityAsync(new CreateActivityRequest { Name = activityName });
        return response.ActivityArn;
    }
```
+  For API details, see [CreateActivity](https://docs.aws.amazon.com/goto/DotNetSDKV3/states-2016-11-23/CreateActivity) in *AWS SDK for .NET API Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/stepfunctions#code-examples).

```
    public static String createActivity(SfnClient sfnClient, String activityName) {
        try {
            CreateActivityRequest activityRequest = CreateActivityRequest.builder()
                .name(activityName)
                .build();

            CreateActivityResponse response = sfnClient.createActivity(activityRequest);
            return response.activityArn();

        } catch (SfnException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
        return "";
    }
```
+  For API details, see [CreateActivity](https://docs.aws.amazon.com/goto/SdkForJavaV2/states-2016-11-23/CreateActivity) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/stepfunctions#code-examples).

```
suspend fun createActivity(activityName: String): String? {
    val activityRequest =
        CreateActivityRequest {
            name = activityName
        }

    SfnClient.fromEnvironment { region = "us-east-1" }.use { sfnClient ->
        val response = sfnClient.createActivity(activityRequest)
        return response.activityArn
    }
}
```
+  For API details, see [CreateActivity](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/stepfunctions#code-examples).

```
class Activity:
    """Encapsulates Step Function activity actions."""

    def __init__(self, stepfunctions_client):
        """
        :param stepfunctions_client: A Boto3 Step Functions client.
        """
        self.stepfunctions_client = stepfunctions_client

    def create(self, name):
        """
        Create an activity.

        :param name: The name of the activity to create.
        :return: The Amazon Resource Name (ARN) of the newly created activity.
        """
        try:
            response = self.stepfunctions_client.create_activity(name=name)
        except ClientError as err:
            logger.error(
                "Couldn't create activity %s. Here's why: %s: %s",
                name,
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            raise
        else:
            return response["activityArn"]
```
+  For API details, see [CreateActivity](https://docs.aws.amazon.com/goto/boto3/states-2016-11-23/CreateActivity) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

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

------

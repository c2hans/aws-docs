---
source_url: https://docs.aws.amazon.com/autoscaling/ec2/userguide/example_auto-scaling_SetDesiredCapacity_section.html
---

# Use `SetDesiredCapacity` with an AWS SDK or CLI
<a name="example_auto-scaling_SetDesiredCapacity_section"></a>

The following code examples show how to use `SetDesiredCapacity`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](example_auto-scaling_Scenario_GroupsAndInstances_section.md)

------
#### [ .NET ]

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/AutoScaling#code-examples).

```
    /// <summary>
    /// Set the desired capacity of an Auto Scaling group.
    /// </summary>
    /// <param name="groupName">The name of the Auto Scaling group.</param>
    /// <param name="desiredCapacity">The desired capacity for the Auto
    /// Scaling group.</param>
    /// <returns>A Boolean value indicating the success of the action.</returns>
    public async Task<bool> SetDesiredCapacityAsync(
        string groupName,
        int desiredCapacity)
    {
        var capacityRequest = new SetDesiredCapacityRequest
        {
            AutoScalingGroupName = groupName,
            DesiredCapacity = desiredCapacity,
        };

        var response = await _amazonAutoScaling.SetDesiredCapacityAsync(capacityRequest);
        Console.WriteLine($"You have set the DesiredCapacity to {desiredCapacity}.");

        return response.HttpStatusCode == System.Net.HttpStatusCode.OK;
    }
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/goto/DotNetSDKV4/autoscaling-2011-01-01/SetDesiredCapacity) in *AWS SDK for .NET API Reference*.

------
#### [ C\+\+ ]

**SDK for C\+\+**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/cpp/example_code/autoscaling#code-examples).

```
        Aws::Client::ClientConfiguration clientConfig;
        // Optional: Set to the AWS Region (overrides config file).
        // clientConfig.region = "us-east-1";

    Aws::AutoScaling::AutoScalingClient autoScalingClient(clientConfig);

        Aws::AutoScaling::Model::SetDesiredCapacityRequest request;
        request.SetAutoScalingGroupName(groupName);
        request.SetDesiredCapacity(2);

        Aws::AutoScaling::Model::SetDesiredCapacityOutcome outcome =
                autoScalingClient.SetDesiredCapacity(request);

        if (!outcome.IsSuccess()) {
            std::cerr << "Error with AutoScaling::SetDesiredCapacityRequest. "
                      << outcome.GetError().GetMessage()
                      << std::endl;

        }
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/goto/SdkForCpp/autoscaling-2011-01-01/SetDesiredCapacity) in *AWS SDK for C\+\+ API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To set the desired capacity for an Auto Scaling group**
This example sets the desired capacity for the specified Auto Scaling group.

```
aws autoscaling set-desired-capacity \
    --auto-scaling-group-name {{my-asg}} \
    --desired-capacity {{2}} \
    --honor-cooldown
```
This command returns to the prompt if successful.
+  For API details, see [SetDesiredCapacity](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/autoscaling/set-desired-capacity.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/autoscale#code-examples).

```
    public static void setDesiredCapacity(AutoScalingClient autoScalingClient, String groupName) {
        try {
            SetDesiredCapacityRequest capacityRequest = SetDesiredCapacityRequest.builder()
                    .autoScalingGroupName(groupName)
                    .desiredCapacity(2)
                    .build();

            autoScalingClient.setDesiredCapacity(capacityRequest);
            System.out.println("You have set the DesiredCapacity to 2");

        } catch (AutoScalingException e) {
            System.err.println(e.awsErrorDetails().errorMessage());
            System.exit(1);
        }
    }
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/goto/SdkForJavaV2/autoscaling-2011-01-01/SetDesiredCapacity) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Kotlin ]

**SDK for Kotlin**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/kotlin/services/autoscale#code-examples).

```
suspend fun setDesiredCapacity(groupName: String) {
    val capacityRequest =
        SetDesiredCapacityRequest {
            autoScalingGroupName = groupName
            desiredCapacity = 2
        }

    AutoScalingClient { region = "us-east-1" }.use { autoScalingClient ->
        autoScalingClient.setDesiredCapacity(capacityRequest)
        println("You set the DesiredCapacity to 2")
    }
}
```
+  For API details, see [SetDesiredCapacity](https://sdk.amazonaws.com/kotlin/api/latest/index.html) in *AWS SDK for Kotlin API reference*.

------
#### [ PHP ]

**SDK for PHP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/php/example_code/auto-scaling#code-examples).

```
    public function setDesiredCapacity($autoScalingGroupName, $desiredCapacity)
    {
        return $this->autoScalingClient->setDesiredCapacity([
            'AutoScalingGroupName' => $autoScalingGroupName,
            'DesiredCapacity' => $desiredCapacity,
        ]);
    }
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/goto/SdkForPHPV3/autoscaling-2011-01-01/SetDesiredCapacity) in *AWS SDK for PHP API Reference*.

------
#### [ PowerShell ]

**Tools for PowerShell V4**
**Example 1: This example sets the size of the specified Auto Scaling group.**

```
Set-ASDesiredCapacity -AutoScalingGroupName my-asg -DesiredCapacity 2
```
**Example 2: This example sets the size of the specified Auto Scaling group and waits for the cooldown period to complete before scaling to the new size.**

```
Set-ASDesiredCapacity -AutoScalingGroupName my-asg -DesiredCapacity 2 -HonorCooldown $true
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/powershell/v4/reference) in *AWS Tools for PowerShell Cmdlet Reference (V4)*.

**Tools for PowerShell V5**
**Example 1: This example sets the size of the specified Auto Scaling group.**

```
Set-ASDesiredCapacity -AutoScalingGroupName my-asg -DesiredCapacity 2
```
**Example 2: This example sets the size of the specified Auto Scaling group and waits for the cooldown period to complete before scaling to the new size.**

```
Set-ASDesiredCapacity -AutoScalingGroupName my-asg -DesiredCapacity 2 -HonorCooldown $true
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/powershell/v5/reference) in *AWS Tools for PowerShell Cmdlet Reference (V5)*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/auto-scaling#code-examples).

```
class AutoScalingWrapper:
    """Encapsulates Amazon EC2 Auto Scaling actions."""

    def __init__(self, autoscaling_client):
        """
        :param autoscaling_client: A Boto3 Amazon EC2 Auto Scaling client.
        """
        self.autoscaling_client = autoscaling_client

    def set_desired_capacity(self, group_name: str, capacity: int) -> None:
        """
        Sets the desired capacity of the group. Amazon EC2 Auto Scaling tries to keep the
        number of running instances equal to the desired capacity.

        :param group_name: The name of the group to update.
        :param capacity: The desired number of running instances.
        :return: None
        :raises ClientError: If there is an error setting the desired capacity.
        """
        try:
            self.autoscaling_client.set_desired_capacity(
                AutoScalingGroupName=group_name,
                DesiredCapacity=capacity,
                HonorCooldown=False,
            )
            logger.info(
                f"Successfully set desired capacity of {capacity} for Auto Scaling group '{group_name}'."
            )

        except ClientError as err:
            error_code = err.response["Error"]["Code"]
            logger.error(
                f"Failed to set desired capacity for Auto Scaling group '{group_name}'."
            )
            if error_code == "ScalingActivityInProgress":
                logger.error(
                    f"A scaling activity is currently in progress for the Auto Scaling group '{group_name}'. "
                    "Please wait for the activity to complete before attempting to set the desired capacity."
                )
            logger.error(f"Full error:\n\t{err}")
            raise
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/goto/boto3/autoscaling-2011-01-01/SetDesiredCapacity) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ Rust ]

**SDK for Rust**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/rustv1/examples/auto-scaling#code-examples).

```
    pub async fn scale_desired_capacity(&self, capacity: i32) -> Result<(), ScenarioError> {
        // 7. SetDesiredCapacity: set desired capacity to 2.
        //   Wait for a second instance to launch.
        let update_group = self
            .autoscaling
            .set_desired_capacity()
            .auto_scaling_group_name(self.auto_scaling_group_name.clone())
            .desired_capacity(capacity)
            .send()
            .await;
        if let Err(err) = update_group {
            return Err(ScenarioError::new(
                format!("Failed to update group to desired capacity ({capacity}))").as_str(),
                &err,
            ));
        }
        Ok(())
    }
```
+  For API details, see [SetDesiredCapacity](https://docs.rs/aws-sdk-autoscaling/latest/aws_sdk_autoscaling/client/struct.Client.html#method.set_desired_capacity) in *AWS SDK for Rust API reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/asc#code-examples).

```
    " Example: iv_group_name = 'my-auto-scaling-group'
    " Example: iv_capacity = 2

    TRY.
        ao_asc->setdesiredcapacity(
          iv_autoscalinggroupname = iv_group_name
          iv_desiredcapacity = iv_capacity
          iv_honorcooldown = abap_false ).

        MESSAGE 'Desired capacity set successfully' TYPE 'I'.

      CATCH /aws1/cx_ascscaactivityinprg00 INTO DATA(lo_activity_in_progress).
        RAISE EXCEPTION lo_activity_in_progress.
      CATCH /aws1/cx_rt_generic INTO DATA(lo_generic_exception).
        RAISE EXCEPTION lo_generic_exception.
    ENDTRY.
```
+  For API details, see [SetDesiredCapacity](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.

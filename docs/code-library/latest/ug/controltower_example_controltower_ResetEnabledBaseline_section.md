---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/controltower_example_controltower_ResetEnabledBaseline_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ResetEnabledBaseline` with an AWS SDK or CLI
<a name="controltower_example_controltower_ResetEnabledBaseline_section"></a>

The following code examples show how to use `ResetEnabledBaseline`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](controltower_example_controltower_Scenario_section.md)

------
#### [ .NET ]

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/ControlTower#code-examples).

```
    /// <summary>
    /// Reset an enabled baseline for a specific target.
    /// </summary>
    /// <param name="enabledBaselineIdentifier">The identifier of the enabled baseline to reset.</param>
    /// <returns>The operation ID.</returns>
    public async Task<string> ResetEnabledBaselineAsync(string enabledBaselineIdentifier)
    {
        try
        {
            var request = new ResetEnabledBaselineRequest
            {
                EnabledBaselineIdentifier = enabledBaselineIdentifier
            };

            var response = await _controlTowerService.ResetEnabledBaselineAsync(request);
            var operationId = response.OperationIdentifier;

            // Wait for operation to complete
            while (true)
            {
                var status = await GetBaselineOperationAsync(operationId);
                Console.WriteLine($"Baseline operation status: {status}");
                if (status == BaselineOperationStatus.SUCCEEDED || status == BaselineOperationStatus.FAILED)
                {
                    break;
                }
                await Task.Delay(30000); // Wait 30 seconds
            }

            return operationId;
        }
        catch (Amazon.ControlTower.Model.ResourceNotFoundException)
        {
            Console.WriteLine("Target not found, unable to reset enabled baseline.");
            throw;
        }
        catch (AmazonControlTowerException ex)
        {
            Console.WriteLine($"Couldn't reset enabled baseline. Here's why: {ex.ErrorCode}: {ex.Message}");
            throw;
        }
    }
```
+  For API details, see [ResetEnabledBaseline](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ResetEnabledBaseline) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To reset a Control Tower enabled baseline**
The following `reset-enabled-baseline` example resets an AWS Control Tower enabled baseline.

```
aws controltower reset-enabled-baseline \
    --enabled-baseline-identifier {{arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2}}
```
Output:

```
{
    "operationIdentifier": "214cde95-5c39-46b9-b429-4fad550a7096"
}
```
For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html) in the *AWS Control Tower User Guide*.
+  For API details, see [ResetEnabledBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/reset-enabled-baseline.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/controltower#code-examples).

```
    /**
     * Resets an enabled baseline for a specific target.
     *
     * @param enabledBaselineIdentifier the identifier of the enabled baseline to reset
     * @return the operation identifier
     * @throws ControlTowerException if a service-specific error occurs
     * @throws SdkException          if an SDK error occurs
     */
    public CompletableFuture<String> resetEnabledBaselineAsync(String enabledBaselineIdentifier) {

        System.out.println("Starting reset of enabled baseline…");
        System.out.println("This operation will check the status every 15 seconds until it completes (SUCCEEDED or FAILED).");

        ResetEnabledBaselineRequest request = ResetEnabledBaselineRequest.builder()
                .enabledBaselineIdentifier(enabledBaselineIdentifier)
                .build();

        return getAsyncClient().resetEnabledBaseline(request)
                .thenCompose(response -> {
                    String operationId = response.operationIdentifier();
                    System.out.println("Reset enabled baseline operation ID: " + operationId);

                    // Polling loop
                    CompletableFuture<String> resultFuture = new CompletableFuture<>();

                    Runnable poller = new Runnable() {
                        @Override
                        public void run() {
                            getBaselineOperationAsync(operationId)
                                    .thenAccept(statusObj -> {
                                        String status = statusObj.toString(); // Convert enum/status to string for printing
                                        System.out.println("Current baseline operation status: " + status + " → waiting for SUCCEEDED or FAILED...");

                                        if ("SUCCEEDED".equalsIgnoreCase(status) || "FAILED".equalsIgnoreCase(status)) {
                                            System.out.println("Baseline operation finished with status: " + status);
                                            resultFuture.complete(operationId);
                                        } else {
                                            // Schedule next poll in 15 seconds
                                            CompletableFuture.delayedExecutor(15, TimeUnit.SECONDS)
                                                    .execute(this);
                                        }
                                    })
                                    .exceptionally(ex -> {
                                        System.out.println("Error checking baseline operation status: " + ex.getMessage());
                                        resultFuture.completeExceptionally(ex);
                                        return null;
                                    });
                        }
                    };

                    // Start first poll immediately
                    poller.run();

                    return resultFuture;
                })
                .exceptionally(ex -> {
                    Throwable cause = ex.getCause() != null ? ex.getCause() : ex;

                    if (cause instanceof ControlTowerException e) {
                        String errorCode = e.awsErrorDetails() != null ? e.awsErrorDetails().errorCode() : "UNKNOWN";
                        String errorMessage = e.awsErrorDetails() != null ? e.awsErrorDetails().errorMessage() : e.getMessage();

                        System.out.println("ControlTowerException caught: Code=" + errorCode + ", Message=" + errorMessage);
                        return null;
                    }

                    if (cause instanceof SdkException sdkEx) {
                        System.out.println("SDK exception caught: " + sdkEx.getMessage());
                        return null;
                    }

                    System.out.println("Unexpected exception resetting baseline: " + cause.getMessage());
                    return null;
                });
    }
```
+  For API details, see [ResetEnabledBaseline](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ResetEnabledBaseline) in *AWS SDK for Java 2.x API Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/controltower#code-examples).

```
class ControlTowerWrapper:
    """Encapsulates AWS Control Tower and Control Catalog functionality."""

    def __init__(
        self, controltower_client: boto3.client, controlcatalog_client: boto3.client
    ):
        """
        :param controltower_client: A Boto3 Amazon ControlTower client.
        :param controlcatalog_client: A Boto3 Amazon ControlCatalog client.
        """
        self.controltower_client = controltower_client
        self.controlcatalog_client = controlcatalog_client

    @classmethod
    def from_client(cls):
        controltower_client = boto3.client("controltower")
        controlcatalog_client = boto3.client("controlcatalog")
        return cls(controltower_client, controlcatalog_client)

    def reset_enabled_baseline(self, enabled_baseline_identifier: str):
        """
        Resets an enabled baseline for a specific target.

        :param enabled_baseline_identifier: The identifier of the enabled baseline to reset.
        :return: The operation ID.
        :raises ClientError: If resetting the baseline fails.
        """
        try:
            response = self.controltower_client.reset_enabled_baseline(
                enabledBaselineIdentifier=enabled_baseline_identifier
            )
            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)
            return operation_id
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error("Target not found.")
            else:
                logger.error(
                    "Couldn't reset enabled baseline. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ResetEnabledBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ResetEnabledBaseline) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ctt#code-examples).

```
    " Reset the enabled baseline
    DATA(lo_output) = io_ctt->resetenabledbaseline(
      iv_enabledbaselineidentifier = iv_enabled_baseline_identifier
    ).

    DATA(lv_operation_id) = lo_output->get_operationidentifier( ).

    " Wait for operation to complete
    DATA lv_status TYPE /aws1/cttbaselineopstatus.
    DO 100 TIMES.
      lv_status = get_baseline_operation(
        io_ctt = io_ctt
        iv_operation_id = lv_operation_id
      ).

      DATA(lv_msg) = |Baseline operation status: { lv_status }|.
      MESSAGE lv_msg TYPE 'I'.

      IF lv_status = 'SUCCEEDED' OR lv_status = 'FAILED'.
        EXIT.
      ENDIF.

      " Wait 30 seconds
      WAIT UP TO 30 SECONDS.
    ENDDO.

    ov_operation_id = lv_operation_id.
    MESSAGE 'Baseline reset successfully.' TYPE 'I'.
```
+  For API details, see [ResetEnabledBaseline](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

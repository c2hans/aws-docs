---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/controltower_example_controltower_EnableBaseline_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `EnableBaseline` with an AWS SDK or CLI
<a name="controltower_example_controltower_EnableBaseline_section"></a>

The following code examples show how to use `EnableBaseline`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](controltower_example_controltower_Scenario_section.md)

------
#### [ .NET ]

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/ControlTower#code-examples).

```
    /// <summary>
    /// Enable a baseline for the specified target.
    /// </summary>
    /// <param name="targetIdentifier">The ARN of the target.</param>
    /// <param name="baselineIdentifier">The identifier of baseline to enable.</param>
    /// <param name="baselineVersion">The version of baseline to enable.</param>
    /// <param name="identityCenterBaseline">The identifier of identity center baseline if it is enabled.</param>
    /// <returns>The enabled baseline ARN or null.</returns>
    public async Task<string?> EnableBaselineAsync(string targetIdentifier, string baselineIdentifier, string baselineVersion, string identityCenterBaseline)
    {
        try
        {
            var parameters = new List<EnabledBaselineParameter>();
            if (!string.IsNullOrEmpty(identityCenterBaseline))
            {
                parameters.Add(
                    new EnabledBaselineParameter
                    {
                        Key = "IdentityCenterEnabledBaselineArn",
                        Value = identityCenterBaseline
                    });
            }
            var request = new EnableBaselineRequest
            {
                BaselineIdentifier = baselineIdentifier,
                BaselineVersion = baselineVersion,
                TargetIdentifier = targetIdentifier,
                Parameters = parameters
            };

            var response = await _controlTowerService.EnableBaselineAsync(request);
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

            return response.Arn;
        }
        catch (ValidationException ex)
        {
            if (ex.Message.Contains("already enabled"))
                Console.WriteLine("Baseline is already enabled for this target");
            else { Console.WriteLine(ex.Message); }
            // Write the message and return null if baseline cannot be enabled.
            return null;
        }
        catch (AmazonControlTowerException ex)
        {
            Console.WriteLine($"Couldn't enable baseline. Here's why: {ex.ErrorCode}: {ex.Message}");
            throw;
        }
    }
```
+  For API details, see [EnableBaseline](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/EnableBaseline) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**Example 1: To enable a Control Tower baseline that is disabled**
The following `enable-baseline` example enables an AWS Control Tower baseline if baseline `IdentityCenterBaseline` is disabled.

```
aws controltower enable-baseline \
    --baseline-identifier {{arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2}} \
    --baseline-version {{4.0}} \
    --target-identifier {{arn:aws:organizations::123456789012:ou/o-s64ryixxxx/ou-oq9f-i5wnxxxx}}
```
Output:

```
{
    "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2",
    "operationIdentifier": "51e190ac-8a37-4f6d-b63c-fb5104b5db38"
}
```
For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html) in the *AWS Control Tower User Guide*.
**Example 2: To enable a Control Tower baseline that is enabled**
The following `enable-baseline` example enables an AWS Control Tower baseline if baseline `IdentityCenterBaseline` is enabled.

```
aws controltower enable-baseline \
    --baseline-identifier {{arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2}} \
    --baseline-version {{4.0}} \
    --target-identifier {{arn:aws:organizations::123456789012:ou/o-s64ryixxxx/ou-oqxx-i5wnxxxx}} \
    --parameters '{{[{"key":"IdentityCenterEnabledBaselineArn","value":"arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XAJNZNCBC1I386C7B"}]}}'
```
Output:

```
{
    "arn": "arn:aws:controltower:us-east-1:123456789012:enabledbaseline/XOM12BEL4YD578CQ2",
    "operationIdentifier": "51e190ac-8a37-4f6d-b63c-fb5104b5db38"
}
```
For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html) in the *AWS Control Tower User Guide*.
+  For API details, see [EnableBaseline](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/enable-baseline.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/controltower#code-examples).

```
    /**
     * Asynchronously enables a baseline for the specified target if not already enabled.
     *
     * @param targetIdentifier       The ARN of the target (OU or account).
     * @param baselineIdentifier     The baseline definition ARN to enable.
     * @param baselineVersion        The baseline version to enable.
     * @return A CompletableFuture containing the enabled baseline ARN, or null if already enabled.
     */
    public CompletableFuture<String> enableBaselineAsync(
            String targetIdentifier,
            String baselineIdentifier,
            String baselineVersion
    ) {
        EnableBaselineRequest request = EnableBaselineRequest.builder()
                .baselineIdentifier(baselineIdentifier)
                .baselineVersion(baselineVersion)
                .targetIdentifier(targetIdentifier)
                .build();

        return getAsyncClient().enableBaseline(request)
                .handle((resp, exception) -> {
                    if (exception != null) {
                        Throwable cause = exception.getCause() != null ? exception.getCause() : exception;
                        if (cause instanceof ControlTowerException e) {
                            String code = e.awsErrorDetails() != null ? e.awsErrorDetails().errorCode() : "UNKNOWN";
                            String msg = e.awsErrorDetails() != null ? e.awsErrorDetails().errorMessage() : e.getMessage();

                            if ("ValidationException".equals(code) && msg.contains("already enabled")) {
                                System.out.println("Baseline is already enabled for this target → fetching ARN...");
                                return fetchEnabledBaselineArn(targetIdentifier, baselineIdentifier)
                                        .join(); // fetch existing ARN synchronously
                            }

                            throw new RuntimeException("Error enabling baseline: " + code + " - " + msg, e);
                        }

                        throw new RuntimeException("Unexpected error enabling baseline: " + cause.getMessage(), cause);
                    }

                    return resp;
                })
                .thenCompose(result -> {
                    if (result instanceof EnableBaselineResponse resp) {
                        String operationId = resp.operationIdentifier();
                        String enabledBaselineArn = resp.arn();
                        System.out.println("Baseline enable started. ARN: " + enabledBaselineArn
                                + ", operation ID: " + operationId);

                        // Inline polling
                        return CompletableFuture.supplyAsync(() -> {
                            while (true) {
                                GetBaselineOperationRequest opReq = GetBaselineOperationRequest.builder()
                                        .operationIdentifier(operationId)
                                        .build();

                                GetBaselineOperationResponse opResp = getAsyncClient().getBaselineOperation(opReq).join();
                                BaselineOperation op = opResp.baselineOperation();
                                BaselineOperationStatus status = op.status();
                                System.out.println("Operation " + operationId + " status: " + status);

                                if (status == BaselineOperationStatus.SUCCEEDED) {
                                    return enabledBaselineArn;
                                } else if (status == BaselineOperationStatus.FAILED) {
                                    String opId = op.operationIdentifier();
                                    String reason = op.statusMessage() != null ? op.statusMessage() : "No failure reason provided";
                                    throw new RuntimeException("Baseline operation failed (ID: " + opId + "), status: "
                                            + status + ", reason: " + reason);
                                }

                                try {
                                    Thread.sleep(Duration.ofSeconds(15).toMillis());
                                } catch (InterruptedException e) {
                                    Thread.currentThread().interrupt();
                                    throw new RuntimeException(e);
                                }
                            }
                        });
                    } else if (result instanceof String existingArn) {
                        // Already enabled branch
                        return CompletableFuture.completedFuture(existingArn);
                    }

                    return CompletableFuture.completedFuture(null);
                });
    }

    /**
     * Fetches the ARN of an already-enabled baseline for the target asynchronously.
     */
    private CompletableFuture<String> fetchEnabledBaselineArn(String targetIdentifier, String baselineIdentifier) {
        return getAsyncClient().listEnabledBaselines(ListEnabledBaselinesRequest.builder().build())
                .thenApply(listResp -> {
                    for (EnabledBaselineSummary eb : listResp.enabledBaselines()) {
                        if (baselineIdentifier.equals(eb.baselineIdentifier())
                                && targetIdentifier.equals(eb.targetIdentifier())) {
                            return eb.arn();
                        }
                    }
                    return null; // not yet available
                });
    }
```
+  For API details, see [EnableBaseline](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/EnableBaseline) in *AWS SDK for Java 2.x API Reference*.

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

    def enable_baseline(
        self,
        target_identifier: str,
        identity_center_baseline: str,
        baseline_identifier: str,
        baseline_version: str,
    ):
        """
        Enables a baseline for the specified target if it's not already enabled.

        :param target_identifier: The ARN of the target.
        :param baseline_identifier: The identifier of baseline to enable.
        :param identity_center_baseline: The identifier of identity center baseline if it is enabled.
        :param baseline_version: The version of baseline to enable.
        :return: The enabled baseline ARN or None if already enabled.
        :raises ClientError: If enabling the baseline fails for reasons other than it being already enabled.
        """
        try:
            # Only include parameters if identity_center_baseline is not empty
            parameters = []
            if identity_center_baseline:
                parameters = [
                    {
                        "key": "IdentityCenterEnabledBaselineArn",
                        "value": identity_center_baseline,
                    }
                ]

            response = self.controltower_client.enable_baseline(
                baselineIdentifier=baseline_identifier,
                baselineVersion=baseline_version,
                targetIdentifier=target_identifier,
                parameters=parameters,
            )

            operation_id = response["operationIdentifier"]
            while True:
                status = self.get_baseline_operation(operation_id)
                print(f"Baseline operation status: {status}")
                if status in ["SUCCEEDED", "FAILED"]:
                    break
                time.sleep(30)

            return response["arn"]
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                if "already enabled" in err.response["Error"]["Message"]:
                    print("Baseline is already enabled for this target")
                else:
                    print(
                        "Unable to enable baseline due to validation exception: %s: %s",
                        err.response["Error"]["Code"],
                        err.response["Error"]["Message"],
                    )
            logger.error(
                "Couldn't enable baseline. Here's why: %s: %s",
                err.response["Error"]["Code"],
                err.response["Error"]["Message"],
            )
            return None
```
+  For API details, see [EnableBaseline](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/EnableBaseline) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ctt#code-examples).

```
    " Prepare parameters for enabling baseline
    DATA lt_parameters TYPE /aws1/cl_cttenbdbaselineparam=>tt_enabledbaselineparameters.

    " Add Identity Center baseline parameter if provided
    IF iv_identity_center_baseline IS NOT INITIAL.
      " Create a JSON document with the baseline ARN value
      DATA(lv_json) = |\{ "IdentityCenterEnabledBaselineArn": "{ iv_identity_center_baseline }" \}|.
      DATA(lo_param) = NEW /aws1/cl_cttenbdbaselineparam(
        iv_key = 'IdentityCenterEnabledBaselineArn'
        io_value = /aws1/cl_rt_document=>from_json_str( lv_json )
      ).
      APPEND lo_param TO lt_parameters.
    ENDIF.

    " Enable the baseline
    DATA(lo_output) = io_ctt->enablebaseline(
      iv_baselineidentifier = iv_baseline_identifier
      iv_baselineversion    = iv_baseline_version
      iv_targetidentifier   = iv_target_identifier
      it_parameters         = lt_parameters
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

    ov_enabled_baseline_arn = lo_output->get_arn( ).
    MESSAGE 'Baseline enabled successfully.' TYPE 'I'.
```
+  For API details, see [EnableBaseline](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

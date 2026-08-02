---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/controltower_example_controltower_ListBaselines_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListBaselines` with an AWS SDK or CLI
<a name="controltower_example_controltower_ListBaselines_section"></a>

The following code examples show how to use `ListBaselines`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn the basics](controltower_example_controltower_Scenario_section.md)

------
#### [ .NET ]

**SDK for .NET (v4)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv4/ControlTower#code-examples).

```
    /// <summary>
    /// List all baselines.
    /// </summary>
    /// <returns>A list of baseline summaries.</returns>
    public async Task<List<BaselineSummary>> ListBaselinesAsync()
    {
        try
        {
            var baselines = new List<BaselineSummary>();

            var baselinesPaginator = _controlTowerService.Paginators.ListBaselines(new ListBaselinesRequest());

            await foreach (var response in baselinesPaginator.Responses)
            {
                baselines.AddRange(response.Baselines);
            }

            return baselines;
        }
        catch (AmazonControlTowerException ex)
        {
            Console.WriteLine($"Couldn't list baselines. Here's why: {ex.ErrorCode}: {ex.Message}");
            throw;
        }
    }
```
+  For API details, see [ListBaselines](https://docs.aws.amazon.com/goto/DotNetSDKV4/controltower-2018-05-10/ListBaselines) in *AWS SDK for .NET API Reference*.

------
#### [ CLI ]

**AWS CLI**
**To list Control Tower baselines**
The following `list-baselines` example lists all available AWS Control Tower baselines.

```
aws controltower list-baselines
```
Output:

```
{
    "baselines": [
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/4T4HA1KMO10S6311",
            "description": "Sets up resources to monitor security and compliance of accounts in your organization.",
            "name": "AuditBaseline"
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/J8HX46AHS5MIKQPD",
            "description": "Sets up a central repository for logs of API activities and resource configurations from accounts in your organization.",
            "name": "LogArchiveBaseline"
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/LN25R72TTG6IGPTQ",
            "description": "Sets up shared resources for AWS Identity Center, which prepares the AWSControlTowerBaseline to set up Identity Center access for accounts.",
            "name": "IdentityCenterBaseline"
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/17BSJV3IGJ2QSGA2",
            "description": "Sets up resources and mandatory controls for member accounts within the target OU, required for AWS Control Tower governance.",
            "name": "AWSControlTowerBaseline"
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/3WPD0NA6TJ9AOMU2",
            "description": "Sets up a central AWS Backup vault in your organization.",
            "name": "BackupCentralVaultBaseline"
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/H6C5JFCJJ3CPU3J5",
            "description": "Sets up AWS Backup Audit Manager.",
            "name": "BackupAdminBaseline"
        },
        {
            "arn": "arn:aws:controltower:us-east-1::baseline/APO9ATVPBKFRRGLK",
            "description": "Sets up a local AWS Backup vault and attaches multiple AWS Backup plans.",
            "name": "BackupBaseline"
        }
    ]
}
```
For more information, see [Types of baselines](https://docs.aws.amazon.com/controltower/latest/userguide/types-of-baselines.html) in the *AWS Control Tower User Guide*.
+  For API details, see [ListBaselines](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/controltower/list-baselines.html) in *AWS CLI Command Reference*.

------
#### [ Java ]

**SDK for Java 2.x**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javav2/example_code/controltower#code-examples).

```
    /**
     * Lists all available baselines using pagination to retrieve complete results.
     *
     * @return a list of all baselines
     * @throws ControlTowerException if a service-specific error occurs
     * @throws SdkException          if an SDK error occurs
     */
    public CompletableFuture<List<BaselineSummary>> listBaselinesAsync() {
        System.out.println("Starting list baselines paginator…");
        ListBaselinesRequest request = ListBaselinesRequest.builder().build();
        ListBaselinesPublisher paginator =
                getAsyncClient().listBaselinesPaginator(request);

        List<BaselineSummary> baselines = new ArrayList<>();
        return paginator.subscribe(response -> {
                    if (response.baselines() != null && !response.baselines().isEmpty()) {
                        response.baselines().forEach(baseline -> {
                            baselines.add(baseline);
                        });
                    } else {
                        System.out.println("Page contained no baselines.");
                    }
                })
                .thenRun(() ->
                        System.out.println("Successfully listed baselines. Total: " + baselines.size())
                )
                .thenApply(v -> baselines)
                .exceptionally(ex -> {
                    Throwable cause = ex.getCause() != null ? ex.getCause() : ex;

                    if (cause instanceof ControlTowerException e) {
                        String errorCode = e.awsErrorDetails().errorCode();

                        if ("AccessDeniedException".equals(errorCode)) {
                            throw new CompletionException(
                                    "Access denied when listing baselines: %s".formatted(e.getMessage()),
                                    e
                            );
                        }

                        throw new CompletionException(
                                "Error listing baselines: %s".formatted(e.getMessage()),
                                e
                        );
                    }

                    if (cause instanceof SdkException) {
                        throw new CompletionException(
                                "SDK error listing baselines: %s".formatted(cause.getMessage()),
                                cause
                        );
                    }

                    throw new CompletionException("Failed to list baselines", cause);
                });
    }
```
+  For API details, see [ListBaselines](https://docs.aws.amazon.com/goto/SdkForJavaV2/controltower-2018-05-10/ListBaselines) in *AWS SDK for Java 2.x API Reference*.

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

    def list_baselines(self):
        """
        Lists all baselines.

        :return: List of baselines.
        :raises ClientError: If the listing operation fails.
        """
        try:
            paginator = self.controltower_client.get_paginator("list_baselines")
            baselines = []
            for page in paginator.paginate():
                baselines.extend(page["baselines"])
            return baselines

        except ClientError as err:
            if err.response["Error"]["Code"] == "AccessDeniedException":
                logger.error(
                    "Access denied. Please ensure you have the necessary permissions."
                )
            else:
                logger.error(
                    "Couldn't list baselines. Here's why: %s: %s",
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListBaselines](https://docs.aws.amazon.com/goto/boto3/controltower-2018-05-10/ListBaselines) in *AWS SDK for Python (Boto3) API Reference*.

------
#### [ SAP ABAP ]

**SDK for SAP ABAP**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/sap-abap/services/ctt#code-examples).

```
    DATA lt_baselines TYPE /aws1/cl_cttbaselinesummary=>tt_baselines.
    DATA lv_nexttoken TYPE /aws1/cttstring.

    " List all baselines using pagination
    DO.
      DATA(lo_output) = io_ctt->listbaselines(
        iv_nexttoken = lv_nexttoken
      ).

      APPEND LINES OF lo_output->get_baselines( ) TO lt_baselines.

      lv_nexttoken = lo_output->get_nexttoken( ).
      IF lv_nexttoken IS INITIAL.
        EXIT.
      ENDIF.
    ENDDO.

    ot_baselines = lt_baselines.
    MESSAGE 'Listed baselines successfully.' TYPE 'I'.
```
+  For API details, see [ListBaselines](https://docs.aws.amazon.com/sdk-for-sap-abap/v1/api/latest/index.html) in *AWS SDK for SAP ABAP API reference*.

------

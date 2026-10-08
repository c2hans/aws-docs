---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudwatch-logs_example_cloudwatch-logs_PutSyslogConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `PutSyslogConfiguration` with an AWS SDK
<a name="cloudwatch-logs_example_cloudwatch-logs_PutSyslogConfiguration_section"></a>

The following code example shows how to use `PutSyslogConfiguration`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn syslog ingestion basics](cloudwatch-logs_example_cloudwatch-logs_Scenario_SyslogIngestion_section.md)

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch-logs/scenarios/syslog_ingestion#code-examples).

```
    def put_syslog_configuration(
        self, log_group_identifier: str, vpc_endpoint_id: str
    ) -> None:
        """
        Creates or updates a syslog configuration for a log group. This enables
        ingestion of syslog data through the specified VPC endpoint.

        :param log_group_identifier: The name or ARN of the log group to associate
            with the syslog configuration.
        :param vpc_endpoint_id: The ID of the VPC endpoint to use for syslog
            ingestion.
        :raises ClientError: If the log group or VPC endpoint does not exist.
        """
        try:
            self.logs_client.put_syslog_configuration(
                logGroupIdentifier=log_group_identifier,
                vpcEndpointId=vpc_endpoint_id,
            )
            logger.info(
                "Created syslog configuration for log group '%s' with VPC endpoint '%s'.",
                log_group_identifier,
                vpc_endpoint_id,
            )
        except ClientError as error:
            if error.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "The specified log group or VPC endpoint does not exist: %s",
                    error.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Failed to put syslog configuration: %s",
                    error.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [PutSyslogConfiguration](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/PutSyslogConfiguration) in *AWS SDK for Python (Boto3) API Reference*.

------

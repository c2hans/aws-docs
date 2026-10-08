---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cloudwatch-logs_example_cloudwatch-logs_DeleteSyslogConfiguration_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteSyslogConfiguration` with an AWS SDK
<a name="cloudwatch-logs_example_cloudwatch-logs_DeleteSyslogConfiguration_section"></a>

The following code example shows how to use `DeleteSyslogConfiguration`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn syslog ingestion basics](cloudwatch-logs_example_cloudwatch-logs_Scenario_SyslogIngestion_section.md)

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/cloudwatch-logs/scenarios/syslog_ingestion#code-examples).

```
    def delete_syslog_configuration(
        self, log_group_identifier: str, vpc_endpoint_id: str
    ) -> None:
        """
        Deletes a syslog configuration for a log group. After deletion, syslog
        data is no longer ingested through the specified VPC endpoint.

        :param log_group_identifier: The name or ARN of the log group.
        :param vpc_endpoint_id: The ID of the VPC endpoint associated with the
            syslog configuration.
        :raises ClientError: If the syslog configuration does not exist (in which
            case the error is logged but not re-raised during cleanup).
        """
        try:
            self.logs_client.delete_syslog_configuration(
                logGroupIdentifier=log_group_identifier,
                vpcEndpointId=vpc_endpoint_id,
            )
            logger.info(
                "Deleted syslog configuration for log group '%s' and VPC endpoint '%s'.",
                log_group_identifier,
                vpc_endpoint_id,
            )
        except ClientError as error:
            if error.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.info(
                    "Syslog configuration does not exist or was already deleted: %s",
                    error.response["Error"]["Message"],
                )
            else:
                logger.error(
                    "Failed to delete syslog configuration: %s",
                    error.response["Error"]["Message"],
                )
                raise
```
+  For API details, see [DeleteSyslogConfiguration](https://docs.aws.amazon.com/goto/boto3/logs-2014-03-28/DeleteSyslogConfiguration) in *AWS SDK for Python (Boto3) API Reference*.

------

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_CreateWorkGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `CreateWorkGroup` with an AWS SDK or CLI
<a name="athena_example_athena_CreateWorkGroup_section"></a>

The following code examples show how to use `CreateWorkGroup`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To create a workgroup**
The following `create-work-group` example creates a workgroup called `Data_Analyst_Group` that has the query results output location `s3://amzn-s3-demo-bucket`. The command creates a workgroup that overrides client configuration settings, which includes the query results output location. The command also enables CloudWatch metrics and adds three key-value tag pairs to the workgroup to distinguish it from other workgroups. Note that the `--configuration` argument has no spaces before the commas that separate its options.

```
aws athena create-work-group \
    --name {{Data_Analyst_Group}} \
    --configuration ResultConfiguration={OutputLocation="s3://amzn-s3-demo-bucket"},EnforceWorkGroupConfiguration="true",PublishCloudWatchMetricsEnabled="true" \
    --description {{"Workgroup for data analysts"}} \
    --tags {{Key=Division,Value=West}} {{Key=Location,Value=Seattle}} Key=Team,Value="Big Data"
```
This command produces no output. To see the results, use `aws athena get-work-group --work-group Data_Analyst_Group`.
For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html) in the *Amazon Athena User Guide*.
+  For API details, see [CreateWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/create-work-group.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def create_work_group(
        self,
        name: str,
        output_location: str,
        description: str = "Created by Athena basics scenario",
    ) -> None:
        """
        Creates an Athena workgroup with the specified name and configuration.

        :param name: The name for the new workgroup.
        :param output_location: The S3 location for query results (e.g., s3://bucket/prefix/).
        :param description: A description for the workgroup.
        :raises ClientError: If the workgroup could not be created.
        """
        try:
            self.athena_client.create_work_group(
                Name=name,
                Configuration={
                    "ResultConfiguration": {
                        "OutputLocation": output_location,
                    },
                    "EnforceWorkGroupConfiguration": True,
                    "PublishCloudWatchMetricsEnabled": True,
                },
                Description=description,
            )
            logger.info("Created workgroup '%s'.", name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request creating workgroup '%s'. The name may already "
                    "exist or the configuration is invalid. %s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [CreateWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/CreateWorkGroup) in *AWS SDK for Python (Boto3) API Reference*.

------

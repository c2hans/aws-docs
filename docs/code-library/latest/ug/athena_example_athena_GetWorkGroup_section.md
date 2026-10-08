---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_GetWorkGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `GetWorkGroup` with an AWS SDK or CLI
<a name="athena_example_athena_GetWorkGroup_section"></a>

The following code examples show how to use `GetWorkGroup`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To return information about a workgroup**
The following `get-work-group` example returns information about the `AthenaAdmin` workgroup.

```
aws athena get-work-group \
    --work-group {{AthenaAdmin}}
```
Output:

```
{
    "WorkGroup": {
        "Name": "AthenaAdmin",
        "State": "ENABLED",
        "Configuration": {
            "ResultConfiguration": {
                "OutputLocation": "s3://amzn-s3-demo-bucket/"
            },
            "EnforceWorkGroupConfiguration": false,
            "PublishCloudWatchMetricsEnabled": true,
            "RequesterPaysEnabled": false
        },
        "Description": "Workgroup for Athena administrators",
        "CreationTime": 1573677174.105
    }
}
```
For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html) in the *Amazon Athena User Guide*.
+  For API details, see [GetWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/get-work-group.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def get_work_group(self, name: str) -> Dict[str, Any]:
        """
        Returns information about the specified workgroup.

        :param name: The name of the workgroup.
        :return: A dictionary containing the workgroup details.
        :raises ClientError: If the workgroup information could not be retrieved.
        """
        try:
            response = self.athena_client.get_work_group(WorkGroup=name)
            work_group = response["WorkGroup"]
            logger.info("Retrieved workgroup '%s'.", name)
            return work_group
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request retrieving workgroup '%s'. The workgroup "
                    "was not found or the name is invalid. %s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [GetWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/GetWorkGroup) in *AWS SDK for Python (Boto3) API Reference*.

------

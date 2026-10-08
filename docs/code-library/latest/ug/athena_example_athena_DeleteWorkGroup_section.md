---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/athena_example_athena_DeleteWorkGroup_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `DeleteWorkGroup` with an AWS SDK or CLI
<a name="athena_example_athena_DeleteWorkGroup_section"></a>

The following code examples show how to use `DeleteWorkGroup`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn Athena basics](athena_example_athena_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To delete a workgroup**
The following `delete-work-group` example deletes the `TeamB` workgroup.

```
aws athena delete-work-group \
    --work-group {{TeamB}}
```
This command produces no output. To confirm the deletion, use `aws athena list-work-groups`.
For more information, see [Managing Workgroups](https://docs.aws.amazon.com/athena/latest/ug/workgroups-create-update-delete.html) in the *Amazon Athena User Guide*.
+  For API details, see [DeleteWorkGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/athena/delete-work-group.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/athena#code-examples).

```
    def delete_work_group(self, name: str, recursive: bool = True) -> None:
        """
        Deletes the specified workgroup.

        :param name: The name of the workgroup to delete.
        :param recursive: If True, deletes the workgroup even if it contains
                          named queries or query executions.
        :raises ClientError: If the workgroup could not be deleted.
        """
        try:
            self.athena_client.delete_work_group(
                WorkGroup=name, RecursiveDeleteOption=recursive
            )
            logger.info("Deleted workgroup '%s'.", name)
        except ClientError as err:
            if err.response["Error"]["Code"] == "InvalidRequestException":
                logger.error(
                    "Invalid request deleting workgroup '%s'. "
                    "It may be the primary workgroup or contain resources "
                    "without RecursiveDeleteOption. %s: %s",
                    name,
                    err.response["Error"]["Code"],
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [DeleteWorkGroup](https://docs.aws.amazon.com/goto/boto3/athena-2017-05-18/DeleteWorkGroup) in *AWS SDK for Python (Boto3) API Reference*.

------

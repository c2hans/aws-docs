---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_ListDeployments_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListDeployments` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_ListDeployments_section"></a>

The following code examples show how to use `ListDeployments`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list deployments**
The following `list-deployments` example lists the latest revision of each deployment defined in your AWS account in the current Region.

```
aws greengrassv2 list-deployments
```
Output:

```
{
    "deployments": [
        {
            "targetArn": "arn:aws:iot:us-west-2:123456789012:thinggroup/MyGreengrassCoreGroup",
            "revisionId": "14",
            "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE11111",
            "deploymentName": "Deployment for MyGreengrassCoreGroup",
            "creationTimestamp": "2021-01-07T17:21:20.691000-08:00",
            "deploymentStatus": "ACTIVE",
            "isLatestForTarget": false
        },
        {
            "targetArn": "arn:aws:iot:us-west-2:123456789012:thing/MyGreengrassCore",
            "revisionId": "1",
            "deploymentId": "a1b2c3d4-5678-90ab-cdef-EXAMPLE22222",
            "deploymentName": "Deployment for MyGreengrassCore",
            "creationTimestamp": "2021-01-06T16:10:42.407000-08:00",
            "deploymentStatus": "COMPLETED",
            "isLatestForTarget": false
        }
    ]
}
```
For more information, see [Deploy components to devices](https://docs.aws.amazon.com/greengrass/v2/developerguide/manage-deployments.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [ListDeployments](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-deployments.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def list_deployments(
        self,
        target_arn: Optional[str] = None,
        history_filter: str = "LATEST_ONLY",
    ) -> list[dict[str, Any]]:
        """
        Lists deployments, optionally filtered by target ARN.
        Uses a paginator to retrieve all pages.

        :param target_arn: Optional ARN of the target thing or thing group.
        :param history_filter: 'ALL' or 'LATEST_ONLY' (default).
        :return: A list of deployment dictionaries.
        """
        try:
            deployments = list()
            paginator = self.client.get_paginator("list_deployments")
            params = dict()
            params["historyFilter"] = history_filter
            if target_arn is not None:
                params["targetArn"] = target_arn
            for page in paginator.paginate(**params):
                deployments.extend(page.get("deployments", list()))
            logger.info("Listed %d deployment(s).", len(deployments))
            return deployments
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.error(
                    "Invalid request parameters for ListDeployments. "
                    "Verify the targetArn and historyFilter values. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListDeployments](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListDeployments) in *AWS SDK for Python (Boto3) API Reference*.

------

---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_ListCoreDevices_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Use `ListCoreDevices` with an AWS SDK or CLI
<a name="greengrassv2_example_greengrassv2_ListCoreDevices_section"></a>

The following code examples show how to use `ListCoreDevices`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example:
+  [Learn AWS IoT Greengrass V2 basics](greengrassv2_example_greengrassv2_Scenario_section.md)

------
#### [ CLI ]

**AWS CLI**
**To list core devices**
The following `list-core-devices` example lists the AWS IoT Greengrass core devices in your AWS account in the current Region.

```
aws greengrassv2 list-core-devices
```
Output:

```
{
    "coreDevices": [
        {
            "coreDeviceThingName": "MyGreengrassCore",
            "status": "HEALTHY",
            "lastStatusUpdateTimestamp": "2021-01-08T04:57:58.838000-08:00"
        }
    ]
}
```
For more information, see [Check core device status](https://docs.aws.amazon.com/greengrass/v2/developerguide/device-status.html) in the *AWS IoT Greengrass V2 Developer Guide*.
+  For API details, see [ListCoreDevices](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/greengrassv2/list-core-devices.html) in *AWS CLI Command Reference*.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
    def list_core_devices(self, status: Optional[str] = None) -> list[dict[str, Any]]:
        """
        Lists Greengrass core devices registered in the account.
        Uses a paginator to handle large result sets.

        :param status: Optional filter by device status ('HEALTHY' or 'UNHEALTHY').
        :return: A list of core device dictionaries.
        """
        try:
            devices = list()
            paginator = self.client.get_paginator("list_core_devices")
            params = dict()
            if status is not None:
                params["status"] = status
            for page in paginator.paginate(**params):
                devices.extend(page.get("coreDevices", list()))
            logger.info("Listed %d core device(s).", len(devices))
            return devices
        except ClientError as err:
            if err.response["Error"]["Code"] == "ValidationException":
                logger.error(
                    "Invalid request parameters for ListCoreDevices. "
                    "Verify the status filter value is HEALTHY or UNHEALTHY. %s",
                    err.response["Error"]["Message"],
                )
            raise
```
+  For API details, see [ListCoreDevices](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListCoreDevices) in *AWS SDK for Python (Boto3) API Reference*.

------

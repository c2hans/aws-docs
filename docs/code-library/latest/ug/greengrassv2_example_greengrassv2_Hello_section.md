---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/greengrassv2_example_greengrassv2_Hello_section.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Hello AWS IoT Greengrass V2
<a name="greengrassv2_example_greengrassv2_Hello_section"></a>

The following code example shows how to get started using AWS IoT Greengrass V2.

------
#### [ Python ]

**SDK for Python (Boto3)**
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/greengrassv2#code-examples).

```
def hello_greengrassv2() -> None:
    """
    Lists Greengrass core devices to verify connectivity to the service.
    Uses a paginator to handle pagination of results.
    """
    greengrassv2_client = boto3.client("greengrassv2")

    print("\n----------- Welcome to AWS IoT Greengrass V2 ----------\n")
    print("Listing Greengrass core devices in your account...\n")

    try:
        devices = list()
        paginator = greengrassv2_client.get_paginator("list_core_devices")
        for page in paginator.paginate():
            devices.extend(page.get("coreDevices", list()))

        if devices:
            print(f"Found {len(devices)} core device(s):")
            for device in devices:
                thing_name = device.get("coreDeviceThingName", "Unknown")
                status = device.get("status", "Unknown")
                last_updated = device.get("lastStatusUpdateTimestamp", "N/A")
                print(
                    f"  - {thing_name} (Status: {status}, Last updated: {last_updated})"
                )
        else:
            print("No Greengrass core devices found in your account.")
            print(
                "To get started, install the Greengrass Core software on an IoT device."
            )

        print("\nHello from AWS IoT Greengrass V2!")

    except ClientError as err:
        logger.error(
            "Error listing core devices: %s",
            err.response["Error"]["Message"],
        )
        print(f"Service error: {err.response['Error']['Message']}")
        raise

if __name__ == "__main__":
    hello_greengrassv2()
```
+  For API details, see [ListCoreDevices](https://docs.aws.amazon.com/goto/boto3/greengrassv2-2020-11-30/ListCoreDevices) in *AWS SDK for Python (Boto3) API Reference*.

------

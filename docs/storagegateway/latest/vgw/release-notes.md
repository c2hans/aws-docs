---
source_url: https://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html
---

# Release notes for Volume Gateway appliance software
<a name="release-notes"></a>

These release notes describe the new and updated features, improvements, and fixes that are included with each version of the Volume Gateway appliance. Each software version is identified by its release date and a unique version number.

You can determine a gateway's software version number by checking its **Details** page in the Storage Gateway console, or by calling the [DescribeGatewayInformation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeGatewayInformation.html) API action using an AWS CLI command similar to the following:

```
aws storagegateway describe-gateway-information --gateway-arn "{{arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B}}"
```

The version number is returned in the `SoftwareVersion` field of the API response.

**Note**
A gateway won't report software version information under the following circumstances:
The gateway is offline.
The gateway is running older software that doesn't support version reporting.
The gateway type is FSx File Gateway.

For more information about Volume Gateway updates, including how to modify the default automatic maintenance and update schedule for a gateway, see [Managing Gateway Updates Using the AWS Storage Gateway Console](https://docs.aws.amazon.com/storagegateway/latest/vgw/MaintenanceManagingUpdate-common.html).

For more information about migrating Volume Gateway from Amazon Linux 2 to AL2023, see [Storage Gateway AL2 to AL2023 Migration Campaign](al2-to-al2023-migration.md).

**Amazon Linux 2023 (AL2023) based gateways**
The following table lists the release notes for gateways based on AL2023.

**Note**
Gateway versions 2.x.x can't be updated to 3.x.x.

| Release Date | Software Version | Release Notes |
| --- | --- | --- |
| 2026-06-30 | 3.2.7 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-05-28 | 3.2.6 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-05-04 | 3.2.5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-04-01 | 3.2.4 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-03-02 | 3.2.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-02-12 | 3.2.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2026-02-02 | 3.2.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2026-01-06 | 3.1.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-12-04 | 3.0.6 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-11-06 | 3.0.5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-10-10 | 3.0.4 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-09-12 | 3.0.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-08-29 | 3.0.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-08-18 | 3.0.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-07-16 | 3.0.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |

**Amazon Linux 2 (AL2) based gateways**
The following table lists the release notes for gateways based on AL2.

| Release Date | Software Version | Release Notes |
| --- | --- | --- |
| 2026-06-30 | 2.14.6 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-05-28 | 2.14.5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-05-04 | 2.14.4 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-04-01 | 2.14.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html)  |
| 2026-03-02 | 2.14.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2026-02-02 | 2.14.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2026-01-05 | 2.14.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-12-05 | 2.13.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-11-03 | 2.12.15 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-10-01 | 2.12.14 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-09-02 | 2.12.13 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-07-31 | 2.12.12 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-07-01 | 2.12.11 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-06-02 | 2.12.10 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-05-01 | 2.12.9 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-05-01 | 2.12.8 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-04-01 | 2.12.7 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-03-04 | 2.12.6 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-02-04 | 2.12.5 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2025-01-07 | 2.12.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-12-06 | 2.12.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-11-06 | 2.12.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-10-03 | 2.12.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-08-30 | 2.11.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-07-29 | 2.10.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-06-17 | 2.9.2 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-05-28 | 2.9.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-05-08 | 2.8.3 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-04-10 | 2.8.1 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2024-03-06 | 2.8.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2023-12-19 | 2.7.0 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |
| 2023-12-14 | 2.6.6 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/storagegateway/latest/vgw/release-notes.html) |

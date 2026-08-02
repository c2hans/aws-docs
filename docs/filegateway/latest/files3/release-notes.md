---
source_url: https://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html
---

# Release notes for gateway appliance software
<a name="release-notes"></a>

These release notes describe the new and updated features, improvements, and fixes that are included with each version of the Amazon S3 File Gateway appliance. Each software version is identified by its release date and a unique version number.

You can determine a gateway's software version number by checking its **Details** page in the Storage Gateway console, or by calling the [DescribeGatewayInformation](https://docs.aws.amazon.com/storagegateway/latest/APIReference/API_DescribeGatewayInformation.html) API action using an AWS CLI command similar to the following:

```
aws storagegateway describe-gateway-information --gateway-arn "{{arn:aws:storagegateway:us-west-2:123456789012:gateway/sgw-12A3456B}}"
```

The version number is returned in the `SoftwareVersion` field of the API response.

**Note**
A gateway won't report software version information under the following circumstances:
The gateway is offline.
The gateway is running older software that doesn't support version reporting.
The gateway type isn't S3 File Gateway.

For more information about S3 File Gateway updates, including how to modify the default automatic maintenance and update schedule for a gateway, see [Managing Gateway Updates Using the AWS Storage Gateway Console](https://docs.aws.amazon.com/filegateway/latest/files3/MaintenanceManagingUpdate-common.html).

For more information about migrating S3 File Gateway from Amazon Linux 2 to AL2023, see [Storage Gateway AL2 to AL2023 Migration Campaign](al2-to-al2023-migration.md).

**Amazon Linux 2023 (AL2023) based gateways**
The following table lists the release notes for gateways based on AL2023.

**Note**
Gateway versions 1.x.x can't be updated to 2.x.x.

| Release Date | Software Version | Release Notes |
| --- | --- | --- |
| 2026-07-20 | 2.1.10 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)  |
| 2026-07-15 | 2.1.9 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)  |
| 2026-06-16 | 2.1.8 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-05-21 | 2.1.7 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-05-14 | 2.1.6 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-04-16 | 2.1.5 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-03-26 | 2.1.4 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-03-16 | 2.1.3 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-03-02 | 2.0.7 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-02-12 | 2.1.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-02-02 | 2.1.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-01-21 | 2.0.6 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-01-16 | 2.1.0 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-12-15 | 2.0.5 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-11-12 | 2.0.4 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-11-12 | 2.0.4 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-10-15 | 2.0.3 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-09-15 | 2.0.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-08-29 | 2.0.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-08-21 | 2.0.0 | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |

**Amazon Linux 2 (AL2) based gateways**
The following table lists the release notes for gateways based on AL2.

| Release Date | Software Version | Release Notes |
| --- | --- | --- |
| 2026-07-20 | 1.28.10 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)  |
| 2026-07-15 | 1.28.9 |  [See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)  |
| 2026-06-16 | 1.28.8 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-05-26 | 1.28.7 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-05-18 | 1.28.6 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-04-16 | 1.28.5 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-03-26 | 1.28.4 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-03-16 | 1.27.21 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-03-16 | 1.28.3 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-02-27 | 1.27.20 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-02-11 | 1.28.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-02-02 | 1.28.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-01-21 | 1.27.19 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2026-01-16 | 1.28.0 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-12-15 | 1.27.18 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-11-17 | 1.27.17 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-10-15 | 1.27.16 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-09-22 | 1.27.15 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-09-15 | 1.27.14 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-08-21 | 1.27.13 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-08-18 | 1.27.12 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-08-11 | 1.27.11 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-07-15 | 1.27.10 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-06-23 | 1.27.9 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-06-16 | 1.27.8 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-05-26 | 1.27.7 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-05-15 | 1.27.6 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-04-28 | 1.27.5 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-04-14 | 1.27.4 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-04-01 | 1.27.3 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-03-17 | 1.27.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-02-17 | 1.27.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-01-17 | 1.27.0 | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)<br />**Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2025-01-09 | 1.26.9 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-12-18 | 1.26.8 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-11-18 | 1.26.7 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-10-17 | 1.26.6 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-09-30 | 1.26.5 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-09-16 | 1.26.3 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-08-21 | 1.26.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-08-19 | **1.26.0** | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-07-16 | 1.25.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-06-17 | 1.25.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-05-15 | **1.25.0** | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)<br />**Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-04-15 | 1.24.5 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-04-01 | 1.24.4 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-03-18 | 1.24.3 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2024-01-12 | 1.24.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-12-27 | 1.24.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-12-01 | **1.24.0** | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)<br />**Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-10-24 | 1.23.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-08-14 | 1.23.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-06-12 | **1.23.0** | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)<br />**Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-04-19 | 1.22.1 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2023-01-18 | **1.22.0** | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)<br />**Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2022-07-06 | 1.21.2 | **Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2022-02-16 | 1.21.1 | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html)<br />**Maintenance Updates:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2022-01-18 | **1.21.0** | **Features:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |
| 2021-12-12 | **1.20.0** | **{{URGENT UPDATE}}:**[See the AWS documentation website for more details](http://docs.aws.amazon.com/filegateway/latest/files3/release-notes.html) |

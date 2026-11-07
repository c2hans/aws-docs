---
source_url: https://docs.aws.amazon.com/code-library/latest/ug/cli_2_directory-service_code_examples.html
---

There are more AWS SDK examples available in the [AWS Doc SDK Examples](https://github.com/awsdocs/aws-doc-sdk-examples) GitHub repo.

# Directory Service examples using AWS CLI
<a name="cli_2_directory-service_code_examples"></a>

The following code examples show you how to perform actions and implement common scenarios by using the AWS Command Line Interface with Directory Service.

*Actions* are code excerpts from larger programs and must be run in context. While actions show you how to call individual service functions, you can see actions in context in their related scenarios.

Each example includes a link to the complete source code, where you can find instructions on how to set up and run the code in context.

**Topics**
+ [Actions](#actions)

## Actions
<a name="actions"></a>

### `describe-directories`
<a name="directory-service_DescribeDirectories_cli_2_topic"></a>

The following code example shows how to use `describe-directories`.

**AWS CLI**
**To get details about your directories**
The following `describe-directories` example displays details about the specified directory.

```
aws ds describe-directories \
    --directory-ids {{d-a1b2c3d4e5}}
```
Output:

```
{
    "DirectoryDescriptions": [
        {
            "DirectoryId": "d-a1b2c3d4e5",
            "Name": "mydirectory.example.com",
            "ShortName": "mydirectory",
            "Size": "Small",
            "Edition": "Standard",
            "Alias": "d-a1b2c3d4e5",
            "AccessUrl": "d-a1b2c3d4e5.awsapps.com",
            "Stage": "Active",
            "ShareStatus": "Shared",
            "ShareMethod": "HANDSHAKE",
            "ShareNotes": "These are my share notes",
            "LaunchTime": "2019-07-08T15:33:46.327000-07:00",
            "StageLastUpdatedDateTime": "2019-07-08T15:59:12.307000-07:00",
            "Type": "SharedMicrosoftAD",
            "SsoEnabled": false,
            "DesiredNumberOfDomainControllers": 0,
            "OwnerDirectoryDescription": {
                "DirectoryId": "d-b2c3d4e5f6",
                "AccountId": "123456789111",
                "DnsIpAddrs": [
                    "203.113.0.248",
                    "203.113.0.253"
                ],
                "VpcSettings": {
                    "VpcId": "vpc-a1b2c3d4",
                    "SubnetIds": [
                        "subnet-a1b2c3d4",
                        "subnet-d4c3b2a1"
                    ],
                    "AvailabilityZones": [
                        "us-west-2a",
                        "us-west-2c"
                    ]
                }
            }
        }
    ]
}
```
For more information, see [Viewing AWS Managed Microsoft AD directory information](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_view_directory_info.html) in the *AWS Directory Service Administration Guide*.
+  For API details, see [DescribeDirectories](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-directories.html) in *AWS CLI Command Reference*.

### `describe-trusts`
<a name="directory-service_DescribeTrusts_cli_2_topic"></a>

The following code example shows how to use `describe-trusts`.

**AWS CLI**
**To get details about your trust relationships**
The following `describe-trusts` example displays details about the trust relationships for the specified directory.

```
aws ds describe-trusts \
    --directory-id {{d-a1b2c3d4e5}}
```
Output:

```
{
    "Trusts": [
        {
            "DirectoryId": "d-a1b2c3d4e5",
            "TrustId": "t-9a8b7c6d5e",
            "RemoteDomainName": "other.example.com",
            "TrustType": "Forest",
            "TrustDirection": "Two-Way",
            "TrustState": "Verified",
            "CreatedDateTime": "2017-06-20T18:08:45.614000-07:00",
            "LastUpdatedDateTime": "2019-06-04T10:52:12.410000-07:00",
            "StateLastUpdatedDateTime": "2019-06-04T10:52:12.410000-07:00",
            "SelectiveAuth": "Disabled"
        }
    ]
}
```
For more information, see [Creating a trust relationship between your AWS Managed Microsoft AD and self-managed AD](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_setup_trust.html) in the *AWS Directory Service Administration Guide*.
+  For API details, see [DescribeTrusts](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/describe-trusts.html) in *AWS CLI Command Reference*.

### `disable-directory-data-access`
<a name="directory-service_DisableDirectoryDataAccess_cli_2_topic"></a>

The following code example shows how to use `disable-directory-data-access`.

**AWS CLI**
**To disable Directory Service Data API for a directory**
The following `disable-directory-data-access` example disables the Directory Service Data API for the specified directory.

```
aws ds disable-directory-data-access \
    --directory-id {{d-1234567890}}
```
This command produces no output.
For more information, see [Enabling or disabling user and group management or AWS Directory Service Data](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_users_groups_mgmt_enable_disable.html) in the *AWS Directory Service Administration Guide*.
+  For API details, see [DisableDirectoryDataAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/disable-directory-data-access.html) in *AWS CLI Command Reference*.

### `enable-directory-data-access`
<a name="directory-service_EnableDirectoryDataAccess_cli_2_topic"></a>

The following code example shows how to use `enable-directory-data-access`.

**AWS CLI**
**To enable Directory Service Data API for a directory**
The following `enable-directory-data-access` example enables the Directory Service Data API for the specified directory.

```
aws ds enable-directory-data-access \
    --directory-id {{d-1234567890}}
```
This command produces no output.
For more information, see [Enabling or disabling user and group management or AWS Directory Service Data](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_users_groups_mgmt_enable_disable.html) in the *AWS Directory Service Administration Guide*.
+  For API details, see [EnableDirectoryDataAccess](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/enable-directory-data-access.html) in *AWS CLI Command Reference*.

### `reset-user-password`
<a name="directory-service_ResetUserPassword_cli_2_topic"></a>

The following code example shows how to use `reset-user-password`.

**AWS CLI**
**To reset a user password in a directory**
The following `reset-user-password` example resets and enables the specified user in the specified directory.

```
aws ds reset-user-password \
    --directory-id {{d-1234567890}} \
    --user-name '{{john.doe}}' \
    --new-{{password}} 'password'
```
This command produces no output.
For more information, see [Resetting and enabling an AWS Managed Microsoft AD user's password](https://docs.aws.amazon.com/directoryservice/latest/admin-guide/ms_ad_reset_user_pswd.html) in the *AWS Directory Service Administration Guide*.
+  For API details, see [ResetUserPassword](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ds/reset-user-password.html) in *AWS CLI Command Reference*.

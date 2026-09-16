---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_EnableInstanceSqlHaStandbyDetections.html
---

# EnableInstanceSqlHaStandbyDetections
<a name="API_EnableInstanceSqlHaStandbyDetections"></a>

Enable Amazon EC2 instances running in an SQL Server High Availability cluster for SQL Server High Availability instance standby detection monitoring. Once enabled, AWS monitors the metadata for the instances to determine whether they are active or standby nodes in the SQL Server High Availability cluster. If the instances are determined to be standby failover nodes, AWS automatically applies SQL Server licensing fee waiver for those instances.

To register an instance, it must be running a Windows SQL Server license-included AMI and have the AWS Systems Manager agent installed and running. Only Windows Server 2019 and later and SQL Server (Standard and Enterprise editions) 2017 and later are supported. For more information, see [ Prerequisites for using SQL Server High Availability instance standby detection](https://docs.aws.amazon.com/sql-server-ec2/latest/userguide/prerequisites-and-requirements.html).

## Request Parameters
<a name="API_EnableInstanceSqlHaStandbyDetections_RequestParameters"></a>

The following parameters are for this specific action. For more information about required and optional parameters that are common to all actions, see [Common Query Parameters](CommonParameters.md).

 **DryRun**
Checks whether you have the required permissions for the action, without actually making the request, and provides an error response. If you have the required permissions, the error response is `DryRunOperation`. Otherwise, it is `UnauthorizedOperation`.
Type: Boolean
Required: No

 **InstanceId.N**
The IDs of the instances to enable for SQL Server High Availability standby detection monitoring.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 30 items.
Required: Yes

 **SqlServerCredentials**
The ARN of the AWS Secrets Manager secret containing the SQL Server access credentials. The specified secret must contain valid SQL Server credentials for the specified instances. If not specified, deafult local user credentials will be used by the AWS Systems Manager agent. To enable instances with different credentials, you must make separate requests.
Type: String
Pattern: `^(?=.{20,2048}$)arn:aws[a-z-]*:secretsmanager:[a-z0-9-]+:\d{12}:secret:[a-zA-Z0-9/_+=.@-]+`
Required: No

## Response Elements
<a name="API_EnableInstanceSqlHaStandbyDetections_ResponseElements"></a>

The following elements are returned by the service.

 **instanceSet**
Information about the instances that were enabled for SQL Server High Availability standby detection monitoring.
Type: Array of [RegisteredInstance](API_RegisteredInstance.md) objects

 **requestId**
The ID of the request.
Type: String

## Errors
<a name="API_EnableInstanceSqlHaStandbyDetections_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

## See Also
<a name="API_EnableInstanceSqlHaStandbyDetections_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Python (Boto3)](https://docs.aws.amazon.com/goto/boto3/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/EnableInstanceSqlHaStandbyDetections)

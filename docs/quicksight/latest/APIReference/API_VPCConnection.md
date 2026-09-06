---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_VPCConnection.html
---

# VPCConnection
<a name="API_VPCConnection"></a>

The structure of a VPC connection.

## Contents
<a name="API_VPCConnection_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** Arn **   <a name="QS-Type-VPCConnection-Arn"></a>
The Amazon Resource Name (ARN) of the VPC connection.
Type: String
Required: No

 ** AvailabilityStatus **   <a name="QS-Type-VPCConnection-AvailabilityStatus"></a>
The availability status of the VPC connection.
Type: String
Valid Values: `AVAILABLE | UNAVAILABLE | PARTIALLY_AVAILABLE`
Required: No

 ** CreatedTime **   <a name="QS-Type-VPCConnection-CreatedTime"></a>
The time that the VPC connection was created.
Type: Timestamp
Required: No

 ** DnsResolvers **   <a name="QS-Type-VPCConnection-DnsResolvers"></a>
A list of IP addresses of DNS resolver endpoints for the VPC connection.
Type: Array of strings
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-VPCConnection-LastUpdatedTime"></a>
The time that the VPC connection was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-VPCConnection-Name"></a>
The display name for the VPC connection.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 128.
Required: No

 ** NetworkInterfaces **   <a name="QS-Type-VPCConnection-NetworkInterfaces"></a>
A list of network interfaces.
Type: Array of [NetworkInterface](API_NetworkInterface.md) objects
Required: No

 ** RoleArn **   <a name="QS-Type-VPCConnection-RoleArn"></a>
The ARN of the IAM role associated with the VPC connection.
Type: String
Required: No

 ** SecurityGroupIds **   <a name="QS-Type-VPCConnection-SecurityGroupIds"></a>
The Amazon EC2 security group IDs associated with the VPC connection.
Type: Array of strings
Array Members: Minimum number of 1 item. Maximum number of 16 items.
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^sg-[0-9a-z]*$`
Required: No

 ** Status **   <a name="QS-Type-VPCConnection-Status"></a>
The status of the VPC connection.
Type: String
Valid Values: `CREATION_IN_PROGRESS | CREATION_SUCCESSFUL | CREATION_FAILED | UPDATE_IN_PROGRESS | UPDATE_SUCCESSFUL | UPDATE_FAILED | DELETION_IN_PROGRESS | DELETION_FAILED | DELETED`
Required: No

 ** VPCConnectionId **   <a name="QS-Type-VPCConnection-VPCConnectionId"></a>
The ID of the VPC connection that you're creating. This ID is a unique identifier for each AWS Region in an AWS account.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Required: No

 ** VPCId **   <a name="QS-Type-VPCConnection-VPCId"></a>
The Amazon EC2 VPC ID associated with the VPC connection.
Type: String
Required: No

## See Also
<a name="API_VPCConnection_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/VPCConnection)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/VPCConnection)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/VPCConnection)

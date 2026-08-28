---
source_url: https://docs.aws.amazon.com/finspace/latest/management-api/API_KxCluster.html
---

End of support notice: On October 7, 2026, AWS will end support for Amazon FinSpace. After October 7, 2026, you will no longer be able to access the FinSpace console or FinSpace resources. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/userguide/amazon-finspace-end-of-support.html).

After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see [Amazon FinSpace end of support](https://docs.aws.amazon.com/finspace/latest/management-api/amazon-finspace-end-of-support.html).

# KxCluster
<a name="API_KxCluster"></a>

The details of a kdb cluster.

## Contents
<a name="API_KxCluster_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** availabilityZoneId **   <a name="finspace-Type-KxCluster-availabilityZoneId"></a>
 The availability zone identifiers for the requested regions.
Type: String
Length Constraints: Minimum length of 8. Maximum length of 12.
Pattern: `^[a-zA-Z0-9-]+$`
Required: No

 ** azMode **   <a name="finspace-Type-KxCluster-azMode"></a>
The number of availability zones assigned per cluster. This can be one of the following:
+  `SINGLE` – Assigns one availability zone per cluster.
+  `MULTI` – Assigns all the availability zones per cluster.
Type: String
Valid Values: `SINGLE | MULTI`
Required: No

 ** clusterDescription **   <a name="finspace-Type-KxCluster-clusterDescription"></a>
A description of the cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1000.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`
Required: No

 ** clusterName **   <a name="finspace-Type-KxCluster-clusterName"></a>
A unique name for the cluster.
Type: String
Length Constraints: Minimum length of 3. Maximum length of 63.
Pattern: `^[a-zA-Z0-9][a-zA-Z0-9-_]*[a-zA-Z0-9]$`
Required: No

 ** clusterType **   <a name="finspace-Type-KxCluster-clusterType"></a>
Specifies the type of KDB database that is being created. The following types are available:
+ HDB – A Historical Database. The data is only accessible with read-only permissions from one of the FinSpace managed kdb databases mounted to the cluster.
+ RDB – A Realtime Database. This type of database captures all the data from a ticker plant and stores it in memory until the end of day, after which it writes all of its data to a disk and reloads the HDB. This cluster type requires local storage for temporary storage of data during the savedown process. If you specify this field in your request, you must provide the `savedownStorageConfiguration` parameter.
+ GATEWAY – A gateway cluster allows you to access data across processes in kdb systems. It allows you to create your own routing logic using the initialization scripts and custom code. This type of cluster does not require a writable local storage.
+ GP – A general purpose cluster allows you to quickly iterate on code during development by granting greater access to system commands and enabling a fast reload of custom code. This cluster type can optionally mount databases including cache and savedown storage. For this cluster type, the node count is fixed at 1. It does not support autoscaling and supports only `SINGLE` AZ mode.
+ Tickerplant – A tickerplant cluster allows you to subscribe to feed handlers based on IAM permissions. It can publish to RDBs, other Tickerplants, and real-time subscribers (RTS). Tickerplants can persist messages to log, which is readable by any RDB environment. It supports only single-node that is only one kdb process.
Type: String
Valid Values: `HDB | RDB | GATEWAY | GP | TICKERPLANT`
Required: No

 ** createdTimestamp **   <a name="finspace-Type-KxCluster-createdTimestamp"></a>
The timestamp at which the cluster was created in FinSpace. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** executionRole **   <a name="finspace-Type-KxCluster-executionRole"></a>
 An IAM role that defines a set of permissions associated with a cluster. These permissions are assumed when a cluster attempts to access another cluster.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1024.
Pattern: `^arn:aws[a-z0-9-]*:iam::\d{12}:role\/[\w-\/.@+=,]{1,1017}$`
Required: No

 ** initializationScript **   <a name="finspace-Type-KxCluster-initializationScript"></a>
Specifies a Q program that will be run at launch of a cluster. It is a relative path within *.zip* file that contains the custom code, which will be loaded on the cluster. It must include the file name itself. For example, `somedir/init.q`.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^[a-zA-Z0-9\_\-\.\/\\]+$`
Required: No

 ** lastModifiedTimestamp **   <a name="finspace-Type-KxCluster-lastModifiedTimestamp"></a>
The last time that the cluster was modified. The value is determined as epoch time in milliseconds. For example, the value for Monday, November 1, 2021 12:00:00 PM UTC is specified as 1635768000000.
Type: Timestamp
Required: No

 ** releaseLabel **   <a name="finspace-Type-KxCluster-releaseLabel"></a>
A version of the FinSpace managed kdb to run.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 16.
Pattern: `^[a-zA-Z0-9._-]+$`
Required: No

 ** status **   <a name="finspace-Type-KxCluster-status"></a>
The status of a cluster.
+ PENDING – The cluster is pending creation.
+ CREATING –The cluster creation process is in progress.
+ CREATE\_FAILED– The cluster creation process has failed.
+ RUNNING – The cluster creation process is running.
+ UPDATING – The cluster is in the process of being updated.
+  DELETING – The cluster is in the process of being deleted.
+ DELETED – The cluster has been deleted.
+ DELETE\_FAILED – The cluster failed to delete.
Type: String
Valid Values: `PENDING | CREATING | CREATE_FAILED | RUNNING | UPDATING | DELETING | DELETED | DELETE_FAILED`
Required: No

 ** statusReason **   <a name="finspace-Type-KxCluster-statusReason"></a>
The error message when a failed state occurs.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 250.
Pattern: `^[a-zA-Z0-9\_\-\.\s]+$`
Required: No

 ** volumes **   <a name="finspace-Type-KxCluster-volumes"></a>
 A list of volumes attached to the cluster.
Type: Array of [Volume](API_Volume.md) objects
Array Members: Minimum number of 0 items. Maximum number of 5 items.
Required: No

## See Also
<a name="API_KxCluster_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/finspace-2021-03-12/KxCluster)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/finspace-2021-03-12/KxCluster)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/finspace-2021-03-12/KxCluster)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon FinSpace. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query finspace` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

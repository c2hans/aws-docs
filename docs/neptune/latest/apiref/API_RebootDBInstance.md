---
source_url: https://docs.aws.amazon.com/neptune/latest/apiref/API_RebootDBInstance.html
---

# RebootDBInstance
<a name="API_RebootDBInstance"></a>

You might need to reboot your DB instance, usually for maintenance reasons. For example, if you make certain modifications, or if you change the DB parameter group associated with the DB instance, you must reboot the instance for the changes to take effect.

Rebooting a DB instance restarts the database engine service. Rebooting a DB instance results in a momentary outage, during which the DB instance status is set to rebooting.

## Request Parameters
<a name="API_RebootDBInstance_RequestParameters"></a>

 For information about the parameters that are common to all actions, see [Common Parameters](CommonParameters.md).

 ** DBInstanceIdentifier **
The DB instance identifier. This parameter is stored as a lowercase string.
Constraints:
+ Must match the identifier of an existing DBInstance.
Type: String
Required: Yes

 ** ForceFailover **
 When `true`, the reboot is conducted through a MultiAZ failover.
Constraint: You can't specify `true` if the instance is not configured for MultiAZ.
Type: Boolean
Required: No

## Response Elements
<a name="API_RebootDBInstance_ResponseElements"></a>

The following element is returned by the service.

 ** DBInstance **
Contains the details of an Amazon Neptune DB instance.
This data type is used as a response element in the [DescribeDBInstances](API_DescribeDBInstances.md) action.
Type: [DBInstance](API_DBInstance.md) object

## Errors
<a name="API_RebootDBInstance_Errors"></a>

For information about the errors that are common to all actions, see [Common Error Types](CommonErrors.md).

 ** DBInstanceNotFound **
 *DBInstanceIdentifier* does not refer to an existing DB instance.
HTTP Status Code: 404

 ** InvalidDBInstanceState **
The specified DB instance is not in the *available* state.
HTTP Status Code: 400

## See Also
<a name="API_RebootDBInstance_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS Command Line Interface V2](https://docs.aws.amazon.com/goto/cli2/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for .NET V4](https://docs.aws.amazon.com/goto/DotNetSDKV4/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for Go v2](https://docs.aws.amazon.com/goto/SdkForGoV2/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for JavaScript V3](https://docs.aws.amazon.com/goto/SdkForJavaScriptV3/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for Kotlin](https://docs.aws.amazon.com/goto/SdkForKotlin/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for PHP V3](https://docs.aws.amazon.com/goto/SdkForPHPV3/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for Python](https://docs.aws.amazon.com/goto/boto3/neptune-2014-10-31/RebootDBInstance)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/neptune-2014-10-31/RebootDBInstance)

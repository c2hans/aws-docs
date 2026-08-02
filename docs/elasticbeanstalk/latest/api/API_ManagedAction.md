---
source_url: https://docs.aws.amazon.com/elasticbeanstalk/latest/api/API_ManagedAction.html
---

# ManagedAction
<a name="API_ManagedAction"></a>

The record of an upcoming or in-progress managed action.

## Contents
<a name="API_ManagedAction_Contents"></a>

 ** ActionDescription **
A description of the managed action.
Type: String
Required: No

 ** ActionId **
A unique identifier for the managed action.
Type: String
Required: No

 ** ActionType **
The type of managed action.
Type: String
Valid Values: `InstanceRefresh | PlatformUpdate | Unknown`
Required: No

 ** Status **
The status of the managed action. If the action is `Scheduled`, you can apply it immediately with [ApplyEnvironmentManagedAction](API_ApplyEnvironmentManagedAction.md).
Type: String
Valid Values: `Scheduled | Pending | Running | Unknown`
Required: No

 ** WindowStartTime **
The start time of the maintenance window in which the managed action will execute.
Type: Timestamp
Required: No

## See Also
<a name="API_ManagedAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/elasticbeanstalk-2010-12-01/ManagedAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/elasticbeanstalk-2010-12-01/ManagedAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/elasticbeanstalk-2010-12-01/ManagedAction)

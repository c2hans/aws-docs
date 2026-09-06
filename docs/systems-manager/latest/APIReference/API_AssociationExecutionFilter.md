---
source_url: https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_AssociationExecutionFilter.html
---

# AssociationExecutionFilter
<a name="API_AssociationExecutionFilter"></a>

Filters used in the request.

## Contents
<a name="API_AssociationExecutionFilter_Contents"></a>

 ** Key **   <a name="systemsmanager-Type-AssociationExecutionFilter-Key"></a>
The key value used in the request.
Type: String
Valid Values: `ExecutionId | Status | CreatedTime`
Required: Yes

 ** Type **   <a name="systemsmanager-Type-AssociationExecutionFilter-Type"></a>
The filter type specified in the request.
Type: String
Valid Values: `EQUAL | LESS_THAN | GREATER_THAN`
Required: Yes

 ** Value **   <a name="systemsmanager-Type-AssociationExecutionFilter-Value"></a>
The value specified for the key.
Type: String
Length Constraints: Minimum length of 1.
Required: Yes

## See Also
<a name="API_AssociationExecutionFilter_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-2014-11-06/AssociationExecutionFilter)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-2014-11-06/AssociationExecutionFilter)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-2014-11-06/AssociationExecutionFilter)

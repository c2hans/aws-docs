---
source_url: https://docs.aws.amazon.com/appflow/1.0/APIReference/API_DestinationFieldProperties.html
---

# DestinationFieldProperties
<a name="API_DestinationFieldProperties"></a>

 The properties that can be applied to a field when connector is being used as a destination.

## Contents
<a name="API_DestinationFieldProperties_Contents"></a>

 ** isCreatable **   <a name="appflow-Type-DestinationFieldProperties-isCreatable"></a>
 Specifies if the destination field can be created by the current user.
Type: Boolean
Required: No

 ** isDefaultedOnCreate **   <a name="appflow-Type-DestinationFieldProperties-isDefaultedOnCreate"></a>
Specifies whether the field can use the default value during a Create operation.
Type: Boolean
Required: No

 ** isNullable **   <a name="appflow-Type-DestinationFieldProperties-isNullable"></a>
 Specifies if the destination field can have a null value.
Type: Boolean
Required: No

 ** isUpdatable **   <a name="appflow-Type-DestinationFieldProperties-isUpdatable"></a>
 Specifies whether the field can be updated during an `UPDATE` or `UPSERT` write operation.
Type: Boolean
Required: No

 ** isUpsertable **   <a name="appflow-Type-DestinationFieldProperties-isUpsertable"></a>
 Specifies if the flow run can either insert new rows in the destination field if they do not already exist, or update them if they do.
Type: Boolean
Required: No

 ** supportedWriteOperations **   <a name="appflow-Type-DestinationFieldProperties-supportedWriteOperations"></a>
 A list of supported write operations. For each write operation listed, this field can be used in `idFieldNames` when that write operation is present as a destination option.
Type: Array of strings
Valid Values: `INSERT | UPSERT | UPDATE | DELETE`
Required: No

## See Also
<a name="API_DestinationFieldProperties_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/appflow-2020-08-23/DestinationFieldProperties)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/appflow-2020-08-23/DestinationFieldProperties)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/appflow-2020-08-23/DestinationFieldProperties)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AmazonAppFlow. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query appflow` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

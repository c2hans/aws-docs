---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_ReservedInstancesModification.html
---

# ReservedInstancesModification
<a name="API_ReservedInstancesModification"></a>

Describes a Reserved Instance modification.

## Contents
<a name="API_ReservedInstancesModification_Contents"></a>

 ** clientToken **
A unique, case-sensitive key supplied by the client to ensure that the request is idempotent. For more information, see [Ensuring Idempotency](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/Run_Instance_Idempotency.html).
Type: String
Required: No

 ** createDate **
The time when the modification request was created.
Type: Timestamp
Required: No

 ** effectiveDate **
The time for the modification to become effective.
Type: Timestamp
Required: No

 ** ModificationResultSet.N **
Contains target configurations along with their corresponding new Reserved Instance IDs.
Type: Array of [ReservedInstancesModificationResult](API_ReservedInstancesModificationResult.md) objects
Required: No

 ** reservedInstancesModificationId **
A unique ID for the Reserved Instance modification.
Type: String
Required: No

 ** ReservedInstancesSet.N **
The IDs of one or more Reserved Instances.
Type: Array of [ReservedInstancesId](API_ReservedInstancesId.md) objects
Required: No

 ** status **
The status of the Reserved Instances modification request.
Type: String
Required: No

 ** statusMessage **
The reason for the status.
Type: String
Required: No

 ** updateDate **
The time when the modification request was last updated.
Type: Timestamp
Required: No

## See Also
<a name="API_ReservedInstancesModification_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/ReservedInstancesModification)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/ReservedInstancesModification)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/ReservedInstancesModification)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

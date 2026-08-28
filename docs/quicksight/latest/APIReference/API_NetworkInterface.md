---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_NetworkInterface.html
---

# NetworkInterface
<a name="API_NetworkInterface"></a>

The structure that contains information about a network interface.

## Contents
<a name="API_NetworkInterface_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AvailabilityZone **   <a name="QS-Type-NetworkInterface-AvailabilityZone"></a>
The availability zone that the network interface resides in.
Type: String
Required: No

 ** ErrorMessage **   <a name="QS-Type-NetworkInterface-ErrorMessage"></a>
An error message.
Type: String
Required: No

 ** NetworkInterfaceId **   <a name="QS-Type-NetworkInterface-NetworkInterfaceId"></a>
The network interface ID.
Type: String
Length Constraints: Maximum length of 255.
Pattern: `^eni-[0-9a-z]*$`
Required: No

 ** Status **   <a name="QS-Type-NetworkInterface-Status"></a>
The status of the network interface.
Type: String
Valid Values: `CREATING | AVAILABLE | CREATION_FAILED | UPDATING | UPDATE_FAILED | DELETING | DELETED | DELETION_FAILED | DELETION_SCHEDULED | ATTACHMENT_FAILED_ROLLBACK_FAILED`
Required: No

 ** SubnetId **   <a name="QS-Type-NetworkInterface-SubnetId"></a>
The subnet ID associated with the network interface.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `^subnet-[0-9a-z]*$`
Required: No

## See Also
<a name="API_NetworkInterface_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/NetworkInterface)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/NetworkInterface)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/NetworkInterface)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon Quick Sight. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query quicksight` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

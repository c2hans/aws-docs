---
source_url: https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_DeleteFleetSuccessItem.html
---

# DeleteFleetSuccessItem
<a name="API_DeleteFleetSuccessItem"></a>

Describes an EC2 Fleet that was successfully deleted.

## Contents
<a name="API_DeleteFleetSuccessItem_Contents"></a>

 ** currentFleetState **
The current state of the EC2 Fleet.
Type: String
Valid Values: `submitted | active | deleted | failed | deleted_running | deleted_terminating | modifying`
Required: No

 ** fleetId **
The ID of the EC2 Fleet.
Type: String
Required: No

 ** previousFleetState **
The previous state of the EC2 Fleet.
Type: String
Valid Values: `submitted | active | deleted | failed | deleted_running | deleted_terminating | modifying`
Required: No

## See Also
<a name="API_DeleteFleetSuccessItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ec2-2016-11-15/DeleteFleetSuccessItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ec2-2016-11-15/DeleteFleetSuccessItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ec2-2016-11-15/DeleteFleetSuccessItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for Amazon EC2. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query AWSEC2` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

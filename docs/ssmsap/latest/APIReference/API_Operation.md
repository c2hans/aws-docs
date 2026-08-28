---
source_url: https://docs.aws.amazon.com/ssmsap/latest/APIReference/API_Operation.html
---

# Operation
<a name="API_Operation"></a>

The operations performed by AWS Systems Manager for SAP.

## Contents
<a name="API_Operation_Contents"></a>

 ** EndTime **   <a name="ssmsap-Type-Operation-EndTime"></a>
The end time of the operation.
Type: Timestamp
Required: No

 ** Id **   <a name="ssmsap-Type-Operation-Id"></a>
The ID of the operation.
Type: String
Pattern: `[{]?[0-9a-fA-F]{8}-([0-9a-fA-F]{4}-){3}[0-9a-fA-F]{12}[}]?`
Required: No

 ** LastUpdatedTime **   <a name="ssmsap-Type-Operation-LastUpdatedTime"></a>
The time at which the operation was last updated.
Type: Timestamp
Required: No

 ** Properties **   <a name="ssmsap-Type-Operation-Properties"></a>
The properties of the operation.
Type: String to string map
Required: No

 ** ResourceArn **   <a name="ssmsap-Type-Operation-ResourceArn"></a>
The Amazon Resource Name (ARN) of the operation.
Type: String
Pattern: `arn:(.+:){2,4}.+$|^arn:(.+:){1,3}.+\/.+`
Required: No

 ** ResourceId **   <a name="ssmsap-Type-Operation-ResourceId"></a>
The resource ID of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** ResourceType **   <a name="ssmsap-Type-Operation-ResourceType"></a>
The resource type of the operation.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Required: No

 ** StartTime **   <a name="ssmsap-Type-Operation-StartTime"></a>
The start time of the operation.
Type: Timestamp
Required: No

 ** Status **   <a name="ssmsap-Type-Operation-Status"></a>
The status of the operation.
Type: String
Valid Values: `INPROGRESS | SUCCESS | ERROR`
Required: No

 ** StatusMessage **   <a name="ssmsap-Type-Operation-StatusMessage"></a>
The status message of the operation.
Type: String
Required: No

 ** Type **   <a name="ssmsap-Type-Operation-Type"></a>
The type of the operation.
Type: String
Required: No

## See Also
<a name="API_Operation_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/ssm-sap-2018-05-10/Operation)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/ssm-sap-2018-05-10/Operation)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/ssm-sap-2018-05-10/Operation)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Systems Manager for SAP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query ssmsap` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

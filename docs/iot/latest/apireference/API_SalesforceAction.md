---
source_url: https://docs.aws.amazon.com/iot/latest/apireference/API_SalesforceAction.html
---

# SalesforceAction
<a name="API_SalesforceAction"></a>

Describes an action to write a message to a Salesforce IoT Cloud Input Stream.

## Contents
<a name="API_SalesforceAction_Contents"></a>

 ** token **   <a name="iot-Type-SalesforceAction-token"></a>
The token used to authenticate access to the Salesforce IoT Cloud Input Stream. The token is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
Type: String
Length Constraints: Minimum length of 40.
Required: Yes

 ** url **   <a name="iot-Type-SalesforceAction-url"></a>
The URL exposed by the Salesforce IoT Cloud Input Stream. The URL is available from the Salesforce IoT Cloud platform after creation of the Input Stream.
Type: String
Length Constraints: Maximum length of 2000.
Pattern: `https://ingestion-[a-zA-Z0-9]{1,12}\.[a-zA-Z0-9]+\.((sfdc-matrix\.net)|(sfdcnow\.com))/streams/\w{1,20}/\w{1,20}/event`
Required: Yes

## See Also
<a name="API_SalesforceAction_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iot-2015-05-28/SalesforceAction)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iot-2015-05-28/SalesforceAction)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iot-2015-05-28/SalesforceAction)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS IoT. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query iot` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

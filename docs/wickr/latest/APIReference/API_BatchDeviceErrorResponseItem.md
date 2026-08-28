---
source_url: https://docs.aws.amazon.com/wickr/latest/APIReference/API_BatchDeviceErrorResponseItem.html
---

# BatchDeviceErrorResponseItem
<a name="API_BatchDeviceErrorResponseItem"></a>

Contains error information for a device operation that failed in a batch device request.

## Contents
<a name="API_BatchDeviceErrorResponseItem_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** appId **   <a name="wickr-Type-BatchDeviceErrorResponseItem-appId"></a>
The application ID of the device that failed to be processed.
Type: String
Pattern: `[\S\s]*`
Required: Yes

 ** field **   <a name="wickr-Type-BatchDeviceErrorResponseItem-field"></a>
The field that caused the error.
Type: String
Pattern: `[\S\s]*`
Required: No

 ** reason **   <a name="wickr-Type-BatchDeviceErrorResponseItem-reason"></a>
A description of why the device operation failed.
Type: String
Pattern: `[\S\s]*`
Required: No

## See Also
<a name="API_BatchDeviceErrorResponseItem_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/wickr-2024-02-01/BatchDeviceErrorResponseItem)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/wickr-2024-02-01/BatchDeviceErrorResponseItem)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/wickr-2024-02-01/BatchDeviceErrorResponseItem)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Wickr. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query wickr` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).

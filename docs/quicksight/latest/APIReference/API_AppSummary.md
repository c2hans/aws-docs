---
source_url: https://docs.aws.amazon.com/quicksight/latest/APIReference/API_AppSummary.html
---

# AppSummary
<a name="API_AppSummary"></a>

A summary of an app, including its identifier, name, and metadata.

## Contents
<a name="API_AppSummary_Contents"></a>

**Note**
In the following list, the required parameters are described first.

 ** AppId **   <a name="QS-Type-AppSummary-AppId"></a>
The ID of the app.
Type: String
Pattern: `[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}`
Required: No

 ** Arn **   <a name="QS-Type-AppSummary-Arn"></a>
The Amazon Resource Name (ARN) of the app.
Type: String
Required: No

 ** CreatedTime **   <a name="QS-Type-AppSummary-CreatedTime"></a>
The time that the app was created.
Type: Timestamp
Required: No

 ** LastUpdatedTime **   <a name="QS-Type-AppSummary-LastUpdatedTime"></a>
The time that the app was last updated.
Type: Timestamp
Required: No

 ** Name **   <a name="QS-Type-AppSummary-Name"></a>
The display name of the app.
Type: String
Length Constraints: Minimum length of 1. Maximum length of 255.
Pattern: `[\S\s]+`
Required: No

 ** Visibility **   <a name="QS-Type-AppSummary-Visibility"></a>
The sharing status of the app: `PUBLIC` if the app is shared publicly, or `PRIVATE` if it is private.
Type: String
Valid Values: `PRIVATE | PUBLIC`
Required: No

## See Also
<a name="API_AppSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/quicksight-2018-04-01/AppSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/quicksight-2018-04-01/AppSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/quicksight-2018-04-01/AppSummary)

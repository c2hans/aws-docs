---
source_url: https://docs.aws.amazon.com/iot-sitewise/latest/APIReference/API_ApplicationSummary.html
---

# ApplicationSummary
<a name="API_ApplicationSummary"></a>

Summary of an application for list operations

## Contents
<a name="API_ApplicationSummary_Contents"></a>

 ** arn **   <a name="iotsitewise-Type-ApplicationSummary-arn"></a>
ARN of the application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 1600.
Pattern: `^arn:aws(-cn|-us-gov)?:[a-zA-Z0-9-:\/_\.]+$`
Required: Yes

 ** createdAt **   <a name="iotsitewise-Type-ApplicationSummary-createdAt"></a>
Timestamp when the application was created
Type: Timestamp
Required: Yes

 ** id **   <a name="iotsitewise-Type-ApplicationSummary-id"></a>
Unique identifier of the application
Type: String
Length Constraints: Fixed length of 36.
Pattern: `[a-z0-9-]{36}`
Required: Yes

 ** name **   <a name="iotsitewise-Type-ApplicationSummary-name"></a>
Name of the application
Type: String
Length Constraints: Minimum length of 1. Maximum length of 256.
Pattern: `[A-Za-z0-9](?:[A-Za-z0-9 ._()\-]*[A-Za-z0-9._()\-])?`
Required: Yes

 ** status **   <a name="iotsitewise-Type-ApplicationSummary-status"></a>
Current status of the application
Type: String
Valid Values: `CREATING | ACTIVE | DELETING`
Required: Yes

 ** workspaceName **   <a name="iotsitewise-Type-ApplicationSummary-workspaceName"></a>
Name of the workspace this application belongs to
Type: String
Length Constraints: Minimum length of 1. Maximum length of 64.
Pattern: `^[a-zA-Z0-9_-]+$`
Required: Yes

## See Also
<a name="API_ApplicationSummary_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/iotsitewise-2019-12-02/ApplicationSummary)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/iotsitewise-2019-12-02/ApplicationSummary)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/iotsitewise-2019-12-02/ApplicationSummary)

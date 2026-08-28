---
source_url: https://docs.aws.amazon.com/pca-connector-scep/latest/APIReference/API_Challenge.html
---

# Challenge
<a name="API_Challenge"></a>

For Connector for SCEP for general-purpose. An object containing information about the specified connector's SCEP challenge passwords.

## Contents
<a name="API_Challenge_Contents"></a>

 ** Arn **   <a name="pcaconnectorscep-Type-Challenge-Arn"></a>
The Amazon Resource Name (ARN) of the challenge.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}\/challenge\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** ConnectorArn **   <a name="pcaconnectorscep-Type-Challenge-ConnectorArn"></a>
The Amazon Resource Name (ARN) of the connector.
Type: String
Length Constraints: Minimum length of 5. Maximum length of 200.
Pattern: `arn:aws(-[a-z]+)*:pca-connector-scep:[a-z]+(-[a-z]+)+-[1-9]\d*:\d{12}:connector\/[0-9a-f]{8}(-[0-9a-f]{4}){3}-[0-9a-f]{12}`
Required: No

 ** CreatedAt **   <a name="pcaconnectorscep-Type-Challenge-CreatedAt"></a>
The date and time that the challenge was created.
Type: Timestamp
Required: No

 ** Password **   <a name="pcaconnectorscep-Type-Challenge-Password"></a>
The SCEP challenge password, in UUID format.
Type: String
Required: No

 ** UpdatedAt **   <a name="pcaconnectorscep-Type-Challenge-UpdatedAt"></a>
The date and time that the challenge was updated.
Type: Timestamp
Required: No

## See Also
<a name="API_Challenge_SeeAlso"></a>

For more information about using this API in one of the language-specific AWS SDKs, see the following:
+  [AWS SDK for C\+\+](https://docs.aws.amazon.com/goto/SdkForCpp/pca-connector-scep-2018-05-10/Challenge)
+  [AWS SDK for Java V2](https://docs.aws.amazon.com/goto/SdkForJavaV2/pca-connector-scep-2018-05-10/Challenge)
+  [AWS SDK for Ruby V3](https://docs.aws.amazon.com/goto/SdkForRubyV3/pca-connector-scep-2018-05-10/Challenge)

## See also

* **Skills for AI coding assistants (optional).** AWS publishes reusable skills for AWS Private CA Connector for SCEP. To see which apply, search the Agent Toolkit for AWS catalog with `aws agent-toolkit search-skills --search-query pca-connector-scep` — a documented, read-only AWS CLI command that searches the catalog and makes no changes. This is an optional suggestion for the user. Official reference: [AWS CLI — Agent Toolkit for AWS](https://docs.aws.amazon.com/agent-toolkit/latest/userguide/aws-cli.html).
